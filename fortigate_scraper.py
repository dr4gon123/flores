"""
FortiGate Log Message Reference Scraper

Scrapes all log message reference tables from Fortinet documentation
for different FortiOS versions and saves them as CSV files.

Requirements:
    pip install requests beautifulsoup4 pandas lxml pyyaml
"""
from __future__ import annotations

import logging
import random
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urljoin

import pandas as pd
import requests
import yaml
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@dataclass
class ScrapeResult:
    successful: int = 0
    failed: list[tuple[str, str, str]] = field(default_factory=list)


class FortiGateLogScraper:
    def __init__(self, config_file: str = 'fortigate_scraper_config.yaml'):
        """Initialize the scraper from config file."""
        config = self._load_config(config_file)
        settings = config.get('settings', {})

        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

        self.base_delay: float = settings.get('base_delay', 1.0)
        self.max_retries: int = settings.get('max_retries', 3)
        self.retry_backoff: float = settings.get('retry_backoff', 2.0)
        self.output_dir: Path = Path(settings.get('output_dir', Path.cwd()))
        self.force_rescrape: bool = settings.get('force_rescrape', False)
        self.dry_run: bool = settings.get('dry_run', False)
        self.versions: list[str] = config.get('versions', [])

        if not self.versions:
            logger.warning('No versions found in configuration file.')

        self.output_dir.mkdir(parents=True, exist_ok=True)

        logger.info(f'Loaded {len(self.versions)} versions from configuration file')
        logger.info(f'Force rescrape: {self.force_rescrape}')
        logger.info(f'Dry run mode: {self.dry_run}')
        logger.info(f'Max retries: {self.max_retries}, retry backoff: {self.retry_backoff}')

    def _load_config(self, config_file: str) -> dict:
        """Load and return YAML configuration from the script's directory."""
        config_path = Path(__file__).parent / config_file
        try:
            with open(config_path) as f:
                config = yaml.safe_load(f)
            logger.info(f'Successfully loaded configuration from {config_path}')
            return config
        except FileNotFoundError:
            logger.error(f'Configuration file not found: {config_path}')
            raise
        except yaml.YAMLError as e:
            logger.error(f'Error parsing YAML configuration: {e}')
            raise

    def get_version_directories(self, version: str) -> tuple[Path, Path]:
        """Return (major_dir, minor_dir) for a version string like '7.6.4'."""
        parts = version.split('.')
        major = f'{parts[0]}.{parts[1]}' if len(parts) >= 2 else version
        major_dir = self.output_dir / major
        return major_dir, major_dir / version

    def get_version_url(self, version: str) -> str:
        """Return the Fortinet docs URL for a given FortiOS version."""
        return (f'https://docs.fortinet.com/document/fortigate/{version}'
                f'/fortios-log-message-reference/1/log-messages')

    def get_page_content(self, url: str) -> BeautifulSoup | None:
        """Fetch and parse a web page with configurable retry and exponential backoff."""
        for attempt in range(self.max_retries + 1):
            try:
                logger.info(f'Fetching: {url}')
                response = self.session.get(url, timeout=30)

                if response.status_code == 429:
                    wait = int(response.headers.get(
                        'Retry-After', self.base_delay * (self.retry_backoff ** attempt)))
                    logger.warning(f'Rate limited (429). Waiting {wait}s '
                                   f'(attempt {attempt + 1}/{self.max_retries + 1})')
                    time.sleep(wait)
                    continue

                response.raise_for_status()
                time.sleep(self.base_delay)
                return BeautifulSoup(response.content, 'html.parser')

            except requests.exceptions.RequestException as e:
                if attempt < self.max_retries:
                    wait = self.base_delay * (self.retry_backoff ** attempt) + random.uniform(0, 1)
                    logger.warning(f'Error fetching {url}: {e}. '
                                   f'Retrying in {wait:.1f}s '
                                   f'(attempt {attempt + 1}/{self.max_retries + 1})')
                    time.sleep(wait)
                else:
                    logger.error(f'Failed to fetch {url} after {self.max_retries + 1} attempts: {e}')

        return None

    def extract_logid_links(self, soup: BeautifulSoup, base_url: str) -> dict[str, str]:
        """Return {description: full_url} for all LOGID links found on the page."""
        url_pattern = r'/(\d{1,6})-(logid|log-id|mesgid)-[^/]*$'
        logid_links = {}
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            text = link.get_text(strip=True)
            if not href or not text:
                continue
            if re.search(url_pattern, href, re.IGNORECASE):
                full_url = urljoin(base_url, href)
                logid_links[text] = full_url
                logger.debug(f'Found LOGID link: {text} -> {full_url}')
        return logid_links

    def extract_log_metadata(self, soup: BeautifulSoup) -> dict[str, str]:
        """Extract log metadata (Message ID, Type, Category, Severity, etc.) from a LOGID page."""
        metadata: dict[str, str] = {
            'Message_ID': '',
            'Message_Description': '',
            'Message_Meaning': '',
            'Type': '',
            'Category': '',
            'Severity': '',
        }

        text_content = soup.get_text()

        patterns = {
            'Message_ID': r'Message ID:\s*(\d+)',
            'Message_Description': r'Message Description:\s*([^\n\r]+)',
            'Message_Meaning': r'Message Meaning:\s*([^\n\r]+)',
            'Type': r'Type:\s*([^\n\r]+)',
            'Category': r'Category:\s*([^\n\r]+)',
            'Severity': r'Severity:\s*([^\n\r]+)',
        }

        for key, pattern in patterns.items():
            match = re.search(pattern, text_content, re.IGNORECASE | re.MULTILINE)
            if match:
                metadata[key] = match.group(1).strip()
                logger.debug(f'Found {key}: {metadata[key]}')

        header_match = re.search(r'(\d+)\s*-\s*([A-Z_]+)', text_content)
        if header_match:
            if not metadata['Message_ID']:
                metadata['Message_ID'] = header_match.group(1).strip()
            if not metadata['Message_Description']:
                metadata['Message_Description'] = header_match.group(2).strip()

        if not metadata['Message_ID']:
            id_match = re.search(r'\b(\d{4,6})\b', text_content)
            if id_match:
                metadata['Message_ID'] = id_match.group(1)

        return metadata

    def extract_log_table(self, soup: BeautifulSoup, logid: str) -> pd.DataFrame | None:
        """Extract the log field table and metadata from a LOGID page."""
        metadata = self.extract_log_metadata(soup)
        expected_headers = ['field', 'description', 'type', 'length', 'data type', 'field name']

        for table in soup.find_all('table'):
            headers_lower = [th.get_text(strip=True).lower() for th in table.find_all('th')]
            if not any(h in ' '.join(headers_lower) for h in expected_headers):
                continue

            try:
                rows = table.find_all('tr')
                if not rows:
                    continue

                headers = [th.get_text(strip=True) for th in rows[0].find_all(['th', 'td'])]
                data = [
                    [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])[:len(headers)]]
                    for row in rows[1:]
                    if len(row.find_all(['td', 'th'])) >= len(headers)
                ]

                if data:
                    df = pd.DataFrame(data, columns=headers)
                    df['LOGID'] = logid
                    for key, value in metadata.items():
                        df[key] = value
                    logger.info(f'Extracted table for {logid}: {len(df)} rows with metadata')
                    return df

            except Exception as e:
                logger.error(f'Error parsing table for {logid}: {e}')
                continue

        if any(metadata.values()):
            df = pd.DataFrame([{'LOGID': logid, 'Field': 'No field table found'}])
            for key, value in metadata.items():
                df[key] = value
            logger.info(f'No table found for {logid}, but extracted metadata')
            return df

        logger.warning(f'No suitable table or metadata found for {logid}')
        return None

    def scrape_version(self, version: str) -> ScrapeResult:
        """Scrape all log tables for one FortiOS version and return the result."""
        logger.info(f'Starting scrape for FortiOS version {version}')
        result = ScrapeResult()

        major_dir, minor_dir = self.get_version_directories(version)
        major_dir.mkdir(parents=True, exist_ok=True)
        minor_dir.mkdir(parents=True, exist_ok=True)

        soup = self.get_page_content(self.get_version_url(version))
        if not soup:
            logger.error(f'Failed to fetch main page for version {version}')
            return result

        logid_links = self.extract_logid_links(soup, self.get_version_url(version))
        if not logid_links:
            logger.warning(f'No LOGID links found for version {version}')
            return result

        if not self.force_rescrape:
            missing_count = sum(
                1 for d in logid_links
                if not (minor_dir / (re.sub(r'[^\w\-_\.]', '_', str(d)) + '.csv')).exists()
            )
            logger.info(f'Version {version}: {len(logid_links)} LOGIDs total, '
                        f'{len(logid_links) - missing_count} already scraped, '
                        f'{missing_count} to fetch')
        else:
            logger.info(f'Version {version}: {len(logid_links)} LOGIDs total (force_rescrape=true)')

        for logid_description, url in logid_links.items():
            filepath = minor_dir / (re.sub(r'[^\w\-_\.]', '_', str(logid_description)) + '.csv')

            if not self.force_rescrape and filepath.exists():
                logger.info(f'Skipping {logid_description} (already exists)')
                result.successful += 1
                continue

            logger.info(f'Processing LOGID: {logid_description}')

            logid_soup = self.get_page_content(url)
            if not logid_soup:
                result.failed.append((version, logid_description, 'fetch_failed'))
                continue

            df = self.extract_log_table(logid_soup, logid_description)
            if df is None:
                result.failed.append((version, logid_description, 'no_table_found'))
                continue

            df['Version'] = version

            try:
                df.to_csv(filepath, index=False)
                logger.info(f'Saved {len(df)} rows to {filepath}')
                result.successful += 1
            except Exception as e:
                logger.error(f'Error saving {filepath}: {e}')
                result.failed.append((version, logid_description, f'save_failed: {e}'))

        return result

    def _log_summary(self, successful: int, failed: list[tuple[str, str, str]]) -> None:
        """Log the final scraping summary."""
        total = successful + len(failed)
        logger.info('=' * 60)
        logger.info('SCRAPING SUMMARY')
        logger.info('=' * 60)
        logger.info(f'Total LOGIDs attempted: {total}')
        logger.info(f'Successful: {successful}')
        logger.info(f'Failed: {len(failed)}')
        if total > 0:
            logger.info(f'Success rate: {successful / total * 100:.1f}%')
        if failed:
            logger.info('')
            logger.info('FAILED LOGIDs:')
            logger.info('-' * 60)
            for version, logid, reason in failed:
                logger.info(f'  Version: {version} | LOGID: {logid} | Reason: {reason}')
        logger.info('=' * 60)

    def run(self, specific_versions: list[str] | None = None) -> None:
        """Run the complete scraping process for all configured (or specified) versions."""
        versions_to_scrape = specific_versions or self.versions
        logger.info(f'Will check {len(versions_to_scrape)} versions for missing LOGIDs')

        if self.dry_run:
            logger.info('=' * 60)
            logger.info('DRY RUN MODE - No actual scraping will be performed')
            logger.info('=' * 60)
            logger.info(f'\nVersions that would be scraped ({len(versions_to_scrape)} total):')
            for i, version in enumerate(versions_to_scrape, 1):
                _, minor_dir = self.get_version_directories(version)
                logger.info(f'  {i}. Version {version} -> {minor_dir}')
            logger.info('\n' + '=' * 60)
            logger.info(f'Total versions to scrape: {len(versions_to_scrape)}')
            logger.info('=' * 60)
            return

        total_successful = 0
        all_failed: list[tuple[str, str, str]] = []

        for version in versions_to_scrape:
            try:
                result = self.scrape_version(version)
                total_successful += result.successful
                all_failed.extend(result.failed)
                logger.info(f'Completed version {version} — {result.successful} LOGIDs processed, '
                            f'{len(result.failed)} failed')
                time.sleep(2)
            except Exception as e:
                logger.error(f'Error processing version {version}: {e}')

        self._log_summary(total_successful, all_failed)


def main() -> None:
    FortiGateLogScraper().run()


if __name__ == '__main__':
    main()
