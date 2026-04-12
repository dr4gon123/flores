# FortiGate 7.2.0 — Analysis

[← 7.2 Index](../INDEX.md)

**Traffic**

| Category | Fields | LOGIDs |
|----------|--------|--------|
| FORWARD | 151 | 15 |
| LOCAL | 137 | 2 |
| MULTICAST | 137 | 2 |
| SNIFFER | 151 | 2 |
| ZTNA | 137 | 1 |

**Event**

| Category | Fields | LOGIDs |
|----------|--------|--------|
| CIFS-AUTH-FAIL | 30 | 4 |
| CONNECTOR | 18 | 6 |
| ENDPOINT | 41 | 12 |
| FORTIEXTENDER | 16 | 11 |
| HA | 30 | 34 |
| REST-API | 18 | 2 |
| ROUTER | 20 | 10 |
| SDWAN | 37 | 13 |
| SECURITY-RATING | 20 | 2 |
| SWITCH-CONTROLLER | 22 | 50 |
| SYSTEM | 147 | 536 |
| USER | 40 | 49 |
| VPN | 59 | 81 |
| WAD | 38 | 28 |
| WIRELESS | 82 | 186 |

**UTM** *(including GTP)*

| Type | Fields | LOGIDs | Categories | Category List |
|------|--------|--------|------------|---------------|
| AV | 94 | 80 | 15 | ANALYTICS, COMMAND-BLOCKED, CONTENT-DISARM, EMS-THREAT-FEED, FILENAME, FILETYPE-EXECUTABLE, FORTINDR, FORTISANDBOX, INFECTED, MALWARE-LIST, MIMEFRAGMENTED, OUTBREAK-PREVENTION, OVERSIZE, SCANERROR, SWITCHPROTO |
| Anomaly | 46 | 3 | 1 | ANOMALY |
| App | 72 | 14 | 3 | PORT-VIOLATION, PROTOCOL-VIOLATION, SIGNATURE |
| DLP | 78 | 4 | 2 | DLP, DLP-DOCSOURCE |
| DNS | 54 | 12 | 2 | DNS-QUERY, DNS-RESPONSE |
| Email | 56 | 5 | 5 | BANNEDWORD, EMAIL, FTGD_ERR, SPAM, WEBMAIL |
| FILE-FILTER | 68 | 2 | 1 | FILE-FILTER |
| GTP | 84 | 18 | 2 | GTP-ALL, PFCP-ALL |
| ICAP | 35 | 3 | 1 | ICAP |
| IPS | 66 | 6 | 3 | BOTNET, MALICIOUS-URL, SIGNATURE |
| SSH | 42 | 8 | 3 | SSH-CHANNEL, SSH-COMMAND, SSH-HOSTKEY |
| SSL | 63 | 18 | 5 | SSL-ANOMALY, SSL-EXEMPT, SSL-HANDSHAKE, SSL-NEGOTIATION, SSL-SERVER-CERT-INFO |
| VoIP | 44 | 7 | 1 | VOIP |
| WAF | 52 | 12 | 6 | WAF-ADDRESS-LIST, WAF-CUSTOM-SIGNATURE, WAF-HTTP-CONSTRAINT, WAF-HTTP-METHOD, WAF-SIGNATURE, WAF-URL-ACCESS |
| Web | 85 | 55 | 19 | ACTIVEXFILTER, ANTIPHISHING, APPLETFILTER, CONTENT, COOKIEFILTER, FTGD_ALLOW, FTGD_BLK, FTGD_ERR, FTGD_QUOTA, FTGD_QUOTA_COUNTING, FTGD_QUOTA_EXPIRED, HTTP_HEADER_CHANGE, SCRIPTFILTER, SSL-EXEMPT, URLFILTER, URLMONITOR, VIDEOFILTER-CATEGORY, VIDEOFILTER-CHANNEL, WEBFILTER_COMMAND_BLOCK |

### 7.2.0 — Intra-version Inconsistencies

**Summary**

| Conflict Type | Fields |
|--------------|--------|
| Description conflicts | 125 |
| Data Type conflicts | 3 |
| Length conflicts | 16 |

#### Traffic

| Log Field Name | Description | Data Type | Length |
|----------------|-------------|-----------|--------|
| `app` | X |  |  |

`app`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `app` | Application Name | `string` | 96 | SNIFFER<br>ZTNA | 17_-_LOG_ID_TRAFFIC_SNIFFER, 21_-_LOG_ID_TRAFFIC_SNIFFER_STAT<br>24_-_LOG_ID_TRAFFIC_ZTNA |
| `app` | Application name | `string` | 96 | FORWARD<br>LOCAL<br>MULTICAST | 10_-_LOG_ID_TRAFFIC_EXPLICIT_PROXY, 11_-_LOG_ID_TRAFFIC_FAIL_CONN, 13_-_LOG_ID_TRAFFIC_END_FORWARD *(+11 more)*<br>14_-_LOG_ID_TRAFFIC_END_LOCAL, 16_-_LOG_ID_TRAFFIC_START_LOCAL<br>12_-_LOG_ID_TRAFFIC_MULTICAST, 19_-_LOG_ID_TRAFFIC_BROADCAST |

#### Event

| Log Field Name | Description | Data Type | Length |
|----------------|-------------|-----------|--------|
| `action` | X |  |  |
| `cfgattr` | X |  |  |
| `cfgobj` | X |  |  |
| `cfgpath` | X |  |  |
| `cfgtid` | X |  |  |
| `count` | X |  |  |
| `date` | X |  |  |
| `devid` | X |  |  |
| `dst_int` | X |  |  |
| `dstip` | X |  |  |
| `dstport` | X |  |  |
| `duration` | X |  |  |
| `error` | X |  |  |
| `eventtime` | X |  |  |
| `host` | X |  |  |
| `hostname` | X |  |  |
| `ip` | X |  |  |
| `level` | X |  |  |
| `logdesc` | X |  |  |
| `logid` | X |  |  |
| `mode` | X |  |  |
| `msg` | X |  |  |
| `name` | X |  |  |
| `policyid` | X |  |  |
| `profile` | X |  |  |
| `scope` | X |  |  |
| `seq` | X |  |  |
| `server` | X |  |  |
| `sn` | X |  |  |
| `src_int` | X |  |  |
| `srcip` | X |  |  |
| `srcport` | X |  |  |
| `subtype` | X |  |  |
| `time` | X |  |  |
| `type` | X |  |  |
| `tz` | X |  |  |
| `ui` | X |  |  |
| `user` | X |  |  |
| `vd` | X |  |  |
| `version` | X |  |  |

`action`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `action` | *(empty)* | `string` | 65 | FORTIEXTENDER<br>REST-API<br>SWITCH-CONTROLLER | 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+13 more)* |
| `action` | Policy Action | `string` | 65 | CONNECTOR<br>ENDPOINT<br>ROUTER<br>SYSTEM<br>USER<br>VPN<br>WAD<br>WIRELESS | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE<br>20401_-_LOG_ID_ROUTER_CLEAR, 51000_-_LOG_ID_NB_TBL_CHG<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20021_-_LOG_ID_MAIL_RESENT *(+223 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+30 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+72 more)*<br>48000_-_LOG_ID_WAD_SSL_RCV_HS, 48001_-_LOG_ID_WAD_SSL_RCV_WRG_HS, 48002_-_LOG_ID_WAD_SSL_SENT_HS *(+21 more)*<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+183 more)* |

`cfgattr`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `cfgattr` | *(empty)* | `string` | 4096 | SWITCH-CONTROLLER | 32569_-_LOG_ID_FSW_SWITCH_LOG_EVENT, 32693_-_LOG_ID_FGT_SWITCH_GROUP_SWC, 32694_-_LOG_ID_FGT_SWITCH_GROUP_POE *(+5 more)* |
| `cfgattr` | Configuration attribute | `string` | 4096 | SYSTEM | 44546_-_LOGID_EVENT_CONFIG_ATTR, 44547_-_LOGID_EVENT_CONFIG_OBJATTR, 44549_-_LOGID_EVENT_CONFIG_OBJATTR_MTNER *(+1 more)* |

`cfgobj`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `cfgobj` | *(empty)* | `string` | 256 | SWITCH-CONTROLLER | 32569_-_LOG_ID_FSW_SWITCH_LOG_EVENT, 32693_-_LOG_ID_FGT_SWITCH_GROUP_SWC, 32694_-_LOG_ID_FGT_SWITCH_GROUP_POE *(+5 more)* |
| `cfgobj` | Configuration object | `string` | 256 | CONNECTOR<br>SYSTEM | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE<br>44545_-_LOGID_EVENT_CONFIG_OBJ, 44547_-_LOGID_EVENT_CONFIG_OBJATTR, 44549_-_LOGID_EVENT_CONFIG_OBJATTR_MTNER *(+1 more)* |

`cfgpath`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `cfgpath` | *(empty)* | `string` | 128 | SWITCH-CONTROLLER | 32569_-_LOG_ID_FSW_SWITCH_LOG_EVENT, 32693_-_LOG_ID_FGT_SWITCH_GROUP_SWC, 32694_-_LOG_ID_FGT_SWITCH_GROUP_POE *(+5 more)* |
| `cfgpath` | Configuration path | `string` | 128 | SYSTEM | 44544_-_LOGID_EVENT_CONFIG_PATH, 44545_-_LOGID_EVENT_CONFIG_OBJ, 44546_-_LOGID_EVENT_CONFIG_ATTR *(+5 more)* |

`cfgtid`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `cfgtid` | *(empty)* | `uint32` | 10 | SWITCH-CONTROLLER | 32569_-_LOG_ID_FSW_SWITCH_LOG_EVENT, 32693_-_LOG_ID_FGT_SWITCH_GROUP_SWC, 32694_-_LOG_ID_FGT_SWITCH_GROUP_POE *(+5 more)* |
| `cfgtid` | Config transaction id | `uint32` | 10 | SYSTEM | 44544_-_LOGID_EVENT_CONFIG_PATH, 44545_-_LOGID_EVENT_CONFIG_OBJ, 44546_-_LOGID_EVENT_CONFIG_ATTR *(+5 more)* |

`count`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `count` | Count | `uint32` | 10 | SYSTEM | 20003_-_LOG_ID_MAIL_SENT_FAIL, 20021_-_LOG_ID_MAIL_RESENT, 22100_-_LOG_ID_QUAR_DROP_TRAN_JOB *(+2 more)* |
| `count` | Count of EndPoint Connections | `uint32` | 10 | ENDPOINT | 45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE |
| `count` | Number of Packets | `uint32` | 10 | USER | 38656_-_LOGID_EVENT_RAD_RPT_PROTO_ERROR, 38657_-_LOGID_EVENT_RAD_RPT_PROF_NOT_FOUND, 38658_-_LOGID_EVENT_RAD_RPT_CTX_NOT_FOUND *(+4 more)* |

`date`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `date` | *(empty)* | `string` | 10 | CIFS-AUTH-FAIL<br>SWITCH-CONTROLLER | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+47 more)* |
| `date` | Date | `string` | 10 | CONNECTOR<br>ENDPOINT<br>FORTIEXTENDER<br>HA<br>REST-API<br>ROUTER<br>SDWAN<br>SECURITY-RATING<br>SYSTEM<br>USER<br>VPN<br>WAD<br>WIRELESS | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+9 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+31 more)*<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY, 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+533 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>40960_-_LOGID_EVENT_WAD_WEBPROXY_FWD_SRV_ERROR, 48000_-_LOG_ID_WAD_SSL_RCV_HS, 48001_-_LOG_ID_WAD_SSL_RCV_WRG_HS *(+25 more)*<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+183 more)* |

`devid`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `devid` | *(empty)* | `string` | 16 | CIFS-AUTH-FAIL<br>SWITCH-CONTROLLER | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+47 more)* |
| `devid` | Device ID | `string` | 16 | CONNECTOR<br>ENDPOINT<br>FORTIEXTENDER<br>HA<br>REST-API<br>ROUTER<br>SDWAN<br>SECURITY-RATING<br>SYSTEM<br>USER<br>VPN<br>WAD<br>WIRELESS | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+9 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+31 more)*<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY, 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+533 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>40960_-_LOGID_EVENT_WAD_WEBPROXY_FWD_SRV_ERROR, 48000_-_LOG_ID_WAD_SSL_RCV_HS, 48001_-_LOG_ID_WAD_SSL_RCV_WRG_HS *(+25 more)*<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+183 more)* |

`dst_int`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `dst_int` | *(empty)* | `string` | 64 | CIFS-AUTH-FAIL | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)* |
| `dst_int` | Destination Interface | `string` | 64 | SYSTEM | 22810_-_LOG_ID_SCANUNIT_ERROR_BLOCK, 22811_-_LOG_ID_SCANUNIT_ERROR_PASS, 43776_-_LOG_ID_EVENT_NAC_QUARANTINE *(+1 more)* |

`dstip`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `dstip` | *(empty)* | `ip` | 39 | CIFS-AUTH-FAIL | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)* |
| `dstip` | Destination IP | `ip` | 39 | SYSTEM<br>USER<br>WAD | 20007_-_LOG_ID_SOCKET_EXHAUSTED, 20214_-_LOG_ID_LOCAL_OUT_IOC, 22810_-_LOG_ID_SCANUNIT_ERROR_BLOCK *(+14 more)*<br>43008_-_LOG_ID_EVENT_AUTH_SUCCESS, 43009_-_LOG_ID_EVENT_AUTH_FAILED, 43010_-_LOG_ID_EVENT_AUTH_LOCKOUT *(+18 more)*<br>48000_-_LOG_ID_WAD_SSL_RCV_HS, 48001_-_LOG_ID_WAD_SSL_RCV_WRG_HS, 48002_-_LOG_ID_WAD_SSL_SENT_HS *(+24 more)* |

`dstport`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `dstport` | *(empty)* | `uint16` | 5 | CIFS-AUTH-FAIL | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)* |
| `dstport` | Destination Protocol Port | `uint16` | 5 | SYSTEM<br>WAD | 20007_-_LOG_ID_SOCKET_EXHAUSTED, 20214_-_LOG_ID_LOCAL_OUT_IOC, 22223_-_LOG_ID_EXT_RESOURCE_DEBUG *(+8 more)*<br>48000_-_LOG_ID_WAD_SSL_RCV_HS, 48001_-_LOG_ID_WAD_SSL_RCV_WRG_HS, 48002_-_LOG_ID_WAD_SSL_SENT_HS *(+24 more)* |

`duration`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `duration` | Duration | `uint32` | 10 | SYSTEM<br>USER<br>VPN | 22016_-_LOG_ID_IPPOOLPBA_DEALLOCATE, 22100_-_LOG_ID_QUAR_DROP_TRAN_JOB, 32003_-_LOG_ID_ADMIN_LOGOUT *(+5 more)*<br>38656_-_LOGID_EVENT_RAD_RPT_PROTO_ERROR, 38657_-_LOGID_EVENT_RAD_RPT_PROF_NOT_FOUND, 38658_-_LOGID_EVENT_RAD_RPT_CTX_NOT_FOUND *(+3 more)*<br>37138_-_MESGID_CONN_UPDOWN, 37141_-_MESGID_CONN_STATS, 39425_-_LOG_ID_EVENT_SSL_VPN_USER_TUNNEL_DOWN *(+3 more)* |
| `duration` | Duration of the last threatening packed captured from TA | `uint32` | 10 | WIRELESS | 43534_-_LOG_ID_EVENT_WIRELESS_WIDS_LONG_DUR |

`error`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `error` | *(empty)* | `string` | 256 | CIFS-AUTH-FAIL | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)* |
| `error` | Error Reason for Log Upload to Forticloud | `string` | 256 | SYSTEM | 20107_-_LOG_ID_LOG_UPLOAD_ERR, 53301_-_LOG_ID_VNE_PRO_UPDATE_FAILED |

`eventtime`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `eventtime` | *(empty)* | `uint64` | 20 | CIFS-AUTH-FAIL<br>SWITCH-CONTROLLER | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+47 more)* |
| `eventtime` | Event time | `uint64` | 20 | CONNECTOR<br>ENDPOINT<br>FORTIEXTENDER<br>HA<br>REST-API<br>ROUTER<br>SDWAN<br>SECURITY-RATING<br>SYSTEM<br>USER<br>VPN<br>WAD<br>WIRELESS | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+9 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+31 more)*<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY, 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+533 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>40960_-_LOGID_EVENT_WAD_WEBPROXY_FWD_SRV_ERROR, 48000_-_LOG_ID_WAD_SSL_RCV_HS, 48001_-_LOG_ID_WAD_SSL_RCV_WRG_HS *(+25 more)*<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+183 more)* |

`host`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `host` | *(empty)* | `string` | 256 | SYSTEM | 22223_-_LOG_ID_EXT_RESOURCE_DEBUG |
| `host` | Host Name | `string` | 256 | WAD | 48101_-_LOG_ID_WAD_AUTH_FAIL_PSK |

`hostname`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `hostname` | *(empty)* | `string` | 128 | HA | 37892_-_MESGID_VC_MOVE_MEMB_STATE |
| `hostname` | Hostname | `string` | 128 | ENDPOINT<br>SYSTEM | 45114_-_LOG_ID_EC_REG_QUARANTINE, 45115_-_LOG_ID_EC_REG_UNQUARANTINE<br>22223_-_LOG_ID_EXT_RESOURCE_DEBUG, 26001_-_LOG_ID_DHCP_ACK, 26002_-_LOG_ID_DHCP_RELEASE *(+3 more)* |

`ip`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `ip` | *(empty)* | `ip` | 39 | FORTIEXTENDER<br>HA<br>SYSTEM<br>WAD<br>WIRELESS | 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR, 46403_-_LOG_ID_EVENT_EXT_REMOTE_EMERG *(+7 more)*<br>37911_-_MESGID_HA_ACTIVITY_INFO<br>22035_-_LOG_ID_CSF_UPSTREAM_SN_CHANGED, 22036_-_LOG_ID_CSF_FGT_CONNECTED, 22037_-_LOG_ID_CSF_FGT_DISCONNECTED *(+9 more)*<br>40960_-_LOGID_EVENT_WAD_WEBPROXY_FWD_SRV_ERROR<br>43522_-_LOG_ID_EVENT_WIRELESS_WTP, 43526_-_LOG_ID_EVENT_WIRELESS_WTPR, 43528_-_LOG_ID_EVENT_WIRELESS_WTPR_ERROR *(+39 more)* |
| `ip` | Source IP | `ip` | 39 | ENDPOINT | 45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+4 more)* |

`level`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `level` | *(empty)* | `string` | 11 | CIFS-AUTH-FAIL<br>SWITCH-CONTROLLER | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+47 more)* |
| `level` | Log Level | `string` | 11 | CONNECTOR<br>ENDPOINT<br>FORTIEXTENDER<br>HA<br>REST-API<br>ROUTER<br>SDWAN<br>SECURITY-RATING<br>SYSTEM<br>USER<br>VPN<br>WAD<br>WIRELESS | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+9 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+31 more)*<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY, 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+533 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>40960_-_LOGID_EVENT_WAD_WEBPROXY_FWD_SRV_ERROR, 48000_-_LOG_ID_WAD_SSL_RCV_HS, 48001_-_LOG_ID_WAD_SSL_RCV_WRG_HS *(+25 more)*<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+183 more)* |

`logdesc`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `logdesc` | *(empty)* | `string` | 4096 | CIFS-AUTH-FAIL<br>SWITCH-CONTROLLER | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+47 more)* |
| `logdesc` | Log Description | `string` | 4096 | CONNECTOR<br>ENDPOINT<br>FORTIEXTENDER<br>HA<br>REST-API<br>ROUTER<br>SDWAN<br>SECURITY-RATING<br>SYSTEM<br>USER<br>VPN<br>WAD<br>WIRELESS | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+9 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+31 more)*<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY, 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+533 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>40960_-_LOGID_EVENT_WAD_WEBPROXY_FWD_SRV_ERROR, 48000_-_LOG_ID_WAD_SSL_RCV_HS, 48001_-_LOG_ID_WAD_SSL_RCV_WRG_HS *(+25 more)*<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+183 more)* |

`logid`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `logid` | *(empty)* | `string` | 10 | CIFS-AUTH-FAIL<br>SWITCH-CONTROLLER | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+47 more)* |
| `logid` | Log ID | `string` | 10 | CONNECTOR<br>ENDPOINT<br>FORTIEXTENDER<br>HA<br>REST-API<br>ROUTER<br>SDWAN<br>SECURITY-RATING<br>SYSTEM<br>USER<br>VPN<br>WAD<br>WIRELESS | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+9 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+31 more)*<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY, 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+533 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>40960_-_LOGID_EVENT_WAD_WEBPROXY_FWD_SRV_ERROR, 48000_-_LOG_ID_WAD_SSL_RCV_HS, 48001_-_LOG_ID_WAD_SSL_RCV_WRG_HS *(+25 more)*<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+183 more)* |

`mode`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `mode` | IPsec VPN ID protection mode | `string` | 12 | VPN | 37127_-_MESGID_NEG_PROGRESS_P1_NOTIF, 37128_-_MESGID_NEG_PROGRESS_P1_ERROR, 37129_-_MESGID_NEG_PROGRESS_P2_NOTIF *(+1 more)* |
| `mode` | Mode | `string` | 12 | SYSTEM | 22800_-_LOG_ID_SCAN_SERV_FAIL |

`msg`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `msg` | *(empty)* | `string` | 4096 | CIFS-AUTH-FAIL<br>SWITCH-CONTROLLER | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+47 more)* |
| `msg` | Log Message | `string` | 4096 | CONNECTOR<br>ENDPOINT<br>FORTIEXTENDER<br>HA<br>ROUTER<br>SDWAN<br>SYSTEM<br>USER<br>VPN<br>WAD<br>WIRELESS | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+9 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+31 more)*<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+530 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>40960_-_LOGID_EVENT_WAD_WEBPROXY_FWD_SRV_ERROR, 48000_-_LOG_ID_WAD_SSL_RCV_HS, 48001_-_LOG_ID_WAD_SSL_RCV_WRG_HS *(+25 more)*<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+183 more)* |

`name`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `name` | *(empty)* | `string` | 128 | SWITCH-CONTROLLER | 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT, 22853_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_MISS, 22861_-_LOG_ID_FLPOLD_NAC_ADD *(+40 more)* |
| `name` | Display Name of the Connection | `string` | 128 | ENDPOINT<br>SYSTEM<br>VPN | 45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE<br>22009_-_LOG_ID_FAIL_FIND_AV_PROFILE, 22203_-_LOG_ID_AUTO_GEN_CERT_FAIL, 22204_-_LOG_ID_AUTO_GEN_CERT_PENDING *(+12 more)*<br>41984_-_LOG_ID_EVENT_VPN_CERT_LOAD, 41985_-_LOG_ID_EVENT_VPN_CERT_REMOVAL, 41986_-_LOG_ID_EVENT_VPN_CERT_REGEN *(+5 more)* |

`policyid`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `policyid` | *(empty)* | `uint32` | 10 | CIFS-AUTH-FAIL | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)* |
| `policyid` | Policy ID | `uint32` | 10 | SYSTEM<br>USER<br>WAD | 43776_-_LOG_ID_EVENT_NAC_QUARANTINE, 43777_-_LOG_ID_EVENT_NAC_ANOMALY_QUARANTINE<br>43008_-_LOG_ID_EVENT_AUTH_SUCCESS, 43009_-_LOG_ID_EVENT_AUTH_FAILED, 43010_-_LOG_ID_EVENT_AUTH_LOCKOUT *(+8 more)*<br>48000_-_LOG_ID_WAD_SSL_RCV_HS, 48001_-_LOG_ID_WAD_SSL_RCV_WRG_HS, 48002_-_LOG_ID_WAD_SSL_SENT_HS *(+24 more)* |

`profile`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `profile` | *(empty)* | `string` | 64 | CIFS-AUTH-FAIL | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)* |
| `profile` | Profile Name | `string` | 64 | SYSTEM<br>WIRELESS | 22223_-_LOG_ID_EXT_RESOURCE_DEBUG, 32001_-_LOG_ID_ADMIN_LOGIN_SUCC, 32053_-_LOG_ID_ADMIN_MTNER_LOGIN_SUCC *(+2 more)*<br>43522_-_LOG_ID_EVENT_WIRELESS_WTP, 43551_-_LOG_ID_EVENT_WIRELESS_WTP_JOIN, 43552_-_LOG_ID_EVENT_WIRELESS_WTP_LEAVE *(+17 more)* |

`scope`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `scope` | *(empty)* | `string` | 16 | SYSTEM | 22040_-_LOG_ID_CSF_DEVICE_JOIN, 22041_-_LOG_ID_CSF_DEVICE_LEAVE, 22042_-_LOG_ID_CSF_DEVICE_UPDATE *(+3 more)* |
| `scope` | FortiGuard Override Scope | `string` | 16 | USER | 43020_-_LOG_ID_EVENT_AUTH_FGOVRD_SUCCESS, 43029_-_LOG_ID_EVENT_AUTH_WARNING_SUCCESS |

`seq`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `seq` | *(empty)* | `string` | 512 | SYSTEM | 32151_-_LOG_ID_ADD_IP6_LOCAL_POL, 32152_-_LOG_ID_CHG_IP6_LOCAL_POL, 32153_-_LOG_ID_DEL_IP6_LOCAL_POL *(+3 more)* |
| `seq` | Sequence | `string` | 512 | VPN<br>WIRELESS | 37131_-_MESGID_ESP_ERROR, 37132_-_MESGID_ESP_CRITICAL<br>43530_-_LOG_ID_EVENT_WIRELESS_WIDS_WL_BRIDGE, 43531_-_LOG_ID_EVENT_WIRELESS_WIDS_BR_DEAUTH, 43532_-_LOG_ID_EVENT_WIRELESS_WIDS_NL_PBRESP *(+5 more)* |

`server`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `server` | AD server FQDN or IP | `string` | 64 | USER<br>WIRELESS | 38031_-_LOG_ID_FSSO_LOGON, 38032_-_LOG_ID_FSSO_LOGOFF, 38033_-_LOG_ID_FSSO_SVR_STATUS *(+4 more)*<br>43658_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_NO_RESP, 43659_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_DIFF_OFFER, 43660_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_NO_ACK *(+22 more)* |
| `server` | Server IP Address | `string` | 64 | SYSTEM | 20107_-_LOG_ID_LOG_UPLOAD_ERR, 20108_-_LOG_ID_LOG_UPLOAD_DONE, 22912_-_LOG_ID_FDS_SRV_ERRCON *(+12 more)* |

`sn`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `sn` | *(empty)* | `string` | 64 | SWITCH-CONTROLLER | 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT, 22853_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_MISS, 22861_-_LOG_ID_FLPOLD_NAC_ADD *(+40 more)* |
| `sn` | Serial Number | `string` | 64 | ENDPOINT<br>FORTIEXTENDER<br>HA<br>SYSTEM<br>WIRELESS | 45124_-_LOG_ID_EC_VPND_CONNECT, 45125_-_LOG_ID_EC_VPND_DISCONNECT<br>46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR, 46403_-_LOG_ID_EVENT_EXT_REMOTE_EMERG *(+7 more)*<br>37892_-_MESGID_VC_MOVE_MEMB_STATE, 37893_-_MESGID_VC_DETECT_MEMB_DEAD, 37894_-_MESGID_VC_DETECT_MEMB_JOIN<br>22031_-_LOG_ID_SUCCESS_CSF_LOG_SYNC_CONFIG_CHANGED, 22032_-_LOG_ID_CSF_LOOP_FOUND, 22035_-_LOG_ID_CSF_UPSTREAM_SN_CHANGED *(+24 more)*<br>43522_-_LOG_ID_EVENT_WIRELESS_WTP, 43524_-_LOG_ID_EVENT_WIRELESS_STA, 43526_-_LOG_ID_EVENT_WIRELESS_WTPR *(+145 more)* |
| `sn` | Serial number for login or logout events. Used to correlate login and logout events. | `string` | 64 | SYSTEM | 32001_-_LOG_ID_ADMIN_LOGIN_SUCC, 32002_-_LOG_ID_ADMIN_LOGIN_FAIL, 32003_-_LOG_ID_ADMIN_LOGOUT |

`src_int`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `src_int` | *(empty)* | `string` | 64 | CIFS-AUTH-FAIL | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)* |
| `src_int` | Source Interface | `string` | 64 | ROUTER<br>SYSTEM | 51000_-_LOG_ID_NB_TBL_CHG<br>22810_-_LOG_ID_SCANUNIT_ERROR_BLOCK, 22811_-_LOG_ID_SCANUNIT_ERROR_PASS, 43776_-_LOG_ID_EVENT_NAC_QUARANTINE *(+1 more)* |

`srcip`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `srcip` | *(empty)* | `ip` | 39 | CIFS-AUTH-FAIL<br>SWITCH-CONTROLLER | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22904_-_LOG_ID_CAPUTP_SESSION_NOTIF |
| `srcip` | Source IP | `ip` | 39 | ENDPOINT<br>ROUTER<br>SYSTEM<br>USER<br>WAD<br>WIRELESS | 45071_-_LOG_ID_FCC_VULN_SCAN<br>51000_-_LOG_ID_NB_TBL_CHG<br>20007_-_LOG_ID_SOCKET_EXHAUSTED, 20214_-_LOG_ID_LOCAL_OUT_IOC, 22810_-_LOG_ID_SCANUNIT_ERROR_BLOCK *(+12 more)*<br>38031_-_LOG_ID_FSSO_LOGON, 38032_-_LOG_ID_FSSO_LOGOFF, 38662_-_LOGID_EVENT_RAD_STAT_PROTO_ERROR *(+30 more)*<br>48000_-_LOG_ID_WAD_SSL_RCV_HS, 48001_-_LOG_ID_WAD_SSL_RCV_WRG_HS, 48002_-_LOG_ID_WAD_SSL_SENT_HS *(+24 more)*<br>43524_-_LOG_ID_EVENT_WIRELESS_STA, 43572_-_LOG_ID_EVENT_WIRELESS_STA_ASSO, 43573_-_LOG_ID_EVENT_WIRELESS_STA_AUTH *(+22 more)* |

`srcport`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `srcport` | *(empty)* | `uint16` | 5 | CIFS-AUTH-FAIL | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)* |
| `srcport` | Source port | `uint16` | 5 | SYSTEM<br>WAD | 20007_-_LOG_ID_SOCKET_EXHAUSTED, 20214_-_LOG_ID_LOCAL_OUT_IOC, 22810_-_LOG_ID_SCANUNIT_ERROR_BLOCK *(+4 more)*<br>48000_-_LOG_ID_WAD_SSL_RCV_HS, 48001_-_LOG_ID_WAD_SSL_RCV_WRG_HS, 48002_-_LOG_ID_WAD_SSL_SENT_HS *(+24 more)* |

`subtype`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `subtype` | *(empty)* | `string` | 20 | CIFS-AUTH-FAIL<br>SWITCH-CONTROLLER | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+47 more)* |
| `subtype` | Log Subtype | `string` | 20 | CONNECTOR<br>ENDPOINT<br>FORTIEXTENDER<br>HA<br>REST-API<br>ROUTER<br>SDWAN<br>SECURITY-RATING<br>SYSTEM<br>USER<br>VPN<br>WAD<br>WIRELESS | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+9 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+31 more)*<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY, 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+533 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>40960_-_LOGID_EVENT_WAD_WEBPROXY_FWD_SRV_ERROR, 48000_-_LOG_ID_WAD_SSL_RCV_HS, 48001_-_LOG_ID_WAD_SSL_RCV_WRG_HS *(+25 more)*<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+183 more)* |

`time`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `time` | *(empty)* | `string` | 8 | CIFS-AUTH-FAIL<br>SWITCH-CONTROLLER | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+47 more)* |
| `time` | Time | `string` | 8 | CONNECTOR<br>ENDPOINT<br>FORTIEXTENDER<br>HA<br>REST-API<br>ROUTER<br>SDWAN<br>SECURITY-RATING<br>SYSTEM<br>USER<br>VPN<br>WAD<br>WIRELESS | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+9 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+31 more)*<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY, 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+533 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>40960_-_LOGID_EVENT_WAD_WEBPROXY_FWD_SRV_ERROR, 48000_-_LOG_ID_WAD_SSL_RCV_HS, 48001_-_LOG_ID_WAD_SSL_RCV_WRG_HS *(+25 more)*<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+183 more)* |

`type`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `type` | *(empty)* | `string` | 16 | CIFS-AUTH-FAIL<br>SWITCH-CONTROLLER | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+47 more)* |
| `type` | Log Type | `string` | 16 | CONNECTOR<br>ENDPOINT<br>FORTIEXTENDER<br>HA<br>REST-API<br>ROUTER<br>SDWAN<br>SECURITY-RATING<br>SYSTEM<br>USER<br>VPN<br>WAD<br>WIRELESS | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+9 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+31 more)*<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY, 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+533 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>40960_-_LOGID_EVENT_WAD_WEBPROXY_FWD_SRV_ERROR, 48000_-_LOG_ID_WAD_SSL_RCV_HS, 48001_-_LOG_ID_WAD_SSL_RCV_WRG_HS *(+25 more)*<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+183 more)* |

`tz`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `tz` | *(empty)* | `string` | 5 | CIFS-AUTH-FAIL<br>SWITCH-CONTROLLER | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+47 more)* |
| `tz` | Time zone | `string` | 5 | CONNECTOR<br>ENDPOINT<br>FORTIEXTENDER<br>HA<br>REST-API<br>ROUTER<br>SDWAN<br>SECURITY-RATING<br>SYSTEM<br>USER<br>VPN<br>WAD<br>WIRELESS | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+9 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+31 more)*<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY, 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+533 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>40960_-_LOGID_EVENT_WAD_WEBPROXY_FWD_SRV_ERROR, 48000_-_LOG_ID_WAD_SSL_RCV_HS, 48001_-_LOG_ID_WAD_SSL_RCV_WRG_HS *(+25 more)*<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+183 more)* |

`ui`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `ui` | *(empty)* | `string` | 64 | SWITCH-CONTROLLER | 22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+46 more)* |
| `ui` | User Interface | `string` | 64 | HA<br>REST-API<br>ROUTER<br>SYSTEM<br>USER<br>VPN | 35014_-_LOG_ID_HA_RESET_UPTIME, 35015_-_LOG_ID_HA_CLEAR_HISTORY<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20401_-_LOG_ID_ROUTER_CLEAR<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+149 more)*<br>38011_-_LOG_ID_FIPS_DECRY_FAIL<br>41984_-_LOG_ID_EVENT_VPN_CERT_LOAD, 41985_-_LOG_ID_EVENT_VPN_CERT_REMOVAL, 41986_-_LOG_ID_EVENT_VPN_CERT_REGEN *(+2 more)* |

`user`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `user` | *(empty)* | `string` | 256 | SWITCH-CONTROLLER | 22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+46 more)* |
| `user` | User name of authenticated user | `string` | 256 | ENDPOINT<br>HA<br>REST-API<br>ROUTER<br>SYSTEM<br>USER<br>VPN<br>WIRELESS | 45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+5 more)*<br>35014_-_LOG_ID_HA_RESET_UPTIME, 35015_-_LOG_ID_HA_CLEAR_HISTORY<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20401_-_LOG_ID_ROUTER_CLEAR<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+185 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+25 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+53 more)*<br>43524_-_LOG_ID_EVENT_WIRELESS_STA, 43572_-_LOG_ID_EVENT_WIRELESS_STA_ASSO, 43573_-_LOG_ID_EVENT_WIRELESS_STA_AUTH *(+64 more)* |

`vd`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `vd` | *(empty)* | `string` | 32 | CIFS-AUTH-FAIL<br>SWITCH-CONTROLLER | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+47 more)* |
| `vd` | Virtual Domain Name | `string` | 32 | CONNECTOR<br>ENDPOINT<br>FORTIEXTENDER<br>HA<br>REST-API<br>ROUTER<br>SDWAN<br>SECURITY-RATING<br>SYSTEM<br>USER<br>VPN<br>WAD<br>WIRELESS | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+9 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+31 more)*<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY, 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+533 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>40960_-_LOGID_EVENT_WAD_WEBPROXY_FWD_SRV_ERROR, 48000_-_LOG_ID_WAD_SSL_RCV_HS, 48001_-_LOG_ID_WAD_SSL_RCV_WRG_HS *(+25 more)*<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+183 more)* |

`version`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `version` | *(empty)* | `string` | 64 | FORTIEXTENDER | 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR |
| `version` | Version | `string` | 64 | SYSTEM<br>VPN | 22080_-_LOG_ID_PROVISION_LATEST_SUCCEEDED, 22081_-_LOG_ID_PROVISION_LATEST_FAILED, 22090_-_LOG_ID_FEDERATED_UPGRADE_CANCELLED *(+5 more)*<br>37127_-_MESGID_NEG_PROGRESS_P1_NOTIF, 37128_-_MESGID_NEG_PROGRESS_P1_ERROR, 37129_-_MESGID_NEG_PROGRESS_P2_NOTIF *(+1 more)* |

#### UTM

| Log Field Name | Description | Data Type | Length |
|----------------|-------------|-----------|--------|
| `action` | X |  | X |
| `agent` | X |  |  |
| `analyticscksum` | X |  |  |
| `analyticssubmit` | X |  |  |
| `attachment` | X |  |  |
| `attack` | X |  |  |
| `authserver` | X |  |  |
| `cat` | X |  |  |
| `catdesc` | X |  |  |
| `cc` | X |  | X |
| `checksum` | X |  |  |
| `command` | X |  | X |
| `contentdisarmed` | X |  |  |
| `count` | X |  |  |
| `craction` | X |  |  |
| `crlevel` | X |  |  |
| `crscore` | X |  |  |
| `date` | X |  |  |
| `devid` | X |  |  |
| `direction` | X |  | X |
| `dstintf` | X |  | X |
| `dstintfrole` | X |  |  |
| `dstip` | X |  |  |
| `dstport` | X |  |  |
| `dtype` | X |  |  |
| `duration` | X |  |  |
| `epoch` | X |  |  |
| `error` | X |  |  |
| `eventid` | X |  |  |
| `eventtime` | X |  |  |
| `eventtype` | X |  |  |
| `fctuid` | X |  |  |
| `filehash` | X |  |  |
| `filehashsrc` | X |  |  |
| `filename` | X |  |  |
| `filesize` | X |  |  |
| `filetype` | X |  | X |
| `filtername` | X |  | X |
| `filtertype` | X |  | X |
| `forwardedfor` | X |  |  |
| `from` | X | X |  |
| `fsaverdict` | X |  |  |
| `group` | X |  |  |
| `hostname` | X |  |  |
| `icmpcode` | X |  |  |
| `icmpid` | X |  |  |
| `icmptype` | X |  |  |
| `level` | X |  |  |
| `logid` | X |  |  |
| `msg` | X |  | X |
| `policyid` | X |  |  |
| `policytype` | X |  |  |
| `profile` | X |  | X |
| `proto` | X |  |  |
| `quarskip` | X |  |  |
| `ratemethod` |  |  | X |
| `rawdata` | X |  |  |
| `recipient` | X |  |  |
| `ref` | X |  | X |
| `referralurl` | X |  |  |
| `sender` | X |  |  |
| `service` | X |  | X |
| `sessionid` | X |  |  |
| `severity` | X |  | X |
| `srccountry` | X |  |  |
| `srcintf` | X |  | X |
| `srcintfrole` | X |  |  |
| `srcip` | X |  |  |
| `srcport` | X |  |  |
| `status` | X |  |  |
| `subject` | X |  |  |
| `subtype` | X |  |  |
| `time` | X |  |  |
| `to` | X | X |  |
| `trueclntip` | X |  |  |
| `type` | X |  |  |
| `tz` | X |  |  |
| `unauthuser` | X |  |  |
| `unauthusersource` | X |  |  |
| `url` | X |  |  |
| `user` | X |  |  |
| `vd` | X |  |  |
| `virus` | X |  |  |
| `virusid` | X | X | X |
| `vrf` | X |  |  |

`action`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `action` | *(empty)* | `string` | 11 | Web | 13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `action` | *(empty)* | `string` | 17 | ICAP | 60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN |
| `action` | *(empty)* | `string` | 18 | AV | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `action` | *(empty)* | `string` | 20 | FILE-FILTER<br>SSL | 64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)* |
| `action` | Action | `string` | 16 | Anomaly | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS |
| `action` | Action. Eg. block , allow | `string` | 15 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |
| `action` | Security action of the email filter. Eg. blocked, tagged, allow | `string` | 8 | Email | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)* |
| `action` | Security action performed by DNS filter | `string` | 16 | DNS | 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK, 54401_-_LOG_ID_DNS_URL_FILTER_ALLOW *(+8 more)* |
| `action` | Security action performed by IPS:<br> detected - Attack is detected , but NOT blocked (similar to monitor)<br> dropped - Silent packet blocked<br> reset - Blocked and respond with Reset<br> reset_client - Blocked and reset sent to the client<br> reset_server - Blocked and reset sent to the server<br> drop_session - Silent block<br> pass_session - Session allowed<br> clear_session - Session was removed /closed | `string` | 16 | IPS | 16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |
| `action` | Security action performed by WF:<br> blocked - url is blocked by webfilter<br> passthrough - url is allowed by webfilter | `string` | 11 | Web | 12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+42 more)* |
| `action` | Status of the session. Uses following definition: - Deny = blocked by firewall policy. - Start = session start log (special option to enable logging at start of a session). This means firewall allowed. - All Others = allowed by Firewall Policy and the status indicates how it was closed. | `string` | 17 | WAF | 30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `action` | The status of the session:<br> blocked - Blocked infected file by AV engine<br> passthrough - Allowed by AV engine<br> monitored - Log, but do NOT block infected file<br> analytics - Submitted to Sandbox for analysis | `string` | 18 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+49 more)* |
| `action` | The status of the session:<br> log-only - DLP event is detected , but NOT blocked (similar to monitor action)<br> block - Blocked<br> exempt - Allowed<br> ban - blocked (Not in used since FortiOS 5.0, replaced by blocked)<br> ban-sender - blocks all data being sent by an ip or user (Not in used since FortiOS 5.0, replaced by quarantine)<br> quarantine-ip - Blocked and band the source ip (Not in used since FortiOS 5.0)<br> quarantine-interface - Blocked and band the source interface (Not in used since FortiOS 5.0) | `string` | 20 | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |
| `action` | The status of the session:<br> pass - Application is allowed<br> block - Application is blocked (silent)<br> reject - Quarantine<br> reset - Application is blocked and Reset was sent<br>Sometimes, there is a block page for blocking | `string` | 16 | App | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)* |
| `action` | The status of the ssh-channel:<br> passthrough - channel is allowed<br> blocked - channel is blocked | `string` | 17 | SSH | 61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)* |

`agent`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `agent` | *(empty)* | `string` | 1024 | AV<br>App<br>Email<br>FILE-FILTER<br>IPS | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16399_-_LOGID_ATTACK_MALICIOUS_URL |
| `agent` | Agent | `string` | 1024 | WAF | 30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `agent` | User agent - eg. agent="Mozilla/5.0" | `string` | 1024 | AV<br>DLP<br>Web | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+46 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+49 more)* |

`analyticscksum`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `analyticscksum` | *(empty)* | `string` | 64 | AV | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `analyticscksum` | The checksum of the file submitted for analytics | `string` | 64 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+39 more)* |

`analyticssubmit`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `analyticssubmit` | *(empty)* | `string` | 10 | AV | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `analyticssubmit` | The flag for analytics submission | `string` | 10 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+36 more)* |

`attachment`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `attachment` | *(empty)* | `string` | 3 | AV<br>DLP<br>FILE-FILTER | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+69 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG |
| `attachment` | Possible values: yes , no | `string` | 3 | Email | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)* |

`attack`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `attack` | Attack | `string` | 256 | Anomaly | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS |
| `attack` | Attack Name | `string` | 256 | IPS | 16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |

`authserver`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `authserver` | *(empty)* | `string` | 64 | AV<br>Email<br>FILE-FILTER | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG |
| `authserver` | Authentication Server | `string` | 64 | DLP<br>WAF | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `authserver` | Authentication server for the user | `string` | 64 | App<br>IPS<br>Web | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |
| `authserver` | Server used to authenticate the involved user | `string` | 64 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+48 more)* |

`cat`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `cat` | *(empty)* | `uint8` | 3 | SSL | 62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+2 more)* |
| `cat` | DNS category ID | `uint8` | 3 | DNS | 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK, 54401_-_LOG_ID_DNS_URL_FILTER_ALLOW *(+8 more)* |
| `cat` | Web category ID | `uint8` | 3 | Web | 12688_-_LOG_ID_WEB_SSL_EXEMPT, 13056_-_LOG_ID_WEB_FTGD_CAT_BLK, 13057_-_LOG_ID_WEB_FTGD_CAT_WARN *(+10 more)* |

`catdesc`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `catdesc` | *(empty)* | `string` | 64 | SSL | 62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+2 more)* |
| `catdesc` | DNS category description | `string` | 64 | DNS | 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK, 54401_-_LOG_ID_DNS_URL_FILTER_ALLOW *(+8 more)* |
| `catdesc` | Web category description | `string` | 64 | Web | 12688_-_LOG_ID_WEB_SSL_EXEMPT, 12802_-_LOG_ID_WEB_FTGD_QUOTA, 13056_-_LOG_ID_WEB_FTGD_CAT_BLK *(+11 more)* |

`cc`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `cc` | *(empty)* | `string` | 512 | AV<br>DLP<br>FILE-FILTER | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+69 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG |
| `cc` | Email address(es) from the Email Headers (IMAP/POP3/SMTP) | `string` | 4096 | Email | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)* |

`checksum`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `checksum` | *(empty)* | `string` | 16 | AV | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `checksum` | The checksum of the scanned file | `string` | 16 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+41 more)* |

`command`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `command` | *(empty)* | `string` | 16 | AV | 8452_-_MESGID_BLOCK_COMMAND |
| `command` | Shell command | `string` | 256 | SSH | 61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)* |

`contentdisarmed`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `contentdisarmed` | *(empty)* | `string` | 13 | AV | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `contentdisarmed` | Content Disarm action- eg. disarmed, detected | `string` | 13 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+36 more)* |

`count`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `count` | Count | `uint32` | 10 | Anomaly | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS |
| `count` | Session count | `uint32` | 10 | VoIP | 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK |

`craction`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `craction` | *(empty)* | `uint32` | 10 | AV | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `craction` | Action performed by Threat Weight | `uint32` | 10 | IPS | 16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |
| `craction` | Client Reputation Action | `uint32` | 10 | Anomaly<br>App<br>Web | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+42 more)* |
| `craction` | Threat Weight action | `uint32` | 10 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+48 more)* |

`crlevel`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `crlevel` | *(empty)* | `string` | 10 | AV | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `crlevel` | Client Reputation Level | `string` | 10 | Anomaly<br>App<br>IPS | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |
| `crlevel` | Client Reputation level | `string` | 10 | Web | 12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+42 more)* |
| `crlevel` | Threat Weight Level | `string` | 10 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+48 more)* |

`crscore`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `crscore` | *(empty)* | `uint32` | 10 | AV | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `crscore` | Client Reputation Score | `uint32` | 10 | Anomaly<br>App<br>IPS<br>Web | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+42 more)* |
| `crscore` | Threat Weight Score | `uint32` | 10 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+48 more)* |

`date`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `date` | *(empty)* | `string` | 10 | AV<br>FILE-FILTER<br>ICAP<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `date` | Date | `string` | 10 | AV<br>Anomaly<br>App<br>DLP<br>DNS<br>Email<br>GTP<br>IPS<br>SSH<br>WAF<br>Web | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+49 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF, 24578_-_LOG_ID_DLP_DOC_SOURCE *(+1 more)*<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+15 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+46 more)* |
| `date` | Day, month, and year when the log message was recorded. | `string` | 10 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |

`devid`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `devid` | *(empty)* | `string` | 16 | AV<br>FILE-FILTER<br>ICAP<br>SSL<br>Web | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+77 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `devid` | Deivce ID | `string` | 16 | Anomaly<br>App<br>IPS | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |
| `devid` | Device ID | `string` | 16 | DLP<br>DNS<br>Email<br>GTP<br>SSH<br>WAF<br>Web | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF, 24578_-_LOG_ID_DLP_DOC_SOURCE *(+1 more)*<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+15 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+46 more)* |
| `devid` | Serial number of the device for the traffic's origin. | `string` | 16 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |

`direction`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `direction` | *(empty)* | `string` | 8 | AV<br>FILE-FILTER | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG |
| `direction` | Direction | `string` | 4096 | WAF | 30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `direction` | Direction of packets | `string` | 8 | DLP<br>Email | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)* |
| `direction` | Direction of session | `string` | 4096 | SSH | 61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)* |
| `direction` | Direction of the packets | `string` | 8 | App | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)* |
| `direction` | Direction of the web traffic | `string` | 8 | Web | 12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+41 more)* |
| `direction` | Message/packets direction | `string` | 8 | AV<br>IPS | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+48 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |

`dstintf`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `dstintf` | *(empty)* | `string` | 32 | AV<br>FILE-FILTER<br>ICAP<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `dstintf` | Destination Interface | `string` | 32 | AV<br>DLP<br>DNS<br>SSH<br>WAF<br>Web | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+48 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |
| `dstintf` | Destination Interface | `string` | 64 | Anomaly<br>App<br>Email<br>IPS | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |

`dstintfrole`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `dstintfrole` | *(empty)* | `string` | 10 | AV<br>FILE-FILTER<br>ICAP<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `dstintfrole` | Destination Interface Role | `string` | 10 | DNS | 54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)* |
| `dstintfrole` | Destination Interface's assigned role (LAN, WAN, etc.) | `string` | 10 | AV<br>Anomaly<br>App<br>DLP<br>IPS<br>SSH<br>WAF<br>Web | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+48 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |
| `dstintfrole` | Destination interface Role, ex: LAN, WAN, etc | `string` | 10 | Email | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)* |

`dstip`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `dstip` | *(empty)* | `ip` | 39 | AV<br>FILE-FILTER<br>ICAP<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `dstip` | Destination IP | `ip` | 39 | Anomaly<br>App<br>DLP<br>DNS<br>Email<br>IPS<br>SSH<br>VoIP<br>Web | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+44 more)* |
| `dstip` | Destination IP Address | `ip` | 39 | AV<br>WAF | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+49 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |

`dstport`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `dstport` | *(empty)* | `uint16` | 5 | AV<br>FILE-FILTER<br>ICAP<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `dstport` | Destination Port | `uint16` | 5 | AV<br>Anomaly<br>App<br>DLP<br>DNS<br>Email<br>GTP<br>IPS<br>SSH<br>WAF<br>Web | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+49 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+11 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16399_-_LOGID_ATTACK_MALICIOUS_URL, 16400_-_LOGID_ATTACK_BOTNET_WARNING *(+1 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+44 more)* |

`dtype`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `dtype` | *(empty)* | `string` | 32 | AV | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `dtype` | Data type for virus category | `string` | 32 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+37 more)* |

`duration`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `duration` | Duration of the session. Ex: 180 (in seconds) | `uint32` | 10 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+1 more)* |
| `duration` | Tunnel duration | `uint32` | 10 | GTP | 41221_-_LOGID_GTP_TRAFFIC_COUNT, 41228_-_LOGID_GTPV2_TRAFFIC_COUNT, 41233_-_LOGID_PFCP_TRAFFIC_COUNT |

`epoch`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `epoch` | Epoch | `uint32` | 10 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |
| `epoch` | Epoch used for locating file | `uint32` | 10 | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |

`error`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `error` | DNS filter service error message | `string` | 256 | DNS | 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK, 54401_-_LOG_ID_DNS_URL_FILTER_ALLOW *(+8 more)* |
| `error` | URL rating error message | `string` | 256 | Web | 12558_-_LOG_ID_URL_FILTER_RATING_ERR, 12800_-_LOG_ID_WEB_FTGD_ERR, 12801_-_LOG_ID_WEB_FTGD_WARNING |

`eventid`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `eventid` | Event ID | `uint32` | 10 | WAF | 30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `eventid` | The serial number of the dlparchive file in the same epoch | `uint32` | 10 | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |

`eventtime`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `eventtime` | *(empty)* | `uint64` | 20 | AV<br>FILE-FILTER<br>ICAP<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `eventtime` | Event Time | `uint64` | 20 | App | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)* |
| `eventtime` | Event Time, Time when WAF event detected | `uint64` | 20 | WAF | 30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `eventtime` | Event Time, time when DLP event detected. | `uint64` | 20 | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF, 24578_-_LOG_ID_DLP_DOC_SOURCE *(+1 more)* |
| `eventtime` | Event Timestamp | `uint64` | 20 | DNS | 54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)* |
| `eventtime` | Event time | `uint64` | 20 | SSH | 61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)* |
| `eventtime` | Event time line | `uint64` | 20 | GTP | 41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+15 more)* |
| `eventtime` | Time when detection occured | `uint64` | 20 | AV<br>Anomaly<br>IPS | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+49 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |
| `eventtime` | Time when event occured | `uint64` | 20 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |
| `eventtime` | Web Filter event time | `uint64` | 20 | Web | 12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+46 more)* |
| `eventtime` | the time of the event | `uint64` | 20 | Email | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)* |

`eventtype`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `eventtype` | *(empty)* | `string` | 32 | AV<br>FILE-FILTER<br>ICAP<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `eventtype` | App Control Event Type | `string` | 32 | App | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)* |
| `eventtype` | DLP event type | `string` | 32 | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF, 24578_-_LOG_ID_DLP_DOC_SOURCE *(+1 more)* |
| `eventtype` | DNS Type (DNS query/DNS response) | `string` | 32 | DNS | 54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)* |
| `eventtype` | Email Filter event type | `string` | 32 | Email | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)* |
| `eventtype` | Event Type | `string` | 32 | Anomaly<br>SSH<br>WAF | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `eventtype` | Event type of AV | `string` | 32 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+49 more)* |
| `eventtype` | IPS Event Type | `string` | 32 | IPS | 16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |
| `eventtype` | Web Filter event type | `string` | 32 | Web | 12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+46 more)* |

`fctuid`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `fctuid` | *(empty)* | `string` | 32 | AV<br>FILE-FILTER<br>SSL | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)* |
| `fctuid` | FortiClient ID | `string` | 32 | DNS<br>Email | 54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)* |
| `fctuid` | FortiClient UID | `string` | 32 | Anomaly<br>IPS<br>SSH<br>WAF<br>Web | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+42 more)* |
| `fctuid` | FortiClient User ID | `string` | 32 | App<br>DLP | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |
| `fctuid` | Forticlient user ID | `string` | 32 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+49 more)* |

`filehash`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `filehash` | *(empty)* | `string` | 64 | AV | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `filehash` | Used by Outbreak Prevention External Hash: the hash signature used in the detection | `string` | 64 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+34 more)* |

`filehashsrc`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `filehashsrc` | *(empty)* | `string` | 32 | AV | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `filehashsrc` | Used by Outbreak Prevention External Hash: external source that provided the hash signature | `string` | 32 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+34 more)* |

`filename`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `filename` | *(empty)* | `string` | 256 | AV<br>FILE-FILTER | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG |
| `filename` | File name | `string` | 256 | AV<br>App<br>DLP | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+46 more)*<br>28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |

`filesize`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `filesize` | *(empty)* | `uint64` | 10 | FILE-FILTER | 64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG |
| `filesize` | File size in bytes | `uint64` | 10 | App<br>DLP | 28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |

`filetype`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `filetype` | *(empty)* | `string` | 16 | AV | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `filetype` | *(empty)* | `string` | 23 | FILE-FILTER | 64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG |
| `filetype` | File type | `string` | 16 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+37 more)* |
| `filetype` | File type | `string` | 23 | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |

`filtername`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `filtername` | *(empty)* | `string` | 36 | FILE-FILTER | 64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG |
| `filtername` | DLP rule name | `string` | 128 | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |

`filtertype`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `filtertype` | DLP filter type | `string` | 23 | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |
| `filtertype` | Filter type | `string` | 10 | Web | 13568_-_LOG_ID_WEB_SCRIPTFILTER_ACTIVEX, 13573_-_LOG_ID_WEB_SCRIPTFILTER_COOKIE, 13584_-_LOG_ID_WEB_SCRIPTFILTER_APPLET *(+3 more)* |

`forwardedfor`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `forwardedfor` | *(empty)* | `string` | 128 | AV<br>FILE-FILTER | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+70 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG |
| `forwardedfor` | Forwarded For | `string` | 128 | App<br>DLP | 28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |
| `forwardedfor` | X-Forwarded-For HTTP header | `string` | 128 | IPS<br>Web | 16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+41 more)* |

`from`

**Description conflicts** — same field, different `Description` across LOGIDs
**Data Type conflicts** — same field, different `Data Type` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `from` | *(empty)* | `string` | 128 | AV<br>FILE-FILTER | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG |
| `from` | Email address from the Email Headers (IMAP/POP3/SMTP) | `string` | 128 | AV<br>DLP | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+47 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |
| `from` | Email address(es) from the Email Headers (IMAP/POP3/SMTP) | `string` | 128 | Email | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)* |
| `from` | From | `ip` | 128 | GTP | 41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+12 more)* |
| `from` | MMS-only - From/To headers from the email | `string` | 128 | Web | 12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+2 more)* |
| `from` | Where call was originated from | `string` | 128 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK |

`fsaverdict`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `fsaverdict` | *(empty)* | `string` | 32 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+61 more)* |
| `fsaverdict` | FortiSandbox Verdict returned to FortiGate after analysis (clean, low risk, med risk, high risk, malicious) | `string` | 32 | AV | 9233_-_MESGID_ANALYTICS_SUBMITTED, 9238_-_MESGID_ANALYTICS_FSA_RESULT |

`group`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `group` | *(empty)* | `string` | 64 | AV<br>FILE-FILTER<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `group` | Group name (authentication) | `string` | 64 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+48 more)* |
| `group` | Group name for authentication | `string` | 64 | SSH | 61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)* |
| `group` | User Group Name | `string` | 64 | Anomaly<br>WAF | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `group` | User group name | `string` | 64 | App<br>DLP<br>DNS<br>Email<br>IPS<br>Web | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+2 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |

`hostname`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `hostname` | *(empty)* | `string` | 256 | FILE-FILTER<br>SSL<br>Web | 64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `hostname` | The host name of a URL | `string` | 256 | App<br>DLP<br>IPS<br>Web | 28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16399_-_LOGID_ATTACK_MALICIOUS_URL<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+42 more)* |

`icmpcode`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `icmpcode` | Destination Port of the ICMP message | `string` | 6 | IPS | 16385_-_LOGID_ATTCK_SIGNATURE_ICMP |
| `icmpcode` | ICMP code | `string` | 6 | Anomaly | 18433_-_LOGID_ATTCK_ANOMALY_ICMP |

`icmpid`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `icmpid` | ICMP ID | `string` | 8 | Anomaly | 18433_-_LOGID_ATTCK_ANOMALY_ICMP |
| `icmpid` | Source port of the ICMP message | `string` | 8 | IPS | 16385_-_LOGID_ATTCK_SIGNATURE_ICMP |

`icmptype`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `icmptype` | ICMP Type | `string` | 6 | Anomaly | 18433_-_LOGID_ATTCK_ANOMALY_ICMP |
| `icmptype` | The type of ICMP message | `string` | 6 | IPS | 16385_-_LOGID_ATTCK_SIGNATURE_ICMP |

`level`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `level` | *(empty)* | `string` | 11 | AV<br>FILE-FILTER<br>ICAP<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `level` | Log Level | `string` | 11 | Anomaly<br>DLP<br>DNS<br>Email<br>GTP<br>IPS<br>VoIP<br>WAF<br>Web | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF, 24578_-_LOG_ID_DLP_DOC_SOURCE *(+1 more)*<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+15 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+46 more)* |
| `level` | Log level | `string` | 11 | AV<br>App<br>SSH | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+49 more)*<br>28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)* |

`logid`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `logid` | *(empty)* | `string` | 10 | AV<br>FILE-FILTER<br>ICAP<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `logid` | Log ID | `string` | 10 | AV<br>Anomaly<br>App<br>DLP<br>DNS<br>Email<br>GTP<br>IPS<br>SSH<br>WAF<br>Web | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+49 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF, 24578_-_LOG_ID_DLP_DOC_SOURCE *(+1 more)*<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+15 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+46 more)* |
| `logid` | Unique Log ID | `string` | 10 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |

`msg`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `msg` | *(empty)* | `string` | 4096 | AV<br>ICAP | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN |
| `msg` | *(empty)* | `string` | 512 | FILE-FILTER<br>SSL<br>Web | 64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+13 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `msg` | Log Message | `string` | 4096 | WAF | 30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `msg` | Log Message | `string` | 512 | Email | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)* |
| `msg` | Log Message | `string` | 518 | Anomaly | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS |
| `msg` | Log message | `string` | 4096 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+48 more)* |
| `msg` | Log message | `string` | 512 | App<br>DNS<br>Web | 28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK, 54401_-_LOG_ID_DNS_URL_FILTER_ALLOW *(+8 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |
| `msg` | Log message for the attack | `string` | 518 | IPS | 16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |

`policyid`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `policyid` | *(empty)* | `uint32` | 10 | AV<br>FILE-FILTER<br>ICAP<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `policyid` | Policy ID | `uint32` | 10 | AV<br>Anomaly<br>App<br>DLP<br>DNS<br>Email<br>IPS<br>SSH<br>WAF<br>Web | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+48 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |

`policytype`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `policytype` | *(empty)* | `string` | 24 | AV<br>App<br>DLP<br>DNS<br>Email<br>FILE-FILTER<br>ICAP<br>IPS<br>SSH<br>SSL<br>WAF<br>Web | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+76 more)*<br>28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |
| `policytype` | Policy type | `string` | 24 | Anomaly | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS |

`profile`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `profile` | *(empty)* | `string` | 36 | App | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)* |
| `profile` | *(empty)* | `string` | 64 | AV<br>FILE-FILTER<br>ICAP<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `profile` | DLP profile name | `string` | 64 | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |
| `profile` | Email Filter profile name | `string` | 64 | Email | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)* |
| `profile` | Full profile name | `string` | 64 | SSH<br>WAF | 61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `profile` | Name or number of associated VOIP profile | `string` | 64 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |
| `profile` | Profile Name | `string` | 64 | GTP | 41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+15 more)* |
| `profile` | Profile name for DNS filter | `string` | 64 | DNS | 54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)* |
| `profile` | Profile name for IPS | `string` | 64 | IPS | 16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |
| `profile` | The name of the profile that was used to detect and take action | `string` | 64 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+48 more)* |
| `profile` | Web Filter profile name | `string` | 64 | Web | 12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+44 more)* |

`proto`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `proto` | *(empty)* | `uint8` | 3 | AV<br>FILE-FILTER<br>ICAP<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13603_-_LOG_ID_WEB_WF_COMMAND_BLOCK, 13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR *(+4 more)* |
| `proto` | Protocol | `uint8` | 3 | Anomaly<br>WAF | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `proto` | Protocol number | `uint8` | 3 | AV<br>App<br>DLP<br>DNS<br>Email<br>IPS<br>SSH<br>Web | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+48 more)*<br>28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+42 more)* |
| `proto` | Protocol number. Ex: for SIP it will be proto=17 | `uint8` | 3 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |

`quarskip`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `quarskip` | *(empty)* | `string` | 46 | AV | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `quarskip` | Quarantine skip explanation | `string` | 46 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+39 more)* |

`ratemethod`

**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `ratemethod` | *(empty)* | `string` | 4096 | WAF | 30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `ratemethod` | *(empty)* | `string` | 6 | Web | 12688_-_LOG_ID_WEB_SSL_EXEMPT, 13056_-_LOG_ID_WEB_FTGD_CAT_BLK, 13057_-_LOG_ID_WEB_FTGD_CAT_WARN *(+10 more)* |

`rawdata`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `rawdata` | *(empty)* | `string` | 1024 | AV<br>FILE-FILTER | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+64 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG |
| `rawdata` | Extended logging data including HTTP method, URL, client content type, server content type, user agent, referer, x-forwarded-for | `string` | 1024 | App<br>IPS<br>Web | 28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+41 more)* |
| `rawdata` | Raw Data | `string` | 1024 | DLP<br>WAF | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |

`recipient`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `recipient` | *(empty)* | `string` | 512 | AV<br>FILE-FILTER | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG |
| `recipient` | Email addresses from the SMTP envelope | `string` | 512 | AV<br>DLP<br>Email | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+45 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)* |

`ref`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `ref` | *(empty)* | `string` | 512 | AV | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `ref` | Reference | `string` | 4096 | Anomaly | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS |
| `ref` | The URL of the FortiGuard IPS database entry for the attack | `string` | 512 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+34 more)* |
| `ref` | URL of the FortiGuard IPS database entry for the attack. | `string` | 4096 | IPS | 16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+2 more)* |

`referralurl`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `referralurl` | *(empty)* | `string` | 512 | AV<br>App<br>DLP<br>FILE-FILTER<br>IPS<br>WAF | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+74 more)*<br>28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16399_-_LOGID_ATTACK_MALICIOUS_URL<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `referralurl` | Referrer URI | `string` | 512 | Web | 12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+49 more)* |

`sender`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `sender` | *(empty)* | `string` | 128 | AV<br>FILE-FILTER | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG |
| `sender` | Email address from the SMTP envelope | `string` | 128 | AV<br>DLP | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+45 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |
| `sender` | Email addresses from the SMTP envelope | `string` | 128 | Email | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)* |

`service`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `service` | *(empty)* | `string` | 36 | FILE-FILTER<br>Web | 64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `service` | *(empty)* | `string` | 5 | AV<br>ICAP<br>SSL | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)* |
| `service` | Name of Service | `string` | 80 | Anomaly | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS |
| `service` | Proxy service which scanned this traffic | `string` | 5 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+49 more)* |
| `service` | SMTP, POP3, IMAP, etc. | `string` | 36 | Email | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)* |
| `service` | Service name | `string` | 36 | DLP<br>Web | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |
| `service` | Service name | `string` | 5 | WAF | 30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `service` | Service name | `string` | 80 | App<br>IPS | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |

`sessionid`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `sessionid` | *(empty)* | `uint32` | 10 | AV<br>FILE-FILTER<br>GTP<br>ICAP<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>41233_-_LOGID_PFCP_TRAFFIC_COUNT<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `sessionid` | Session ID | `uint32` | 10 | AV<br>Anomaly<br>App<br>DLP<br>DNS<br>Email<br>IPS<br>SSH<br>WAF<br>Web | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+48 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |

`severity`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `severity` | Severity | `string` | 6 | WAF | 30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `severity` | Severity | `string` | 8 | Anomaly | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS |
| `severity` | Severity level of a DLP rule | `string` | 8 | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |
| `severity` | Severity level of shell command | `string` | 8 | SSH | 61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)* |
| `severity` | Severity of the attack | `string` | 8 | IPS | 16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |

`srccountry`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `srccountry` | *(empty)* | `string` | 64 | AV<br>App<br>DLP<br>DNS<br>Email<br>FILE-FILTER<br>ICAP<br>SSH<br>SSL<br>WAF<br>Web | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+76 more)*<br>28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |
| `srccountry` | Country name for Source IP | `string` | 64 | Anomaly<br>IPS | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |

`srcintf`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `srcintf` | *(empty)* | `string` | 32 | AV<br>FILE-FILTER<br>ICAP<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `srcintf` | Source Interface | `string` | 32 | AV<br>DLP<br>DNS<br>SSH<br>WAF<br>Web | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+48 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |
| `srcintf` | Source Interface | `string` | 64 | Anomaly<br>App<br>Email<br>IPS | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |

`srcintfrole`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `srcintfrole` | *(empty)* | `string` | 10 | AV<br>FILE-FILTER<br>ICAP<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `srcintfrole` | Source Interface Role | `string` | 10 | DNS | 54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)* |
| `srcintfrole` | Source Interface's assigned role (LAN, WAN, etc.) | `string` | 10 | AV<br>Anomaly<br>App<br>DLP<br>IPS<br>SSH<br>WAF<br>Web | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+48 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |
| `srcintfrole` | Source interface Role, ex: LAN, WAN, etc | `string` | 10 | Email | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)* |

`srcip`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `srcip` | *(empty)* | `ip` | 39 | AV<br>FILE-FILTER<br>ICAP<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `srcip` | IP address of the traffic's origin. Ex: srcip=10.1.100.155 | `ip` | 39 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |
| `srcip` | Source IP | `ip` | 39 | Anomaly<br>App<br>DLP<br>DNS<br>Email<br>IPS<br>SSH<br>Web | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+44 more)* |
| `srcip` | Source IP Address | `ip` | 39 | AV<br>WAF | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+49 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |

`srcport`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `srcport` | *(empty)* | `uint16` | 5 | AV<br>FILE-FILTER<br>ICAP<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `srcport` | Source Port | `uint16` | 5 | AV<br>Anomaly<br>App<br>DLP<br>DNS<br>Email<br>GTP<br>IPS<br>SSH<br>WAF<br>Web | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+49 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+11 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16399_-_LOGID_ATTACK_MALICIOUS_URL, 16400_-_LOGID_ATTACK_BOTNET_WARNING *(+1 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+44 more)* |

`status`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `status` | Status | `string` | 23 | GTP | 41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+15 more)* |
| `status` | Status. Ex: status="blocked" , status= "start" | `string` | 23 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44035_-_LOGID_EVENT_VOIP_SCCP_REGISTER *(+3 more)* |

`subject`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `subject` | *(empty)* | `string` | 256 | AV<br>FILE-FILTER | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+69 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG |
| `subject` | The subject title of the email message | `string` | 256 | DLP<br>Email | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)* |

`subtype`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `subtype` | *(empty)* | `string` | 20 | AV<br>FILE-FILTER<br>ICAP<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `subtype` | Log Subtype | `string` | 20 | Anomaly<br>DNS<br>GTP<br>IPS<br>WAF | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+15 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `subtype` | Log subtype | `string` | 20 | App<br>DLP<br>Email<br>SSH<br>Web | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF, 24578_-_LOG_ID_DLP_DOC_SOURCE *(+1 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+46 more)* |
| `subtype` | Subtype | `string` | 20 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |
| `subtype` | Subtype of the virus log | `string` | 20 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+49 more)* |

`time`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `time` | *(empty)* | `string` | 8 | AV<br>FILE-FILTER<br>ICAP<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `time` | Hour clock when the log message was recorded. | `string` | 8 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |
| `time` | Time | `string` | 8 | AV<br>Anomaly<br>App<br>DLP<br>DNS<br>Email<br>GTP<br>IPS<br>SSH<br>WAF<br>Web | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+49 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF, 24578_-_LOG_ID_DLP_DOC_SOURCE *(+1 more)*<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+15 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+46 more)* |

`to`

**Description conflicts** — same field, different `Description` across LOGIDs
**Data Type conflicts** — same field, different `Data Type` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `to` | *(empty)* | `string` | 512 | AV<br>FILE-FILTER | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG |
| `to` | Destination address | `string` | 512 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK |
| `to` | Email address(es) from the Email Headers (IMAP/POP3/SMTP) | `string` | 512 | AV<br>DLP<br>Email | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+47 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)* |
| `to` | MMS-only - From/To headers from the email | `string` | 512 | Web | 12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+2 more)* |
| `to` | To | `ip` | 512 | GTP | 41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+12 more)* |

`trueclntip`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `trueclntip` | *(empty)* | `ip` | 39 | AV<br>FILE-FILTER | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+70 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG |
| `trueclntip` | True client's IP | `ip` | 39 | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |
| `trueclntip` | True-Client-IP | `ip` | 39 | App | 28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)* |
| `trueclntip` | True-Client-IP HTTP header | `ip` | 39 | IPS<br>Web | 16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+41 more)* |

`type`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `type` | *(empty)* | `string` | 16 | AV<br>FILE-FILTER<br>ICAP<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `type` | Log Type | `string` | 16 | Anomaly<br>DNS<br>GTP<br>WAF | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+15 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `type` | Log type | `string` | 16 | AV<br>App<br>DLP<br>Email<br>IPS<br>SSH<br>Web | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+49 more)*<br>28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF, 24578_-_LOG_ID_DLP_DOC_SOURCE *(+1 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+46 more)* |
| `type` | Type of log. Ex: type="utm" | `string` | 16 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |

`tz`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `tz` | *(empty)* | `string` | 5 | AV<br>App<br>DLP<br>Email<br>FILE-FILTER<br>ICAP<br>IPS<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF, 24578_-_LOG_ID_DLP_DOC_SOURCE *(+1 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `tz` | Time Zone | `string` | 5 | AV<br>Web | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+49 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+46 more)* |
| `tz` | Time zone | `string` | 5 | Anomaly<br>DNS<br>GTP<br>SSH<br>VoIP<br>WAF | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+15 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |

`unauthuser`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `unauthuser` | *(empty)* | `string` | 66 | AV<br>Email<br>FILE-FILTER<br>SSL | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+77 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)* |
| `unauthuser` | Unauthenticated User | `string` | 66 | DNS<br>SSH | 54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)* |
| `unauthuser` | Unauthenticated user | `string` | 66 | Anomaly<br>App<br>DLP<br>IPS<br>WAF<br>Web | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+42 more)* |

`unauthusersource`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `unauthusersource` | *(empty)* | `string` | 66 | AV<br>Email<br>FILE-FILTER<br>SSL | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+77 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)* |
| `unauthusersource` | Unauthenticated User Source | `string` | 66 | DNS<br>SSH | 54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)* |
| `unauthusersource` | Unauthenticated user source | `string` | 66 | Anomaly<br>App<br>DLP<br>IPS<br>WAF<br>Web | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+42 more)* |

`url`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `url` | *(empty)* | `string` | 512 | AV<br>FILE-FILTER<br>ICAP<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `url` | The URL address | `string` | 512 | AV<br>App<br>DLP<br>IPS<br>Web | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+46 more)*<br>28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16399_-_LOGID_ATTACK_MALICIOUS_URL<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+44 more)* |
| `url` | URL | `string` | 512 | WAF | 30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |

`user`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `user` | *(empty)* | `string` | 256 | AV<br>FILE-FILTER<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `user` | User | `string` | 256 | Anomaly | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS |
| `user` | User Name | `string` | 256 | WAF | 30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `user` | User name | `string` | 256 | App<br>DLP<br>DNS<br>Email<br>IPS<br>Web | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+45 more)* |
| `user` | User name for authentication | `string` | 256 | SSH | 61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)* |
| `user` | Username (authentication) | `string` | 256 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+48 more)* |

`vd`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `vd` | *(empty)* | `string` | 32 | AV<br>FILE-FILTER<br>ICAP<br>SSL<br>Web | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `vd` | Name of the virtual domain in which the log message was recorded. | `string` | 32 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |
| `vd` | VDOM name | `string` | 32 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+49 more)* |
| `vd` | Virtual Domain | `string` | 32 | Email | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)* |
| `vd` | Virtual Domain Name | `string` | 32 | Anomaly<br>DNS<br>GTP<br>SSH<br>WAF | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+15 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `vd` | Virtual domain name | `string` | 32 | App<br>DLP<br>IPS<br>Web | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF, 24578_-_LOG_ID_DLP_DOC_SOURCE *(+1 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+46 more)* |

`virus`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `virus` | *(empty)* | `string` | 128 | AV | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `virus` | Virus Name | `string` | 128 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+34 more)* |

`virusid`

**Description conflicts** — same field, different `Description` across LOGIDs
**Data Type conflicts** — same field, different `Data Type` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `virusid` | *(empty)* | `string` | 64 | ICAP | 60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN |
| `virusid` | *(empty)* | `uint32` | 10 | AV | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `virusid` | Virus ID (unique virus identifier) | `uint32` | 10 | AV | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+34 more)* |

`vrf`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `vrf` | *(empty)* | `uint8` | 3 | AV<br>FILE-FILTER<br>ICAP<br>SSL<br>Web | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+76 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+15 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `vrf` | Virtual Routing Forwarding | `uint8` | 3 | App<br>DLP | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |
| `vrf` | Virtual router forwarding | `uint8` | 3 | Anomaly<br>Email<br>IPS<br>Web | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+41 more)* |

---

