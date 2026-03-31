from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class EcsField:
    """ECS 9.3 field definition."""
    name: str
    ecs_type: str
    description: str


@dataclass(frozen=True)
class EcsTarget:
    """One ECS mapping target for a FortiGate field."""
    ecs_field: str
    mapping_type: str  # "=" direct or "->" derived


@dataclass(frozen=True)
class FgtMapping:
    """FortiGate field → one or more ECS targets."""
    fgt_field: str
    targets: tuple[EcsTarget, ...]


# ---------------------------------------------------------------------------
# ECS 9.3 field registry
# Fields with (*) in description are custom extensions not in ECS 9.3 core.
# ---------------------------------------------------------------------------

ECS_FIELD_REGISTRY: dict[str, EcsField] = {
    "@timestamp":                        EcsField("@timestamp",                        "date",     "Date/time when the event originated."),
    "event.timezone":                    EcsField("event.timezone",                    "keyword",  "Event time zone."),
    "event.code":                        EcsField("event.code",                        "keyword",  "Identification code for this event."),
    "event.duration":                    EcsField("event.duration",                    "long",     "Duration of the event in nanoseconds."),
    "source.ip":                         EcsField("source.ip",                         "ip",       "IP address of the source."),
    "source.port":                       EcsField("source.port",                       "long",     "Port of the source."),
    "source.mac":                        EcsField("source.mac",                        "keyword",  "MAC address of the source."),
    "source.nat.ip":                     EcsField("source.nat.ip",                     "ip",       "Source NAT ip."),
    "source.nat.port":                   EcsField("source.nat.port",                   "long",     "Source NAT port."),
    "source.user.name":                  EcsField("source.user.name",                  "keyword",  "Short name or login of the user."),
    "source.user.group.name":            EcsField("source.user.group.name",            "keyword",  "Name of the group."),
    "source.bytes":                      EcsField("source.bytes",                      "long",     "Bytes sent from the source to the destination."),
    "source.packets":                    EcsField("source.packets",                    "long",     "Packets sent from the source to the destination."),
    "source.domain":                     EcsField("source.domain",                     "keyword",  "The domain name of the source."),
    "source.address":                    EcsField("source.address",                    "keyword",  "Source network address."),
    "source.risk.static_score":          EcsField("source.risk.static_score",          "float",    "(*) Risk classification score from an external source."),
    "source.risk.static_level":          EcsField("source.risk.static_level",          "keyword",  "(*) Risk classification level from an external source."),
    "destination.ip":                    EcsField("destination.ip",                    "ip",       "IP address of the destination."),
    "destination.port":                  EcsField("destination.port",                  "long",     "Port of the destination."),
    "destination.mac":                   EcsField("destination.mac",                   "keyword",  "MAC address of the destination."),
    "destination.nat.ip":                EcsField("destination.nat.ip",                "ip",       "Destination NAT ip."),
    "destination.nat.port":              EcsField("destination.nat.port",              "long",     "Destination NAT Port."),
    "destination.user.name":             EcsField("destination.user.name",             "keyword",  "Short name or login of the user."),
    "destination.user.group.name":       EcsField("destination.user.group.name",       "keyword",  "Name of the group."),
    "destination.bytes":                 EcsField("destination.bytes",                 "long",     "Bytes sent from the destination to the source."),
    "destination.packets":               EcsField("destination.packets",               "long",     "Packets sent from the destination to the source."),
    "destination.address":               EcsField("destination.address",               "keyword",  "Destination network address."),
    "host.risk.static_score":            EcsField("host.risk.static_score",            "float",    "A risk classification score obtained from outside the system, such as from some external Threat Intelligence Platform."),
    "host.risk.static_level":            EcsField("host.risk.static_level",            "keyword",  "A risk classification level obtained from outside the system, such as from some external Threat Intelligence Platform."),
    "observer.hostname":                 EcsField("observer.hostname",                 "keyword",  "Hostname of the observer."),
    "observer.name":                     EcsField("observer.name",                     "keyword",  "Custom name of the observer."),
    "observer.product":                  EcsField("observer.product",                  "keyword",  "The product name of the observer."),
    "observer.type":                     EcsField("observer.type",                     "keyword",  "The type of the observer the data is coming from."),
    "observer.vendor":                   EcsField("observer.vendor",                   "keyword",  "Vendor name of the observer."),
    "observer.egress.interface.name":    EcsField("observer.egress.interface.name",    "keyword",  "Interface name as reported by the system."),
    "observer.ingress.interface.name":   EcsField("observer.ingress.interface.name",   "keyword",  "Interface name as reported by the system."),
    "observer.egress.zone":              EcsField("observer.egress.zone",              "keyword",  "Observer Egress zone."),
    "observer.ingress.zone":             EcsField("observer.ingress.zone",             "keyword",  "Observer ingress zone."),
    "network.bytes":                     EcsField("network.bytes",                     "long",     "Total bytes transferred in both directions."),
    "network.packets":                   EcsField("network.packets",                   "long",     "Total packets transferred in both directions."),
    "network.protocol":                  EcsField("network.protocol",                  "keyword",  "Application protocol name."),
    "network.application":               EcsField("network.application",               "keyword",  "Application level protocol name."),
    "network.iana_number":               EcsField("network.iana_number",               "keyword",  "IANA Protocol Number."),
    "network.transport":                 EcsField("network.transport",                 "keyword",  "Protocol Name corresponding to the field `iana_number`."),
    "network.community_id":              EcsField("network.community_id",              "keyword",  "A hash of source and destination IPs and ports, and the protocol used in a communication."),
    "network.direction":                 EcsField("network.direction",                 "keyword",  "Direction of the network traffic."),
    "network.vrf":                       EcsField("network.vrf",                       "keyword",  "(*) Virtual routing and forwarding ID."),
    "network.transport_port":            EcsField("network.transport_port",            "keyword",  "(*) Combination of network transport and destination port (e.g. tcp/443)."),
    "url.original":                      EcsField("url.original",                      "wildcard", "Unmodified original url as seen in the event source."),
    "url.domain":                        EcsField("url.domain",                        "keyword",  "Domain of the url."),
    "url.path":                          EcsField("url.path",                          "wildcard", "Path of the request."),
    "url.query":                         EcsField("url.query",                         "keyword",  "Query string of the request."),
    "url.registered_domain":             EcsField("url.registered_domain",             "keyword",  "The highest registered url domain, stripped of the subdomain."),
    "url.top_level_domain":              EcsField("url.top_level_domain",              "keyword",  "The effective top level domain (com, org, net, co.uk)."),
    "related.ip":                        EcsField("related.ip",                        "ip",       "All of the IPs seen on your event."),
    "rule.id":                           EcsField("rule.id",                           "keyword",  "Rule ID."),
    "rule.name":                         EcsField("rule.name",                         "keyword",  "Rule name."),
    "rule.ruleset":                      EcsField("rule.ruleset",                      "keyword",  "Rule ruleset."),
    "rule.uuid":                         EcsField("rule.uuid",                         "keyword",  "Rule UUID."),
    "rule.comment":                      EcsField("rule.comment",                      "keyword",  "(*) Description or comment pertaining to the rule."),
    "session.id":                        EcsField("session.id",                        "keyword",  "(*) Unique identifier for the session."),
    # --- event classification / log level ---
    "message":                           EcsField("message",                           "match_only_text", "Log message optimized for viewing in a log viewer."),
    "event.action":                      EcsField("event.action",                      "keyword",  "The action captured by the event."),
    "event.category":                    EcsField("event.category",                    "keyword",  "Event category. The second categorization field in the hierarchy."),
    "event.reason":                      EcsField("event.reason",                      "keyword",  "Reason why this event happened, according to the source."),
    "event.reference":                   EcsField("event.reference",                   "keyword",  "Event reference URL."),
    "event.severity":                    EcsField("event.severity",                    "long",     "Numeric severity of the event."),
    "log.level":                         EcsField("log.level",                         "keyword",  "Log level of the log event."),
    # --- geo ---
    "source.geo.country_name":           EcsField("source.geo.country_name",           "keyword",  "Country name."),
    "source.geo.city_name":              EcsField("source.geo.city_name",              "keyword",  "City name."),
    "destination.geo.country_name":      EcsField("destination.geo.country_name",      "keyword",  "Country name."),
    "destination.geo.city_name":         EcsField("destination.geo.city_name",         "keyword",  "City name."),
    # --- observer ---
    "observer.serial_number":            EcsField("observer.serial_number",            "keyword",  "Observer serial number."),
    # --- email ---
    "email.from.address":                EcsField("email.from.address",                "keyword",  "The sender's email address."),
    "email.to.address":                  EcsField("email.to.address",                  "keyword",  "Email address of recipient."),
    "email.cc.address":                  EcsField("email.cc.address",                  "keyword",  "Email address of CC recipient."),
    "email.subject":                     EcsField("email.subject",                     "keyword",  "The subject of the email message."),
    "email.sender.address":              EcsField("email.sender.address",              "keyword",  "Address of the message sender."),
    # --- threat ---
    "threat.indicator.name":             EcsField("threat.indicator.name",             "keyword",  "Indicator display name."),
    "threat.indicator.ip":               EcsField("threat.indicator.ip",               "ip",       "Indicator IP address."),
    "threat.indicator.id":               EcsField("threat.indicator.id",               "keyword",  "ID of the indicator."),
    "threat.indicator.url.domain":       EcsField("threat.indicator.url.domain",       "keyword",  "Domain of the url."),
    # --- vulnerability ---
    "vulnerability.id":                  EcsField("vulnerability.id",                  "keyword",  "ID of the vulnerability."),
    "network.forwarded_ip":              EcsField("network.forwarded_ip",              "ip",       "Host IP address when the source IP address is the proxy."),
    "http.request.method":               EcsField("http.request.method",               "keyword",  "HTTP request method."),
    "http.response.status_code":         EcsField("http.response.status_code",         "long",     "HTTP response status code."),
    "http.request.referrer":             EcsField("http.request.referrer",             "keyword",  "Referrer for this HTTP request."),
    "http.request.mime_type":            EcsField("http.request.mime_type",            "keyword",  "Mime type of the body of the request."),
    "http.response.mime_type":           EcsField("http.response.mime_type",           "keyword",  "Mime type of the body of the response."),
    "user_agent.original":               EcsField("user_agent.original",               "keyword",  "Unparsed user_agent string."),
    "dns.resolved_ip":                   EcsField("dns.resolved_ip",                   "ip",       "Array containing all IPs seen in answers.data."),
    "dns.question.class":                EcsField("dns.question.class",                "keyword",  "The class of records being queried."),
    "dns.question.name":                 EcsField("dns.question.name",                 "keyword",  "The name being queried."),
    "dns.question.type":                 EcsField("dns.question.type",                 "keyword",  "The type of record being queried."),
    "dns.question.registered_domain":    EcsField("dns.question.registered_domain",    "keyword",  "The highest registered domain, stripped of the subdomain."),
    "dns.question.top_level_domain":     EcsField("dns.question.top_level_domain",     "keyword",  "The effective top level domain (com, org, net, co.uk)."),
    "dns.id":                            EcsField("dns.id",                            "keyword",  "The DNS packet identifier assigned by the program that generated the query."),
    "tls.client.issuer":                 EcsField("tls.client.issuer",                 "keyword",  "Distinguished name of subject of the issuer of the x.509 certificate presented by the client."),
    "tls.client.server_name":            EcsField("tls.client.server_name",            "keyword",  "Hostname the client is trying to connect to. Also called the SNI."),
    "tls.server.issuer":                 EcsField("tls.server.issuer",                 "keyword",  "Subject of the issuer of the x.509 certificate presented by the server."),
    "tls.version":                       EcsField("tls.version",                       "keyword",  "Numeric part of the TLS version parsed from the original string."),
    "file.hash.sha1":                    EcsField("file.hash.sha1",                    "keyword",  "SHA1 hash."),
    "file.name":                         EcsField("file.name",                         "keyword",  "Name of the file including the extension, without the directory."),
    "file.size":                         EcsField("file.size",                         "long",     "File size in bytes."),
    "file.extension":                    EcsField("file.extension",                    "keyword",  "File extension, excluding the leading dot."),
}


# ---------------------------------------------------------------------------
# Mapping tables (derived from fortigate.yaml VRL transforms)
# One FgtMapping per logical relationship; build_lookup() merges by fgt_field.
# ---------------------------------------------------------------------------

def _t(ecs_field: str, mapping_type: str) -> EcsTarget:
    return EcsTarget(ecs_field, mapping_type)


TRAFFIC_MAPPINGS: list[FgtMapping] = [
    # event
    FgtMapping("tz",                ((_t("event.timezone",                "=")),)),
    FgtMapping("logid",             ((_t("event.code",                    "=")),)),
    FgtMapping("duration",          ((_t("event.duration",                "->")),)),  # seconds × 10^9
    # source
    FgtMapping("srcip",             ((_t("source.ip",                     "=")),)),
    FgtMapping("srcip",             ((_t("network.community_id",          "->")),)),
    FgtMapping("srcip",             ((_t("network.direction",             "->")),)),
    FgtMapping("srcip",             ((_t("related.ip",                    "->")),)),
    FgtMapping("srcport",           ((_t("source.port",                   "->")),)),  # to_int
    FgtMapping("srcmac",            ((_t("source.mac",                    "=")),)),
    FgtMapping("transip",           ((_t("source.nat.ip",                 "=")),)),
    FgtMapping("transip",           ((_t("related.ip",                    "->")),)),
    FgtMapping("transport",         ((_t("source.nat.port",               "->")),)),  # to_int
    FgtMapping("transport",         ((_t("network.transport_port",        "->")),)),
    FgtMapping("user",              ((_t("source.user.name",              "=")),)),
    FgtMapping("unauthuser",        ((_t("source.user.name",              "=")),)),
    FgtMapping("group",             ((_t("source.user.group.name",        "=")),)),
    FgtMapping("unauthusersource",  ((_t("source.user.group.name",        "=")),)),
    FgtMapping("crscore",           ((_t("host.risk.static_score",        "->")),)),  # to_int
    FgtMapping("crlevel",           ((_t("host.risk.static_level",        "=")),)),
    FgtMapping("sentbyte",          ((_t("source.bytes",                  "->")),)),  # to_int
    FgtMapping("sentbyte",          ((_t("network.bytes",                 "->")),)),
    FgtMapping("sentpkt",           ((_t("source.packets",                "->")),)),  # to_int
    FgtMapping("sentpkt",           ((_t("network.packets",               "->")),)),
    FgtMapping("srcdomain",         ((_t("source.domain",                 "=")),)),
    FgtMapping("srcname",           ((_t("source.address",                "=")),)),
    # destination
    FgtMapping("dstip",             ((_t("destination.ip",                "=")),)),
    FgtMapping("dstip",             ((_t("network.community_id",          "->")),)),
    FgtMapping("dstip",             ((_t("network.direction",             "->")),)),
    FgtMapping("dstip",             ((_t("related.ip",                    "->")),)),
    FgtMapping("dstport",           ((_t("destination.port",              "->")),)),  # to_int
    FgtMapping("dstport",           ((_t("network.transport_port",        "->")),)),
    FgtMapping("dstmac",            ((_t("destination.mac",               "=")),)),
    FgtMapping("tranip",            ((_t("destination.nat.ip",            "=")),)),
    FgtMapping("tranip",            ((_t("related.ip",                    "->")),)),
    FgtMapping("tranport",          ((_t("destination.nat.port",          "->")),)),  # to_int
    FgtMapping("dstuser",           ((_t("destination.user.name",         "=")),)),
    FgtMapping("dstunauthuser",     ((_t("destination.user.name",         "=")),)),
    FgtMapping("dstunauthusersource", ((_t("destination.user.group.name", "=")),)),
    FgtMapping("rcvdbyte",          ((_t("destination.bytes",             "->")),)),  # to_int
    FgtMapping("rcvdbyte",          ((_t("network.bytes",                 "->")),)),
    FgtMapping("rcvdpkt",           ((_t("destination.packets",           "->")),)),  # to_int
    FgtMapping("rcvdpkt",           ((_t("network.packets",               "->")),)),
    FgtMapping("dstname",           ((_t("destination.address",           "=")),)),
    # observer
    FgtMapping("dstintf",           ((_t("observer.egress.interface.name",  "=")),)),
    FgtMapping("srcintf",           ((_t("observer.ingress.interface.name", "=")),)),
    FgtMapping("dstzone",           ((_t("observer.egress.zone",            "=")),)),
    FgtMapping("srczone",           ((_t("observer.ingress.zone",           "=")),)),
    # network
    FgtMapping("vrf",               ((_t("network.vrf",                   "=")),)),
    FgtMapping("service",           ((_t("network.protocol",              "=")),)),
    FgtMapping("app",               ((_t("network.application",           "=")),)),
    FgtMapping("proto",             ((_t("network.iana_number",           "->")),)),  # to_int
    FgtMapping("proto",             ((_t("network.transport",             "->")),)),  # IANA lookup
    FgtMapping("proto",             ((_t("network.community_id",          "->")),)),
    # url
    FgtMapping("url",               ((_t("url.original",                  "=")),)),
    FgtMapping("url",               ((_t("url.path",                      "->")),)),  # parse_url
    FgtMapping("url",               ((_t("url.query",                     "->")),)),  # parse_url
    FgtMapping("url",               ((_t("url.registered_domain",         "->")),)),  # parse_etld
    FgtMapping("url",               ((_t("url.top_level_domain",          "->")),)),  # parse_etld
    FgtMapping("hostname",          ((_t("url.domain",                    "=")),)),
    FgtMapping("hostname",          ((_t("url.registered_domain",         "->")),)),  # parse_etld
    FgtMapping("hostname",          ((_t("url.top_level_domain",          "->")),)),  # parse_etld
    # rule
    FgtMapping("policyid",          ((_t("rule.id",                       "=")),)),
    FgtMapping("policyname",        ((_t("rule.name",                     "=")),)),
    FgtMapping("policytype",        ((_t("rule.ruleset",                  "=")),)),
    FgtMapping("poluuid",           ((_t("rule.uuid",                     "=")),)),
    FgtMapping("comment",           ((_t("rule.comment",                  "=")),)),
    # session
    FgtMapping("sessionid",         ((_t("session.id",                   "=")),)),
    # http
    FgtMapping("httpmethod",        ((_t("http.request.method",           "=")),)),
    FgtMapping("statuscode",        ((_t("http.response.status_code",     "->")),)),  # integer parse
    FgtMapping("referralurl",       ((_t("http.request.referrer",         "=")),)),
    # user agent
    FgtMapping("agent",             ((_t("user_agent.original",           "=")),)),
    # event classification
    FgtMapping("msg",               ((_t("message",                       "=")),)),
    FgtMapping("level",             ((_t("log.level",                     "=")),)),
    # geo
    FgtMapping("srccountry",        ((_t("source.geo.country_name",       "=")),)),
    FgtMapping("srccity",           ((_t("source.geo.city_name",          "=")),)),
    FgtMapping("dstcountry",        ((_t("destination.geo.country_name",  "=")),)),
    FgtMapping("dstcity",           ((_t("destination.geo.city_name",     "=")),)),
    # observer
    FgtMapping("devid",             ((_t("observer.serial_number",        "=")),)),
]

UTM_MAPPINGS: list[FgtMapping] = [
    # event
    FgtMapping("tz",                ((_t("event.timezone",                "=")),)),
    FgtMapping("logid",             ((_t("event.code",                    "=")),)),
    # source
    FgtMapping("srcip",             ((_t("source.ip",                     "=")),)),
    FgtMapping("srcip",             ((_t("network.community_id",          "->")),)),
    FgtMapping("srcip",             ((_t("network.direction",             "->")),)),
    FgtMapping("srcip",             ((_t("related.ip",                    "->")),)),
    FgtMapping("srcport",           ((_t("source.port",                   "->")),)),  # to_int; VoIP uses src_port
    FgtMapping("srcmac",            ((_t("source.mac",                    "=")),)),
    FgtMapping("transip",           ((_t("source.nat.ip",                 "=")),)),
    FgtMapping("transip",           ((_t("related.ip",                    "->")),)),
    FgtMapping("transport",         ((_t("source.nat.port",               "->")),)),
    FgtMapping("transport",         ((_t("network.transport_port",        "->")),)),
    FgtMapping("user",              ((_t("source.user.name",              "=")),)),
    FgtMapping("unauthuser",        ((_t("source.user.name",              "=")),)),
    FgtMapping("group",             ((_t("source.user.group.name",        "=")),)),
    FgtMapping("unauthusersource",  ((_t("source.user.group.name",        "=")),)),
    FgtMapping("crscore",           ((_t("source.risk.static_score",      "->")),)),  # to_int; UTM uses source.risk not host.risk
    FgtMapping("crlevel",           ((_t("source.risk.static_level",      "=")),)),
    FgtMapping("sentbyte",          ((_t("source.bytes",                  "->")),)),  # to_int
    FgtMapping("sentbyte",          ((_t("network.bytes",                 "->")),)),
    FgtMapping("srcdomain",         ((_t("source.domain",                 "=")),)),
    # destination
    FgtMapping("dstip",             ((_t("destination.ip",                "=")),)),
    FgtMapping("dstip",             ((_t("network.community_id",          "->")),)),
    FgtMapping("dstip",             ((_t("network.direction",             "->")),)),
    FgtMapping("dstip",             ((_t("related.ip",                    "->")),)),
    FgtMapping("dstport",           ((_t("destination.port",              "->")),)),  # to_int; VoIP uses dst_port
    FgtMapping("dstport",           ((_t("network.transport_port",        "->")),)),
    FgtMapping("dstuser",           ((_t("destination.user.name",         "=")),)),
    FgtMapping("rcvdbyte",          ((_t("destination.bytes",             "->")),)),  # to_int
    FgtMapping("rcvdbyte",          ((_t("network.bytes",                 "->")),)),
    # dns
    FgtMapping("ipaddr",            ((_t("dns.resolved_ip",               "->")),)),  # split(",") + strip
    FgtMapping("qclass",            ((_t("dns.question.class",            "=")),)),
    FgtMapping("qname",             ((_t("dns.question.name",             "=")),)),
    FgtMapping("qname",             ((_t("dns.question.registered_domain", "->")),)),  # parse_etld
    FgtMapping("qname",             ((_t("dns.question.top_level_domain", "->")),)),   # parse_etld
    FgtMapping("qtype",             ((_t("dns.question.type",             "=")),)),
    FgtMapping("xid",               ((_t("dns.id",                        "=")),)),
    # observer
    FgtMapping("dstintf",           ((_t("observer.egress.interface.name",  "=")),)),  # VoIP uses dst_int
    FgtMapping("srcintf",           ((_t("observer.ingress.interface.name", "=")),)),  # VoIP uses src_int
    FgtMapping("dstzone",           ((_t("observer.egress.zone",            "=")),)),
    FgtMapping("srczone",           ((_t("observer.ingress.zone",           "=")),)),
    # rule
    FgtMapping("policyid",          ((_t("rule.id",                       "=")),)),   # VoIP uses policy_id
    FgtMapping("policytype",        ((_t("rule.ruleset",                  "=")),)),
    FgtMapping("poluuid",           ((_t("rule.uuid",                     "=")),)),
    # session
    FgtMapping("sessionid",         ((_t("session.id",                   "=")),)),
    FgtMapping("session_id",        ((_t("session.id",                   "=")),)),   # VoIP uses session_id
    # network
    FgtMapping("vrf",               ((_t("network.vrf",                   "=")),)),
    FgtMapping("service",           ((_t("network.protocol",              "=")),)),   # VoIP uses voip_proto
    FgtMapping("app",               ((_t("network.application",           "=")),)),
    FgtMapping("proto",             ((_t("network.iana_number",           "->")),)),  # to_int
    FgtMapping("proto",             ((_t("network.transport",             "->")),)),  # IANA lookup
    FgtMapping("proto",             ((_t("network.community_id",          "->")),)),
    # url
    FgtMapping("url",               ((_t("url.original",                  "=")),)),
    FgtMapping("url",               ((_t("url.path",                      "->")),)),
    FgtMapping("url",               ((_t("url.query",                     "->")),)),
    FgtMapping("url",               ((_t("url.registered_domain",         "->")),)),
    FgtMapping("url",               ((_t("url.top_level_domain",          "->")),)),
    FgtMapping("hostname",          ((_t("url.domain",                    "=")),)),
    FgtMapping("hostname",          ((_t("url.registered_domain",         "->")),)),
    FgtMapping("hostname",          ((_t("url.top_level_domain",          "->")),)),
    # tls
    FgtMapping("ccertissuer",       ((_t("tls.client.issuer",             "=")),)),
    FgtMapping("scertcname",        ((_t("tls.client.server_name",        "=")),)),
    FgtMapping("scertissuer",       ((_t("tls.server.issuer",             "=")),)),
    FgtMapping("sni",               ((_t("tls.client.server_name",        "=")),)),
    FgtMapping("tlsver",            ((_t("tls.version",                   "=")),)),
    # file
    FgtMapping("filehash",          ((_t("file.hash.sha1",                "=")),)),
    FgtMapping("filename",          ((_t("file.name",                     "=")),)),
    FgtMapping("filesize",          ((_t("file.size",                     "=")),)),
    FgtMapping("filetype",          ((_t("file.extension",                "=")),)),
    # http (from rawdata and direct fields)
    FgtMapping("httpmethod",        ((_t("http.request.method",           "=")),)),
    FgtMapping("rawdata",           ((_t("http.request.mime_type",        "->")),)),  # parsed from rawdata blob
    FgtMapping("rawdata",           ((_t("http.response.mime_type",       "->")),)),
    FgtMapping("rawdata",           ((_t("http.request.referrer",         "->")),)),
    # user agent
    FgtMapping("agent",             ((_t("user_agent.original",           "=")),)),
    # event classification
    FgtMapping("msg",               ((_t("message",                       "=")),)),
    FgtMapping("level",             ((_t("log.level",                     "=")),)),
    FgtMapping("ref",               ((_t("event.reference",               "=")),)),
    # geo
    FgtMapping("srccountry",        ((_t("source.geo.country_name",       "=")),)),
    FgtMapping("dstcountry",        ((_t("destination.geo.country_name",  "=")),)),
    # observer
    FgtMapping("devid",             ((_t("observer.serial_number",        "=")),)),
    # email (DLP/Virus/SMTP contexts)
    FgtMapping("from",              ((_t("email.from.address",            "=")),)),
    FgtMapping("to",                ((_t("email.to.address",              "=")),)),
    FgtMapping("sender",            ((_t("email.sender.address",          "=")),)),
    FgtMapping("recipient",         ((_t("email.to.address",              "=")),)),
    FgtMapping("cc",                ((_t("email.cc.address",              "=")),)),
    FgtMapping("subject",           ((_t("email.subject",                 "=")),)),
    # threat indicators
    FgtMapping("attack",            ((_t("threat.indicator.name",         "=")),)),
    FgtMapping("virus",             ((_t("threat.indicator.name",         "=")),)),
    FgtMapping("attackid",          ((_t("threat.indicator.id",           "->")),)),  # uint32 → string
    FgtMapping("virusid",           ((_t("threat.indicator.id",           "->")),)),
    FgtMapping("botnetip",          ((_t("threat.indicator.ip",           "=")),)),
    FgtMapping("botnetip",          ((_t("related.ip",                    "->")),)),
    FgtMapping("botnetdomain",      ((_t("threat.indicator.url.domain",   "->")),)),
    # x-forwarded-for (may be comma-separated chain; parse to extract client IP)
    FgtMapping("forwardedfor",      ((_t("network.forwarded_ip",          "->")),)),
    FgtMapping("forwardedfor",      ((_t("related.ip",                    "->")),)),
]

EVENT_MAPPINGS: list[FgtMapping] = [
    # event
    FgtMapping("tz",                ((_t("event.timezone",                "=")),)),
    FgtMapping("logid",             ((_t("event.code",                    "=")),)),
    FgtMapping("duration",          ((_t("event.duration",                "->")),)),  # seconds × 10^9
    # source
    FgtMapping("saddr",             ((_t("source.address",                "=")),)),
    FgtMapping("srcip",             ((_t("source.ip",                     "=")),)),
    FgtMapping("srcmac",            ((_t("source.mac",                    "=")),)),
    FgtMapping("sentbyte",          ((_t("source.bytes",                  "=")),)),   # no to_int in event VRL
    FgtMapping("srcport",           ((_t("source.port",                   "->")),)),  # to_int
    # destination
    FgtMapping("daddr",             ((_t("destination.address",           "=")),)),
    FgtMapping("dstip",             ((_t("destination.ip",                "=")),)),
    FgtMapping("rcvdbyte",          ((_t("destination.bytes",             "=")),)),   # no to_int in event VRL
    FgtMapping("dstport",           ((_t("destination.port",              "->")),)),  # to_int
    # file
    FgtMapping("filename",          ((_t("file.name",                     "=")),)),
    FgtMapping("filesize",          ((_t("file.size",                     "=")),)),
    # network
    FgtMapping("service",           ((_t("network.protocol",              "=")),)),
    FgtMapping("proto",             ((_t("network.iana_number",           "->")),)),  # to_int
    FgtMapping("proto",             ((_t("network.transport",             "->")),)),  # IANA lookup
    # user agent
    FgtMapping("agent",             ((_t("user_agent.original",           "=")),)),
    # event classification
    FgtMapping("msg",               ((_t("message",                       "=")),)),
    FgtMapping("level",             ((_t("log.level",                     "=")),)),
    # geo
    FgtMapping("srccountry",        ((_t("source.geo.country_name",       "=")),)),
    # observer
    FgtMapping("devid",             ((_t("observer.serial_number",        "=")),)),
    # vulnerability
    FgtMapping("cveid",             ((_t("vulnerability.id",              "=")),)),
    # email (notification contexts)
    FgtMapping("from",              ((_t("email.from.address",            "=")),)),
]

LOG_TYPE_SPECS: list[tuple[str, list[FgtMapping]]] = [
    ("traffic", TRAFFIC_MAPPINGS),
    ("utm",     UTM_MAPPINGS),
    ("event",   EVENT_MAPPINGS),
]

OUTPUT_COLS: list[str] = [
    "Log Field Name",
    "Data Type",
    "Length",
    "Description",
    "Mapping Type",
    "ECS Field",
    "ECS Type",
    "ECS Description",
]


# ---------------------------------------------------------------------------
# Core transform (pure, no I/O)
# ---------------------------------------------------------------------------

def build_lookup(mappings: list[FgtMapping]) -> dict[str, list[EcsTarget]]:
    """Merge all EcsTarget entries for the same fgt_field into one ordered list."""
    result: dict[str, list[EcsTarget]] = {}
    for m in mappings:
        result.setdefault(m.fgt_field, []).extend(m.targets)
    return result


def _targets_to_row(targets: list[EcsTarget]) -> tuple[str, str, str, str]:
    """Convert a list of EcsTargets to the four ECS column values joined with newlines."""
    mapping_types: list[str] = []
    ecs_fields: list[str] = []
    ecs_types: list[str] = []
    ecs_descs: list[str] = []
    for t in targets:
        field_def = ECS_FIELD_REGISTRY.get(t.ecs_field)
        if field_def is None:
            raise KeyError(f"ECS field {t.ecs_field!r} not found in ECS_FIELD_REGISTRY")
        mapping_types.append(t.mapping_type)
        ecs_fields.append(t.ecs_field)
        ecs_types.append(field_def.ecs_type)
        ecs_descs.append(field_def.description)
    return (
        "\n".join(mapping_types),
        "\n".join(ecs_fields),
        "\n".join(ecs_types),
        "\n".join(ecs_descs),
    )


def apply_mappings(df: pd.DataFrame, lookup: dict[str, list[EcsTarget]]) -> pd.DataFrame:
    """Left-join ECS columns onto a fields DataFrame.

    Uses vectorized Series.map; fields without a mapping get empty ECS columns.
    """
    row_map: dict[str, tuple[str, str, str, str]] = {
        fgt_field: _targets_to_row(targets)
        for fgt_field, targets in lookup.items()
    }
    ecs_cols = df["Log Field Name"].map(
        lambda fgt: row_map.get(fgt, ("", "", "", ""))
    )
    ecs_df = pd.DataFrame(
        ecs_cols.tolist(),
        columns=["Mapping Type", "ECS Field", "ECS Type", "ECS Description"],
        index=df.index,
    )
    return pd.concat([df, ecs_df], axis=1)[OUTPUT_COLS]


# ---------------------------------------------------------------------------
# I/O
# ---------------------------------------------------------------------------

def load_fields_csv(path: Path) -> pd.DataFrame:
    """Read a *_fields.csv and return its DataFrame, or empty DataFrame if missing."""
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def write_ecs_csv(path: Path, df: pd.DataFrame) -> None:
    """Write the ECS-mapped DataFrame to path, creating the ECS/ directory if needed."""
    path.parent.mkdir(exist_ok=True)
    df.to_csv(path, index=False)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    root = Path(__file__).parent
    major_dirs = sorted(
        (d for d in root.iterdir() if d.is_dir() and d.name.replace(".", "").isdigit() and d.name.count(".") == 1),
        key=lambda d: tuple(int(x) for x in d.name.split(".")),
    )

    for major_dir in major_dirs:
        for log_type, mappings in LOG_TYPE_SPECS:
            src = major_dir / "fields" / f"{log_type}_fields.csv"
            dst = major_dir / "ECS"    / f"{log_type}_ecs.csv"

            df = load_fields_csv(src)
            if df.empty:
                print(f"Skipped (no source): {src}")
                continue

            lookup = build_lookup(mappings)
            result = apply_mappings(df, lookup)
            write_ecs_csv(dst, result)

            mapped = result["ECS Field"].astype(bool).sum()
            print(f"Written: {dst} ({len(result)} fields, {mapped} mapped)")


if __name__ == "__main__":
    main()
