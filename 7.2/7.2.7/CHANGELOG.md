# FortiGate 7.2.7 — Analysis

[← 7.2 Index](../INDEX.md)

**Traffic**

| Category | Fields | LOGIDs |
|----------|--------|--------|
| forward | 158 | 15 |
| local | 144 | 2 |
| multicast | 144 | 2 |
| sniffer | 158 | 2 |
| ztna | 144 | 1 |

**Event**

| Category | Fields | LOGIDs |
|----------|--------|--------|
| cifs-auth-fail | 30 | 4 |
| connector | 20 | 6 |
| endpoint | 41 | 16 |
| fortiextender | 16 | 11 |
| ha | 30 | 36 |
| rest-api | 17 | 2 |
| router | 20 | 10 |
| sdwan | 37 | 13 |
| security-rating | 20 | 2 |
| switch-controller | 22 | 52 |
| system | 151 | 553 |
| user | 40 | 49 |
| vpn | 59 | 81 |
| wanopt | 28 | 5 |
| webproxy | 17 | 1 |
| wireless | 82 | 187 |

**UTM** *(including GTP)*

| Type | Fields | LOGIDs | Categories | Category List |
|------|--------|--------|------------|---------------|
| APP-CTRL | 72 | 14 | 3 | port-violation, protocol-violation, signature |
| Anomaly | 46 | 3 | 1 | anomaly |
| DLP | 78 | 4 | 2 | dlp, dlp-docsource |
| DNS | 54 | 12 | 2 | dns-query, dns-response |
| EmailFilter | 56 | 5 | 5 | bannedword, email, ftgd_err, spam, webmail |
| FILE-FILTER | 68 | 2 | 1 | file-filter |
| FORTI-SWITCH | 18 | 1 | 1 | fsw-flow |
| GTP | 86 | 18 | 2 | gtp-all, pfcp-all |
| ICAP | 36 | 3 | 1 | icap |
| IPS | 66 | 6 | 3 | botnet, malicious-url, signature |
| SSH | 42 | 8 | 3 | ssh-channel, ssh-command, ssh-hostkey |
| SSL | 63 | 19 | 5 | ssl-anomaly, ssl-exempt, ssl-handshake, ssl-negotiation, ssl-server-cert-info |
| Virus | 97 | 82 | 16 | analytics, command-blocked, content-disarm, ems-threat-feed, exempt-hash, filename, filetype-executable, fortindr, fortisandbox, infected, malware-list, mimefragmented, outbreak-prevention, oversize, scanerror, switchproto |
| VoIP | 45 | 7 | 1 | voip |
| WAF | 52 | 12 | 6 | waf-address-list, waf-custom-signature, waf-http-constraint, waf-http-method, waf-signature, waf-url-access |
| Webfilter | 87 | 57 | 20 | activexfilter, antiphishing, appletfilter, content, cookiefilter, ftgd_allow, ftgd_blk, ftgd_err, ftgd_quota, ftgd_quota_counting, ftgd_quota_expired, http_header_change, scriptfilter, ssl-exempt, unknown-ce, urlfilter, urlmonitor, videofilter-category, videofilter-channel, webfilter_command_block |

### 7.2.7 — Intra-version Inconsistencies

**Summary**

| Conflict Type | Fields |
|--------------|--------|
| Description conflicts | 124 |
| Data Type conflicts | 4 |
| Length conflicts | 17 |

#### Traffic

| Log Field Name | Description | Data Type | Length |
|----------------|-------------|-----------|--------|
| `app` | X |  |  |

`app`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `app` | Application Name | `string` | 96 | sniffer<br>ztna | 17_-_LOG_ID_TRAFFIC_SNIFFER, 21_-_LOG_ID_TRAFFIC_SNIFFER_STAT<br>24_-_LOG_ID_TRAFFIC_ZTNA |
| `app` | Application name | `string` | 96 | forward<br>local<br>multicast | 10_-_LOG_ID_TRAFFIC_EXPLICIT_PROXY, 11_-_LOG_ID_TRAFFIC_FAIL_CONN, 13_-_LOG_ID_TRAFFIC_END_FORWARD *(+11 more)*<br>14_-_LOG_ID_TRAFFIC_END_LOCAL, 16_-_LOG_ID_TRAFFIC_START_LOCAL<br>12_-_LOG_ID_TRAFFIC_MULTICAST, 19_-_LOG_ID_TRAFFIC_BROADCAST |

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
| `severity` | X |  |  |
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
| `action` | *(empty)* | `string` | 65 | fortiextender<br>switch-controller | 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+15 more)* |
| `action` | Policy Action | `string` | 65 | connector<br>endpoint<br>router<br>system<br>user<br>vpn<br>wireless | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE<br>20401_-_LOG_ID_ROUTER_CLEAR, 51000_-_LOG_ID_NB_TBL_CHG<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20021_-_LOG_ID_MAIL_RESENT *(+224 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+30 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+72 more)*<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+184 more)* |

`cfgattr`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `cfgattr` | *(empty)* | `string` | 4096 | switch-controller | 32569_-_LOG_ID_FSW_SWITCH_LOG_EVENT, 32693_-_LOG_ID_FGT_SWITCH_GROUP_SWC, 32694_-_LOG_ID_FGT_SWITCH_GROUP_POE *(+5 more)* |
| `cfgattr` | Configuration attribute | `string` | 4096 | system | 44546_-_LOGID_EVENT_CONFIG_ATTR, 44547_-_LOGID_EVENT_CONFIG_OBJATTR |

`cfgobj`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `cfgobj` | *(empty)* | `string` | 256 | switch-controller | 32569_-_LOG_ID_FSW_SWITCH_LOG_EVENT, 32693_-_LOG_ID_FGT_SWITCH_GROUP_SWC, 32694_-_LOG_ID_FGT_SWITCH_GROUP_POE *(+5 more)* |
| `cfgobj` | Configuration object | `string` | 256 | connector<br>system | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE<br>44545_-_LOGID_EVENT_CONFIG_OBJ, 44547_-_LOGID_EVENT_CONFIG_OBJATTR |

`cfgpath`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `cfgpath` | *(empty)* | `string` | 128 | switch-controller | 32569_-_LOG_ID_FSW_SWITCH_LOG_EVENT, 32693_-_LOG_ID_FGT_SWITCH_GROUP_SWC, 32694_-_LOG_ID_FGT_SWITCH_GROUP_POE *(+5 more)* |
| `cfgpath` | Configuration path | `string` | 128 | system | 44544_-_LOGID_EVENT_CONFIG_PATH, 44545_-_LOGID_EVENT_CONFIG_OBJ, 44546_-_LOGID_EVENT_CONFIG_ATTR *(+1 more)* |

`cfgtid`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `cfgtid` | *(empty)* | `uint32` | 10 | switch-controller | 32569_-_LOG_ID_FSW_SWITCH_LOG_EVENT, 32693_-_LOG_ID_FGT_SWITCH_GROUP_SWC, 32694_-_LOG_ID_FGT_SWITCH_GROUP_POE *(+5 more)* |
| `cfgtid` | Config transaction id | `uint32` | 10 | system | 44544_-_LOGID_EVENT_CONFIG_PATH, 44545_-_LOGID_EVENT_CONFIG_OBJ, 44546_-_LOGID_EVENT_CONFIG_ATTR *(+1 more)* |

`count`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `count` | Count | `uint32` | 10 | system | 20003_-_LOG_ID_MAIL_SENT_FAIL, 20021_-_LOG_ID_MAIL_RESENT, 22100_-_LOG_ID_QUAR_DROP_TRAN_JOB *(+2 more)* |
| `count` | Number of Packets | `uint32` | 10 | endpoint<br>user | 45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE<br>38656_-_LOGID_EVENT_RAD_RPT_PROTO_ERROR, 38657_-_LOGID_EVENT_RAD_RPT_PROF_NOT_FOUND, 38658_-_LOGID_EVENT_RAD_RPT_CTX_NOT_FOUND *(+4 more)* |

`date`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `date` | *(empty)* | `string` | 10 | cifs-auth-fail<br>switch-controller | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+49 more)* |
| `date` | Date | `string` | 10 | connector<br>endpoint<br>fortiextender<br>ha<br>rest-api<br>router<br>sdwan<br>security-rating<br>system<br>user<br>vpn<br>wanopt<br>webproxy<br>wireless | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+13 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+33 more)*<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY, 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+550 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>48040_-_LOG_ID_WANOPT_TUNNEL_CREATE, 48041_-_LOG_ID_WANOPT_TUNNEL_CLOSED, 48101_-_LOG_ID_WANOPT_AUTH_FAIL_PSK *(+2 more)*<br>40960_-_LOGID_EVENT_WEBPROXY_FWD_SRV_ERROR<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+184 more)* |

`devid`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `devid` | *(empty)* | `string` | 16 | cifs-auth-fail<br>switch-controller | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+49 more)* |
| `devid` | Device ID | `string` | 16 | connector<br>endpoint<br>fortiextender<br>ha<br>rest-api<br>router<br>sdwan<br>security-rating<br>system<br>user<br>vpn<br>wanopt<br>webproxy<br>wireless | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+13 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+33 more)*<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY, 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+550 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>48040_-_LOG_ID_WANOPT_TUNNEL_CREATE, 48041_-_LOG_ID_WANOPT_TUNNEL_CLOSED, 48101_-_LOG_ID_WANOPT_AUTH_FAIL_PSK *(+2 more)*<br>40960_-_LOGID_EVENT_WEBPROXY_FWD_SRV_ERROR<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+184 more)* |

`dst_int`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `dst_int` | *(empty)* | `string` | 64 | cifs-auth-fail | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)* |
| `dst_int` | Destination Interface | `string` | 64 | system | 22810_-_LOG_ID_SCANUNIT_ERROR_BLOCK, 22811_-_LOG_ID_SCANUNIT_ERROR_PASS, 43776_-_LOG_ID_EVENT_NAC_QUARANTINE *(+1 more)* |

`dstip`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `dstip` | *(empty)* | `ip` | 39 | cifs-auth-fail | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)* |
| `dstip` | Destination IP | `ip` | 39 | system<br>user<br>wanopt | 20007_-_LOG_ID_SOCKET_EXHAUSTED, 20214_-_LOG_ID_LOCAL_OUT_IOC, 22810_-_LOG_ID_SCANUNIT_ERROR_BLOCK *(+11 more)*<br>43008_-_LOG_ID_EVENT_AUTH_SUCCESS, 43009_-_LOG_ID_EVENT_AUTH_FAILED, 43010_-_LOG_ID_EVENT_AUTH_LOCKOUT *(+18 more)*<br>48040_-_LOG_ID_WANOPT_TUNNEL_CREATE, 48041_-_LOG_ID_WANOPT_TUNNEL_CLOSED, 48101_-_LOG_ID_WANOPT_AUTH_FAIL_PSK *(+2 more)* |

`dstport`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `dstport` | *(empty)* | `uint16` | 5 | cifs-auth-fail | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)* |
| `dstport` | Destination Protocol Port | `uint16` | 5 | system<br>wanopt | 20007_-_LOG_ID_SOCKET_EXHAUSTED, 20214_-_LOG_ID_LOCAL_OUT_IOC, 22223_-_LOG_ID_EXT_RESOURCE_DEBUG *(+8 more)*<br>48040_-_LOG_ID_WANOPT_TUNNEL_CREATE, 48041_-_LOG_ID_WANOPT_TUNNEL_CLOSED, 48101_-_LOG_ID_WANOPT_AUTH_FAIL_PSK *(+2 more)* |

`duration`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `duration` | Duration | `uint32` | 10 | system<br>user<br>vpn | 22016_-_LOG_ID_IPPOOLPBA_DEALLOCATE, 22100_-_LOG_ID_QUAR_DROP_TRAN_JOB, 32003_-_LOG_ID_ADMIN_LOGOUT *(+3 more)*<br>38656_-_LOGID_EVENT_RAD_RPT_PROTO_ERROR, 38657_-_LOGID_EVENT_RAD_RPT_PROF_NOT_FOUND, 38658_-_LOGID_EVENT_RAD_RPT_CTX_NOT_FOUND *(+3 more)*<br>37138_-_MESGID_CONN_UPDOWN, 37141_-_MESGID_CONN_STATS, 39425_-_LOG_ID_EVENT_SSL_VPN_USER_TUNNEL_DOWN *(+3 more)* |
| `duration` | Duration of the last threatening packed captured from TA | `uint32` | 10 | wireless | 43534_-_LOG_ID_EVENT_WIRELESS_WIDS_LONG_DUR |

`error`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `error` | *(empty)* | `string` | 256 | cifs-auth-fail | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)* |
| `error` | Error Reason for Log Upload to Forticloud | `string` | 256 | system | 20107_-_LOG_ID_LOG_UPLOAD_ERR, 53301_-_LOG_ID_VNE_PRO_UPDATE_FAILED |

`eventtime`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `eventtime` | *(empty)* | `uint64` | 20 | cifs-auth-fail<br>switch-controller | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+49 more)* |
| `eventtime` | Event time | `uint64` | 20 | connector<br>endpoint<br>fortiextender<br>ha<br>rest-api<br>router<br>sdwan<br>security-rating<br>system<br>user<br>vpn<br>wanopt<br>webproxy<br>wireless | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+13 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+33 more)*<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY, 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+550 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>48040_-_LOG_ID_WANOPT_TUNNEL_CREATE, 48041_-_LOG_ID_WANOPT_TUNNEL_CLOSED, 48101_-_LOG_ID_WANOPT_AUTH_FAIL_PSK *(+2 more)*<br>40960_-_LOGID_EVENT_WEBPROXY_FWD_SRV_ERROR<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+184 more)* |

`hostname`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `hostname` | *(empty)* | `string` | 128 | ha | 37892_-_MESGID_VC_MOVE_MEMB_STATE |
| `hostname` | Hostname | `string` | 128 | endpoint<br>system | 45114_-_LOG_ID_EC_REG_QUARANTINE, 45115_-_LOG_ID_EC_REG_UNQUARANTINE<br>22223_-_LOG_ID_EXT_RESOURCE_DEBUG, 26001_-_LOG_ID_DHCP_ACK, 26002_-_LOG_ID_DHCP_RELEASE *(+3 more)* |

`ip`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `ip` | *(empty)* | `ip` | 39 | fortiextender<br>ha<br>system<br>webproxy<br>wireless | 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR, 46403_-_LOG_ID_EVENT_EXT_REMOTE_EMERG *(+7 more)*<br>37911_-_MESGID_HA_ACTIVITY_INFO<br>22035_-_LOG_ID_CSF_UPSTREAM_SN_CHANGED, 22036_-_LOG_ID_CSF_FGT_CONNECTED, 22037_-_LOG_ID_CSF_FGT_DISCONNECTED *(+9 more)*<br>40960_-_LOGID_EVENT_WEBPROXY_FWD_SRV_ERROR<br>43522_-_LOG_ID_EVENT_WIRELESS_WTP, 43526_-_LOG_ID_EVENT_WIRELESS_WTPR, 43528_-_LOG_ID_EVENT_WIRELESS_WTPR_ERROR *(+39 more)* |
| `ip` | Source IP | `ip` | 39 | endpoint | 45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+4 more)* |

`level`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `level` | *(empty)* | `string` | 11 | cifs-auth-fail<br>switch-controller | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+49 more)* |
| `level` | Log Level | `string` | 11 | connector<br>endpoint<br>fortiextender<br>ha<br>rest-api<br>router<br>sdwan<br>security-rating<br>system<br>user<br>vpn<br>wanopt<br>webproxy<br>wireless | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+13 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+33 more)*<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY, 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+550 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>48040_-_LOG_ID_WANOPT_TUNNEL_CREATE, 48041_-_LOG_ID_WANOPT_TUNNEL_CLOSED, 48101_-_LOG_ID_WANOPT_AUTH_FAIL_PSK *(+2 more)*<br>40960_-_LOGID_EVENT_WEBPROXY_FWD_SRV_ERROR<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+184 more)* |

`logdesc`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `logdesc` | *(empty)* | `string` | 4096 | cifs-auth-fail<br>switch-controller | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+49 more)* |
| `logdesc` | Log Description | `string` | 4096 | connector<br>endpoint<br>fortiextender<br>ha<br>rest-api<br>router<br>sdwan<br>security-rating<br>system<br>user<br>vpn<br>wanopt<br>webproxy<br>wireless | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+13 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+33 more)*<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY, 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+550 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>48040_-_LOG_ID_WANOPT_TUNNEL_CREATE, 48041_-_LOG_ID_WANOPT_TUNNEL_CLOSED, 48101_-_LOG_ID_WANOPT_AUTH_FAIL_PSK *(+2 more)*<br>40960_-_LOGID_EVENT_WEBPROXY_FWD_SRV_ERROR<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+184 more)* |

`logid`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `logid` | *(empty)* | `string` | 10 | cifs-auth-fail<br>switch-controller | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+49 more)* |
| `logid` | Log ID | `string` | 10 | connector<br>endpoint<br>fortiextender<br>ha<br>rest-api<br>router<br>sdwan<br>security-rating<br>system<br>user<br>vpn<br>wanopt<br>webproxy<br>wireless | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+13 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+33 more)*<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY, 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+550 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>48040_-_LOG_ID_WANOPT_TUNNEL_CREATE, 48041_-_LOG_ID_WANOPT_TUNNEL_CLOSED, 48101_-_LOG_ID_WANOPT_AUTH_FAIL_PSK *(+2 more)*<br>40960_-_LOGID_EVENT_WEBPROXY_FWD_SRV_ERROR<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+184 more)* |

`mode`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `mode` | IPsec VPN ID protection mode | `string` | 12 | vpn | 37127_-_MESGID_NEG_PROGRESS_P1_NOTIF, 37128_-_MESGID_NEG_PROGRESS_P1_ERROR, 37129_-_MESGID_NEG_PROGRESS_P2_NOTIF *(+1 more)* |
| `mode` | Mode | `string` | 12 | system | 22800_-_LOG_ID_SCAN_SERV_FAIL |

`msg`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `msg` | *(empty)* | `string` | 4096 | cifs-auth-fail<br>switch-controller | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+49 more)* |
| `msg` | Log Message | `string` | 4096 | connector<br>endpoint<br>fortiextender<br>ha<br>router<br>sdwan<br>system<br>user<br>vpn<br>wanopt<br>webproxy<br>wireless | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+13 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+33 more)*<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+546 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>48040_-_LOG_ID_WANOPT_TUNNEL_CREATE, 48041_-_LOG_ID_WANOPT_TUNNEL_CLOSED, 48101_-_LOG_ID_WANOPT_AUTH_FAIL_PSK *(+2 more)*<br>40960_-_LOGID_EVENT_WEBPROXY_FWD_SRV_ERROR<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+184 more)* |

`name`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `name` | *(empty)* | `string` | 128 | switch-controller | 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT, 22853_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_MISS, 22861_-_LOG_ID_FLPOLD_NAC_ADD *(+42 more)* |
| `name` | Display Name of the Connection | `string` | 128 | endpoint<br>system<br>vpn | 45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE<br>22009_-_LOG_ID_FAIL_FIND_AV_PROFILE, 22203_-_LOG_ID_AUTO_GEN_CERT_FAIL, 22204_-_LOG_ID_AUTO_GEN_CERT_PENDING *(+12 more)*<br>41984_-_LOG_ID_EVENT_VPN_CERT_LOAD, 41985_-_LOG_ID_EVENT_VPN_CERT_REMOVAL, 41986_-_LOG_ID_EVENT_VPN_CERT_REGEN *(+5 more)* |

`policyid`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `policyid` | *(empty)* | `uint32` | 10 | cifs-auth-fail | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)* |
| `policyid` | Policy ID | `uint32` | 10 | system<br>user<br>wanopt | 43776_-_LOG_ID_EVENT_NAC_QUARANTINE, 43777_-_LOG_ID_EVENT_NAC_ANOMALY_QUARANTINE<br>43008_-_LOG_ID_EVENT_AUTH_SUCCESS, 43009_-_LOG_ID_EVENT_AUTH_FAILED, 43010_-_LOG_ID_EVENT_AUTH_LOCKOUT *(+8 more)*<br>48040_-_LOG_ID_WANOPT_TUNNEL_CREATE, 48041_-_LOG_ID_WANOPT_TUNNEL_CLOSED, 48101_-_LOG_ID_WANOPT_AUTH_FAIL_PSK *(+2 more)* |

`profile`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `profile` | *(empty)* | `string` | 64 | cifs-auth-fail | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)* |
| `profile` | Profile Name | `string` | 64 | system<br>wireless | 22223_-_LOG_ID_EXT_RESOURCE_DEBUG, 32001_-_LOG_ID_ADMIN_LOGIN_SUCC, 43776_-_LOG_ID_EVENT_NAC_QUARANTINE *(+1 more)*<br>43522_-_LOG_ID_EVENT_WIRELESS_WTP, 43551_-_LOG_ID_EVENT_WIRELESS_WTP_JOIN, 43552_-_LOG_ID_EVENT_WIRELESS_WTP_LEAVE *(+17 more)* |

`scope`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `scope` | *(empty)* | `string` | 16 | system | 22040_-_LOG_ID_CSF_DEVICE_JOIN, 22041_-_LOG_ID_CSF_DEVICE_LEAVE, 22042_-_LOG_ID_CSF_DEVICE_UPDATE |
| `scope` | FortiGuard Override Scope | `string` | 16 | user | 43020_-_LOG_ID_EVENT_AUTH_FGOVRD_SUCCESS, 43029_-_LOG_ID_EVENT_AUTH_WARNING_SUCCESS |

`seq`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `seq` | *(empty)* | `string` | 512 | system | 32151_-_LOG_ID_ADD_IP6_LOCAL_POL, 32152_-_LOG_ID_CHG_IP6_LOCAL_POL, 32153_-_LOG_ID_DEL_IP6_LOCAL_POL *(+3 more)* |
| `seq` | Sequence | `string` | 512 | vpn<br>wireless | 37131_-_MESGID_ESP_ERROR, 37132_-_MESGID_ESP_CRITICAL<br>43530_-_LOG_ID_EVENT_WIRELESS_WIDS_WL_BRIDGE, 43531_-_LOG_ID_EVENT_WIRELESS_WIDS_BR_DEAUTH, 43532_-_LOG_ID_EVENT_WIRELESS_WIDS_NL_PBRESP *(+5 more)* |

`server`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `server` | AD server FQDN or IP | `string` | 64 | user<br>wireless | 38031_-_LOG_ID_FSSO_LOGON, 38032_-_LOG_ID_FSSO_LOGOFF, 38033_-_LOG_ID_FSSO_SVR_STATUS *(+4 more)*<br>43658_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_NO_RESP, 43659_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_DIFF_OFFER, 43660_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_NO_ACK *(+22 more)* |
| `server` | Server IP Address | `string` | 64 | system | 20107_-_LOG_ID_LOG_UPLOAD_ERR, 20108_-_LOG_ID_LOG_UPLOAD_DONE, 22912_-_LOG_ID_FDS_SRV_ERRCON *(+11 more)* |

`severity`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `severity` | *(empty)* | `string` | 10 | system | 20232_-_LOG_ID_SYS_SECURITY_LOAD_MODULE_VIOLATION, 20233_-_LOG_ID_SYS_SECURITY_FILE_HASH_MISSING, 20234_-_LOG_ID_SYS_SECURITY_FILE_HASH_MISMATCH |
| `severity` | Severity | `string` | 10 | endpoint | 45071_-_LOG_ID_FCC_VULN_SCAN |

`sn`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `sn` | *(empty)* | `string` | 64 | switch-controller | 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT, 22853_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_MISS, 22861_-_LOG_ID_FLPOLD_NAC_ADD *(+42 more)* |
| `sn` | Serial Number | `string` | 64 | endpoint<br>fortiextender<br>ha<br>system<br>wireless | 45124_-_LOG_ID_EC_VPND_CONNECT, 45125_-_LOG_ID_EC_VPND_DISCONNECT<br>46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR, 46403_-_LOG_ID_EVENT_EXT_REMOTE_EMERG *(+7 more)*<br>37892_-_MESGID_VC_MOVE_MEMB_STATE, 37893_-_MESGID_VC_DETECT_MEMB_DEAD, 37894_-_MESGID_VC_DETECT_MEMB_JOIN *(+1 more)*<br>22031_-_LOG_ID_SUCCESS_CSF_LOG_SYNC_CONFIG_CHANGED, 22032_-_LOG_ID_CSF_LOOP_FOUND, 22035_-_LOG_ID_CSF_UPSTREAM_SN_CHANGED *(+24 more)*<br>43522_-_LOG_ID_EVENT_WIRELESS_WTP, 43524_-_LOG_ID_EVENT_WIRELESS_STA, 43526_-_LOG_ID_EVENT_WIRELESS_WTPR *(+146 more)* |
| `sn` | Serial number for login or logout events. Used to correlate login and logout events. | `string` | 64 | system | 32001_-_LOG_ID_ADMIN_LOGIN_SUCC, 32002_-_LOG_ID_ADMIN_LOGIN_FAIL, 32003_-_LOG_ID_ADMIN_LOGOUT |

`src_int`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `src_int` | *(empty)* | `string` | 64 | cifs-auth-fail | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)* |
| `src_int` | Source Interface | `string` | 64 | router<br>system | 51000_-_LOG_ID_NB_TBL_CHG<br>22810_-_LOG_ID_SCANUNIT_ERROR_BLOCK, 22811_-_LOG_ID_SCANUNIT_ERROR_PASS, 43776_-_LOG_ID_EVENT_NAC_QUARANTINE *(+1 more)* |

`srcip`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `srcip` | *(empty)* | `ip` | 39 | cifs-auth-fail<br>switch-controller | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22904_-_LOG_ID_CAPUTP_SESSION_NOTIF |
| `srcip` | Source IP | `ip` | 39 | endpoint<br>router<br>system<br>user<br>wanopt<br>wireless | 45071_-_LOG_ID_FCC_VULN_SCAN<br>51000_-_LOG_ID_NB_TBL_CHG<br>20007_-_LOG_ID_SOCKET_EXHAUSTED, 20214_-_LOG_ID_LOCAL_OUT_IOC, 22810_-_LOG_ID_SCANUNIT_ERROR_BLOCK *(+9 more)*<br>38031_-_LOG_ID_FSSO_LOGON, 38032_-_LOG_ID_FSSO_LOGOFF, 38662_-_LOGID_EVENT_RAD_STAT_PROTO_ERROR *(+30 more)*<br>48040_-_LOG_ID_WANOPT_TUNNEL_CREATE, 48041_-_LOG_ID_WANOPT_TUNNEL_CLOSED, 48101_-_LOG_ID_WANOPT_AUTH_FAIL_PSK *(+2 more)*<br>43524_-_LOG_ID_EVENT_WIRELESS_STA, 43572_-_LOG_ID_EVENT_WIRELESS_STA_ASSO, 43573_-_LOG_ID_EVENT_WIRELESS_STA_AUTH *(+22 more)* |

`srcport`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `srcport` | *(empty)* | `uint16` | 5 | cifs-auth-fail | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)* |
| `srcport` | Source port | `uint16` | 5 | system<br>wanopt | 20007_-_LOG_ID_SOCKET_EXHAUSTED, 20214_-_LOG_ID_LOCAL_OUT_IOC, 22810_-_LOG_ID_SCANUNIT_ERROR_BLOCK *(+4 more)*<br>48040_-_LOG_ID_WANOPT_TUNNEL_CREATE, 48041_-_LOG_ID_WANOPT_TUNNEL_CLOSED, 48101_-_LOG_ID_WANOPT_AUTH_FAIL_PSK *(+2 more)* |

`subtype`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `subtype` | *(empty)* | `string` | 20 | cifs-auth-fail<br>switch-controller | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+49 more)* |
| `subtype` | Log Subtype | `string` | 20 | connector<br>endpoint<br>fortiextender<br>ha<br>rest-api<br>router<br>sdwan<br>security-rating<br>system<br>user<br>vpn<br>wanopt<br>webproxy<br>wireless | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+13 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+33 more)*<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY, 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+550 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>48040_-_LOG_ID_WANOPT_TUNNEL_CREATE, 48041_-_LOG_ID_WANOPT_TUNNEL_CLOSED, 48101_-_LOG_ID_WANOPT_AUTH_FAIL_PSK *(+2 more)*<br>40960_-_LOGID_EVENT_WEBPROXY_FWD_SRV_ERROR<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+184 more)* |

`time`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `time` | *(empty)* | `string` | 8 | cifs-auth-fail<br>switch-controller | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+49 more)* |
| `time` | Time | `string` | 8 | connector<br>endpoint<br>fortiextender<br>ha<br>rest-api<br>router<br>sdwan<br>security-rating<br>system<br>user<br>vpn<br>wanopt<br>webproxy<br>wireless | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+13 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+33 more)*<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY, 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+550 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>48040_-_LOG_ID_WANOPT_TUNNEL_CREATE, 48041_-_LOG_ID_WANOPT_TUNNEL_CLOSED, 48101_-_LOG_ID_WANOPT_AUTH_FAIL_PSK *(+2 more)*<br>40960_-_LOGID_EVENT_WEBPROXY_FWD_SRV_ERROR<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+184 more)* |

`type`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `type` | *(empty)* | `string` | 16 | cifs-auth-fail<br>switch-controller | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+49 more)* |
| `type` | Log Type | `string` | 16 | connector<br>endpoint<br>fortiextender<br>ha<br>rest-api<br>router<br>sdwan<br>security-rating<br>system<br>user<br>vpn<br>wanopt<br>webproxy<br>wireless | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+13 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+33 more)*<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY, 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+550 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>48040_-_LOG_ID_WANOPT_TUNNEL_CREATE, 48041_-_LOG_ID_WANOPT_TUNNEL_CLOSED, 48101_-_LOG_ID_WANOPT_AUTH_FAIL_PSK *(+2 more)*<br>40960_-_LOGID_EVENT_WEBPROXY_FWD_SRV_ERROR<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+184 more)* |

`tz`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `tz` | *(empty)* | `string` | 5 | cifs-auth-fail<br>switch-controller | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+49 more)* |
| `tz` | Time zone | `string` | 5 | connector<br>endpoint<br>fortiextender<br>ha<br>rest-api<br>router<br>sdwan<br>security-rating<br>system<br>user<br>vpn<br>wanopt<br>webproxy<br>wireless | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+13 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+33 more)*<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY, 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+550 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>48040_-_LOG_ID_WANOPT_TUNNEL_CREATE, 48041_-_LOG_ID_WANOPT_TUNNEL_CLOSED, 48101_-_LOG_ID_WANOPT_AUTH_FAIL_PSK *(+2 more)*<br>40960_-_LOGID_EVENT_WEBPROXY_FWD_SRV_ERROR<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+184 more)* |

`ui`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `ui` | *(empty)* | `string` | 64 | switch-controller | 22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+48 more)* |
| `ui` | User Interface | `string` | 64 | ha<br>rest-api<br>router<br>system<br>user<br>vpn | 35014_-_LOG_ID_HA_RESET_UPTIME, 35015_-_LOG_ID_HA_CLEAR_HISTORY<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20401_-_LOG_ID_ROUTER_CLEAR<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+144 more)*<br>38011_-_LOG_ID_FIPS_DECRY_FAIL<br>41984_-_LOG_ID_EVENT_VPN_CERT_LOAD, 41985_-_LOG_ID_EVENT_VPN_CERT_REMOVAL, 41986_-_LOG_ID_EVENT_VPN_CERT_REGEN *(+2 more)* |

`user`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `user` | *(empty)* | `string` | 256 | switch-controller | 22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+48 more)* |
| `user` | User name of authenticated user | `string` | 256 | endpoint<br>ha<br>rest-api<br>router<br>system<br>user<br>vpn<br>wireless | 45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+5 more)*<br>35014_-_LOG_ID_HA_RESET_UPTIME, 35015_-_LOG_ID_HA_CLEAR_HISTORY<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20401_-_LOG_ID_ROUTER_CLEAR<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+182 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+25 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+53 more)*<br>43524_-_LOG_ID_EVENT_WIRELESS_STA, 43572_-_LOG_ID_EVENT_WIRELESS_STA_ASSO, 43573_-_LOG_ID_EVENT_WIRELESS_STA_AUTH *(+64 more)* |

`vd`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `vd` | *(empty)* | `string` | 32 | cifs-auth-fail<br>switch-controller | 63002_-_LOG_ID_CIFS_CONN_FAIL, 63003_-_LOG_ID_CIFS_AUTH_FAIL, 63004_-_LOG_ID_CIFS_AUTH_INTERNAL_ERROR *(+1 more)*<br>22850_-_LOG_ID_USER_QUARANTINE_MAC_ADD, 22851_-_LOG_ID_USER_QUARANTINE_MAC_DELETE, 22852_-_LOG_ID_USER_QUARANTINE_MAC_BOUNCE_PORT_HIT *(+49 more)* |
| `vd` | Virtual Domain Name | `string` | 32 | connector<br>endpoint<br>fortiextender<br>ha<br>rest-api<br>router<br>sdwan<br>security-rating<br>system<br>user<br>vpn<br>wanopt<br>webproxy<br>wireless | 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD, 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE, 53202_-_LOG_ID_CONNECTOR_API_FAILED *(+3 more)*<br>45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(+13 more)*<br>46400_-_LOG_ID_EVENT_EXT_SYS, 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR *(+8 more)*<br>35001_-_LOG_ID_HA_SYNC_VIRDB, 35002_-_LOG_ID_HA_SYNC_ETDB, 35003_-_LOG_ID_HA_SYNC_EXDB *(+33 more)*<br>47301_-_LOG_ID_EVENT_REST_API_OK, 47302_-_LOG_ID_EVENT_REST_API_ERR<br>20300_-_LOG_ID_BGP_NB_STAT_CHG, 20301_-_LOG_ID_VZ_LOG_INFO, 20302_-_LOG_ID_OSPF_NB_STAT_CHG *(+7 more)*<br>22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS, 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS, 22925_-_LOG_ID_EVENT_VWL_SLA_INFO *(+10 more)*<br>52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY, 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE<br>20002_-_LOG_ID_DOMAIN_UNRESOLVABLE, 20003_-_LOG_ID_MAIL_SENT_FAIL, 20004_-_LOG_ID_POLICY_TOO_BIG *(+550 more)*<br>38010_-_LOG_ID_FIPS_ENCRY_FAIL, 38011_-_LOG_ID_FIPS_DECRY_FAIL, 38012_-_LOG_ID_ENTROPY_TOKEN *(+46 more)*<br>23101_-_LOG_ID_IPSEC_TUNNEL_UP, 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN, 23103_-_LOG_ID_IPSEC_TUNNEL_STAT *(+78 more)*<br>48040_-_LOG_ID_WANOPT_TUNNEL_CREATE, 48041_-_LOG_ID_WANOPT_TUNNEL_CLOSED, 48101_-_LOG_ID_WANOPT_AUTH_FAIL_PSK *(+2 more)*<br>40960_-_LOGID_EVENT_WEBPROXY_FWD_SRV_ERROR<br>43520_-_LOG_ID_EVENT_WIRELESS_SYS, 43521_-_LOG_ID_EVENT_WIRELESS_ROGUE, 43522_-_LOG_ID_EVENT_WIRELESS_WTP *(+184 more)* |

`version`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `version` | *(empty)* | `string` | 64 | fortiextender | 46401_-_LOG_ID_EVENT_EXT_LOCAL, 46402_-_LOG_ID_EVENT_EXT_LOCAL_ERROR |
| `version` | Version | `string` | 64 | system<br>vpn | 22080_-_LOG_ID_PROVISION_LATEST_SUCCEEDED, 22081_-_LOG_ID_PROVISION_LATEST_FAILED, 22085_-_LOG_ID_DEVICE_UPGRADE_SUCCEEDED *(+9 more)*<br>37127_-_MESGID_NEG_PROGRESS_P1_NOTIF, 37128_-_MESGID_NEG_PROGRESS_P1_ERROR, 37129_-_MESGID_NEG_PROGRESS_P2_NOTIF *(+1 more)* |

#### UTM

| Log Field Name | Description | Data Type | Length |
|----------------|-------------|-----------|--------|
| `action` | X |  | X |
| `agent` | X |  |  |
| `analyticscksum` | X |  |  |
| `analyticssubmit` | X |  |  |
| `attack` | X |  |  |
| `authserver` | X |  |  |
| `banword` | X |  |  |
| `cat` | X |  |  |
| `catdesc` | X |  |  |
| `cc` |  |  | X |
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
| `filtername` |  |  | X |
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
| `rcvdbyte` | X | X | X |
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
| `action` | *(empty)* | `string` | 11 | Webfilter | 13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `action` | *(empty)* | `string` | 17 | ICAP | 60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN |
| `action` | *(empty)* | `string` | 18 | Virus | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `action` | *(empty)* | `string` | 20 | FILE-FILTER<br>SSL | 64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)* |
| `action` | *(empty)* | `string` | 8 | EmailFilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)* |
| `action` | Action | `string` | 16 | Anomaly | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS |
| `action` | Action. Eg. block , allow | `string` | 15 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |
| `action` | Security action performed by DNS filter | `string` | 16 | DNS | 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK, 54401_-_LOG_ID_DNS_URL_FILTER_ALLOW *(+8 more)* |
| `action` | Security action performed by IPS:<br> detected - Attack is detected , but NOT blocked (similar to monitor)<br> dropped - Silent packet blocked<br> reset - Blocked and respond with Reset<br> reset_client - Blocked and reset sent to the client<br> reset_server - Blocked and reset sent to the server<br> drop_session - Silent block<br> pass_session - Session allowed<br> clear_session - Session was removed /closed | `string` | 16 | IPS | 16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |
| `action` | Security action performed by WF:<br> blocked - url is blocked by webfilter<br> passthrough - url is allowed by webfilter | `string` | 11 | Webfilter | 12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+42 more)* |
| `action` | Status of the session. Uses following definition: - Deny = blocked by firewall policy. - Start = session start log (special option to enable logging at start of a session). This means firewall allowed. - All Others = allowed by Firewall Policy and the status indicates how it was closed. | `string` | 17 | WAF | 30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `action` | The status of the session:<br> blocked - Blocked infected file by AV engine<br> passthrough - Allowed by AV engine<br> monitored - Log, but do NOT block infected file<br> analytics - Submitted to Sandbox for analysis | `string` | 18 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+51 more)* |
| `action` | The status of the session:<br> log-only - DLP event is detected , but NOT blocked (similar to monitor action)<br> block - Blocked<br> exempt - Allowed<br> ban - blocked (Not in used since FortiOS 5.0, replaced by blocked)<br> ban-sender - blocks all data being sent by an ip or user (Not in used since FortiOS 5.0, replaced by quarantine)<br> quarantine-ip - Blocked and band the source ip (Not in used since FortiOS 5.0)<br> quarantine-interface - Blocked and band the source interface (Not in used since FortiOS 5.0) | `string` | 20 | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |
| `action` | The status of the session:<br> pass - Application is allowed<br> block - Application is blocked (silent)<br> reject - Quarantine<br> reset - Application is blocked and Reset was sent<br>Sometimes, there is a block page for blocking | `string` | 16 | APP-CTRL | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)* |
| `action` | The status of the ssh-channel:<br> passthrough - channel is allowed<br> blocked - channel is blocked | `string` | 17 | SSH | 61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)* |

`agent`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `agent` | *(empty)* | `string` | 1024 | APP-CTRL<br>EmailFilter<br>FILE-FILTER<br>IPS<br>Virus | 28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16399_-_LOGID_ATTACK_MALICIOUS_URL<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `agent` | Agent | `string` | 1024 | WAF | 30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `agent` | User agent - eg. agent="Mozilla/5.0" | `string` | 1024 | DLP<br>Virus<br>Webfilter | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+48 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+49 more)* |

`analyticscksum`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `analyticscksum` | *(empty)* | `string` | 64 | Virus | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `analyticscksum` | The checksum of the file submitted for analytics | `string` | 64 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+41 more)* |

`analyticssubmit`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `analyticssubmit` | *(empty)* | `string` | 10 | Virus | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `analyticssubmit` | The flag for analytics submission | `string` | 10 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+38 more)* |

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
| `authserver` | *(empty)* | `string` | 64 | EmailFilter<br>FILE-FILTER<br>Virus | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `authserver` | Authentication Server | `string` | 64 | DLP<br>WAF | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `authserver` | Authentication server for the user | `string` | 64 | APP-CTRL<br>IPS<br>Webfilter | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |
| `authserver` | Server used to authenticate the involved user | `string` | 64 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+50 more)* |

`banword`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `banword` | *(empty)* | `string` | 128 | EmailFilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)* |
| `banword` | Banned word | `string` | 128 | Webfilter | 12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+2 more)* |

`cat`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `cat` | *(empty)* | `uint8` | 3 | SSL | 62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+2 more)* |
| `cat` | DNS category ID | `uint8` | 3 | DNS | 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK, 54401_-_LOG_ID_DNS_URL_FILTER_ALLOW *(+8 more)* |
| `cat` | Web category ID | `uint8` | 3 | Webfilter | 12688_-_LOG_ID_WEB_SSL_EXEMPT, 13056_-_LOG_ID_WEB_FTGD_CAT_BLK, 13057_-_LOG_ID_WEB_FTGD_CAT_WARN *(+10 more)* |

`catdesc`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `catdesc` | *(empty)* | `string` | 64 | SSL | 62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+2 more)* |
| `catdesc` | DNS category description | `string` | 64 | DNS | 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK, 54401_-_LOG_ID_DNS_URL_FILTER_ALLOW *(+8 more)* |
| `catdesc` | Web category description | `string` | 64 | Webfilter | 12688_-_LOG_ID_WEB_SSL_EXEMPT, 12802_-_LOG_ID_WEB_FTGD_QUOTA, 13056_-_LOG_ID_WEB_FTGD_CAT_BLK *(+11 more)* |

`cc`

**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `cc` | *(empty)* | `string` | 4096 | EmailFilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)* |
| `cc` | *(empty)* | `string` | 512 | DLP<br>FILE-FILTER<br>Virus | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+71 more)* |

`checksum`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `checksum` | *(empty)* | `string` | 16 | Virus | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `checksum` | The checksum of the scanned file | `string` | 16 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+43 more)* |

`command`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `command` | *(empty)* | `string` | 16 | Virus | 8452_-_MESGID_BLOCK_COMMAND |
| `command` | Shell command | `string` | 256 | SSH | 61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)* |

`contentdisarmed`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `contentdisarmed` | *(empty)* | `string` | 13 | Virus | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `contentdisarmed` | Content Disarm action- eg. disarmed, detected | `string` | 13 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+38 more)* |

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
| `craction` | *(empty)* | `uint32` | 10 | Virus | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `craction` | Action performed by Threat Weight | `uint32` | 10 | IPS | 16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |
| `craction` | Client Reputation Action | `uint32` | 10 | APP-CTRL<br>Anomaly<br>Webfilter | 28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+42 more)* |
| `craction` | Threat Weight action | `uint32` | 10 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+50 more)* |

`crlevel`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `crlevel` | *(empty)* | `string` | 10 | Virus | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `crlevel` | Client Reputation Level | `string` | 10 | APP-CTRL<br>Anomaly<br>IPS | 28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |
| `crlevel` | Client Reputation level | `string` | 10 | Webfilter | 12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+42 more)* |
| `crlevel` | Threat Weight Level | `string` | 10 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+50 more)* |

`crscore`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `crscore` | *(empty)* | `uint32` | 10 | Virus | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `crscore` | Client Reputation Score | `uint32` | 10 | APP-CTRL<br>Anomaly<br>IPS<br>Webfilter | 28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+42 more)* |
| `crscore` | Threat Weight Score | `uint32` | 10 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+50 more)* |

`date`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `date` | *(empty)* | `string` | 10 | EmailFilter<br>FILE-FILTER<br>FORTI-SWITCH<br>ICAP<br>SSL<br>Virus<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>56001_-_LOG_ID_FSW_FLOW<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `date` | Date | `string` | 10 | APP-CTRL<br>Anomaly<br>DLP<br>DNS<br>GTP<br>IPS<br>SSH<br>Virus<br>WAF<br>Webfilter | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF, 24578_-_LOG_ID_DLP_DOC_SOURCE *(+1 more)*<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+15 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+51 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+46 more)* |
| `date` | Day, month, and year when the log message was recorded. | `string` | 10 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |

`devid`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `devid` | *(empty)* | `string` | 16 | EmailFilter<br>FILE-FILTER<br>FORTI-SWITCH<br>ICAP<br>SSL<br>Virus<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>56001_-_LOG_ID_FSW_FLOW<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+79 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `devid` | Deivce ID | `string` | 16 | APP-CTRL<br>Anomaly<br>IPS | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |
| `devid` | Device ID | `string` | 16 | DLP<br>DNS<br>GTP<br>SSH<br>WAF<br>Webfilter | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF, 24578_-_LOG_ID_DLP_DOC_SOURCE *(+1 more)*<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+15 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+46 more)* |
| `devid` | Serial number of the device for the traffic's origin. | `string` | 16 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |

`direction`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `direction` | *(empty)* | `string` | 8 | EmailFilter<br>FILE-FILTER<br>Virus | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `direction` | Direction | `string` | 4096 | WAF | 30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `direction` | Direction of packets | `string` | 8 | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |
| `direction` | Direction of session | `string` | 4096 | SSH | 61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)* |
| `direction` | Direction of the packets | `string` | 8 | APP-CTRL | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)* |
| `direction` | Direction of the web traffic | `string` | 8 | Webfilter | 12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+41 more)* |
| `direction` | Message/packets direction | `string` | 8 | IPS<br>Virus | 16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+50 more)* |

`dstintf`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `dstintf` | *(empty)* | `string` | 32 | FILE-FILTER<br>ICAP<br>SSL<br>Virus<br>Webfilter | 64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `dstintf` | *(empty)* | `string` | 64 | EmailFilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)* |
| `dstintf` | Destination Interface | `string` | 32 | DLP<br>DNS<br>SSH<br>Virus<br>WAF<br>Webfilter | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+50 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |
| `dstintf` | Destination Interface | `string` | 64 | APP-CTRL<br>Anomaly<br>IPS | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |

`dstintfrole`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `dstintfrole` | *(empty)* | `string` | 10 | EmailFilter<br>FILE-FILTER<br>ICAP<br>SSL<br>Virus<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `dstintfrole` | Destination Interface Role | `string` | 10 | DNS | 54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)* |
| `dstintfrole` | Destination Interface's assigned role (LAN, WAN, etc.) | `string` | 10 | APP-CTRL<br>Anomaly<br>DLP<br>IPS<br>SSH<br>Virus<br>WAF<br>Webfilter | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+50 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |

`dstip`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `dstip` | *(empty)* | `ip` | 39 | EmailFilter<br>FILE-FILTER<br>FORTI-SWITCH<br>ICAP<br>SSL<br>Virus<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>56001_-_LOG_ID_FSW_FLOW<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `dstip` | Destination IP | `ip` | 39 | APP-CTRL<br>Anomaly<br>DLP<br>DNS<br>IPS<br>SSH<br>VoIP<br>Webfilter | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+44 more)* |
| `dstip` | Destination IP Address | `ip` | 39 | Virus<br>WAF | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+51 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |

`dstport`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `dstport` | *(empty)* | `uint16` | 5 | EmailFilter<br>FILE-FILTER<br>ICAP<br>SSL<br>Virus<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `dstport` | Destination Port | `uint16` | 5 | APP-CTRL<br>Anomaly<br>DLP<br>DNS<br>GTP<br>IPS<br>SSH<br>Virus<br>WAF<br>Webfilter | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+11 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16399_-_LOGID_ATTACK_MALICIOUS_URL, 16400_-_LOGID_ATTACK_BOTNET_WARNING *(+1 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+51 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+44 more)* |

`dtype`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `dtype` | *(empty)* | `string` | 32 | Virus | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `dtype` | Data type for virus category | `string` | 32 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+39 more)* |

`duration`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `duration` | *(empty)* | `uint32` | 10 | FORTI-SWITCH | 56001_-_LOG_ID_FSW_FLOW |
| `duration` | Duration of the session. Ex: 180 (in seconds) | `uint32` | 10 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+1 more)* |
| `duration` | Tunnel duration | `uint32` | 10 | GTP | 41221_-_LOGID_GTP_TRAFFIC_COUNT, 41228_-_LOGID_GTPV2_TRAFFIC_COUNT, 41233_-_LOGID_PFCP_TRAFFIC_COUNT |

`epoch`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `epoch` | *(empty)* | `uint32` | 10 | Virus | 9239_-_MESGID_CONTENT_DISARM_NOTIF, 9240_-_MESGID_CONTENT_DISARM_WARNING |
| `epoch` | Epoch | `uint32` | 10 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |
| `epoch` | Epoch used for locating file | `uint32` | 10 | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |

`error`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `error` | DNS filter service error message | `string` | 256 | DNS | 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK, 54401_-_LOG_ID_DNS_URL_FILTER_ALLOW *(+8 more)* |
| `error` | URL rating error message | `string` | 256 | Webfilter | 12558_-_LOG_ID_URL_FILTER_RATING_ERR, 12800_-_LOG_ID_WEB_FTGD_ERR, 12801_-_LOG_ID_WEB_FTGD_WARNING |

`eventid`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `eventid` | *(empty)* | `uint32` | 10 | Virus | 9239_-_MESGID_CONTENT_DISARM_NOTIF, 9240_-_MESGID_CONTENT_DISARM_WARNING |
| `eventid` | Event ID | `uint32` | 10 | WAF | 30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `eventid` | The serial number of the dlparchive file in the same epoch | `uint32` | 10 | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |

`eventtime`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `eventtime` | *(empty)* | `uint64` | 20 | EmailFilter<br>FILE-FILTER<br>FORTI-SWITCH<br>ICAP<br>SSL<br>Virus<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>56001_-_LOG_ID_FSW_FLOW<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `eventtime` | Event Time | `uint64` | 20 | APP-CTRL | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)* |
| `eventtime` | Event Time, Time when WAF event detected | `uint64` | 20 | WAF | 30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `eventtime` | Event Time, time when DLP event detected. | `uint64` | 20 | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF, 24578_-_LOG_ID_DLP_DOC_SOURCE *(+1 more)* |
| `eventtime` | Event Timestamp | `uint64` | 20 | DNS | 54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)* |
| `eventtime` | Event time | `uint64` | 20 | SSH | 61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)* |
| `eventtime` | Event time line | `uint64` | 20 | GTP | 41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+15 more)* |
| `eventtime` | Time when detection occured | `uint64` | 20 | Anomaly<br>IPS<br>Virus | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+51 more)* |
| `eventtime` | Time when event occured | `uint64` | 20 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |
| `eventtime` | Web Filter event time | `uint64` | 20 | Webfilter | 12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+46 more)* |

`eventtype`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `eventtype` | *(empty)* | `string` | 32 | EmailFilter<br>FILE-FILTER<br>ICAP<br>SSL<br>Virus<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `eventtype` | App Control Event Type | `string` | 32 | APP-CTRL | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)* |
| `eventtype` | DLP event type | `string` | 32 | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF, 24578_-_LOG_ID_DLP_DOC_SOURCE *(+1 more)* |
| `eventtype` | DNS Type (DNS query/DNS response) | `string` | 32 | DNS | 54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)* |
| `eventtype` | Event Type | `string` | 32 | Anomaly<br>SSH<br>WAF | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `eventtype` | Event type of AV | `string` | 32 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+51 more)* |
| `eventtype` | IPS Event Type | `string` | 32 | IPS | 16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |
| `eventtype` | Web Filter event type | `string` | 32 | Webfilter | 12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+46 more)* |

`fctuid`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `fctuid` | *(empty)* | `string` | 32 | EmailFilter<br>FILE-FILTER<br>SSL<br>Virus | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `fctuid` | FortiClient ID | `string` | 32 | DNS | 54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)* |
| `fctuid` | FortiClient UID | `string` | 32 | Anomaly<br>IPS<br>SSH<br>WAF<br>Webfilter | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+42 more)* |
| `fctuid` | FortiClient User ID | `string` | 32 | APP-CTRL<br>DLP | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |
| `fctuid` | Forticlient user ID | `string` | 32 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+51 more)* |

`filehash`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `filehash` | *(empty)* | `string` | 64 | Virus | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `filehash` | Used by Outbreak Prevention External Hash: the hash signature used in the detection | `string` | 64 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+36 more)* |

`filehashsrc`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `filehashsrc` | *(empty)* | `string` | 32 | Virus | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `filehashsrc` | Used by Outbreak Prevention External Hash: external source that provided the hash signature | `string` | 32 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+36 more)* |

`filename`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `filename` | *(empty)* | `string` | 256 | FILE-FILTER<br>Virus | 64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `filename` | File name | `string` | 256 | APP-CTRL<br>DLP<br>Virus | 28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+48 more)* |

`filesize`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `filesize` | *(empty)* | `uint64` | 10 | FILE-FILTER | 64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG |
| `filesize` | File size in bytes | `uint64` | 10 | APP-CTRL<br>DLP | 28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |

`filetype`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `filetype` | *(empty)* | `string` | 16 | Virus | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `filetype` | *(empty)* | `string` | 23 | FILE-FILTER | 64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG |
| `filetype` | File type | `string` | 16 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+39 more)* |
| `filetype` | File type | `string` | 23 | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |

`filtername`

**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `filtername` | *(empty)* | `string` | 128 | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |
| `filtername` | *(empty)* | `string` | 36 | FILE-FILTER | 64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG |

`filtertype`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `filtertype` | DLP filter type | `string` | 23 | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |
| `filtertype` | Filter type | `string` | 10 | Webfilter | 13568_-_LOG_ID_WEB_SCRIPTFILTER_ACTIVEX, 13573_-_LOG_ID_WEB_SCRIPTFILTER_COOKIE, 13584_-_LOG_ID_WEB_SCRIPTFILTER_APPLET *(+3 more)* |

`forwardedfor`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `forwardedfor` | *(empty)* | `string` | 128 | FILE-FILTER<br>Virus | 64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+72 more)* |
| `forwardedfor` | Forwarded For | `string` | 128 | APP-CTRL<br>DLP | 28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |
| `forwardedfor` | X-Forwarded-For HTTP header | `string` | 128 | IPS<br>Webfilter | 16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+41 more)* |

`from`

**Description conflicts** — same field, different `Description` across LOGIDs
**Data Type conflicts** — same field, different `Data Type` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `from` | *(empty)* | `string` | 128 | EmailFilter<br>FILE-FILTER<br>Virus | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `from` | Email address from the Email Headers (IMAP/POP3/SMTP) | `string` | 128 | DLP<br>Virus | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+49 more)* |
| `from` | From | `ip` | 128 | GTP | 41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+12 more)* |
| `from` | MMS-only - From/To headers from the email | `string` | 128 | Webfilter | 12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+2 more)* |
| `from` | Where call was originated from | `string` | 128 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK |

`fsaverdict`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `fsaverdict` | *(empty)* | `string` | 32 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+63 more)* |
| `fsaverdict` | FortiSandbox Verdict returned to FortiGate after analysis (clean, low risk, med risk, high risk, malicious) | `string` | 32 | Virus | 9233_-_MESGID_ANALYTICS_SUBMITTED, 9238_-_MESGID_ANALYTICS_FSA_RESULT |

`group`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `group` | *(empty)* | `string` | 512 | EmailFilter<br>FILE-FILTER<br>SSL<br>Virus<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `group` | Group name (authentication) | `string` | 512 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+50 more)* |
| `group` | Group name for authentication | `string` | 512 | SSH | 61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)* |
| `group` | User Group Name | `string` | 512 | Anomaly<br>WAF | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `group` | User group name | `string` | 512 | APP-CTRL<br>DLP<br>DNS<br>IPS<br>Webfilter | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+2 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |

`hostname`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `hostname` | *(empty)* | `string` | 256 | FILE-FILTER<br>SSL<br>Webfilter | 64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+3 more)* |
| `hostname` | The host name of a URL | `string` | 256 | APP-CTRL<br>DLP<br>IPS<br>Webfilter | 28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16399_-_LOGID_ATTACK_MALICIOUS_URL<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+42 more)* |

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
| `level` | *(empty)* | `string` | 11 | EmailFilter<br>FILE-FILTER<br>FORTI-SWITCH<br>ICAP<br>SSL<br>Virus<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>56001_-_LOG_ID_FSW_FLOW<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `level` | Log Level | `string` | 11 | Anomaly<br>DLP<br>DNS<br>GTP<br>IPS<br>VoIP<br>WAF<br>Webfilter | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF, 24578_-_LOG_ID_DLP_DOC_SOURCE *(+1 more)*<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+15 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+46 more)* |
| `level` | Log level | `string` | 11 | APP-CTRL<br>SSH<br>Virus | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+51 more)* |

`logid`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `logid` | *(empty)* | `string` | 10 | EmailFilter<br>FILE-FILTER<br>FORTI-SWITCH<br>ICAP<br>SSL<br>Virus<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>56001_-_LOG_ID_FSW_FLOW<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `logid` | Log ID | `string` | 10 | APP-CTRL<br>Anomaly<br>DLP<br>DNS<br>GTP<br>IPS<br>SSH<br>Virus<br>WAF<br>Webfilter | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF, 24578_-_LOG_ID_DLP_DOC_SOURCE *(+1 more)*<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+15 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+51 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+46 more)* |
| `logid` | Unique Log ID | `string` | 10 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |

`msg`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `msg` | *(empty)* | `string` | 4096 | ICAP<br>Virus | 60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `msg` | *(empty)* | `string` | 512 | EmailFilter<br>FILE-FILTER<br>SSL<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+14 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `msg` | Log Message | `string` | 4096 | WAF | 30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `msg` | Log Message | `string` | 518 | Anomaly | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS |
| `msg` | Log message | `string` | 4096 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+50 more)* |
| `msg` | Log message | `string` | 512 | APP-CTRL<br>DNS<br>Webfilter | 28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK, 54401_-_LOG_ID_DNS_URL_FILTER_ALLOW *(+8 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |
| `msg` | Log message for the attack | `string` | 518 | IPS | 16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |

`policyid`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `policyid` | *(empty)* | `uint32` | 10 | EmailFilter<br>FILE-FILTER<br>ICAP<br>SSL<br>Virus<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `policyid` | Policy ID | `uint32` | 10 | APP-CTRL<br>Anomaly<br>DLP<br>DNS<br>IPS<br>SSH<br>Virus<br>WAF<br>Webfilter | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+50 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |

`policytype`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `policytype` | *(empty)* | `string` | 24 | APP-CTRL<br>DLP<br>DNS<br>EmailFilter<br>FILE-FILTER<br>ICAP<br>IPS<br>SSH<br>SSL<br>Virus<br>WAF<br>Webfilter | 28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+78 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |
| `policytype` | Policy type | `string` | 24 | Anomaly | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS |

`profile`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `profile` | *(empty)* | `string` | 36 | APP-CTRL | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)* |
| `profile` | *(empty)* | `string` | 64 | EmailFilter<br>FILE-FILTER<br>ICAP<br>SSL<br>Virus<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `profile` | DLP profile name | `string` | 64 | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |
| `profile` | Full profile name | `string` | 64 | SSH<br>WAF | 61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `profile` | Name or number of associated VOIP profile | `string` | 64 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |
| `profile` | Profile Name | `string` | 64 | GTP | 41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+15 more)* |
| `profile` | Profile name for DNS filter | `string` | 64 | DNS | 54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)* |
| `profile` | Profile name for IPS | `string` | 64 | IPS | 16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |
| `profile` | The name of the profile that was used to detect and take action | `string` | 64 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+50 more)* |
| `profile` | Web Filter profile name | `string` | 64 | Webfilter | 12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+44 more)* |

`proto`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `proto` | *(empty)* | `uint8` | 3 | EmailFilter<br>FILE-FILTER<br>FORTI-SWITCH<br>ICAP<br>SSL<br>Virus<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>56001_-_LOG_ID_FSW_FLOW<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13603_-_LOG_ID_WEB_WF_COMMAND_BLOCK, 13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR *(+6 more)* |
| `proto` | Protocol | `uint8` | 3 | Anomaly<br>WAF | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `proto` | Protocol number | `uint8` | 3 | APP-CTRL<br>DLP<br>DNS<br>IPS<br>SSH<br>Virus<br>Webfilter | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+50 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+42 more)* |
| `proto` | Protocol number. Ex: for SIP it will be proto=17 | `uint8` | 3 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |

`quarskip`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `quarskip` | *(empty)* | `string` | 46 | Virus | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `quarskip` | Quarantine skip explanation | `string` | 46 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+41 more)* |

`ratemethod`

**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `ratemethod` | *(empty)* | `string` | 4096 | WAF | 30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `ratemethod` | *(empty)* | `string` | 6 | Webfilter | 12688_-_LOG_ID_WEB_SSL_EXEMPT, 13056_-_LOG_ID_WEB_FTGD_CAT_BLK, 13057_-_LOG_ID_WEB_FTGD_CAT_WARN *(+10 more)* |

`rawdata`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `rawdata` | *(empty)* | `string` | 1024 | FILE-FILTER<br>Virus | 64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+66 more)* |
| `rawdata` | Extended logging data including HTTP method, URL, client content type, server content type, user agent, referer, x-forwarded-for | `string` | 1024 | APP-CTRL<br>IPS<br>Webfilter | 28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+41 more)* |
| `rawdata` | Raw Data | `string` | 1024 | DLP<br>WAF | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |

`rcvdbyte`

**Description conflicts** — same field, different `Description` across LOGIDs
**Data Type conflicts** — same field, different `Data Type` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `rcvdbyte` | *(empty)* | `uint32` | 10 | FORTI-SWITCH | 56001_-_LOG_ID_FSW_FLOW |
| `rcvdbyte` | Received Bytes | `uint64` | 20 | Webfilter | 12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+41 more)* |

`recipient`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `recipient` | *(empty)* | `string` | 512 | EmailFilter<br>FILE-FILTER<br>Virus | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `recipient` | Email addresses from the SMTP envelope | `string` | 512 | DLP<br>Virus | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+47 more)* |

`ref`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `ref` | *(empty)* | `string` | 512 | Virus | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `ref` | Reference | `string` | 4096 | Anomaly | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS |
| `ref` | The URL of the FortiGuard IPS database entry for the attack | `string` | 512 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+36 more)* |
| `ref` | URL of the FortiGuard IPS database entry for the attack. | `string` | 4096 | IPS | 16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+2 more)* |

`referralurl`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `referralurl` | *(empty)* | `string` | 512 | APP-CTRL<br>DLP<br>FILE-FILTER<br>IPS<br>Virus<br>WAF | 28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16399_-_LOGID_ATTACK_MALICIOUS_URL<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+76 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `referralurl` | Referrer URI | `string` | 512 | Webfilter | 12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+49 more)* |

`sender`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `sender` | *(empty)* | `string` | 128 | EmailFilter<br>FILE-FILTER<br>Virus | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `sender` | Email address from the SMTP envelope | `string` | 128 | DLP<br>Virus | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+47 more)* |

`service`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `service` | *(empty)* | `string` | 36 | EmailFilter<br>FILE-FILTER<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `service` | *(empty)* | `string` | 5 | ICAP<br>SSL<br>Virus | 60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `service` | Name of Service | `string` | 80 | Anomaly | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS |
| `service` | Proxy service which scanned this traffic | `string` | 5 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+51 more)* |
| `service` | Service name | `string` | 36 | DLP<br>Webfilter | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |
| `service` | Service name | `string` | 5 | WAF | 30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `service` | Service name | `string` | 80 | APP-CTRL<br>IPS | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |

`sessionid`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `sessionid` | *(empty)* | `uint32` | 10 | EmailFilter<br>FILE-FILTER<br>GTP<br>ICAP<br>SSL<br>Virus<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>41233_-_LOGID_PFCP_TRAFFIC_COUNT<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `sessionid` | Session ID | `uint32` | 10 | APP-CTRL<br>Anomaly<br>DLP<br>DNS<br>IPS<br>SSH<br>Virus<br>WAF<br>Webfilter | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+50 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |

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
| `srccountry` | *(empty)* | `string` | 64 | APP-CTRL<br>DLP<br>DNS<br>EmailFilter<br>FILE-FILTER<br>ICAP<br>SSH<br>SSL<br>Virus<br>WAF<br>Webfilter | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+78 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |
| `srccountry` | Country name for Source IP | `string` | 64 | Anomaly<br>IPS | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |

`srcintf`

**Description conflicts** — same field, different `Description` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `srcintf` | *(empty)* | `string` | 32 | FILE-FILTER<br>ICAP<br>SSL<br>Virus<br>Webfilter | 64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `srcintf` | *(empty)* | `string` | 64 | EmailFilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)* |
| `srcintf` | Source Interface | `string` | 32 | DLP<br>DNS<br>SSH<br>Virus<br>WAF<br>Webfilter | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+50 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |
| `srcintf` | Source Interface | `string` | 64 | APP-CTRL<br>Anomaly<br>IPS | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)* |

`srcintfrole`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `srcintfrole` | *(empty)* | `string` | 10 | EmailFilter<br>FILE-FILTER<br>ICAP<br>SSL<br>Virus<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `srcintfrole` | Source Interface Role | `string` | 10 | DNS | 54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)* |
| `srcintfrole` | Source Interface's assigned role (LAN, WAN, etc.) | `string` | 10 | APP-CTRL<br>Anomaly<br>DLP<br>IPS<br>SSH<br>Virus<br>WAF<br>Webfilter | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+50 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+43 more)* |

`srcip`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `srcip` | *(empty)* | `ip` | 39 | EmailFilter<br>FILE-FILTER<br>FORTI-SWITCH<br>ICAP<br>SSL<br>Virus<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>56001_-_LOG_ID_FSW_FLOW<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `srcip` | IP address of the traffic's origin. Ex: srcip=10.1.100.155 | `ip` | 39 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |
| `srcip` | Source IP | `ip` | 39 | APP-CTRL<br>Anomaly<br>DLP<br>DNS<br>IPS<br>SSH<br>Webfilter | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+44 more)* |
| `srcip` | Source IP Address | `ip` | 39 | Virus<br>WAF | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+51 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |

`srcport`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `srcport` | *(empty)* | `uint16` | 5 | EmailFilter<br>FILE-FILTER<br>ICAP<br>SSL<br>Virus<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `srcport` | Source Port | `uint16` | 5 | APP-CTRL<br>Anomaly<br>DLP<br>DNS<br>GTP<br>IPS<br>SSH<br>Virus<br>WAF<br>Webfilter | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+11 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16399_-_LOGID_ATTACK_MALICIOUS_URL, 16400_-_LOGID_ATTACK_BOTNET_WARNING *(+1 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+51 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+44 more)* |

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
| `subject` | *(empty)* | `string` | 256 | EmailFilter<br>FILE-FILTER<br>Virus | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+71 more)* |
| `subject` | The subject title of the email message | `string` | 256 | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |

`subtype`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `subtype` | *(empty)* | `string` | 20 | EmailFilter<br>FILE-FILTER<br>FORTI-SWITCH<br>ICAP<br>SSL<br>Virus<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>56001_-_LOG_ID_FSW_FLOW<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `subtype` | Log Subtype | `string` | 20 | Anomaly<br>DNS<br>GTP<br>IPS<br>WAF | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+15 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `subtype` | Log subtype | `string` | 20 | APP-CTRL<br>DLP<br>SSH<br>Webfilter | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF, 24578_-_LOG_ID_DLP_DOC_SOURCE *(+1 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+46 more)* |
| `subtype` | Subtype | `string` | 20 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |
| `subtype` | Subtype of the virus log | `string` | 20 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+51 more)* |

`time`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `time` | *(empty)* | `string` | 8 | EmailFilter<br>FILE-FILTER<br>FORTI-SWITCH<br>ICAP<br>SSL<br>Virus<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>56001_-_LOG_ID_FSW_FLOW<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `time` | Hour clock when the log message was recorded. | `string` | 8 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |
| `time` | Time | `string` | 8 | APP-CTRL<br>Anomaly<br>DLP<br>DNS<br>GTP<br>IPS<br>SSH<br>Virus<br>WAF<br>Webfilter | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF, 24578_-_LOG_ID_DLP_DOC_SOURCE *(+1 more)*<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+15 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+51 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+46 more)* |

`to`

**Description conflicts** — same field, different `Description` across LOGIDs
**Data Type conflicts** — same field, different `Data Type` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `to` | *(empty)* | `string` | 512 | EmailFilter<br>FILE-FILTER<br>Virus | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `to` | Destination address | `string` | 512 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK |
| `to` | Email address(es) from the Email Headers (IMAP/POP3/SMTP) | `string` | 512 | DLP<br>Virus | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+49 more)* |
| `to` | MMS-only - From/To headers from the email | `string` | 512 | Webfilter | 12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+2 more)* |
| `to` | To | `ip` | 512 | GTP | 41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+12 more)* |

`trueclntip`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `trueclntip` | *(empty)* | `ip` | 39 | FILE-FILTER<br>Virus | 64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+72 more)* |
| `trueclntip` | True client's IP | `ip` | 39 | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |
| `trueclntip` | True-Client-IP | `ip` | 39 | APP-CTRL | 28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)* |
| `trueclntip` | True-Client-IP HTTP header | `ip` | 39 | IPS<br>Webfilter | 16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+41 more)* |

`type`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `type` | *(empty)* | `string` | 16 | EmailFilter<br>FILE-FILTER<br>FORTI-SWITCH<br>ICAP<br>SSL<br>Virus<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>56001_-_LOG_ID_FSW_FLOW<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `type` | Log Type | `string` | 16 | Anomaly<br>DNS<br>GTP<br>WAF | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+15 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `type` | Log type | `string` | 16 | APP-CTRL<br>DLP<br>IPS<br>SSH<br>Virus<br>Webfilter | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF, 24578_-_LOG_ID_DLP_DOC_SOURCE *(+1 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+51 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+46 more)* |
| `type` | Type of log. Ex: type="utm" | `string` | 16 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |

`tz`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `tz` | *(empty)* | `string` | 5 | APP-CTRL<br>DLP<br>EmailFilter<br>FILE-FILTER<br>FORTI-SWITCH<br>ICAP<br>IPS<br>SSL<br>Virus<br>Webfilter | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF, 24578_-_LOG_ID_DLP_DOC_SOURCE *(+1 more)*<br>20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>56001_-_LOG_ID_FSW_FLOW<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `tz` | Time Zone | `string` | 5 | Virus<br>Webfilter | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+51 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+46 more)* |
| `tz` | Time zone | `string` | 5 | Anomaly<br>DNS<br>GTP<br>SSH<br>VoIP<br>WAF | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+15 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |

`unauthuser`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `unauthuser` | *(empty)* | `string` | 66 | EmailFilter<br>FILE-FILTER<br>SSL<br>Virus | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+79 more)* |
| `unauthuser` | Unauthenticated User | `string` | 66 | DNS<br>SSH | 54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)* |
| `unauthuser` | Unauthenticated user | `string` | 66 | APP-CTRL<br>Anomaly<br>DLP<br>IPS<br>WAF<br>Webfilter | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+42 more)* |

`unauthusersource`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `unauthusersource` | *(empty)* | `string` | 66 | EmailFilter<br>FILE-FILTER<br>SSL<br>Virus | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+79 more)* |
| `unauthusersource` | Unauthenticated User Source | `string` | 66 | DNS<br>SSH | 54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)* |
| `unauthusersource` | Unauthenticated user source | `string` | 66 | APP-CTRL<br>Anomaly<br>DLP<br>IPS<br>WAF<br>Webfilter | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+42 more)* |

`url`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `url` | *(empty)* | `string` | 512 | FILE-FILTER<br>ICAP<br>Virus<br>Webfilter | 64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `url` | The URL address | `string` | 512 | APP-CTRL<br>DLP<br>IPS<br>Virus<br>Webfilter | 28704_-_LOGID_APP_CTRL_IPS_PASS, 28705_-_LOGID_APP_CTRL_IPS_BLOCK, 28706_-_LOGID_APP_CTRL_IPS_RESET *(+2 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16399_-_LOGID_ATTACK_MALICIOUS_URL<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+48 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+44 more)* |
| `url` | URL | `string` | 512 | WAF | 30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |

`user`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `user` | *(empty)* | `string` | 256 | EmailFilter<br>FILE-FILTER<br>SSL<br>Virus<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `user` | User | `string` | 256 | Anomaly | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS |
| `user` | User Name | `string` | 256 | WAF | 30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `user` | User name | `string` | 256 | APP-CTRL<br>DLP<br>DNS<br>IPS<br>Webfilter | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+45 more)* |
| `user` | User name for authentication | `string` | 256 | SSH | 61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)* |
| `user` | Username (authentication) | `string` | 256 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+50 more)* |

`vd`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `vd` | *(empty)* | `string` | 32 | EmailFilter<br>FILE-FILTER<br>FORTI-SWITCH<br>ICAP<br>SSL<br>Virus<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>56001_-_LOG_ID_FSW_FLOW<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `vd` | Name of the virtual domain in which the log message was recorded. | `string` | 32 | VoIP | 44032_-_LOGID_EVENT_VOIP_SIP, 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK, 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING *(+4 more)* |
| `vd` | VDOM name | `string` | 32 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+51 more)* |
| `vd` | Virtual Domain Name | `string` | 32 | Anomaly<br>DNS<br>GTP<br>SSH<br>WAF | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>54000_-_LOG_ID_DNS_QUERY, 54200_-_LOG_ID_DNS_RESOLV_ERROR, 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK *(+9 more)*<br>41216_-_LOGID_GTP_FORWARD, 41217_-_LOGID_GTP_DENY, 41218_-_LOGID_GTP_RATE_LIMIT *(+15 more)*<br>61000_-_LOG_ID_SSH_COMMAND_BLOCK, 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT, 61002_-_LOG_ID_SSH_COMMAND_PASS *(+5 more)*<br>30248_-_LOGID_WAF_SIGNATURE_BLOCK, 30249_-_LOGID_WAF_SIGNATURE_PASS, 30250_-_LOGID_WAF_SIGNATURE_ERASE *(+9 more)* |
| `vd` | Virtual domain name | `string` | 32 | APP-CTRL<br>DLP<br>IPS<br>Webfilter | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF, 24578_-_LOG_ID_DLP_DOC_SOURCE *(+1 more)*<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+46 more)* |

`virus`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `virus` | *(empty)* | `string` | 128 | Virus | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `virus` | Virus Name | `string` | 128 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+36 more)* |

`virusid`

**Description conflicts** — same field, different `Description` across LOGIDs
**Data Type conflicts** — same field, different `Data Type` across LOGIDs
**Length conflicts** — same field, different `Length` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `virusid` | *(empty)* | `string` | 64 | ICAP | 60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN |
| `virusid` | *(empty)* | `uint32` | 10 | Virus | 8216_-_MESGID_FILE_HASH_EMS_WARNING, 8217_-_MESGID_FILE_HASH_EMS_NOTIF, 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING *(+25 more)* |
| `virusid` | Virus ID (unique virus identifier) | `uint32` | 10 | Virus | 8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+36 more)* |

`vrf`

**Description conflicts** — same field, different `Description` across LOGIDs

| Log Field Name | Description | Data Type | Length | Type | LOGIDs |
|----------------|-------------|-----------|--------|------|--------|
| `vrf` | *(empty)* | `uint8` | 3 | EmailFilter<br>FILE-FILTER<br>ICAP<br>SSL<br>Virus<br>Webfilter | 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF, 20481_-_LOGID_EMAIL_GENERAL_NOTIF, 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF *(+2 more)*<br>64000_-_LOG_ID_FILE_FILTER_BLOCK, 64001_-_LOG_ID_FILE_FILTER_LOG<br>60000_-_LOG_ID_ICAP_SERVER_ERROR, 60001_-_LOG_ID_ICAP_INFECTION_BLOCK, 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN<br>62004_-_LOG_ID_SSL_EXEMPT_ADDR, 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST, 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY *(+16 more)*<br>8192_-_MESGID_INFECT_WARNING, 8193_-_MESGID_INFECT_NOTIF, 8194_-_MESGID_INFECT_MIME_WARNING *(+78 more)*<br>13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK, 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR, 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW *(+5 more)* |
| `vrf` | Virtual Routing Forwarding | `uint8` | 3 | APP-CTRL<br>DLP | 28672_-_LOGID_APP_CTRL_IM_BASIC, 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS, 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT *(+11 more)*<br>24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |
| `vrf` | Virtual router forwarding | `uint8` | 3 | Anomaly<br>IPS<br>Webfilter | 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP, 18433_-_LOGID_ATTCK_ANOMALY_ICMP, 18434_-_LOGID_ATTCK_ANOMALY_OTHERS<br>16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP, 16385_-_LOGID_ATTCK_SIGNATURE_ICMP, 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS *(+3 more)*<br>12288_-_LOG_ID_WEB_CONTENT_BANWORD, 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD, 12292_-_LOG_ID_WEB_CONTENT_KEYWORD *(+41 more)* |

---

### 7.2.6 → 7.2.7 — Inter-version Changes

| Metric | Count |
|--------|-------|
| LOGIDs added | 1 |
| LOGIDs removed | 0 |
| Fields added | 4 |
| Fields removed | 0 |
| Type changes | 0 |
| Description changes | 7 |
| Length changes | 0 |

#### Event

**LOGIDs added**

| LOGID | Category |
|-------|----------|
| `53405_-_LOG_ID_DP_RX_DROP_DETECTED` | system |

**Fields added**

| Log Field Name | Description | Data Type | Length | Category | LOGIDs |
|----------------|-------------|-----------|--------|----------|--------|
| `activity` | HA activity message | `string` | 128 | system | 43800_-_LOG_ID_EVENT_ELBC_BLADE_JOIN, 43801_-_LOG_ID_EVENT_ELBC_BLADE_LEAVE |
| `max` | *(empty)* | `uint8` | 3 | system | 43801_-_LOG_ID_EVENT_ELBC_BLADE_LEAVE |
| `new_status` | New Status | `string` | 512 | system | 43800_-_LOG_ID_EVENT_ELBC_BLADE_JOIN, 43801_-_LOG_ID_EVENT_ELBC_BLADE_LEAVE |
| `old_status` | Original Status | `string` | 512 | system | 43800_-_LOG_ID_EVENT_ELBC_BLADE_JOIN, 43801_-_LOG_ID_EVENT_ELBC_BLADE_LEAVE |

**Description changes**

| Log Field Name | Old Description | New Description | Category | LOGIDs |
|----------------|-----------------|-----------------|----------|--------|
| `connection_type` | FortiClient Connection Type | *(empty)* | endpoint | 45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE |
| `count` | Count of EndPoint Connections | Number of Packets | endpoint | 45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE |
| `license_limit` | Maximum Number of FortiClients for the License | *(empty)* | endpoint | 45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE |
| `unit` | Unit | *(empty)* | system | 22104_-_LOG_ID_POWER_RESTORE, 22105_-_LOG_ID_POWER_FAILURE |
| `used_for_type` | Connection for the type | *(empty)* | endpoint | 45057_-_LOG_ID_FCC_ADD, 45058_-_LOG_ID_FCC_CLOSE, 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE |

#### UTM

**Description changes**

| Log Field Name | Old Description | New Description | Type | LOGIDs |
|----------------|-----------------|-----------------|------|--------|
| `filteridx` | DLP filter ID | *(empty)* | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |
| `filtername` | DLP rule name | *(empty)* | DLP | 24576_-_LOG_ID_DLP_WARN, 24577_-_LOG_ID_DLP_NOTIF |

---

