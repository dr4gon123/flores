"""
Checks docs.fortinet.com for FortiOS Log Message Reference releases that are
missing from the scraper config and optionally adds them to it.

Run from repo root: python3 check_new_versions.py [--update-config] [--github-output]
"""
from __future__ import annotations

import argparse
import asyncio
import json
import logging
import os
import random
import re
from dataclasses import dataclass, field
from pathlib import Path

import httpx
import yaml
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

# "Major" = the two-digit FortiOS branch (7.4, 7.6, 8.0, ...). Only branches at
# or above this floor are discovered; e.g. 7.2 and lower are never auto-added.
MIN_TRACKED_MAJOR = "7.4"

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
)
PRODUCT_URL = "https://docs.fortinet.com/product/fortigate"
BRANCH_URL = "https://docs.fortinet.com/product/fortigate/{branch}"
CONFIG_PATH = Path(__file__).parent / "fortigate_scraper_config.yaml"
BASE_DELAY = 1.0
MAX_RETRIES = 3

BRANCH_HREF_RE = re.compile(r"product/fortigate/(\d+\.\d+)(?:[/?#]|$)")
LMR_HREF_RE = re.compile(
    r"/document/fortigate/(\d+\.\d+\.\d+)/fortios-log-message-reference(?:[/?#]|$)"
)
VERSION_ENTRY_RE = re.compile(r'^\s*-\s*"(\d+\.\d+\.\d+)"\s*$')


@dataclass
class ReleaseCheck:
    configured: list[str] = field(default_factory=list)
    discovered: list[str] = field(default_factory=list)
    new_versions: list[str] = field(default_factory=list)


def version_key(version: str) -> tuple[int, ...]:
    return tuple(int(part) for part in version.split("."))


def branch_of(version: str) -> str:
    return ".".join(version.split(".")[:2])


async def fetch_soup(client: httpx.AsyncClient, url: str) -> BeautifulSoup:
    for attempt in range(MAX_RETRIES + 1):
        try:
            logger.info(f"Fetching: {url}")
            response = await client.get(url)

            if response.status_code == 429:
                wait = int(response.headers.get("Retry-After", BASE_DELAY * 2**attempt))
                logger.warning(
                    f"Rate limited (429). Waiting {wait}s "
                    f"(attempt {attempt + 1}/{MAX_RETRIES + 1})"
                )
                await asyncio.sleep(wait)
                continue

            response.raise_for_status()
            await asyncio.sleep(BASE_DELAY)
            return BeautifulSoup(response.content, "html.parser")

        except httpx.HTTPError as e:
            if attempt < MAX_RETRIES:
                wait = BASE_DELAY * 2**attempt + random.uniform(0, 1)
                logger.warning(
                    f"Error fetching {url}: {e}. Retrying in {wait:.1f}s "
                    f"(attempt {attempt + 1}/{MAX_RETRIES + 1})"
                )
                await asyncio.sleep(wait)
            else:
                raise RuntimeError(
                    f"Failed to fetch {url} after {MAX_RETRIES + 1} attempts: {e}"
                ) from e

    raise RuntimeError(f"Failed to fetch {url}: retries exhausted")


def extract_branches(soup: BeautifulSoup) -> list[str]:
    branches = {
        match.group(1)
        for link in soup.find_all("a", href=True)
        if (match := BRANCH_HREF_RE.search(link["href"]))
    }
    if not branches:
        raise RuntimeError(
            f"No FortiOS branch links found on {PRODUCT_URL} — "
            "docs page layout may have changed"
        )
    return sorted(branches, key=version_key, reverse=True)


def extract_lmr_versions(soup: BeautifulSoup, branch: str) -> list[str]:
    versions = {
        match.group(1)
        for link in soup.find_all("a", href=True)
        if (match := LMR_HREF_RE.search(link["href"]))
    }
    if not versions:
        raise RuntimeError(
            f"No Log Message Reference links found for branch {branch} — "
            "docs page layout may have changed"
        )
    return sorted(versions, key=version_key)


def load_configured_versions(config_path: Path) -> list[str]:
    with config_path.open() as f:
        config = yaml.safe_load(f) or {}
    versions = [str(v) for v in config.get("versions", [])]
    if not versions:
        raise RuntimeError(f"No versions found in {config_path}")
    return versions


async def discover_versions(client: httpx.AsyncClient, min_major: str) -> list[str]:
    branches = [
        branch
        for branch in extract_branches(await fetch_soup(client, PRODUCT_URL))
        if version_key(branch) >= version_key(min_major)
    ]
    logger.info(f"Tracking branches at or above {min_major}: {', '.join(branches)}")

    discovered: list[str] = []
    for branch in branches:
        soup = await fetch_soup(client, BRANCH_URL.format(branch=branch))
        discovered.extend(extract_lmr_versions(soup, branch))
    return discovered


def find_insert_index(lines: list[str], version: str) -> int:
    versions_start = next(
        (i for i, line in enumerate(lines) if line.rstrip() == "versions:"), None
    )
    if versions_start is None:
        raise RuntimeError(f"No 'versions:' key found in {CONFIG_PATH}")

    entries = [
        (i, match.group(1))
        for i, line in enumerate(lines[versions_start + 1 :], versions_start + 1)
        if (match := VERSION_ENTRY_RE.match(line))
    ]

    branch = branch_of(version)
    same_branch = [i for i, v in entries if branch_of(v) == branch]
    if same_branch:
        return same_branch[-1] + 1
    lower_branches = [i for i, v in entries if version_key(branch_of(v)) < version_key(branch)]
    if lower_branches:
        return lower_branches[0]
    return versions_start + 1


def update_config(new_versions: list[str]) -> None:
    # Ascending order: each insertion lands directly above the first entry of a
    # lower branch, so equal-branch entries stack in ascending patch order.
    for version in sorted(new_versions, key=version_key):
        lines = CONFIG_PATH.read_text().splitlines(keepends=True)
        lines.insert(find_insert_index(lines, version), f'  - "{version}"\n')
        CONFIG_PATH.write_text("".join(lines))

    with CONFIG_PATH.open() as f:
        config = yaml.safe_load(f)
    configured = [str(v) for v in config["versions"]]
    missing = [v for v in new_versions if v not in configured]
    if missing:
        raise RuntimeError(f"Config update failed, versions missing after write: {missing}")
    logger.info(f"Added {len(new_versions)} versions to {CONFIG_PATH}")


def display_versions(versions: list[str]) -> str:
    if len(versions) <= 2:
        return " and ".join(versions)
    return ", ".join(versions[:-1]) + " and " + versions[-1]


def write_github_output(check: ReleaseCheck) -> None:
    output_path = os.environ.get("GITHUB_OUTPUT")
    if not output_path:
        raise RuntimeError("--github-output set but GITHUB_OUTPUT is not defined")
    with Path(output_path).open("a") as f:
        f.write(f"count={len(check.new_versions)}\n")
        f.write(f"new_versions={json.dumps(check.new_versions)}\n")
        f.write(f"display={display_versions(check.new_versions)}\n")


async def run(min_major: str, update: bool) -> ReleaseCheck:
    configured = load_configured_versions(CONFIG_PATH)

    async with httpx.AsyncClient(
        headers={"User-Agent": USER_AGENT},
        follow_redirects=True,
        timeout=30,
    ) as client:
        discovered = await discover_versions(client, min_major)

    known = set(configured)
    new_versions = sorted(
        (v for v in discovered if v not in known), key=version_key, reverse=True
    )
    check = ReleaseCheck(
        configured=configured,
        discovered=sorted(discovered, key=version_key, reverse=True),
        new_versions=new_versions,
    )

    logger.info(
        f"Configured versions: {len(check.configured)}, "
        f"discovered: {len(check.discovered)}, new: {len(new_versions)}"
    )
    if not new_versions:
        logger.info("No new FortiOS releases found")
        return check

    logger.info(f"New FortiOS releases: {', '.join(new_versions)}")
    if update:
        update_config(new_versions)
    else:
        logger.info("Dry run (no --update-config): config not modified")
    return check


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Check docs.fortinet.com for new FortIOS releases and "
        "optionally add them to the scraper config"
    )
    parser.add_argument(
        "--update-config",
        action="store_true",
        help="Add discovered versions to fortigate_scraper_config.yaml",
    )
    parser.add_argument(
        "--github-output",
        action="store_true",
        help="Write results to $GITHUB_OUTPUT for GitHub Actions",
    )
    parser.add_argument(
        "--min-major",
        default=MIN_TRACKED_MAJOR,
        help=f"Lowest FortiOS branch to track (default: {MIN_TRACKED_MAJOR})",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    check = asyncio.run(run(args.min_major, args.update_config))
    if args.github_output:
        write_github_output(check)


if __name__ == "__main__":
    main()
