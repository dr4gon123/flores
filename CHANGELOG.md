# FortiGate Log Field Changelog

## 7.2

### 7.2.0 → 7.2.1

**Summary:** 29 LOGID added, 39 removed | 145 fields added, 17 removed | 0 type changed | 0 descriptions changed | 325 lengths changed

#### Traffic

##### 10_-_LOG_ID_TRAFFIC_EXPLICIT_PROXY
- Field added: `saasname` (string, len: 80) — ""
- Field added: `shapingpolicyname` (string, len: 36) — ""
- Field added: `srcmacvendor` (string, len: 66) — ""
- Length changed: `group` 64 → 512

##### 11_-_LOG_ID_TRAFFIC_FAIL_CONN
- Field added: `saasname` (string, len: 80) — ""
- Field added: `shapingpolicyname` (string, len: 36) — ""
- Field added: `srcmacvendor` (string, len: 66) — ""
- Length changed: `group` 64 → 512

##### 12_-_LOG_ID_TRAFFIC_MULTICAST
- Field added: `saasname` (string, len: 80) — ""
- Field added: `shapingpolicyname` (string, len: 36) — ""
- Field added: `srcmacvendor` (string, len: 66) — ""
- Length changed: `group` 64 → 512

##### 13_-_LOG_ID_TRAFFIC_END_FORWARD
- Field added: `saasname` (string, len: 80) — ""
- Field added: `shapingpolicyname` (string, len: 36) — ""
- Field added: `srcmacvendor` (string, len: 66) — ""
- Length changed: `group` 64 → 512

##### 14_-_LOG_ID_TRAFFIC_END_LOCAL
- Field added: `saasname` (string, len: 80) — ""
- Field added: `shapingpolicyname` (string, len: 36) — ""
- Field added: `srcmacvendor` (string, len: 66) — ""
- Length changed: `group` 64 → 512

##### 15_-_LOG_ID_TRAFFIC_START_FORWARD
- Field added: `saasname` (string, len: 80) — ""
- Field added: `shapingpolicyname` (string, len: 36) — ""
- Field added: `srcmacvendor` (string, len: 66) — ""
- Length changed: `group` 64 → 512

##### 16_-_LOG_ID_TRAFFIC_START_LOCAL
- Field added: `saasname` (string, len: 80) — ""
- Field added: `shapingpolicyname` (string, len: 36) — ""
- Field added: `srcmacvendor` (string, len: 66) — ""
- Length changed: `group` 64 → 512

##### 17_-_LOG_ID_TRAFFIC_SNIFFER
- Field added: `saasname` (string, len: 80) — ""
- Field added: `shapingpolicyname` (string, len: 36) — ""
- Field added: `srcmacvendor` (string, len: 66) — ""
- Length changed: `group` 64 → 512

##### 19_-_LOG_ID_TRAFFIC_BROADCAST
- Field added: `saasname` (string, len: 80) — ""
- Field added: `shapingpolicyname` (string, len: 36) — ""
- Field added: `srcmacvendor` (string, len: 66) — ""
- Length changed: `group` 64 → 512

##### 20_-_LOG_ID_TRAFFIC_STAT
- Field added: `saasname` (string, len: 80) — ""
- Field added: `shapingpolicyname` (string, len: 36) — ""
- Field added: `srcmacvendor` (string, len: 66) — ""
- Length changed: `group` 64 → 512

##### 21_-_LOG_ID_TRAFFIC_SNIFFER_STAT
- Field added: `saasname` (string, len: 80) — ""
- Field added: `shapingpolicyname` (string, len: 36) — ""
- Field added: `srcmacvendor` (string, len: 66) — ""
- Length changed: `group` 64 → 512

##### 22_-_LOG_ID_TRAFFIC_UTM_CORRELATION
- Field added: `saasname` (string, len: 80) — ""
- Field added: `shapingpolicyname` (string, len: 36) — ""
- Field added: `srcmacvendor` (string, len: 66) — ""
- Length changed: `group` 64 → 512

##### 24_-_LOG_ID_TRAFFIC_ZTNA
- Field added: `saasname` (string, len: 80) — ""
- Field added: `shapingpolicyname` (string, len: 36) — ""
- Field added: `srcmacvendor` (string, len: 66) — ""
- Length changed: `group` 64 → 512

##### 2_-_LOG_ID_TRAFFIC_ALLOW
- Field added: `saasname` (string, len: 80) — ""
- Field added: `shapingpolicyname` (string, len: 36) — ""
- Field added: `srcmacvendor` (string, len: 66) — ""
- Length changed: `group` 64 → 512

##### 3_-_LOG_ID_TRAFFIC_DENY
- Field added: `saasname` (string, len: 80) — ""
- Field added: `shapingpolicyname` (string, len: 36) — ""
- Field added: `srcmacvendor` (string, len: 66) — ""
- Length changed: `group` 64 → 512

##### 4_-_LOG_ID_TRAFFIC_OTHER_START
- Field added: `saasname` (string, len: 80) — ""
- Field added: `shapingpolicyname` (string, len: 36) — ""
- Field added: `srcmacvendor` (string, len: 66) — ""
- Length changed: `group` 64 → 512

##### 5_-_LOG_ID_TRAFFIC_OTHER_ICMP_ALLOW
- Field added: `saasname` (string, len: 80) — ""
- Field added: `shapingpolicyname` (string, len: 36) — ""
- Field added: `srcmacvendor` (string, len: 66) — ""
- Length changed: `group` 64 → 512

##### 6_-_LOG_ID_TRAFFIC_OTHER_ICMP_DENY
- Field added: `saasname` (string, len: 80) — ""
- Field added: `shapingpolicyname` (string, len: 36) — ""
- Field added: `srcmacvendor` (string, len: 66) — ""
- Length changed: `group` 64 → 512

##### 7_-_LOG_ID_TRAFFIC_OTHER_INVALID
- Field added: `saasname` (string, len: 80) — ""
- Field added: `shapingpolicyname` (string, len: 36) — ""
- Field added: `srcmacvendor` (string, len: 66) — ""
- Length changed: `group` 64 → 512

##### 8_-_LOG_ID_TRAFFIC_WANOPT
- Field added: `saasname` (string, len: 80) — ""
- Field added: `shapingpolicyname` (string, len: 36) — ""
- Field added: `srcmacvendor` (string, len: 66) — ""
- Length changed: `group` 64 → 512

##### 9_-_LOG_ID_TRAFFIC_WEBCACHE
- Field added: `saasname` (string, len: 80) — ""
- Field added: `shapingpolicyname` (string, len: 36) — ""
- Field added: `srcmacvendor` (string, len: 66) — ""
- Length changed: `group` 64 → 512

#### Event

##### 20133_-_LOG_ID_FIREWALL_POLICY_EXPIRE *(new)*

##### 20134_-_LOG_ID_FIREWALL_POLICY_EXPIRED *(new)*

##### 20135_-_LOG_ID_FAIS_LIC_EXPIRE *(new)*

##### 22060_-_LOG_ID_IPAMSD_ADD_ENTRY *(new)*

##### 22061_-_LOG_ID_IPAMSD_DELETE_ENTRY *(new)*

##### 22062_-_LOG_ID_IPAMSD_FLAG_CONFLICT *(new)*

##### 22063_-_LOG_ID_IPAMSD_UNFLAG_CONFLICT *(new)*

##### 22116_-_LOG_ID_POWER_REDUNDANCY_DEGRADE *(new)*

##### 22117_-_LOG_ID_POWER_REDUNDANCY_FAILURE *(new)*

##### 22207_-_LOG_ID_CERT_EXPIRE_WARNING *(new)*

##### 32263_-_LOG_ID_AUTO_IMG_UPD_SCHEDULED *(new)*

##### 32554_-_LOG_ID_UPD_ADMIN_DB *(new)*

##### 34428_-_LOG_ID_NP7_HPE_PACKET_DROP *(new)*

##### 34430_-_LOG_ID_NP7_HPE_PACKET_FLOOD *(new)*

##### 37912_-_MESGID_FGSP_MEMBER_JOIN *(new)*

##### 37913_-_MESGID_FGSP_MEMBER_LEAVE *(new)*

##### 43719_-_LOG_ID_EVENT_WIRELESS_STA_PROBE_LOW_RSSI *(new)*

##### 45128_-_LOG_ID_EC_EMS_REST_API_NEW_SUCCESS *(new)*

##### 45129_-_LOG_ID_EC_EMS_EMS_VERIFY *(new)*

##### 45130_-_LOG_ID_EC_EMS_EMS_VERIFY_FAILED *(new)*

##### 45131_-_LOG_ID_EC_EMS_EMS_UNVERIFY *(new)*

##### 46517_-_LOG_ID_INTERNAL_LTE_MODEM_WRONG_PIN *(new)*

##### 48040_-_LOG_ID_WAD_WANOPT_TUNNEL_CREATE *(new)*

##### 48041_-_LOG_ID_WAD_WANOPT_TUNNEL_CLOSED *(new)*

##### 53311_-_LOG_ID_NPU_PER_MAPPING_ALLOCATION *(new)*

##### 53315_-_LOG_ID_LPM_ERROR *(new)*

##### 53316_-_LOG_ID_LPM_INFO *(new)*

##### 20047_-_LOG_ID_RAD_FAIL_IPV6_SOCKET *(removed)*

##### 20048_-_LOG_ID_RAD_FAIL_OPT_IPV6_PKTINFO *(removed)*

##### 20049_-_LOG_ID_RAD_FAIL_OPT_IPV6_CHECKSUM *(removed)*

##### 20050_-_LOG_ID_RAD_FAIL_OPT_IPV6_UNICAST_HOPS *(removed)*

##### 20051_-_LOG_ID_RAD_FAIL_OPT_IPV6_MULTICAST_HOPS *(removed)*

##### 20052_-_LOG_ID_RAD_FAIL_OPT_IPV6_HOPLIMIT *(removed)*

##### 20053_-_LOG_ID_RAD_FAIL_OPT_IPPROTO_ICMPV6 *(removed)*

##### 20054_-_LOG_ID_RAD_EXIT_BY_SIGNAL *(removed)*

##### 20055_-_LOG_ID_RAD_FAIL_CMDB_QUERY *(removed)*

##### 20056_-_LOG_ID_RAD_FAIL_CMDB_FOR_EACH *(removed)*

##### 20057_-_LOG_ID_RAD_FAIL_FIND_VIRT_INTF *(removed)*

##### 20058_-_LOG_ID_RAD_UNLOAD_INTF *(removed)*

##### 22060_-_LOG_ID_IPAMSD_ADDRESS_ALLOCATED *(removed)*

##### 22061_-_LOG_ID_IPAMSD_ADDRESS_FREED *(removed)*

##### 22914_-_LOG_ID_FDS_SRV_CHG *(removed)*

##### 48000_-_LOG_ID_WAD_SSL_RCV_HS *(removed)*

##### 48001_-_LOG_ID_WAD_SSL_RCV_WRG_HS *(removed)*

##### 48002_-_LOG_ID_WAD_SSL_SENT_HS *(removed)*

##### 48003_-_LOG_ID_WAD_SSL_WRG_HS_LEN *(removed)*

##### 48004_-_LOG_ID_WAD_SSL_RCV_CCS *(removed)*

##### 48005_-_LOG_ID_WAD_SSL_RSA_DH_FAIL *(removed)*

##### 48006_-_LOG_ID_WAD_SSL_SENT_CCS *(removed)*

##### 48007_-_LOG_ID_WAD_SSL_BAD_HASH *(removed)*

##### 48009_-_LOG_ID_WAD_SSL_DECRY_FAIL *(removed)*

##### 48011_-_LOG_ID_WAD_SSL_LESS_MINOR *(removed)*

##### 48013_-_LOG_ID_WAD_SSL_NOT_SUPPORT_CS *(removed)*

##### 48016_-_LOG_ID_WAD_SSL_HS_FIN *(removed)*

##### 48017_-_LOG_ID_WAD_SSL_HS_TOO_LONG *(removed)*

##### 48018_-_LOG_ID_WAD_SSL_MORE_MINOR *(removed)*

##### 48019_-_LOG_ID_WAD_SSL_SENT_ALERT *(removed)*

##### 48023_-_LOG_ID_WAD_SSL_RCV_ALERT *(removed)*

##### 48027_-_LOG_ID_WAD_SSL_INVALID_CONT_TYPE *(removed)*

##### 48029_-_LOG_ID_WAD_SSL_BAD_CCS_LEN *(removed)*

##### 48031_-_LOG_ID_WAD_SSL_BAD_DH *(removed)*

##### 48032_-_LOG_ID_WAD_SSL_PUB_KEY_TOO_BIG *(removed)*

##### 48034_-_LOG_ID_WAD_SSL_SERVER_KEY_HASH_ALGORITHM_MISMATCH *(removed)*

##### 48035_-_LOG_ID_WAD_SSL_SERVER_KEY_SIGNATURE_ALGORITHM_MISMATCH *(removed)*

##### 48038_-_LOG_ID_WAD_SSL_RCV_FATAL_ALERT *(removed)*

##### 48039_-_LOG_ID_WAD_SSL_SENT_FATAL_ALERT *(removed)*

##### 22040_-_LOG_ID_CSF_DEVICE_JOIN
- Field removed: `direction` (string)
- Field removed: `reason` (string)

##### 22041_-_LOG_ID_CSF_DEVICE_LEAVE
- Field removed: `direction` (string)
- Field removed: `reason` (string)

##### 22042_-_LOG_ID_CSF_DEVICE_UPDATE
- Field removed: `direction` (string)
- Field removed: `reason` (string)

##### 22043_-_LOG_ID_CSF_NEW_AUTH_REQ
- Field removed: `direction` (string)
- Field removed: `reason` (string)
- Field removed: `scope` (string)

##### 22044_-_LOG_ID_CSF_UPDATE_AUTH_REQ
- Field removed: `direction` (string)
- Field removed: `reason` (string)
- Field removed: `scope` (string)

##### 22045_-_LOG_ID_CSF_REMOVE_AUTH_REQ
- Field removed: `direction` (string)
- Field removed: `reason` (string)
- Field removed: `scope` (string)

##### 23101_-_LOG_ID_IPSEC_TUNNEL_UP
- Length changed: `group` 64 → 512

##### 23102_-_LOG_ID_IPSEC_TUNNEL_DOWN
- Length changed: `group` 64 → 512

##### 23103_-_LOG_ID_IPSEC_TUNNEL_STAT
- Length changed: `group` 64 → 512

##### 37120_-_MESGID_NEG_GENERIC_P1_NOTIF
- Length changed: `group` 64 → 512

##### 37121_-_MESGID_NEG_GENERIC_P1_ERROR
- Length changed: `group` 64 → 512

##### 37122_-_MESGID_NEG_GENERIC_P2_NOTIF
- Length changed: `group` 64 → 512

##### 37123_-_MESGID_NEG_GENERIC_P2_ERROR
- Length changed: `group` 64 → 512

##### 37124_-_MESGID_NEG_I_P1_ERROR
- Length changed: `group` 64 → 512

##### 37125_-_MESGID_NEG_I_P2_ERROR
- Length changed: `group` 64 → 512

##### 37126_-_MESGID_NEG_NO_STATE_ERROR
- Length changed: `group` 64 → 512

##### 37127_-_MESGID_NEG_PROGRESS_P1_NOTIF
- Length changed: `group` 64 → 512

##### 37128_-_MESGID_NEG_PROGRESS_P1_ERROR
- Length changed: `group` 64 → 512

##### 37129_-_MESGID_NEG_PROGRESS_P2_NOTIF
- Length changed: `group` 64 → 512

##### 37130_-_MESGID_NEG_PROGRESS_P2_ERROR
- Length changed: `group` 64 → 512

##### 37131_-_MESGID_ESP_ERROR
- Length changed: `group` 64 → 512

##### 37132_-_MESGID_ESP_CRITICAL
- Length changed: `group` 64 → 512

##### 37133_-_MESGID_INSTALL_SA
- Length changed: `group` 64 → 512

##### 37134_-_MESGID_DELETE_P1_SA
- Length changed: `group` 64 → 512

##### 37135_-_MESGID_DELETE_P2_SA
- Length changed: `group` 64 → 512

##### 37136_-_MESGID_DPD_FAILURE
- Length changed: `group` 64 → 512

##### 37137_-_MESGID_CONN_FAILURE
- Length changed: `group` 64 → 512

##### 37138_-_MESGID_CONN_UPDOWN
- Length changed: `group` 64 → 512

##### 37139_-_MESGID_P2_UPDOWN
- Length changed: `group` 64 → 512

##### 37141_-_MESGID_CONN_STATS
- Length changed: `group` 64 → 512

##### 39424_-_LOG_ID_EVENT_SSL_VPN_USER_TUNNEL_UP
- Length changed: `group` 64 → 512

##### 39425_-_LOG_ID_EVENT_SSL_VPN_USER_TUNNEL_DOWN
- Length changed: `group` 64 → 512

##### 39426_-_LOG_ID_EVENT_SSL_VPN_USER_SSL_LOGIN_FAIL
- Length changed: `group` 64 → 512

##### 39936_-_LOG_ID_EVENT_SSL_VPN_SESSION_WEB_TUNNEL_STATS
- Length changed: `group` 64 → 512

##### 39937_-_LOG_ID_EVENT_SSL_VPN_SESSION_WEBAPP_DENY
- Length changed: `group` 64 → 512

##### 39938_-_LOG_ID_EVENT_SSL_VPN_SESSION_WEBAPP_PASS
- Length changed: `group` 64 → 512

##### 39939_-_LOG_ID_EVENT_SSL_VPN_SESSION_WEBAPP_TIMEOUT
- Length changed: `group` 64 → 512

##### 39940_-_LOG_ID_EVENT_SSL_VPN_SESSION_WEBAPP_CLOSE
- Length changed: `group` 64 → 512

##### 39941_-_LOG_ID_EVENT_SSL_VPN_SESSION_SYS_BUSY
- Length changed: `group` 64 → 512

##### 39942_-_LOG_ID_EVENT_SSL_VPN_SESSION_CERT_OK
- Length changed: `group` 64 → 512

##### 39943_-_LOG_ID_EVENT_SSL_VPN_SESSION_NEW_CON
- Length changed: `group` 64 → 512

##### 39944_-_LOG_ID_EVENT_SSL_VPN_SESSION_ALERT
- Length changed: `group` 64 → 512

##### 39945_-_LOG_ID_EVENT_SSL_VPN_SESSION_EXIT_FAIL
- Length changed: `group` 64 → 512

##### 39946_-_LOG_ID_EVENT_SSL_VPN_SESSION_EXIT_ERR
- Length changed: `group` 64 → 512

##### 39947_-_LOG_ID_EVENT_SSL_VPN_SESSION_TUNNEL_UP
- Length changed: `group` 64 → 512

##### 39948_-_LOG_ID_EVENT_SSL_VPN_SESSION_TUNNEL_DOWN
- Length changed: `group` 64 → 512

##### 39949_-_LOG_ID_EVENT_SSL_VPN_SESSION_TUNNEL_STATS
- Length changed: `group` 64 → 512

##### 39950_-_LOG_ID_EVENT_SSL_VPN_SESSION_TUNNEL_UNKNOWNTAG
- Length changed: `group` 64 → 512

##### 39951_-_LOG_ID_EVENT_SSL_VPN_SESSION_TUNNEL_ERROR
- Length changed: `group` 64 → 512

##### 39952_-_LOG_ID_EVENT_SSL_VPN_SESSION_ENTER_CONSERVE_MODE
- Length changed: `group` 64 → 512

##### 39953_-_LOG_ID_EVENT_SSL_VPN_SESSION_LEAVE_CONSERVE_MODE
- Length changed: `group` 64 → 512

##### 40001_-_LOG_ID_PPTP_TUNNEL_UP
- Length changed: `group` 64 → 512

##### 40002_-_LOG_ID_PPTP_TUNNEL_DOWN
- Length changed: `group` 64 → 512

##### 40003_-_LOG_ID_PPTP_TUNNEL_STAT
- Length changed: `group` 64 → 512

##### 40101_-_LOG_ID_L2TP_TUNNEL_UP
- Length changed: `group` 64 → 512

##### 40102_-_LOG_ID_L2TP_TUNNEL_DOWN
- Length changed: `group` 64 → 512

##### 40103_-_LOG_ID_L2TP_TUNNEL_STAT
- Length changed: `group` 64 → 512

##### 43008_-_LOG_ID_EVENT_AUTH_SUCCESS
- Length changed: `group` 64 → 512

##### 43009_-_LOG_ID_EVENT_AUTH_FAILED
- Length changed: `group` 64 → 512

##### 43010_-_LOG_ID_EVENT_AUTH_LOCKOUT
- Length changed: `group` 64 → 512

##### 43011_-_LOG_ID_EVENT_AUTH_TIME_OUT
- Length changed: `group` 64 → 512

##### 43016_-_LOG_ID_EVENT_AUTH_NTLM_AUTH_SUCCESS
- Length changed: `group` 64 → 512

##### 43017_-_LOG_ID_EVENT_AUTH_NTLM_AUTH_FAIL
- Length changed: `group` 64 → 512

##### 43025_-_LOG_ID_EVENT_AUTH_PROXY_SUCCESS
- Length changed: `group` 64 → 512

##### 43026_-_LOG_ID_EVENT_AUTH_PROXY_FAILED
- Length changed: `group` 64 → 512

##### 43028_-_LOG_ID_EVENT_AUTH_PROXY_GROUP_INFO_FAILED
- Length changed: `group` 64 → 512

##### 43032_-_LOG_ID_EVENT_AUTH_PROXY_USER_LIMIT_REACHED
- Length changed: `group` 64 → 512

##### 43033_-_LOG_ID_EVENT_AUTH_PROXY_MULTIPLE_LOGIN
- Length changed: `group` 64 → 512

##### 43041_-_LOG_ID_EVENT_AUTH_DISCLAIMER_ACCEPT
- Length changed: `group` 64 → 512

##### 43042_-_LOG_ID_EVENT_AUTH_DISCLAIMER_DECLINE
- Length changed: `group` 64 → 512

##### 43043_-_LOG_ID_EVENT_AUTH_EMAIL_COLLECTING_SUCCESS
- Length changed: `group` 64 → 512

##### 43044_-_LOG_ID_EVENT_AUTH_EMAIL_COLLECTING_FAIL
- Length changed: `group` 64 → 512

##### 43524_-_LOG_ID_EVENT_WIRELESS_STA
- Length changed: `group` 64 → 512

##### 43572_-_LOG_ID_EVENT_WIRELESS_STA_ASSO
- Length changed: `group` 64 → 512

##### 43573_-_LOG_ID_EVENT_WIRELESS_STA_AUTH
- Length changed: `group` 64 → 512

##### 43574_-_LOG_ID_EVENT_WIRELESS_STA_DASS
- Field added: `remotewtptime` (string, len: 32) — "The time of AP when client trying to connect"
- Length changed: `group` 64 → 512

##### 43575_-_LOG_ID_EVENT_WIRELESS_STA_DAUT
- Length changed: `group` 64 → 512

##### 43576_-_LOG_ID_EVENT_WIRELESS_STA_IDLE
- Length changed: `group` 64 → 512

##### 43577_-_LOG_ID_EVENT_WIRELESS_STA_DENY
- Length changed: `group` 64 → 512

##### 43578_-_LOG_ID_EVENT_WIRELESS_STA_KICK
- Length changed: `group` 64 → 512

##### 43579_-_LOG_ID_EVENT_WIRELESS_STA_IP
- Length changed: `group` 64 → 512

##### 43580_-_LOG_ID_EVENT_WIRELESS_STA_LEAVE_WTP
- Length changed: `group` 64 → 512

##### 43581_-_LOG_ID_EVENT_WIRELESS_STA_WTP_DISCONN
- Length changed: `group` 64 → 512

##### 43601_-_LOG_ID_EVENT_WIRELESS_STA_CAP_SIGNON
- Length changed: `group` 64 → 512

##### 43602_-_LOG_ID_EVENT_WIRELESS_STA_CAP_SIGNON_SUCCESS
- Length changed: `group` 64 → 512

##### 43603_-_LOG_ID_EVENT_WIRELESS_STA_CAP_SIGNON_FAILURE
- Length changed: `group` 64 → 512

##### 43604_-_LOG_ID_EVENT_WIRELESS_STA_CAP_EMAIL_REQUEST
- Length changed: `group` 64 → 512

##### 43605_-_LOG_ID_EVENT_WIRELESS_STA_CAP_EMAIL_SUCCESS
- Length changed: `group` 64 → 512

##### 43606_-_LOG_ID_EVENT_WIRELESS_STA_CAP_EMAIL_FAILURE
- Length changed: `group` 64 → 512

##### 43607_-_LOG_ID_EVENT_WIRELESS_STA_CAP_DISCLAIMER_CHECK
- Length changed: `group` 64 → 512

##### 43608_-_LOG_ID_EVENT_WIRELESS_STA_CAP_DISCLAIMER_DECLINE
- Length changed: `group` 64 → 512

##### 43625_-_LOG_ID_EVENT_WIRELESS_STA_CAP_CMCC_SUCCESS
- Length changed: `group` 64 → 512

##### 43626_-_LOG_ID_EVENT_WIRELESS_STA_CAP_CMCC_FAILURE
- Length changed: `group` 64 → 512

##### 43627_-_LOG_ID_EVENT_WIRELESS_STA_CAP_CMCC_TIMEOUT
- Length changed: `group` 64 → 512

##### 43628_-_LOG_ID_EVENT_WIRELESS_STA_CAP_CMCC_MAC_AUTH_SUCCESS
- Length changed: `group` 64 → 512

##### 43717_-_LOG_ID_EVENT_WIRELESS_STA_L3R_REHOME
- Length changed: `group` 64 → 512

##### 43776_-_LOG_ID_EVENT_NAC_QUARANTINE
- Length changed: `group` 64 → 512

##### 43777_-_LOG_ID_EVENT_NAC_ANOMALY_QUARANTINE
- Length changed: `group` 64 → 512

##### 47301_-_LOG_ID_EVENT_REST_API_OK
- Field removed: `action` (string)

##### 47302_-_LOG_ID_EVENT_REST_API_ERR
- Field removed: `action` (string)

##### 53200_-_LOG_ID_CONNECTOR_OBJECT_ADD
- Field added: `port` (uint16, len: 5) — "Port Number"
- Field added: `protocol` (string, len: 128) — ""

##### 53201_-_LOG_ID_CONNECTOR_OBJECT_REMOVE
- Field added: `port` (uint16, len: 5) — "Port Number"
- Field added: `protocol` (string, len: 128) — ""

#### UTM — new subtypes: APP-CTRL, FORTI-SWITCH, Virus, Webfilter | removed subtypes: AV, App, Web

##### 56001_-_LOG_ID_FSW_FLOW *(new)*

##### 62307_-_LOG_ID_SSL_ANOMALY_CERT_SNI_MISMATCHED_INFO *(new)*

##### 12288_-_LOG_ID_WEB_CONTENT_BANWORD
- Length changed: `group` 64 → 512

##### 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD
- Length changed: `group` 64 → 512

##### 12292_-_LOG_ID_WEB_CONTENT_KEYWORD
- Length changed: `group` 64 → 512

##### 12293_-_LOG_ID_WEB_CONTENT_SEARCH
- Length changed: `group` 64 → 512

##### 12544_-_LOG_ID_URL_FILTER_BLOCK
- Length changed: `group` 64 → 512

##### 12545_-_LOG_ID_URL_FILTER_EXEMPT
- Length changed: `group` 64 → 512

##### 12546_-_LOG_ID_URL_FILTER_ALLOW
- Length changed: `group` 64 → 512

##### 12547_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_HTTP_BLK
- Length changed: `group` 64 → 512

##### 12548_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_HTTPS_BLK
- Length changed: `group` 64 → 512

##### 12549_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_HTTP_PASS
- Length changed: `group` 64 → 512

##### 12550_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_HTTPS_PASS
- Length changed: `group` 64 → 512

##### 12551_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_SNI_BLK
- Length changed: `group` 64 → 512

##### 12552_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_SNI_PASS
- Length changed: `group` 64 → 512

##### 12553_-_LOG_ID_URL_FILTER_INVALID_CERT
- Length changed: `group` 64 → 512

##### 12554_-_LOG_ID_URL_FILTER_INVALID_SESSION
- Length changed: `group` 64 → 512

##### 12555_-_LOG_ID_URL_FILTER_SRV_CERT_ERR_BLK
- Length changed: `group` 64 → 512

##### 12556_-_LOG_ID_URL_FILTER_SRV_CERT_ERR_PASS
- Length changed: `group` 64 → 512

##### 12559_-_LOG_ID_URL_FILTER_PASS
- Length changed: `group` 64 → 512

##### 12560_-_LOG_ID_URL_WISP_BLOCK
- Length changed: `group` 64 → 512

##### 12561_-_LOG_ID_URL_WISP_REDIR
- Length changed: `group` 64 → 512

##### 12562_-_LOG_ID_URL_WISP_ALLOW
- Length changed: `group` 64 → 512

##### 12688_-_LOG_ID_WEB_SSL_EXEMPT
- Length changed: `group` 64 → 512

##### 12800_-_LOG_ID_WEB_FTGD_ERR
- Length changed: `group` 64 → 512

##### 12801_-_LOG_ID_WEB_FTGD_WARNING
- Length changed: `group` 64 → 512

##### 13056_-_LOG_ID_WEB_FTGD_CAT_BLK
- Length changed: `group` 64 → 512

##### 13057_-_LOG_ID_WEB_FTGD_CAT_WARN
- Length changed: `group` 64 → 512

##### 13312_-_LOG_ID_WEB_FTGD_CAT_ALLOW
- Length changed: `group` 64 → 512

##### 13315_-_LOG_ID_WEB_FTGD_QUOTA_COUNTING
- Length changed: `group` 64 → 512

##### 13316_-_LOG_ID_WEB_FTGD_QUOTA_EXPIRED
- Length changed: `group` 64 → 512

##### 13317_-_LOG_ID_WEB_URL
- Length changed: `group` 64 → 512

##### 13568_-_LOG_ID_WEB_SCRIPTFILTER_ACTIVEX
- Length changed: `group` 64 → 512

##### 13573_-_LOG_ID_WEB_SCRIPTFILTER_COOKIE
- Length changed: `group` 64 → 512

##### 13584_-_LOG_ID_WEB_SCRIPTFILTER_APPLET
- Length changed: `group` 64 → 512

##### 13600_-_LOG_ID_WEB_SCRIPTFILTER_OTHER
- Length changed: `group` 64 → 512

##### 13601_-_LOG_ID_WEB_WF_COOKIE
- Length changed: `group` 64 → 512

##### 13602_-_LOG_ID_WEB_WF_REFERER
- Length changed: `group` 64 → 512

##### 13603_-_LOG_ID_WEB_WF_COMMAND_BLOCK
- Length changed: `group` 64 → 512

##### 13616_-_LOG_ID_CONTENT_TYPE_BLOCK
- Length changed: `group` 64 → 512

##### 13632_-_LOGID_HTTP_HDR_CHG_REQ
- Length changed: `group` 64 → 512

##### 13633_-_LOGID_HTTP_HDR_CHG_RESP
- Length changed: `group` 64 → 512

##### 13648_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_URL_ALLOW
- Length changed: `group` 64 → 512

##### 13649_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_FTGD_ALLOW
- Length changed: `group` 64 → 512

##### 13650_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_DEFAULT_ALLOW
- Length changed: `group` 64 → 512

##### 13651_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_URL_BLOCK
- Length changed: `group` 64 → 512

##### 13652_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_FTGD_BLOCK
- Length changed: `group` 64 → 512

##### 13653_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_DEFAULT_BLOCK
- Length changed: `group` 64 → 512

##### 13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK
- Field added: `videocategoryname` (string, len: 256) — ""
- Length changed: `group` 64 → 512

##### 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR
- Field added: `videocategoryname` (string, len: 256) — ""
- Length changed: `group` 64 → 512

##### 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW
- Field added: `videocategoryname` (string, len: 256) — ""
- Length changed: `group` 64 → 512

##### 13680_-_LOG_ID_VIDEOFILTER_CHANNEL_BLOCK
- Field added: `videocategoryname` (string, len: 256) — ""
- Length changed: `group` 64 → 512

##### 13681_-_LOG_ID_VIDEOFILTER_CHANNEL_MONITOR
- Field added: `videocategoryname` (string, len: 256) — ""
- Length changed: `group` 64 → 512

##### 13682_-_LOG_ID_VIDEOFILTER_CHANNEL_ALLOW
- Field added: `videocategoryname` (string, len: 256) — ""
- Length changed: `group` 64 → 512

##### 16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP
- Length changed: `group` 64 → 512

##### 16385_-_LOGID_ATTCK_SIGNATURE_ICMP
- Length changed: `group` 64 → 512

##### 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS
- Length changed: `group` 64 → 512

##### 16400_-_LOGID_ATTACK_BOTNET_WARNING
- Length changed: `group` 64 → 512

##### 16401_-_LOGID_ATTACK_BOTNET_NOTIF
- Length changed: `group` 64 → 512

##### 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP
- Length changed: `group` 64 → 512

##### 18433_-_LOGID_ATTCK_ANOMALY_ICMP
- Length changed: `group` 64 → 512

##### 18434_-_LOGID_ATTCK_ANOMALY_OTHERS
- Length changed: `group` 64 → 512

##### 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF
- Length changed: `group` 64 → 512

##### 20481_-_LOGID_EMAIL_GENERAL_NOTIF
- Length changed: `group` 64 → 512

##### 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF
- Length changed: `group` 64 → 512

##### 20509_-_LOGID_ANTISPAM_FTGD_ERR
- Length changed: `group` 64 → 512

##### 20510_-_LOGID_ANTISPAM_EMAIL_WEBMAIL_NOTIF
- Length changed: `group` 64 → 512

##### 24576_-_LOG_ID_DLP_WARN
- Length changed: `group` 64 → 512

##### 24577_-_LOG_ID_DLP_NOTIF
- Length changed: `group` 64 → 512

##### 28672_-_LOGID_APP_CTRL_IM_BASIC
- Length changed: `group` 64 → 512

##### 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS
- Length changed: `group` 64 → 512

##### 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT
- Length changed: `group` 64 → 512

##### 28675_-_LOGID_APP_CTRL_IM_FILE
- Length changed: `group` 64 → 512

##### 28676_-_LOGID_APP_CTRL_IM_CHAT
- Length changed: `group` 64 → 512

##### 28677_-_LOGID_APP_CTRL_IM_CHAT_BLOCK
- Length changed: `group` 64 → 512

##### 28678_-_LOGID_APP_CTRL_IM_BLOCK
- Length changed: `group` 64 → 512

##### 28704_-_LOGID_APP_CTRL_IPS_PASS
- Length changed: `group` 64 → 512

##### 28705_-_LOGID_APP_CTRL_IPS_BLOCK
- Length changed: `group` 64 → 512

##### 28706_-_LOGID_APP_CTRL_IPS_RESET
- Length changed: `group` 64 → 512

##### 28720_-_LOGID_APP_CTRL_SSH_PASS
- Length changed: `group` 64 → 512

##### 28721_-_LOGID_APP_CTRL_SSH_BLOCK
- Length changed: `group` 64 → 512

##### 28736_-_LOGID_APP_CTRL_PORT_ENF
- Length changed: `group` 64 → 512

##### 28737_-_LOGID_APP_CTRL_PROTO_ENF
- Length changed: `group` 64 → 512

##### 30248_-_LOGID_WAF_SIGNATURE_BLOCK
- Length changed: `group` 64 → 512

##### 30249_-_LOGID_WAF_SIGNATURE_PASS
- Length changed: `group` 64 → 512

##### 30250_-_LOGID_WAF_SIGNATURE_ERASE
- Length changed: `group` 64 → 512

##### 30251_-_LOGID_WAF_CUSTOM_SIGNATURE_BLOCK
- Length changed: `group` 64 → 512

##### 30252_-_LOGID_WAF_CUSTOM_SIGNATURE_PASS
- Length changed: `group` 64 → 512

##### 30253_-_LOGID_WAF_METHOD_BLOCK
- Length changed: `group` 64 → 512

##### 30255_-_LOGID_WAF_ADDRESS_LIST_BLOCK
- Length changed: `group` 64 → 512

##### 30257_-_LOGID_WAF_CONSTRAINTS_BLOCK
- Length changed: `group` 64 → 512

##### 30258_-_LOGID_WAF_CONSTRAINTS_PASS
- Length changed: `group` 64 → 512

##### 30259_-_LOGID_WAF_URL_ACCESS_PERMIT
- Length changed: `group` 64 → 512

##### 30260_-_LOGID_WAF_URL_ACCESS_BYPASS
- Length changed: `group` 64 → 512

##### 30261_-_LOGID_WAF_URL_ACCESS_BLOCK
- Length changed: `group` 64 → 512

##### 41221_-_LOGID_GTP_TRAFFIC_COUNT
- Field added: `clashtunnelidx` (uint32, len: 10) — ""

##### 41228_-_LOGID_GTPV2_TRAFFIC_COUNT
- Field added: `clashtunnelidx` (uint32, len: 10) — ""

##### 54000_-_LOG_ID_DNS_QUERY
- Length changed: `group` 64 → 512

##### 54200_-_LOG_ID_DNS_RESOLV_ERROR
- Length changed: `group` 64 → 512

##### 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK
- Length changed: `group` 64 → 512

##### 54401_-_LOG_ID_DNS_URL_FILTER_ALLOW
- Length changed: `group` 64 → 512

##### 54600_-_LOG_ID_DNS_BOTNET_IP
- Length changed: `group` 64 → 512

##### 54601_-_LOG_ID_DNS_BOTNET_DOMAIN
- Length changed: `group` 64 → 512

##### 54800_-_LOG_ID_DNS_FTGD_WARNING
- Length changed: `group` 64 → 512

##### 54801_-_LOG_ID_DNS_FTGD_ERROR
- Length changed: `group` 64 → 512

##### 54802_-_LOG_ID_DNS_FTGD_CAT_ALLOW
- Length changed: `group` 64 → 512

##### 54803_-_LOG_ID_DNS_FTGD_CAT_BLOCK
- Length changed: `group` 64 → 512

##### 54804_-_LOG_ID_DNS_SAFE_SEARCH
- Length changed: `group` 64 → 512

##### 54805_-_LOG_ID_DNS_LOCAL
- Length changed: `group` 64 → 512

##### 61000_-_LOG_ID_SSH_COMMAND_BLOCK
- Length changed: `group` 64 → 512

##### 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT
- Length changed: `group` 64 → 512

##### 61002_-_LOG_ID_SSH_COMMAND_PASS
- Length changed: `group` 64 → 512

##### 61003_-_LOG_ID_SSH_COMMAND_PASS_ALERT
- Length changed: `group` 64 → 512

##### 61010_-_LOG_ID_SSH_CHANNEL_BLOCK
- Length changed: `group` 64 → 512

##### 61011_-_LOG_ID_SSH_CHANNEL_PASS
- Length changed: `group` 64 → 512

##### 61012_-_LOG_ID_SSH_HOST_KEY_WARNING
- Length changed: `group` 64 → 512

##### 61013_-_LOG_ID_SSH_HOST_KEY_NOTIF
- Length changed: `group` 64 → 512

##### 62004_-_LOG_ID_SSL_EXEMPT_ADDR
- Length changed: `group` 64 → 512

##### 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST
- Length changed: `group` 64 → 512

##### 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY
- Length changed: `group` 64 → 512

##### 62008_-_LOG_ID_SSL_EXEMPT_LOCAL_CATEGORY
- Length changed: `group` 64 → 512

##### 62009_-_LOG_ID_SSL_EXEMPT_USER_CATEGORY
- Length changed: `group` 64 → 512

##### 62100_-_LOG_ID_SSL_NEGOTIATION_INSPECT
- Length changed: `group` 64 → 512

##### 62101_-_LOG_ID_SSL_NEGOTIATION_BLOCK
- Length changed: `group` 64 → 512

##### 62102_-_LOG_ID_SSL_NEGOTIATION_BYPASS
- Length changed: `group` 64 → 512

##### 62103_-_LOG_ID_SSL_NEGOTIATION_INFO
- Length changed: `group` 64 → 512

##### 62200_-_LOG_ID_SSL_SERVER_CERT_INFO
- Length changed: `group` 64 → 512

##### 62220_-_LOG_ID_SSL_HANDSHAKE_INFO
- Length changed: `group` 64 → 512

##### 62300_-_LOG_ID_SSL_ANOMALY_CERT_BLOCKLISTED
- Length changed: `group` 64 → 512

##### 62301_-_LOG_ID_SSL_ANOMALY_CERT_RESIGN_TRUSTED
- Length changed: `group` 64 → 512

##### 62302_-_LOG_ID_SSL_ANOMALY_CERT_RESIGN_UNTRUSTED
- Length changed: `group` 64 → 512

##### 62303_-_LOG_ID_SSL_ANOMALY_CERT_BLOCKED
- Length changed: `group` 64 → 512

##### 62304_-_LOG_ID_SSL_ANOMALY_CERT_SNI_MISMATCHED
- Length changed: `group` 64 → 512

##### 62305_-_LOG_ID_SSL_ANOMALY_CERT_PROBE_FAILURE_BLOCK
- Length changed: `group` 64 → 512

##### 62306_-_LOG_ID_SSL_ANOMALY_CERT_PROBE_FAILURE_PASS
- Length changed: `group` 64 → 512

##### 64000_-_LOG_ID_FILE_FILTER_BLOCK
- Length changed: `group` 64 → 512

##### 64001_-_LOG_ID_FILE_FILTER_LOG
- Length changed: `group` 64 → 512

##### 8192_-_MESGID_INFECT_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8193_-_MESGID_INFECT_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8194_-_MESGID_INFECT_MIME_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8195_-_MESGID_INFECT_MIME_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8200_-_MESGID_MIME_FILETYPE_EXE_WARNING
- Length changed: `group` 64 → 512

##### 8201_-_MESGID_MIME_FILETYPE_EXE_NOTIF
- Length changed: `group` 64 → 512

##### 8202_-_MESGID_AVQUERY_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8203_-_MESGID_AVQUERY_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8204_-_MESGID_MIME_AVQUERY_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8205_-_MESGID_MIME_AVQUERY_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8212_-_MESGID_MALWARE_LIST_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8213_-_MESGID_MALWARE_LIST_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8214_-_MESGID_MIME_MALWARE_LIST_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8215_-_MESGID_MIME_MALWARE_LIST_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8216_-_MESGID_FILE_HASH_EMS_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8217_-_MESGID_FILE_HASH_EMS_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8219_-_MESGID_MIME_FILE_HASH_EMS_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8220_-_MESGID_ICB_FAI_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8221_-_MESGID_ICB_FAI_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8222_-_MESGID_MIME_ICB_FAI_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8223_-_MESGID_MIME_ICB_FAI_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8224_-_MESGID_ICB_FAI_TIMEOUT_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8225_-_MESGID_ICB_FAI_TIMEOUT_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8226_-_MESGID_MIME_ICB_FAI_TIMEOUT_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8227_-_MESGID_MIME_ICB_FAI_TIMEOUT_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8228_-_MESGID_ICB_FAI_ERROR_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8229_-_MESGID_ICB_FAI_ERROR_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8230_-_MESGID_MIME_ICB_FAI_ERROR_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8231_-_MESGID_MIME_ICB_FAI_ERROR_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8232_-_MESGID_ICB_FSA_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8233_-_MESGID_ICB_FSA_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8234_-_MESGID_MIME_ICB_FSA_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8235_-_MESGID_MIME_ICB_FSA_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8236_-_MESGID_ICB_FSA_TIMEOUT_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8237_-_MESGID_ICB_FSA_TIMEOUT_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8238_-_MESGID_MIME_ICB_FSA_TIMEOUT_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8239_-_MESGID_MIME_ICB_FSA_TIMEOUT_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8240_-_MESGID_ICB_FSA_ERROR_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8241_-_MESGID_ICB_FSA_ERROR_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8242_-_MESGID_MIME_ICB_FSA_ERROR_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8243_-_MESGID_MIME_ICB_FSA_ERROR_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8448_-_MESGID_BLOCK_WARNING
- Length changed: `group` 64 → 512

##### 8450_-_MESGID_BLOCK_MIME_WARNING
- Length changed: `group` 64 → 512

##### 8451_-_MESGID_BLOCK_MIME_NOTIF
- Length changed: `group` 64 → 512

##### 8452_-_MESGID_BLOCK_COMMAND
- Length changed: `group` 64 → 512

##### 8704_-_MESGID_OVERSIZE_WARNING
- Length changed: `group` 64 → 512

##### 8705_-_MESGID_OVERSIZE_NOTIF
- Length changed: `group` 64 → 512

##### 8708_-_MESGID_OVERSIZE_STREAM_UNCOMP_WARNING
- Length changed: `group` 64 → 512

##### 8709_-_MESGID_OVERSIZE_STREAM_UNCOMP_NOTIF
- Length changed: `group` 64 → 512

##### 8720_-_MESGID_SWITCH_PROTO_WARNING
- Length changed: `group` 64 → 512

##### 8721_-_MESGID_SWITCH_PROTO_NOTIF
- Length changed: `group` 64 → 512

##### 8960_-_MESGID_SCAN_UNCOMPSIZELIMIT_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8961_-_MESGID_SCAN_UNCOMPSIZELIMIT_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8962_-_MESGID_SCAN_ARCHIVE_ENCRYPTED_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8963_-_MESGID_SCAN_ARCHIVE_ENCRYPTED_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8964_-_MESGID_SCAN_ARCHIVE_CORRUPTED_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8965_-_MESGID_SCAN_ARCHIVE_CORRUPTED_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8966_-_MESGID_SCAN_ARCHIVE_MULTIPART_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8967_-_MESGID_SCAN_ARCHIVE_MULTIPART_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8968_-_MESGID_SCAN_ARCHIVE_NESTED_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8969_-_MESGID_SCAN_ARCHIVE_NESTED_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8970_-_MESGID_SCAN_ARCHIVE_OVERSIZE_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8971_-_MESGID_SCAN_ARCHIVE_OVERSIZE_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8972_-_MESGID_SCAN_ARCHIVE_UNHANDLED_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8973_-_MESGID_SCAN_ARCHIVE_UNHANDLED_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8974_-_MESGID_SCAN_AV_ENGINE_LOAD_FAILED_ERROR
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8975_-_MESGID_SCAN_ARCHIVE_PARTIALLYCORRUPTED_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8976_-_MESGID_SCAN_ARCHIVE_PARTIALLYCORRUPTED_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8979_-_MESGID_SCAN_ARCHIVE_TIMEOUT_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8980_-_MESGID_SCAN_ARCHIVE_TIMEOUT_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 8981_-_MESGID_SCAN_AV_CDR_INTERNAL_ERROR
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 9233_-_MESGID_ANALYTICS_SUBMITTED
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 9234_-_MESGID_ANALYTICS_INFECT_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 9235_-_MESGID_ANALYTICS_INFECT_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 9236_-_MESGID_ANALYTICS_INFECT_MIME_WARNING
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 9237_-_MESGID_ANALYTICS_INFECT_MIME_NOTIF
- Field added: `fndrverdict` (string, len: 5) — ""
- Length changed: `group` 64 → 512

##### 9239_-_MESGID_CONTENT_DISARM_NOTIF
- Field added: `epoch` (uint32, len: 10) — ""
- Field added: `eventid` (uint32, len: 10) — ""
- Length changed: `group` 64 → 512

##### 9240_-_MESGID_CONTENT_DISARM_WARNING
- Field added: `epoch` (uint32, len: 10) — ""
- Field added: `eventid` (uint32, len: 10) — ""
- Length changed: `group` 64 → 512

---

### 7.2.1 → 7.2.2

**Summary:** 0 LOGID added, 0 removed | 0 fields added, 0 removed | 0 type changed | 195 descriptions changed | 0 lengths changed

#### Traffic

*(no changes)*

#### Event

*(no changes)*

#### UTM — new subtypes: EmailFilter | removed subtypes: Email

##### 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF
- Description changed: `action`
  - Before: "Security action of the email filter. Eg. blocked, tagged, allow"
  - After:  ""
- Description changed: `attachment`
  - Before: "Possible values: yes , no"
  - After:  ""
- Description changed: `banword`
  - Before: "Banned word"
  - After:  ""
- Description changed: `cc`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `date`
  - Before: "Date"
  - After:  ""
- Description changed: `devid`
  - Before: "Device ID"
  - After:  ""
- Description changed: `direction`
  - Before: "Direction of packets"
  - After:  ""
- Description changed: `dstintf`
  - Before: "Destination Interface"
  - After:  ""
- Description changed: `dstintfrole`
  - Before: "Destination interface Role, ex: LAN, WAN, etc"
  - After:  ""
- Description changed: `dstip`
  - Before: "Destination IP"
  - After:  ""
- Description changed: `dstport`
  - Before: "Destination Port"
  - After:  ""
- Description changed: `eventtime`
  - Before: "the time of the event"
  - After:  ""
- Description changed: `eventtype`
  - Before: "Email Filter event type"
  - After:  ""
- Description changed: `fctuid`
  - Before: "FortiClient ID"
  - After:  ""
- Description changed: `from`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `group`
  - Before: "User group name"
  - After:  ""
- Description changed: `level`
  - Before: "Log Level"
  - After:  ""
- Description changed: `logid`
  - Before: "Log ID"
  - After:  ""
- Description changed: `msg`
  - Before: "Log Message"
  - After:  ""
- Description changed: `policyid`
  - Before: "Policy ID"
  - After:  ""
- Description changed: `profile`
  - Before: "Email Filter profile name"
  - After:  ""
- Description changed: `proto`
  - Before: "Protocol number"
  - After:  ""
- Description changed: `recipient`
  - Before: "Email addresses from the SMTP envelope"
  - After:  ""
- Description changed: `sender`
  - Before: "Email addresses from the SMTP envelope"
  - After:  ""
- Description changed: `service`
  - Before: "SMTP, POP3, IMAP, etc."
  - After:  ""
- Description changed: `sessionid`
  - Before: "Session ID"
  - After:  ""
- Description changed: `size`
  - Before: "Email size in Bytes?"
  - After:  ""
- Description changed: `srcintf`
  - Before: "Source Interface"
  - After:  ""
- Description changed: `srcintfrole`
  - Before: "Source interface Role, ex: LAN, WAN, etc"
  - After:  ""
- Description changed: `srcip`
  - Before: "Source IP"
  - After:  ""
- Description changed: `srcport`
  - Before: "Source Port"
  - After:  ""
- Description changed: `subject`
  - Before: "The subject title of the email message"
  - After:  ""
- Description changed: `subtype`
  - Before: "Log subtype"
  - After:  ""
- Description changed: `time`
  - Before: "Time"
  - After:  ""
- Description changed: `to`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `type`
  - Before: "Log type"
  - After:  ""
- Description changed: `user`
  - Before: "User name"
  - After:  ""
- Description changed: `vd`
  - Before: "Virtual Domain"
  - After:  ""
- Description changed: `vrf`
  - Before: "Virtual router forwarding"
  - After:  ""

##### 20481_-_LOGID_EMAIL_GENERAL_NOTIF
- Description changed: `action`
  - Before: "Security action of the email filter. Eg. blocked, tagged, allow"
  - After:  ""
- Description changed: `attachment`
  - Before: "Possible values: yes , no"
  - After:  ""
- Description changed: `banword`
  - Before: "Banned word"
  - After:  ""
- Description changed: `cc`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `date`
  - Before: "Date"
  - After:  ""
- Description changed: `devid`
  - Before: "Device ID"
  - After:  ""
- Description changed: `direction`
  - Before: "Direction of packets"
  - After:  ""
- Description changed: `dstintf`
  - Before: "Destination Interface"
  - After:  ""
- Description changed: `dstintfrole`
  - Before: "Destination interface Role, ex: LAN, WAN, etc"
  - After:  ""
- Description changed: `dstip`
  - Before: "Destination IP"
  - After:  ""
- Description changed: `dstport`
  - Before: "Destination Port"
  - After:  ""
- Description changed: `eventtime`
  - Before: "the time of the event"
  - After:  ""
- Description changed: `eventtype`
  - Before: "Email Filter event type"
  - After:  ""
- Description changed: `fctuid`
  - Before: "FortiClient ID"
  - After:  ""
- Description changed: `from`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `group`
  - Before: "User group name"
  - After:  ""
- Description changed: `level`
  - Before: "Log Level"
  - After:  ""
- Description changed: `logid`
  - Before: "Log ID"
  - After:  ""
- Description changed: `msg`
  - Before: "Log Message"
  - After:  ""
- Description changed: `policyid`
  - Before: "Policy ID"
  - After:  ""
- Description changed: `profile`
  - Before: "Email Filter profile name"
  - After:  ""
- Description changed: `proto`
  - Before: "Protocol number"
  - After:  ""
- Description changed: `recipient`
  - Before: "Email addresses from the SMTP envelope"
  - After:  ""
- Description changed: `sender`
  - Before: "Email addresses from the SMTP envelope"
  - After:  ""
- Description changed: `service`
  - Before: "SMTP, POP3, IMAP, etc."
  - After:  ""
- Description changed: `sessionid`
  - Before: "Session ID"
  - After:  ""
- Description changed: `size`
  - Before: "Email size in Bytes?"
  - After:  ""
- Description changed: `srcintf`
  - Before: "Source Interface"
  - After:  ""
- Description changed: `srcintfrole`
  - Before: "Source interface Role, ex: LAN, WAN, etc"
  - After:  ""
- Description changed: `srcip`
  - Before: "Source IP"
  - After:  ""
- Description changed: `srcport`
  - Before: "Source Port"
  - After:  ""
- Description changed: `subject`
  - Before: "The subject title of the email message"
  - After:  ""
- Description changed: `subtype`
  - Before: "Log subtype"
  - After:  ""
- Description changed: `time`
  - Before: "Time"
  - After:  ""
- Description changed: `to`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `type`
  - Before: "Log type"
  - After:  ""
- Description changed: `user`
  - Before: "User name"
  - After:  ""
- Description changed: `vd`
  - Before: "Virtual Domain"
  - After:  ""
- Description changed: `vrf`
  - Before: "Virtual router forwarding"
  - After:  ""

##### 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF
- Description changed: `action`
  - Before: "Security action of the email filter. Eg. blocked, tagged, allow"
  - After:  ""
- Description changed: `attachment`
  - Before: "Possible values: yes , no"
  - After:  ""
- Description changed: `banword`
  - Before: "Banned word"
  - After:  ""
- Description changed: `cc`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `date`
  - Before: "Date"
  - After:  ""
- Description changed: `devid`
  - Before: "Device ID"
  - After:  ""
- Description changed: `direction`
  - Before: "Direction of packets"
  - After:  ""
- Description changed: `dstintf`
  - Before: "Destination Interface"
  - After:  ""
- Description changed: `dstintfrole`
  - Before: "Destination interface Role, ex: LAN, WAN, etc"
  - After:  ""
- Description changed: `dstip`
  - Before: "Destination IP"
  - After:  ""
- Description changed: `dstport`
  - Before: "Destination Port"
  - After:  ""
- Description changed: `eventtime`
  - Before: "the time of the event"
  - After:  ""
- Description changed: `eventtype`
  - Before: "Email Filter event type"
  - After:  ""
- Description changed: `fctuid`
  - Before: "FortiClient ID"
  - After:  ""
- Description changed: `from`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `group`
  - Before: "User group name"
  - After:  ""
- Description changed: `level`
  - Before: "Log Level"
  - After:  ""
- Description changed: `logid`
  - Before: "Log ID"
  - After:  ""
- Description changed: `msg`
  - Before: "Log Message"
  - After:  ""
- Description changed: `policyid`
  - Before: "Policy ID"
  - After:  ""
- Description changed: `profile`
  - Before: "Email Filter profile name"
  - After:  ""
- Description changed: `proto`
  - Before: "Protocol number"
  - After:  ""
- Description changed: `recipient`
  - Before: "Email addresses from the SMTP envelope"
  - After:  ""
- Description changed: `sender`
  - Before: "Email addresses from the SMTP envelope"
  - After:  ""
- Description changed: `service`
  - Before: "SMTP, POP3, IMAP, etc."
  - After:  ""
- Description changed: `sessionid`
  - Before: "Session ID"
  - After:  ""
- Description changed: `size`
  - Before: "Email size in Bytes?"
  - After:  ""
- Description changed: `srcintf`
  - Before: "Source Interface"
  - After:  ""
- Description changed: `srcintfrole`
  - Before: "Source interface Role, ex: LAN, WAN, etc"
  - After:  ""
- Description changed: `srcip`
  - Before: "Source IP"
  - After:  ""
- Description changed: `srcport`
  - Before: "Source Port"
  - After:  ""
- Description changed: `subject`
  - Before: "The subject title of the email message"
  - After:  ""
- Description changed: `subtype`
  - Before: "Log subtype"
  - After:  ""
- Description changed: `time`
  - Before: "Time"
  - After:  ""
- Description changed: `to`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `type`
  - Before: "Log type"
  - After:  ""
- Description changed: `user`
  - Before: "User name"
  - After:  ""
- Description changed: `vd`
  - Before: "Virtual Domain"
  - After:  ""
- Description changed: `vrf`
  - Before: "Virtual router forwarding"
  - After:  ""

##### 20509_-_LOGID_ANTISPAM_FTGD_ERR
- Description changed: `action`
  - Before: "Security action of the email filter. Eg. blocked, tagged, allow"
  - After:  ""
- Description changed: `attachment`
  - Before: "Possible values: yes , no"
  - After:  ""
- Description changed: `banword`
  - Before: "Banned word"
  - After:  ""
- Description changed: `cc`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `date`
  - Before: "Date"
  - After:  ""
- Description changed: `devid`
  - Before: "Device ID"
  - After:  ""
- Description changed: `direction`
  - Before: "Direction of packets"
  - After:  ""
- Description changed: `dstintf`
  - Before: "Destination Interface"
  - After:  ""
- Description changed: `dstintfrole`
  - Before: "Destination interface Role, ex: LAN, WAN, etc"
  - After:  ""
- Description changed: `dstip`
  - Before: "Destination IP"
  - After:  ""
- Description changed: `dstport`
  - Before: "Destination Port"
  - After:  ""
- Description changed: `eventtime`
  - Before: "the time of the event"
  - After:  ""
- Description changed: `eventtype`
  - Before: "Email Filter event type"
  - After:  ""
- Description changed: `fctuid`
  - Before: "FortiClient ID"
  - After:  ""
- Description changed: `from`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `group`
  - Before: "User group name"
  - After:  ""
- Description changed: `level`
  - Before: "Log Level"
  - After:  ""
- Description changed: `logid`
  - Before: "Log ID"
  - After:  ""
- Description changed: `msg`
  - Before: "Log Message"
  - After:  ""
- Description changed: `policyid`
  - Before: "Policy ID"
  - After:  ""
- Description changed: `profile`
  - Before: "Email Filter profile name"
  - After:  ""
- Description changed: `proto`
  - Before: "Protocol number"
  - After:  ""
- Description changed: `recipient`
  - Before: "Email addresses from the SMTP envelope"
  - After:  ""
- Description changed: `sender`
  - Before: "Email addresses from the SMTP envelope"
  - After:  ""
- Description changed: `service`
  - Before: "SMTP, POP3, IMAP, etc."
  - After:  ""
- Description changed: `sessionid`
  - Before: "Session ID"
  - After:  ""
- Description changed: `size`
  - Before: "Email size in Bytes?"
  - After:  ""
- Description changed: `srcintf`
  - Before: "Source Interface"
  - After:  ""
- Description changed: `srcintfrole`
  - Before: "Source interface Role, ex: LAN, WAN, etc"
  - After:  ""
- Description changed: `srcip`
  - Before: "Source IP"
  - After:  ""
- Description changed: `srcport`
  - Before: "Source Port"
  - After:  ""
- Description changed: `subject`
  - Before: "The subject title of the email message"
  - After:  ""
- Description changed: `subtype`
  - Before: "Log subtype"
  - After:  ""
- Description changed: `time`
  - Before: "Time"
  - After:  ""
- Description changed: `to`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `type`
  - Before: "Log type"
  - After:  ""
- Description changed: `user`
  - Before: "User name"
  - After:  ""
- Description changed: `vd`
  - Before: "Virtual Domain"
  - After:  ""
- Description changed: `vrf`
  - Before: "Virtual router forwarding"
  - After:  ""

##### 20510_-_LOGID_ANTISPAM_EMAIL_WEBMAIL_NOTIF
- Description changed: `action`
  - Before: "Security action of the email filter. Eg. blocked, tagged, allow"
  - After:  ""
- Description changed: `attachment`
  - Before: "Possible values: yes , no"
  - After:  ""
- Description changed: `banword`
  - Before: "Banned word"
  - After:  ""
- Description changed: `cc`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `date`
  - Before: "Date"
  - After:  ""
- Description changed: `devid`
  - Before: "Device ID"
  - After:  ""
- Description changed: `direction`
  - Before: "Direction of packets"
  - After:  ""
- Description changed: `dstintf`
  - Before: "Destination Interface"
  - After:  ""
- Description changed: `dstintfrole`
  - Before: "Destination interface Role, ex: LAN, WAN, etc"
  - After:  ""
- Description changed: `dstip`
  - Before: "Destination IP"
  - After:  ""
- Description changed: `dstport`
  - Before: "Destination Port"
  - After:  ""
- Description changed: `eventtime`
  - Before: "the time of the event"
  - After:  ""
- Description changed: `eventtype`
  - Before: "Email Filter event type"
  - After:  ""
- Description changed: `fctuid`
  - Before: "FortiClient ID"
  - After:  ""
- Description changed: `from`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `group`
  - Before: "User group name"
  - After:  ""
- Description changed: `level`
  - Before: "Log Level"
  - After:  ""
- Description changed: `logid`
  - Before: "Log ID"
  - After:  ""
- Description changed: `msg`
  - Before: "Log Message"
  - After:  ""
- Description changed: `policyid`
  - Before: "Policy ID"
  - After:  ""
- Description changed: `profile`
  - Before: "Email Filter profile name"
  - After:  ""
- Description changed: `proto`
  - Before: "Protocol number"
  - After:  ""
- Description changed: `recipient`
  - Before: "Email addresses from the SMTP envelope"
  - After:  ""
- Description changed: `sender`
  - Before: "Email addresses from the SMTP envelope"
  - After:  ""
- Description changed: `service`
  - Before: "SMTP, POP3, IMAP, etc."
  - After:  ""
- Description changed: `sessionid`
  - Before: "Session ID"
  - After:  ""
- Description changed: `size`
  - Before: "Email size in Bytes?"
  - After:  ""
- Description changed: `srcintf`
  - Before: "Source Interface"
  - After:  ""
- Description changed: `srcintfrole`
  - Before: "Source interface Role, ex: LAN, WAN, etc"
  - After:  ""
- Description changed: `srcip`
  - Before: "Source IP"
  - After:  ""
- Description changed: `srcport`
  - Before: "Source Port"
  - After:  ""
- Description changed: `subject`
  - Before: "The subject title of the email message"
  - After:  ""
- Description changed: `subtype`
  - Before: "Log subtype"
  - After:  ""
- Description changed: `time`
  - Before: "Time"
  - After:  ""
- Description changed: `to`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `type`
  - Before: "Log type"
  - After:  ""
- Description changed: `user`
  - Before: "User name"
  - After:  ""
- Description changed: `vd`
  - Before: "Virtual Domain"
  - After:  ""
- Description changed: `vrf`
  - Before: "Virtual router forwarding"
  - After:  ""

---

### 7.2.2 → 7.2.3

**Summary:** 0 LOGID added, 0 removed | 0 fields added, 2 removed | 0 type changed | 195 descriptions changed | 0 lengths changed

#### Traffic

*(no changes)*

#### Event

##### 22925_-_LOG_ID_EVENT_VWL_SLA_INFO
- Field removed: `slatargetid` (uint32)

##### 22933_-_LOG_ID_EVENT_VWL_SLA_INFO_NOTIF
- Field removed: `slatargetid` (uint32)

#### UTM — new subtypes: Email | removed subtypes: EmailFilter

##### 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF
- Description changed: `action`
  - Before: ""
  - After:  "Security action of the email filter. Eg. blocked, tagged, allow"
- Description changed: `attachment`
  - Before: ""
  - After:  "Possible values: yes , no"
- Description changed: `banword`
  - Before: ""
  - After:  "Banned word"
- Description changed: `cc`
  - Before: ""
  - After:  "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
- Description changed: `date`
  - Before: ""
  - After:  "Date"
- Description changed: `devid`
  - Before: ""
  - After:  "Device ID"
- Description changed: `direction`
  - Before: ""
  - After:  "Direction of packets"
- Description changed: `dstintf`
  - Before: ""
  - After:  "Destination Interface"
- Description changed: `dstintfrole`
  - Before: ""
  - After:  "Destination interface Role, ex: LAN, WAN, etc"
- Description changed: `dstip`
  - Before: ""
  - After:  "Destination IP"
- Description changed: `dstport`
  - Before: ""
  - After:  "Destination Port"
- Description changed: `eventtime`
  - Before: ""
  - After:  "the time of the event"
- Description changed: `eventtype`
  - Before: ""
  - After:  "Email Filter event type"
- Description changed: `fctuid`
  - Before: ""
  - After:  "FortiClient ID"
- Description changed: `from`
  - Before: ""
  - After:  "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
- Description changed: `group`
  - Before: ""
  - After:  "User group name"
- Description changed: `level`
  - Before: ""
  - After:  "Log Level"
- Description changed: `logid`
  - Before: ""
  - After:  "Log ID"
- Description changed: `msg`
  - Before: ""
  - After:  "Log Message"
- Description changed: `policyid`
  - Before: ""
  - After:  "Policy ID"
- Description changed: `profile`
  - Before: ""
  - After:  "Email Filter profile name"
- Description changed: `proto`
  - Before: ""
  - After:  "Protocol number"
- Description changed: `recipient`
  - Before: ""
  - After:  "Email addresses from the SMTP envelope"
- Description changed: `sender`
  - Before: ""
  - After:  "Email addresses from the SMTP envelope"
- Description changed: `service`
  - Before: ""
  - After:  "SMTP, POP3, IMAP, etc."
- Description changed: `sessionid`
  - Before: ""
  - After:  "Session ID"
- Description changed: `size`
  - Before: ""
  - After:  "Email size in Bytes?"
- Description changed: `srcintf`
  - Before: ""
  - After:  "Source Interface"
- Description changed: `srcintfrole`
  - Before: ""
  - After:  "Source interface Role, ex: LAN, WAN, etc"
- Description changed: `srcip`
  - Before: ""
  - After:  "Source IP"
- Description changed: `srcport`
  - Before: ""
  - After:  "Source Port"
- Description changed: `subject`
  - Before: ""
  - After:  "The subject title of the email message"
- Description changed: `subtype`
  - Before: ""
  - After:  "Log subtype"
- Description changed: `time`
  - Before: ""
  - After:  "Time"
- Description changed: `to`
  - Before: ""
  - After:  "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
- Description changed: `type`
  - Before: ""
  - After:  "Log type"
- Description changed: `user`
  - Before: ""
  - After:  "User name"
- Description changed: `vd`
  - Before: ""
  - After:  "Virtual Domain"
- Description changed: `vrf`
  - Before: ""
  - After:  "Virtual router forwarding"

##### 20481_-_LOGID_EMAIL_GENERAL_NOTIF
- Description changed: `action`
  - Before: ""
  - After:  "Security action of the email filter. Eg. blocked, tagged, allow"
- Description changed: `attachment`
  - Before: ""
  - After:  "Possible values: yes , no"
- Description changed: `banword`
  - Before: ""
  - After:  "Banned word"
- Description changed: `cc`
  - Before: ""
  - After:  "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
- Description changed: `date`
  - Before: ""
  - After:  "Date"
- Description changed: `devid`
  - Before: ""
  - After:  "Device ID"
- Description changed: `direction`
  - Before: ""
  - After:  "Direction of packets"
- Description changed: `dstintf`
  - Before: ""
  - After:  "Destination Interface"
- Description changed: `dstintfrole`
  - Before: ""
  - After:  "Destination interface Role, ex: LAN, WAN, etc"
- Description changed: `dstip`
  - Before: ""
  - After:  "Destination IP"
- Description changed: `dstport`
  - Before: ""
  - After:  "Destination Port"
- Description changed: `eventtime`
  - Before: ""
  - After:  "the time of the event"
- Description changed: `eventtype`
  - Before: ""
  - After:  "Email Filter event type"
- Description changed: `fctuid`
  - Before: ""
  - After:  "FortiClient ID"
- Description changed: `from`
  - Before: ""
  - After:  "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
- Description changed: `group`
  - Before: ""
  - After:  "User group name"
- Description changed: `level`
  - Before: ""
  - After:  "Log Level"
- Description changed: `logid`
  - Before: ""
  - After:  "Log ID"
- Description changed: `msg`
  - Before: ""
  - After:  "Log Message"
- Description changed: `policyid`
  - Before: ""
  - After:  "Policy ID"
- Description changed: `profile`
  - Before: ""
  - After:  "Email Filter profile name"
- Description changed: `proto`
  - Before: ""
  - After:  "Protocol number"
- Description changed: `recipient`
  - Before: ""
  - After:  "Email addresses from the SMTP envelope"
- Description changed: `sender`
  - Before: ""
  - After:  "Email addresses from the SMTP envelope"
- Description changed: `service`
  - Before: ""
  - After:  "SMTP, POP3, IMAP, etc."
- Description changed: `sessionid`
  - Before: ""
  - After:  "Session ID"
- Description changed: `size`
  - Before: ""
  - After:  "Email size in Bytes?"
- Description changed: `srcintf`
  - Before: ""
  - After:  "Source Interface"
- Description changed: `srcintfrole`
  - Before: ""
  - After:  "Source interface Role, ex: LAN, WAN, etc"
- Description changed: `srcip`
  - Before: ""
  - After:  "Source IP"
- Description changed: `srcport`
  - Before: ""
  - After:  "Source Port"
- Description changed: `subject`
  - Before: ""
  - After:  "The subject title of the email message"
- Description changed: `subtype`
  - Before: ""
  - After:  "Log subtype"
- Description changed: `time`
  - Before: ""
  - After:  "Time"
- Description changed: `to`
  - Before: ""
  - After:  "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
- Description changed: `type`
  - Before: ""
  - After:  "Log type"
- Description changed: `user`
  - Before: ""
  - After:  "User name"
- Description changed: `vd`
  - Before: ""
  - After:  "Virtual Domain"
- Description changed: `vrf`
  - Before: ""
  - After:  "Virtual router forwarding"

##### 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF
- Description changed: `action`
  - Before: ""
  - After:  "Security action of the email filter. Eg. blocked, tagged, allow"
- Description changed: `attachment`
  - Before: ""
  - After:  "Possible values: yes , no"
- Description changed: `banword`
  - Before: ""
  - After:  "Banned word"
- Description changed: `cc`
  - Before: ""
  - After:  "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
- Description changed: `date`
  - Before: ""
  - After:  "Date"
- Description changed: `devid`
  - Before: ""
  - After:  "Device ID"
- Description changed: `direction`
  - Before: ""
  - After:  "Direction of packets"
- Description changed: `dstintf`
  - Before: ""
  - After:  "Destination Interface"
- Description changed: `dstintfrole`
  - Before: ""
  - After:  "Destination interface Role, ex: LAN, WAN, etc"
- Description changed: `dstip`
  - Before: ""
  - After:  "Destination IP"
- Description changed: `dstport`
  - Before: ""
  - After:  "Destination Port"
- Description changed: `eventtime`
  - Before: ""
  - After:  "the time of the event"
- Description changed: `eventtype`
  - Before: ""
  - After:  "Email Filter event type"
- Description changed: `fctuid`
  - Before: ""
  - After:  "FortiClient ID"
- Description changed: `from`
  - Before: ""
  - After:  "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
- Description changed: `group`
  - Before: ""
  - After:  "User group name"
- Description changed: `level`
  - Before: ""
  - After:  "Log Level"
- Description changed: `logid`
  - Before: ""
  - After:  "Log ID"
- Description changed: `msg`
  - Before: ""
  - After:  "Log Message"
- Description changed: `policyid`
  - Before: ""
  - After:  "Policy ID"
- Description changed: `profile`
  - Before: ""
  - After:  "Email Filter profile name"
- Description changed: `proto`
  - Before: ""
  - After:  "Protocol number"
- Description changed: `recipient`
  - Before: ""
  - After:  "Email addresses from the SMTP envelope"
- Description changed: `sender`
  - Before: ""
  - After:  "Email addresses from the SMTP envelope"
- Description changed: `service`
  - Before: ""
  - After:  "SMTP, POP3, IMAP, etc."
- Description changed: `sessionid`
  - Before: ""
  - After:  "Session ID"
- Description changed: `size`
  - Before: ""
  - After:  "Email size in Bytes?"
- Description changed: `srcintf`
  - Before: ""
  - After:  "Source Interface"
- Description changed: `srcintfrole`
  - Before: ""
  - After:  "Source interface Role, ex: LAN, WAN, etc"
- Description changed: `srcip`
  - Before: ""
  - After:  "Source IP"
- Description changed: `srcport`
  - Before: ""
  - After:  "Source Port"
- Description changed: `subject`
  - Before: ""
  - After:  "The subject title of the email message"
- Description changed: `subtype`
  - Before: ""
  - After:  "Log subtype"
- Description changed: `time`
  - Before: ""
  - After:  "Time"
- Description changed: `to`
  - Before: ""
  - After:  "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
- Description changed: `type`
  - Before: ""
  - After:  "Log type"
- Description changed: `user`
  - Before: ""
  - After:  "User name"
- Description changed: `vd`
  - Before: ""
  - After:  "Virtual Domain"
- Description changed: `vrf`
  - Before: ""
  - After:  "Virtual router forwarding"

##### 20509_-_LOGID_ANTISPAM_FTGD_ERR
- Description changed: `action`
  - Before: ""
  - After:  "Security action of the email filter. Eg. blocked, tagged, allow"
- Description changed: `attachment`
  - Before: ""
  - After:  "Possible values: yes , no"
- Description changed: `banword`
  - Before: ""
  - After:  "Banned word"
- Description changed: `cc`
  - Before: ""
  - After:  "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
- Description changed: `date`
  - Before: ""
  - After:  "Date"
- Description changed: `devid`
  - Before: ""
  - After:  "Device ID"
- Description changed: `direction`
  - Before: ""
  - After:  "Direction of packets"
- Description changed: `dstintf`
  - Before: ""
  - After:  "Destination Interface"
- Description changed: `dstintfrole`
  - Before: ""
  - After:  "Destination interface Role, ex: LAN, WAN, etc"
- Description changed: `dstip`
  - Before: ""
  - After:  "Destination IP"
- Description changed: `dstport`
  - Before: ""
  - After:  "Destination Port"
- Description changed: `eventtime`
  - Before: ""
  - After:  "the time of the event"
- Description changed: `eventtype`
  - Before: ""
  - After:  "Email Filter event type"
- Description changed: `fctuid`
  - Before: ""
  - After:  "FortiClient ID"
- Description changed: `from`
  - Before: ""
  - After:  "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
- Description changed: `group`
  - Before: ""
  - After:  "User group name"
- Description changed: `level`
  - Before: ""
  - After:  "Log Level"
- Description changed: `logid`
  - Before: ""
  - After:  "Log ID"
- Description changed: `msg`
  - Before: ""
  - After:  "Log Message"
- Description changed: `policyid`
  - Before: ""
  - After:  "Policy ID"
- Description changed: `profile`
  - Before: ""
  - After:  "Email Filter profile name"
- Description changed: `proto`
  - Before: ""
  - After:  "Protocol number"
- Description changed: `recipient`
  - Before: ""
  - After:  "Email addresses from the SMTP envelope"
- Description changed: `sender`
  - Before: ""
  - After:  "Email addresses from the SMTP envelope"
- Description changed: `service`
  - Before: ""
  - After:  "SMTP, POP3, IMAP, etc."
- Description changed: `sessionid`
  - Before: ""
  - After:  "Session ID"
- Description changed: `size`
  - Before: ""
  - After:  "Email size in Bytes?"
- Description changed: `srcintf`
  - Before: ""
  - After:  "Source Interface"
- Description changed: `srcintfrole`
  - Before: ""
  - After:  "Source interface Role, ex: LAN, WAN, etc"
- Description changed: `srcip`
  - Before: ""
  - After:  "Source IP"
- Description changed: `srcport`
  - Before: ""
  - After:  "Source Port"
- Description changed: `subject`
  - Before: ""
  - After:  "The subject title of the email message"
- Description changed: `subtype`
  - Before: ""
  - After:  "Log subtype"
- Description changed: `time`
  - Before: ""
  - After:  "Time"
- Description changed: `to`
  - Before: ""
  - After:  "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
- Description changed: `type`
  - Before: ""
  - After:  "Log type"
- Description changed: `user`
  - Before: ""
  - After:  "User name"
- Description changed: `vd`
  - Before: ""
  - After:  "Virtual Domain"
- Description changed: `vrf`
  - Before: ""
  - After:  "Virtual router forwarding"

##### 20510_-_LOGID_ANTISPAM_EMAIL_WEBMAIL_NOTIF
- Description changed: `action`
  - Before: ""
  - After:  "Security action of the email filter. Eg. blocked, tagged, allow"
- Description changed: `attachment`
  - Before: ""
  - After:  "Possible values: yes , no"
- Description changed: `banword`
  - Before: ""
  - After:  "Banned word"
- Description changed: `cc`
  - Before: ""
  - After:  "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
- Description changed: `date`
  - Before: ""
  - After:  "Date"
- Description changed: `devid`
  - Before: ""
  - After:  "Device ID"
- Description changed: `direction`
  - Before: ""
  - After:  "Direction of packets"
- Description changed: `dstintf`
  - Before: ""
  - After:  "Destination Interface"
- Description changed: `dstintfrole`
  - Before: ""
  - After:  "Destination interface Role, ex: LAN, WAN, etc"
- Description changed: `dstip`
  - Before: ""
  - After:  "Destination IP"
- Description changed: `dstport`
  - Before: ""
  - After:  "Destination Port"
- Description changed: `eventtime`
  - Before: ""
  - After:  "the time of the event"
- Description changed: `eventtype`
  - Before: ""
  - After:  "Email Filter event type"
- Description changed: `fctuid`
  - Before: ""
  - After:  "FortiClient ID"
- Description changed: `from`
  - Before: ""
  - After:  "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
- Description changed: `group`
  - Before: ""
  - After:  "User group name"
- Description changed: `level`
  - Before: ""
  - After:  "Log Level"
- Description changed: `logid`
  - Before: ""
  - After:  "Log ID"
- Description changed: `msg`
  - Before: ""
  - After:  "Log Message"
- Description changed: `policyid`
  - Before: ""
  - After:  "Policy ID"
- Description changed: `profile`
  - Before: ""
  - After:  "Email Filter profile name"
- Description changed: `proto`
  - Before: ""
  - After:  "Protocol number"
- Description changed: `recipient`
  - Before: ""
  - After:  "Email addresses from the SMTP envelope"
- Description changed: `sender`
  - Before: ""
  - After:  "Email addresses from the SMTP envelope"
- Description changed: `service`
  - Before: ""
  - After:  "SMTP, POP3, IMAP, etc."
- Description changed: `sessionid`
  - Before: ""
  - After:  "Session ID"
- Description changed: `size`
  - Before: ""
  - After:  "Email size in Bytes?"
- Description changed: `srcintf`
  - Before: ""
  - After:  "Source Interface"
- Description changed: `srcintfrole`
  - Before: ""
  - After:  "Source interface Role, ex: LAN, WAN, etc"
- Description changed: `srcip`
  - Before: ""
  - After:  "Source IP"
- Description changed: `srcport`
  - Before: ""
  - After:  "Source Port"
- Description changed: `subject`
  - Before: ""
  - After:  "The subject title of the email message"
- Description changed: `subtype`
  - Before: ""
  - After:  "Log subtype"
- Description changed: `time`
  - Before: ""
  - After:  "Time"
- Description changed: `to`
  - Before: ""
  - After:  "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
- Description changed: `type`
  - Before: ""
  - After:  "Log type"
- Description changed: `user`
  - Before: ""
  - After:  "User name"
- Description changed: `vd`
  - Before: ""
  - After:  "Virtual Domain"
- Description changed: `vrf`
  - Before: ""
  - After:  "Virtual router forwarding"

---

### 7.2.3 → 7.2.4

**Summary:** 16 LOGID added, 13 removed | 129 fields added, 0 removed | 14 type changed | 1 descriptions changed | 56 lengths changed

#### Traffic

##### 10_-_LOG_ID_TRAFFIC_EXPLICIT_PROXY
- Field added: `accessctrl` (string, len: 80) — ""
- Field added: `clientdevicemanageable` (string, len: 16) — ""
- Field added: `emsconnection` (string, len: 8) — ""
- Field added: `proxyapptype` (string, len: 9) — ""
- Length changed: `dstname` 66 → 256
- Length changed: `srcname` 66 → 256

##### 11_-_LOG_ID_TRAFFIC_FAIL_CONN
- Field added: `accessctrl` (string, len: 80) — ""
- Field added: `clientdevicemanageable` (string, len: 16) — ""
- Field added: `emsconnection` (string, len: 8) — ""
- Field added: `proxyapptype` (string, len: 9) — ""
- Length changed: `dstname` 66 → 256
- Length changed: `srcname` 66 → 256

##### 12_-_LOG_ID_TRAFFIC_MULTICAST
- Field added: `accessctrl` (string, len: 80) — ""
- Field added: `clientdevicemanageable` (string, len: 16) — ""
- Field added: `emsconnection` (string, len: 8) — ""
- Field added: `proxyapptype` (string, len: 9) — ""
- Length changed: `dstname` 66 → 256
- Length changed: `srcname` 66 → 256

##### 13_-_LOG_ID_TRAFFIC_END_FORWARD
- Field added: `accessctrl` (string, len: 80) — ""
- Field added: `clientdevicemanageable` (string, len: 16) — ""
- Field added: `emsconnection` (string, len: 8) — ""
- Field added: `proxyapptype` (string, len: 9) — ""
- Length changed: `dstname` 66 → 256
- Length changed: `srcname` 66 → 256

##### 14_-_LOG_ID_TRAFFIC_END_LOCAL
- Field added: `accessctrl` (string, len: 80) — ""
- Field added: `clientdevicemanageable` (string, len: 16) — ""
- Field added: `emsconnection` (string, len: 8) — ""
- Field added: `proxyapptype` (string, len: 9) — ""
- Length changed: `dstname` 66 → 256
- Length changed: `srcname` 66 → 256

##### 15_-_LOG_ID_TRAFFIC_START_FORWARD
- Field added: `accessctrl` (string, len: 80) — ""
- Field added: `clientdevicemanageable` (string, len: 16) — ""
- Field added: `emsconnection` (string, len: 8) — ""
- Field added: `proxyapptype` (string, len: 9) — ""
- Length changed: `dstname` 66 → 256
- Length changed: `srcname` 66 → 256

##### 16_-_LOG_ID_TRAFFIC_START_LOCAL
- Field added: `accessctrl` (string, len: 80) — ""
- Field added: `clientdevicemanageable` (string, len: 16) — ""
- Field added: `emsconnection` (string, len: 8) — ""
- Field added: `proxyapptype` (string, len: 9) — ""
- Length changed: `dstname` 66 → 256
- Length changed: `srcname` 66 → 256

##### 17_-_LOG_ID_TRAFFIC_SNIFFER
- Field added: `accessctrl` (string, len: 80) — ""
- Field added: `clientdevicemanageable` (string, len: 16) — ""
- Field added: `emsconnection` (string, len: 8) — ""
- Field added: `proxyapptype` (string, len: 9) — ""
- Length changed: `dstname` 66 → 256
- Length changed: `srcname` 66 → 256

##### 19_-_LOG_ID_TRAFFIC_BROADCAST
- Field added: `accessctrl` (string, len: 80) — ""
- Field added: `clientdevicemanageable` (string, len: 16) — ""
- Field added: `emsconnection` (string, len: 8) — ""
- Field added: `proxyapptype` (string, len: 9) — ""
- Length changed: `dstname` 66 → 256
- Length changed: `srcname` 66 → 256

##### 20_-_LOG_ID_TRAFFIC_STAT
- Field added: `accessctrl` (string, len: 80) — ""
- Field added: `clientdevicemanageable` (string, len: 16) — ""
- Field added: `emsconnection` (string, len: 8) — ""
- Field added: `proxyapptype` (string, len: 9) — ""
- Length changed: `dstname` 66 → 256
- Length changed: `srcname` 66 → 256

##### 21_-_LOG_ID_TRAFFIC_SNIFFER_STAT
- Field added: `accessctrl` (string, len: 80) — ""
- Field added: `clientdevicemanageable` (string, len: 16) — ""
- Field added: `emsconnection` (string, len: 8) — ""
- Field added: `proxyapptype` (string, len: 9) — ""
- Length changed: `dstname` 66 → 256
- Length changed: `srcname` 66 → 256

##### 22_-_LOG_ID_TRAFFIC_UTM_CORRELATION
- Field added: `accessctrl` (string, len: 80) — ""
- Field added: `clientdevicemanageable` (string, len: 16) — ""
- Field added: `emsconnection` (string, len: 8) — ""
- Field added: `proxyapptype` (string, len: 9) — ""
- Length changed: `dstname` 66 → 256
- Length changed: `srcname` 66 → 256

##### 24_-_LOG_ID_TRAFFIC_ZTNA
- Field added: `accessctrl` (string, len: 80) — ""
- Field added: `clientdevicemanageable` (string, len: 16) — ""
- Field added: `emsconnection` (string, len: 8) — ""
- Field added: `proxyapptype` (string, len: 9) — ""
- Length changed: `dstname` 66 → 256
- Length changed: `srcname` 66 → 256

##### 2_-_LOG_ID_TRAFFIC_ALLOW
- Field added: `accessctrl` (string, len: 80) — ""
- Field added: `clientdevicemanageable` (string, len: 16) — ""
- Field added: `emsconnection` (string, len: 8) — ""
- Field added: `proxyapptype` (string, len: 9) — ""
- Length changed: `dstname` 66 → 256
- Length changed: `srcname` 66 → 256

##### 3_-_LOG_ID_TRAFFIC_DENY
- Field added: `accessctrl` (string, len: 80) — ""
- Field added: `clientdevicemanageable` (string, len: 16) — ""
- Field added: `emsconnection` (string, len: 8) — ""
- Field added: `proxyapptype` (string, len: 9) — ""
- Length changed: `dstname` 66 → 256
- Length changed: `srcname` 66 → 256

##### 4_-_LOG_ID_TRAFFIC_OTHER_START
- Field added: `accessctrl` (string, len: 80) — ""
- Field added: `clientdevicemanageable` (string, len: 16) — ""
- Field added: `emsconnection` (string, len: 8) — ""
- Field added: `proxyapptype` (string, len: 9) — ""
- Length changed: `dstname` 66 → 256
- Length changed: `srcname` 66 → 256

##### 5_-_LOG_ID_TRAFFIC_OTHER_ICMP_ALLOW
- Field added: `accessctrl` (string, len: 80) — ""
- Field added: `clientdevicemanageable` (string, len: 16) — ""
- Field added: `emsconnection` (string, len: 8) — ""
- Field added: `proxyapptype` (string, len: 9) — ""
- Length changed: `dstname` 66 → 256
- Length changed: `srcname` 66 → 256

##### 6_-_LOG_ID_TRAFFIC_OTHER_ICMP_DENY
- Field added: `accessctrl` (string, len: 80) — ""
- Field added: `clientdevicemanageable` (string, len: 16) — ""
- Field added: `emsconnection` (string, len: 8) — ""
- Field added: `proxyapptype` (string, len: 9) — ""
- Length changed: `dstname` 66 → 256
- Length changed: `srcname` 66 → 256

##### 7_-_LOG_ID_TRAFFIC_OTHER_INVALID
- Field added: `accessctrl` (string, len: 80) — ""
- Field added: `clientdevicemanageable` (string, len: 16) — ""
- Field added: `emsconnection` (string, len: 8) — ""
- Field added: `proxyapptype` (string, len: 9) — ""
- Length changed: `dstname` 66 → 256
- Length changed: `srcname` 66 → 256

##### 8_-_LOG_ID_TRAFFIC_WANOPT
- Field added: `accessctrl` (string, len: 80) — ""
- Field added: `clientdevicemanageable` (string, len: 16) — ""
- Field added: `emsconnection` (string, len: 8) — ""
- Field added: `proxyapptype` (string, len: 9) — ""
- Length changed: `dstname` 66 → 256
- Length changed: `srcname` 66 → 256

##### 9_-_LOG_ID_TRAFFIC_WEBCACHE
- Field added: `accessctrl` (string, len: 80) — ""
- Field added: `clientdevicemanageable` (string, len: 16) — ""
- Field added: `emsconnection` (string, len: 8) — ""
- Field added: `proxyapptype` (string, len: 9) — ""
- Length changed: `dstname` 66 → 256
- Length changed: `srcname` 66 → 256

#### Event

##### 22047_-_LOG_ID_CSF_ADVPN_SYNC *(new)*

##### 22049_-_LOG_ID_CSF_DAEMON_CLOSE *(new)*

##### 22085_-_LOG_ID_DEVICE_UPGRADE_SUCCEEDED *(new)*

##### 22086_-_LOG_ID_DEVICE_UPGRADE_FAILED *(new)*

##### 22872_-_LOG_ID_FLPOLD_NAC_MAX_ERROR *(new)*

##### 22873_-_LOG_ID_FLPOLD_DPP_MAX_ERROR *(new)*

##### 40707_-_LOG_ID_EVENT_SYS_CPU_USAGE_SINGLE_CORE *(new)*

##### 40960_-_LOGID_EVENT_WEBPROXY_FWD_SRV_ERROR *(new)*

##### 48040_-_LOG_ID_WANOPT_TUNNEL_CREATE *(new)*

##### 48041_-_LOG_ID_WANOPT_TUNNEL_CLOSED *(new)*

##### 48101_-_LOG_ID_WANOPT_AUTH_FAIL_PSK *(new)*

##### 48102_-_LOG_ID_WANOPT_AUTH_FAIL_OTH *(new)*

##### 32053_-_LOG_ID_ADMIN_MTNER_LOGIN_SUCC *(removed)*

##### 32054_-_LOG_ID_ADMIN_MTNER_LOGOUT *(removed)*

##### 32570_-_LOG_ID_ADMIN_MTNER_LOGOUT_DISCONNECT *(removed)*

##### 40960_-_LOGID_EVENT_WAD_WEBPROXY_FWD_SRV_ERROR *(removed)*

##### 41010_-_LOG_ID_UPD_DB_SIGN_PASSED *(removed)*

##### 44549_-_LOGID_EVENT_CONFIG_OBJATTR_MTNER *(removed)*

##### 44550_-_LOGID_EVENT_CONFIG_OBJ_MTNER *(removed)*

##### 44551_-_LOGID_EVENT_CONFIG_ATTR_MTNER *(removed)*

##### 44552_-_LOGID_EVENT_CONFIG_PATH_MTNER *(removed)*

##### 48040_-_LOG_ID_WAD_WANOPT_TUNNEL_CREATE *(removed)*

##### 48041_-_LOG_ID_WAD_WANOPT_TUNNEL_CLOSED *(removed)*

##### 48101_-_LOG_ID_WAD_AUTH_FAIL_PSK *(removed)*

##### 48102_-_LOG_ID_WAD_AUTH_FAIL_OTH *(removed)*

##### 43526_-_LOG_ID_EVENT_WIRELESS_WTPR
- Field added: `channel` (uint8, len: 3) — "Channel"

##### 43528_-_LOG_ID_EVENT_WIRELESS_WTPR_ERROR
- Field added: `channel` (uint8, len: 3) — "Channel"

##### 43586_-_LOG_ID_EVENT_WIRELESS_WTPR_DARRP_CHAN
- Field added: `channel` (uint8, len: 3) — "Channel"

##### 43587_-_LOG_ID_EVENT_WIRELESS_WTPR_DARRP_START
- Field added: `channel` (uint8, len: 3) — "Channel"

##### 43588_-_LOG_ID_EVENT_WIRELESS_WTPR_OPER_CHAN
- Field added: `channel` (uint8, len: 3) — "Channel"

##### 43589_-_LOG_ID_EVENT_WIRELESS_WTPR_RADAR
- Field added: `channel` (uint8, len: 3) — "Channel"

##### 43590_-_LOG_ID_EVENT_WIRELESS_WTPR_NOL
- Field added: `channel` (uint8, len: 3) — "Channel"

##### 43591_-_LOG_ID_EVENT_WIRELESS_WTPR_COUNTRY_CFG_SUCCESS
- Field added: `channel` (uint8, len: 3) — "Channel"

##### 43592_-_LOG_ID_EVENT_WIRELESS_WTPR_OPER_COUNTRY
- Field added: `channel` (uint8, len: 3) — "Channel"

##### 43593_-_LOG_ID_EVENT_WIRELESS_WTPR_CFG_TXPOWER
- Field added: `channel` (uint8, len: 3) — "Channel"

##### 43594_-_LOG_ID_EVENT_WIRELESS_WTPR_OPER_TXPOWER
- Field added: `channel` (uint8, len: 3) — "Channel"

##### 43600_-_LOG_ID_EVENT_WIRELESS_WTPR_DARRP_STOP
- Field added: `channel` (uint8, len: 3) — "Channel"

##### 43609_-_LOG_ID_EVENT_WIRELESS_WTPR_DARRP_OPTIMIZATION_START
- Field added: `channel` (uint8, len: 3) — "Channel"

##### 43610_-_LOG_ID_EVENT_WIRELESS_WTPR_DARRP_OPTIMIZATION_STOP
- Field added: `channel` (uint8, len: 3) — "Channel"

##### 43616_-_LOG_ID_EVENT_WIRELESS_WTPR_NOL_ADD
- Field added: `channel` (uint8, len: 3) — "Channel"

##### 43692_-_LOG_ID_EVENT_WIRELESS_WTPR_ANTENNA_DEFECT_DETECT
- Field added: `channel` (uint8, len: 3) — "Channel"

##### 43696_-_LOG_ID_EVENT_WIRELESS_WTPR_DRMA_START
- Field added: `channel` (uint8, len: 3) — "Channel"

##### 43697_-_LOG_ID_EVENT_WIRELESS_WTPR_DRMA_STOP
- Field added: `channel` (uint8, len: 3) — "Channel"

##### 43698_-_LOG_ID_EVENT_WIRELESS_WTPR_DRMA_MODE
- Field added: `channel` (uint8, len: 3) — "Channel"

##### 43707_-_LOG_ID_EVENT_WIRELESS_WTPR_SSID_UP
- Field added: `channel` (uint8, len: 3) — "Channel"

##### 43708_-_LOG_ID_EVENT_WIRELESS_WTPR_SSID_DOWN
- Field added: `channel` (uint8, len: 3) — "Channel"

##### 43715_-_LOG_ID_EVENT_WIRELESS_WTPR_BSS_COLOR_COLLISION
- Field added: `channel` (uint8, len: 3) — "Channel"

##### 48301_-_LOG_ID_UNEXP_APP_TYPE
- Description changed: `app-type`
  - Before: "Application type"
  - After:  ""

#### UTM

##### 13696_-_LOG_ID_UNKNOWN_CE_BLOCK *(new)*

##### 13697_-_LOG_ID_UNKNOWN_CE_BYPASS *(new)*

##### 8206_-_MESGID_AV_EXEMPT_NOTIF *(new)*

##### 8207_-_MESGID_MIME_AV_EXEMPT_NOTIF *(new)*

##### 13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK
- Field added: `poluuid` (string, len: 37) — ""

##### 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR
- Field added: `poluuid` (string, len: 37) — ""

##### 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW
- Field added: `poluuid` (string, len: 37) — ""

##### 13680_-_LOG_ID_VIDEOFILTER_CHANNEL_BLOCK
- Field added: `poluuid` (string, len: 37) — ""

##### 13681_-_LOG_ID_VIDEOFILTER_CHANNEL_MONITOR
- Field added: `poluuid` (string, len: 37) — ""

##### 13682_-_LOG_ID_VIDEOFILTER_CHANNEL_ALLOW
- Field added: `poluuid` (string, len: 37) — ""

##### 41216_-_LOGID_GTP_FORWARD
- Field added: `msgtypename` (string, len: 50) — ""
- Type changed: `msg-type` `string` → `uint8`
- Length changed: `msg-type` 50 → 3

##### 41217_-_LOGID_GTP_DENY
- Field added: `msgtypename` (string, len: 50) — ""
- Type changed: `msg-type` `string` → `uint8`
- Length changed: `msg-type` 50 → 3

##### 41218_-_LOGID_GTP_RATE_LIMIT
- Field added: `msgtypename` (string, len: 50) — ""
- Type changed: `msg-type` `string` → `uint8`
- Length changed: `msg-type` 50 → 3

##### 41219_-_LOGID_GTP_STATE_INVALID
- Field added: `msgtypename` (string, len: 50) — ""
- Type changed: `msg-type` `string` → `uint8`
- Length changed: `msg-type` 50 → 3

##### 41220_-_LOGID_GTP_TUNNEL_LIMIT
- Field added: `msgtypename` (string, len: 50) — ""
- Type changed: `msg-type` `string` → `uint8`
- Length changed: `msg-type` 50 → 3

##### 41223_-_LOGID_GTPV2_FORWARD
- Field added: `msgtypename` (string, len: 50) — ""
- Type changed: `msg-type` `string` → `uint8`
- Length changed: `msg-type` 50 → 3

##### 41224_-_LOGID_GTPV2_DENY
- Field added: `msgtypename` (string, len: 50) — ""
- Type changed: `msg-type` `string` → `uint8`
- Length changed: `msg-type` 50 → 3

##### 41225_-_LOGID_GTPV2_RATE_LIMIT
- Field added: `msgtypename` (string, len: 50) — ""
- Type changed: `msg-type` `string` → `uint8`
- Length changed: `msg-type` 50 → 3

##### 41226_-_LOGID_GTPV2_STATE_INVALID
- Field added: `msgtypename` (string, len: 50) — ""
- Type changed: `msg-type` `string` → `uint8`
- Length changed: `msg-type` 50 → 3

##### 41227_-_LOGID_GTPV2_TUNNEL_LIMIT
- Field added: `msgtypename` (string, len: 50) — ""
- Type changed: `msg-type` `string` → `uint8`
- Length changed: `msg-type` 50 → 3

##### 41229_-_LOGID_GTPU_FORWARD
- Field added: `msgtypename` (string, len: 50) — ""
- Type changed: `msg-type` `string` → `uint8`
- Length changed: `msg-type` 50 → 3

##### 41230_-_LOGID_GTPU_DENY
- Field added: `msgtypename` (string, len: 50) — ""
- Type changed: `msg-type` `string` → `uint8`
- Length changed: `msg-type` 50 → 3

##### 41231_-_LOGID_PFCP_FORWARD
- Field added: `msgtypename` (string, len: 50) — ""
- Type changed: `msg-type` `string` → `uint8`
- Length changed: `msg-type` 50 → 3

##### 41232_-_LOGID_PFCP_DENY
- Field added: `msgtypename` (string, len: 50) — ""
- Type changed: `msg-type` `string` → `uint8`
- Length changed: `msg-type` 50 → 3

##### 60000_-_LOG_ID_ICAP_SERVER_ERROR
- Field added: `violations` (string, len: 256) — ""

##### 60001_-_LOG_ID_ICAP_INFECTION_BLOCK
- Field added: `violations` (string, len: 256) — ""

##### 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN
- Field added: `violations` (string, len: 256) — ""

---

### 7.2.4 → 7.2.5

**Summary:** 11 LOGID added, 1 removed | 5 fields added, 0 removed | 0 type changed | 195 descriptions changed | 0 lengths changed

#### Traffic

*(no changes)*

#### Event

##### 20230_-_LOG_ID_SYS_SECURITY_WRITE_VIOLATION *(new)*

##### 20231_-_LOG_ID_SYS_SECURITY_HARDLINK_VIOLATION *(new)*

##### 20232_-_LOG_ID_SYS_SECURITY_LOAD_MODULE_VIOLATION *(new)*

##### 20233_-_LOG_ID_SYS_SECURITY_FILE_HASH_MISSING *(new)*

##### 20234_-_LOG_ID_SYS_SECURITY_FILE_HASH_MISMATCH *(new)*

##### 22047_-_LOG_ID_CSF_FILE_MEM_USAGE *(new)*

##### 22048_-_LOG_ID_CSF_ADVPN_SYNC *(new)*

##### 22111_-_LOG_ID_PSU_ACTION_FPC_DOWN *(new)*

##### 22112_-_LOG_ID_PSU_ACTION_FPC_UP *(new)*

##### 32270_-_LOG_ID_SSH_HOST_KEY_REGEN *(new)*

##### 41011_-_LOG_ID_UPD_DB_UNSIGNED_INSTALLED *(new)*

##### 22047_-_LOG_ID_CSF_ADVPN_SYNC *(removed)*

##### 37904_-_MESGID_HA_ACTIVITY
- Field added: `ha_group` (uint16, len: 4) — "HA Group Number - can be 0 - 255"
- Field added: `sn` (string, len: 64) — "Serial Number"

#### UTM — new subtypes: EmailFilter | removed subtypes: Email

##### 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF
- Description changed: `action`
  - Before: "Security action of the email filter. Eg. blocked, tagged, allow"
  - After:  ""
- Description changed: `attachment`
  - Before: "Possible values: yes , no"
  - After:  ""
- Description changed: `banword`
  - Before: "Banned word"
  - After:  ""
- Description changed: `cc`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `date`
  - Before: "Date"
  - After:  ""
- Description changed: `devid`
  - Before: "Device ID"
  - After:  ""
- Description changed: `direction`
  - Before: "Direction of packets"
  - After:  ""
- Description changed: `dstintf`
  - Before: "Destination Interface"
  - After:  ""
- Description changed: `dstintfrole`
  - Before: "Destination interface Role, ex: LAN, WAN, etc"
  - After:  ""
- Description changed: `dstip`
  - Before: "Destination IP"
  - After:  ""
- Description changed: `dstport`
  - Before: "Destination Port"
  - After:  ""
- Description changed: `eventtime`
  - Before: "the time of the event"
  - After:  ""
- Description changed: `eventtype`
  - Before: "Email Filter event type"
  - After:  ""
- Description changed: `fctuid`
  - Before: "FortiClient ID"
  - After:  ""
- Description changed: `from`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `group`
  - Before: "User group name"
  - After:  ""
- Description changed: `level`
  - Before: "Log Level"
  - After:  ""
- Description changed: `logid`
  - Before: "Log ID"
  - After:  ""
- Description changed: `msg`
  - Before: "Log Message"
  - After:  ""
- Description changed: `policyid`
  - Before: "Policy ID"
  - After:  ""
- Description changed: `profile`
  - Before: "Email Filter profile name"
  - After:  ""
- Description changed: `proto`
  - Before: "Protocol number"
  - After:  ""
- Description changed: `recipient`
  - Before: "Email addresses from the SMTP envelope"
  - After:  ""
- Description changed: `sender`
  - Before: "Email addresses from the SMTP envelope"
  - After:  ""
- Description changed: `service`
  - Before: "SMTP, POP3, IMAP, etc."
  - After:  ""
- Description changed: `sessionid`
  - Before: "Session ID"
  - After:  ""
- Description changed: `size`
  - Before: "Email size in Bytes?"
  - After:  ""
- Description changed: `srcintf`
  - Before: "Source Interface"
  - After:  ""
- Description changed: `srcintfrole`
  - Before: "Source interface Role, ex: LAN, WAN, etc"
  - After:  ""
- Description changed: `srcip`
  - Before: "Source IP"
  - After:  ""
- Description changed: `srcport`
  - Before: "Source Port"
  - After:  ""
- Description changed: `subject`
  - Before: "The subject title of the email message"
  - After:  ""
- Description changed: `subtype`
  - Before: "Log subtype"
  - After:  ""
- Description changed: `time`
  - Before: "Time"
  - After:  ""
- Description changed: `to`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `type`
  - Before: "Log type"
  - After:  ""
- Description changed: `user`
  - Before: "User name"
  - After:  ""
- Description changed: `vd`
  - Before: "Virtual Domain"
  - After:  ""
- Description changed: `vrf`
  - Before: "Virtual router forwarding"
  - After:  ""

##### 20481_-_LOGID_EMAIL_GENERAL_NOTIF
- Description changed: `action`
  - Before: "Security action of the email filter. Eg. blocked, tagged, allow"
  - After:  ""
- Description changed: `attachment`
  - Before: "Possible values: yes , no"
  - After:  ""
- Description changed: `banword`
  - Before: "Banned word"
  - After:  ""
- Description changed: `cc`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `date`
  - Before: "Date"
  - After:  ""
- Description changed: `devid`
  - Before: "Device ID"
  - After:  ""
- Description changed: `direction`
  - Before: "Direction of packets"
  - After:  ""
- Description changed: `dstintf`
  - Before: "Destination Interface"
  - After:  ""
- Description changed: `dstintfrole`
  - Before: "Destination interface Role, ex: LAN, WAN, etc"
  - After:  ""
- Description changed: `dstip`
  - Before: "Destination IP"
  - After:  ""
- Description changed: `dstport`
  - Before: "Destination Port"
  - After:  ""
- Description changed: `eventtime`
  - Before: "the time of the event"
  - After:  ""
- Description changed: `eventtype`
  - Before: "Email Filter event type"
  - After:  ""
- Description changed: `fctuid`
  - Before: "FortiClient ID"
  - After:  ""
- Description changed: `from`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `group`
  - Before: "User group name"
  - After:  ""
- Description changed: `level`
  - Before: "Log Level"
  - After:  ""
- Description changed: `logid`
  - Before: "Log ID"
  - After:  ""
- Description changed: `msg`
  - Before: "Log Message"
  - After:  ""
- Description changed: `policyid`
  - Before: "Policy ID"
  - After:  ""
- Description changed: `profile`
  - Before: "Email Filter profile name"
  - After:  ""
- Description changed: `proto`
  - Before: "Protocol number"
  - After:  ""
- Description changed: `recipient`
  - Before: "Email addresses from the SMTP envelope"
  - After:  ""
- Description changed: `sender`
  - Before: "Email addresses from the SMTP envelope"
  - After:  ""
- Description changed: `service`
  - Before: "SMTP, POP3, IMAP, etc."
  - After:  ""
- Description changed: `sessionid`
  - Before: "Session ID"
  - After:  ""
- Description changed: `size`
  - Before: "Email size in Bytes?"
  - After:  ""
- Description changed: `srcintf`
  - Before: "Source Interface"
  - After:  ""
- Description changed: `srcintfrole`
  - Before: "Source interface Role, ex: LAN, WAN, etc"
  - After:  ""
- Description changed: `srcip`
  - Before: "Source IP"
  - After:  ""
- Description changed: `srcport`
  - Before: "Source Port"
  - After:  ""
- Description changed: `subject`
  - Before: "The subject title of the email message"
  - After:  ""
- Description changed: `subtype`
  - Before: "Log subtype"
  - After:  ""
- Description changed: `time`
  - Before: "Time"
  - After:  ""
- Description changed: `to`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `type`
  - Before: "Log type"
  - After:  ""
- Description changed: `user`
  - Before: "User name"
  - After:  ""
- Description changed: `vd`
  - Before: "Virtual Domain"
  - After:  ""
- Description changed: `vrf`
  - Before: "Virtual router forwarding"
  - After:  ""

##### 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF
- Description changed: `action`
  - Before: "Security action of the email filter. Eg. blocked, tagged, allow"
  - After:  ""
- Description changed: `attachment`
  - Before: "Possible values: yes , no"
  - After:  ""
- Description changed: `banword`
  - Before: "Banned word"
  - After:  ""
- Description changed: `cc`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `date`
  - Before: "Date"
  - After:  ""
- Description changed: `devid`
  - Before: "Device ID"
  - After:  ""
- Description changed: `direction`
  - Before: "Direction of packets"
  - After:  ""
- Description changed: `dstintf`
  - Before: "Destination Interface"
  - After:  ""
- Description changed: `dstintfrole`
  - Before: "Destination interface Role, ex: LAN, WAN, etc"
  - After:  ""
- Description changed: `dstip`
  - Before: "Destination IP"
  - After:  ""
- Description changed: `dstport`
  - Before: "Destination Port"
  - After:  ""
- Description changed: `eventtime`
  - Before: "the time of the event"
  - After:  ""
- Description changed: `eventtype`
  - Before: "Email Filter event type"
  - After:  ""
- Description changed: `fctuid`
  - Before: "FortiClient ID"
  - After:  ""
- Description changed: `from`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `group`
  - Before: "User group name"
  - After:  ""
- Description changed: `level`
  - Before: "Log Level"
  - After:  ""
- Description changed: `logid`
  - Before: "Log ID"
  - After:  ""
- Description changed: `msg`
  - Before: "Log Message"
  - After:  ""
- Description changed: `policyid`
  - Before: "Policy ID"
  - After:  ""
- Description changed: `profile`
  - Before: "Email Filter profile name"
  - After:  ""
- Description changed: `proto`
  - Before: "Protocol number"
  - After:  ""
- Description changed: `recipient`
  - Before: "Email addresses from the SMTP envelope"
  - After:  ""
- Description changed: `sender`
  - Before: "Email addresses from the SMTP envelope"
  - After:  ""
- Description changed: `service`
  - Before: "SMTP, POP3, IMAP, etc."
  - After:  ""
- Description changed: `sessionid`
  - Before: "Session ID"
  - After:  ""
- Description changed: `size`
  - Before: "Email size in Bytes?"
  - After:  ""
- Description changed: `srcintf`
  - Before: "Source Interface"
  - After:  ""
- Description changed: `srcintfrole`
  - Before: "Source interface Role, ex: LAN, WAN, etc"
  - After:  ""
- Description changed: `srcip`
  - Before: "Source IP"
  - After:  ""
- Description changed: `srcport`
  - Before: "Source Port"
  - After:  ""
- Description changed: `subject`
  - Before: "The subject title of the email message"
  - After:  ""
- Description changed: `subtype`
  - Before: "Log subtype"
  - After:  ""
- Description changed: `time`
  - Before: "Time"
  - After:  ""
- Description changed: `to`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `type`
  - Before: "Log type"
  - After:  ""
- Description changed: `user`
  - Before: "User name"
  - After:  ""
- Description changed: `vd`
  - Before: "Virtual Domain"
  - After:  ""
- Description changed: `vrf`
  - Before: "Virtual router forwarding"
  - After:  ""

##### 20509_-_LOGID_ANTISPAM_FTGD_ERR
- Description changed: `action`
  - Before: "Security action of the email filter. Eg. blocked, tagged, allow"
  - After:  ""
- Description changed: `attachment`
  - Before: "Possible values: yes , no"
  - After:  ""
- Description changed: `banword`
  - Before: "Banned word"
  - After:  ""
- Description changed: `cc`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `date`
  - Before: "Date"
  - After:  ""
- Description changed: `devid`
  - Before: "Device ID"
  - After:  ""
- Description changed: `direction`
  - Before: "Direction of packets"
  - After:  ""
- Description changed: `dstintf`
  - Before: "Destination Interface"
  - After:  ""
- Description changed: `dstintfrole`
  - Before: "Destination interface Role, ex: LAN, WAN, etc"
  - After:  ""
- Description changed: `dstip`
  - Before: "Destination IP"
  - After:  ""
- Description changed: `dstport`
  - Before: "Destination Port"
  - After:  ""
- Description changed: `eventtime`
  - Before: "the time of the event"
  - After:  ""
- Description changed: `eventtype`
  - Before: "Email Filter event type"
  - After:  ""
- Description changed: `fctuid`
  - Before: "FortiClient ID"
  - After:  ""
- Description changed: `from`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `group`
  - Before: "User group name"
  - After:  ""
- Description changed: `level`
  - Before: "Log Level"
  - After:  ""
- Description changed: `logid`
  - Before: "Log ID"
  - After:  ""
- Description changed: `msg`
  - Before: "Log Message"
  - After:  ""
- Description changed: `policyid`
  - Before: "Policy ID"
  - After:  ""
- Description changed: `profile`
  - Before: "Email Filter profile name"
  - After:  ""
- Description changed: `proto`
  - Before: "Protocol number"
  - After:  ""
- Description changed: `recipient`
  - Before: "Email addresses from the SMTP envelope"
  - After:  ""
- Description changed: `sender`
  - Before: "Email addresses from the SMTP envelope"
  - After:  ""
- Description changed: `service`
  - Before: "SMTP, POP3, IMAP, etc."
  - After:  ""
- Description changed: `sessionid`
  - Before: "Session ID"
  - After:  ""
- Description changed: `size`
  - Before: "Email size in Bytes?"
  - After:  ""
- Description changed: `srcintf`
  - Before: "Source Interface"
  - After:  ""
- Description changed: `srcintfrole`
  - Before: "Source interface Role, ex: LAN, WAN, etc"
  - After:  ""
- Description changed: `srcip`
  - Before: "Source IP"
  - After:  ""
- Description changed: `srcport`
  - Before: "Source Port"
  - After:  ""
- Description changed: `subject`
  - Before: "The subject title of the email message"
  - After:  ""
- Description changed: `subtype`
  - Before: "Log subtype"
  - After:  ""
- Description changed: `time`
  - Before: "Time"
  - After:  ""
- Description changed: `to`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `type`
  - Before: "Log type"
  - After:  ""
- Description changed: `user`
  - Before: "User name"
  - After:  ""
- Description changed: `vd`
  - Before: "Virtual Domain"
  - After:  ""
- Description changed: `vrf`
  - Before: "Virtual router forwarding"
  - After:  ""

##### 20510_-_LOGID_ANTISPAM_EMAIL_WEBMAIL_NOTIF
- Description changed: `action`
  - Before: "Security action of the email filter. Eg. blocked, tagged, allow"
  - After:  ""
- Description changed: `attachment`
  - Before: "Possible values: yes , no"
  - After:  ""
- Description changed: `banword`
  - Before: "Banned word"
  - After:  ""
- Description changed: `cc`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `date`
  - Before: "Date"
  - After:  ""
- Description changed: `devid`
  - Before: "Device ID"
  - After:  ""
- Description changed: `direction`
  - Before: "Direction of packets"
  - After:  ""
- Description changed: `dstintf`
  - Before: "Destination Interface"
  - After:  ""
- Description changed: `dstintfrole`
  - Before: "Destination interface Role, ex: LAN, WAN, etc"
  - After:  ""
- Description changed: `dstip`
  - Before: "Destination IP"
  - After:  ""
- Description changed: `dstport`
  - Before: "Destination Port"
  - After:  ""
- Description changed: `eventtime`
  - Before: "the time of the event"
  - After:  ""
- Description changed: `eventtype`
  - Before: "Email Filter event type"
  - After:  ""
- Description changed: `fctuid`
  - Before: "FortiClient ID"
  - After:  ""
- Description changed: `from`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `group`
  - Before: "User group name"
  - After:  ""
- Description changed: `level`
  - Before: "Log Level"
  - After:  ""
- Description changed: `logid`
  - Before: "Log ID"
  - After:  ""
- Description changed: `msg`
  - Before: "Log Message"
  - After:  ""
- Description changed: `policyid`
  - Before: "Policy ID"
  - After:  ""
- Description changed: `profile`
  - Before: "Email Filter profile name"
  - After:  ""
- Description changed: `proto`
  - Before: "Protocol number"
  - After:  ""
- Description changed: `recipient`
  - Before: "Email addresses from the SMTP envelope"
  - After:  ""
- Description changed: `sender`
  - Before: "Email addresses from the SMTP envelope"
  - After:  ""
- Description changed: `service`
  - Before: "SMTP, POP3, IMAP, etc."
  - After:  ""
- Description changed: `sessionid`
  - Before: "Session ID"
  - After:  ""
- Description changed: `size`
  - Before: "Email size in Bytes?"
  - After:  ""
- Description changed: `srcintf`
  - Before: "Source Interface"
  - After:  ""
- Description changed: `srcintfrole`
  - Before: "Source interface Role, ex: LAN, WAN, etc"
  - After:  ""
- Description changed: `srcip`
  - Before: "Source IP"
  - After:  ""
- Description changed: `srcport`
  - Before: "Source Port"
  - After:  ""
- Description changed: `subject`
  - Before: "The subject title of the email message"
  - After:  ""
- Description changed: `subtype`
  - Before: "Log subtype"
  - After:  ""
- Description changed: `time`
  - Before: "Time"
  - After:  ""
- Description changed: `to`
  - Before: "Email address(es) from the Email Headers (IMAP/POP3/SMTP)"
  - After:  ""
- Description changed: `type`
  - Before: "Log type"
  - After:  ""
- Description changed: `user`
  - Before: "User name"
  - After:  ""
- Description changed: `vd`
  - Before: "Virtual Domain"
  - After:  ""
- Description changed: `vrf`
  - Before: "Virtual router forwarding"
  - After:  ""

##### 44032_-_LOGID_EVENT_VOIP_SIP
- Field added: `logsrc` (string, len: 32) — ""

##### 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK
- Field added: `logsrc` (string, len: 32) — ""

##### 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING
- Field added: `logsrc` (string, len: 32) — ""

---

### 7.2.5 → 7.2.6

**Summary:** 6 LOGID added, 0 removed | 0 fields added, 0 removed | 0 type changed | 0 descriptions changed | 0 lengths changed

#### Traffic

*(no changes)*

#### Event

##### 20235_-_LOG_ID_SYS_SECURITY_MOUNT_VIOLATION *(new)*

##### 22094_-_LOG_ID_FEDERATED_UPGRADE_ROOT_COMPLETED *(new)*

##### 22095_-_LOG_ID_FEDERATED_UPGRADE_ROOT_NOT_COMPLETED *(new)*

##### 32264_-_LOG_ID_BLE_FIRMWARE_CHECK *(new)*

##### 32265_-_LOG_ID_BLE_FIRMWARE_UPDATE *(new)*

##### 53406_-_LOG_ID_2GB_CSF_UPGRADE *(new)*

#### UTM

*(no changes)*

---

### 7.2.6 → 7.2.7

**Summary:** 1 LOGID added, 0 removed | 7 fields added, 0 removed | 0 type changed | 18 descriptions changed | 0 lengths changed

#### Traffic

*(no changes)*

#### Event

##### 53405_-_LOG_ID_DP_RX_DROP_DETECTED *(new)*

##### 22104_-_LOG_ID_POWER_RESTORE
- Description changed: `unit`
  - Before: "Unit"
  - After:  ""

##### 22105_-_LOG_ID_POWER_FAILURE
- Description changed: `unit`
  - Before: "Unit"
  - After:  ""

##### 43800_-_LOG_ID_EVENT_ELBC_BLADE_JOIN
- Field added: `activity` (string, len: 128) — "HA activity message"
- Field added: `new_status` (string, len: 512) — "New Status"
- Field added: `old_status` (string, len: 512) — "Original Status"

##### 43801_-_LOG_ID_EVENT_ELBC_BLADE_LEAVE
- Field added: `activity` (string, len: 128) — "HA activity message"
- Field added: `max` (uint8, len: 3) — ""
- Field added: `new_status` (string, len: 512) — "New Status"
- Field added: `old_status` (string, len: 512) — "Original Status"

##### 45057_-_LOG_ID_FCC_ADD
- Description changed: `connection_type`
  - Before: "FortiClient Connection Type"
  - After:  ""
- Description changed: `count`
  - Before: "Count of EndPoint Connections"
  - After:  "Number of Packets"
- Description changed: `license_limit`
  - Before: "Maximum Number of FortiClients for the License"
  - After:  ""
- Description changed: `used_for_type`
  - Before: "Connection for the type"
  - After:  ""

##### 45058_-_LOG_ID_FCC_CLOSE
- Description changed: `connection_type`
  - Before: "FortiClient Connection Type"
  - After:  ""
- Description changed: `count`
  - Before: "Count of EndPoint Connections"
  - After:  "Number of Packets"
- Description changed: `license_limit`
  - Before: "Maximum Number of FortiClients for the License"
  - After:  ""
- Description changed: `used_for_type`
  - Before: "Connection for the type"
  - After:  ""

##### 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE
- Description changed: `connection_type`
  - Before: "FortiClient Connection Type"
  - After:  ""
- Description changed: `count`
  - Before: "Count of EndPoint Connections"
  - After:  "Number of Packets"
- Description changed: `license_limit`
  - Before: "Maximum Number of FortiClients for the License"
  - After:  ""
- Description changed: `used_for_type`
  - Before: "Connection for the type"
  - After:  ""

#### UTM

##### 24576_-_LOG_ID_DLP_WARN
- Description changed: `filteridx`
  - Before: "DLP filter ID"
  - After:  ""
- Description changed: `filtername`
  - Before: "DLP rule name"
  - After:  ""

##### 24577_-_LOG_ID_DLP_NOTIF
- Description changed: `filteridx`
  - Before: "DLP filter ID"
  - After:  ""
- Description changed: `filtername`
  - Before: "DLP rule name"
  - After:  ""

---

### 7.2.7 → 7.2.8

**Summary:** 2 LOGID added, 2 removed | 21 fields added, 9 removed | 0 type changed | 0 descriptions changed | 0 lengths changed

#### Traffic

##### 10_-_LOG_ID_TRAFFIC_EXPLICIT_PROXY
- Field added: `srcremote` (ip, len: 39) — ""

##### 11_-_LOG_ID_TRAFFIC_FAIL_CONN
- Field added: `srcremote` (ip, len: 39) — ""

##### 12_-_LOG_ID_TRAFFIC_MULTICAST
- Field added: `srcremote` (ip, len: 39) — ""

##### 13_-_LOG_ID_TRAFFIC_END_FORWARD
- Field added: `srcremote` (ip, len: 39) — ""

##### 14_-_LOG_ID_TRAFFIC_END_LOCAL
- Field added: `srcremote` (ip, len: 39) — ""

##### 15_-_LOG_ID_TRAFFIC_START_FORWARD
- Field added: `srcremote` (ip, len: 39) — ""

##### 16_-_LOG_ID_TRAFFIC_START_LOCAL
- Field added: `srcremote` (ip, len: 39) — ""

##### 17_-_LOG_ID_TRAFFIC_SNIFFER
- Field added: `srcremote` (ip, len: 39) — ""

##### 19_-_LOG_ID_TRAFFIC_BROADCAST
- Field added: `srcremote` (ip, len: 39) — ""

##### 20_-_LOG_ID_TRAFFIC_STAT
- Field added: `srcremote` (ip, len: 39) — ""

##### 21_-_LOG_ID_TRAFFIC_SNIFFER_STAT
- Field added: `srcremote` (ip, len: 39) — ""

##### 22_-_LOG_ID_TRAFFIC_UTM_CORRELATION
- Field added: `srcremote` (ip, len: 39) — ""

##### 24_-_LOG_ID_TRAFFIC_ZTNA
- Field added: `srcremote` (ip, len: 39) — ""

##### 2_-_LOG_ID_TRAFFIC_ALLOW
- Field added: `srcremote` (ip, len: 39) — ""

##### 3_-_LOG_ID_TRAFFIC_DENY
- Field added: `srcremote` (ip, len: 39) — ""

##### 4_-_LOG_ID_TRAFFIC_OTHER_START
- Field added: `srcremote` (ip, len: 39) — ""

##### 5_-_LOG_ID_TRAFFIC_OTHER_ICMP_ALLOW
- Field added: `srcremote` (ip, len: 39) — ""

##### 6_-_LOG_ID_TRAFFIC_OTHER_ICMP_DENY
- Field added: `srcremote` (ip, len: 39) — ""

##### 7_-_LOG_ID_TRAFFIC_OTHER_INVALID
- Field added: `srcremote` (ip, len: 39) — ""

##### 8_-_LOG_ID_TRAFFIC_WANOPT
- Field added: `srcremote` (ip, len: 39) — ""

##### 9_-_LOG_ID_TRAFFIC_WEBCACHE
- Field added: `srcremote` (ip, len: 39) — ""

#### Event

##### 22022_-_LOG_ID_ENTER_EXTREME_LOW_MEM_MODE *(new)*

##### 22023_-_LOG_ID_LEAVE_EXTREME_LOW_MEM_MODE *(new)*

##### 22104_-_LOG_ID_POWER_RESTORE *(removed)*

##### 53405_-_LOG_ID_DP_RX_DROP_DETECTED *(removed)*

##### 20232_-_LOG_ID_SYS_SECURITY_LOAD_MODULE_VIOLATION
- Field removed: `severity` (string)

##### 22105_-_LOG_ID_POWER_FAILURE
- Field removed: `unit` (uint32)

##### 43800_-_LOG_ID_EVENT_ELBC_BLADE_JOIN
- Field removed: `activity` (string)
- Field removed: `new_status` (string)
- Field removed: `old_status` (string)

##### 43801_-_LOG_ID_EVENT_ELBC_BLADE_LEAVE
- Field removed: `activity` (string)
- Field removed: `max` (uint8)
- Field removed: `new_status` (string)
- Field removed: `old_status` (string)

#### UTM

*(no changes)*

---

### 7.2.8 → 7.2.9

**Summary:** 2 LOGID added, 0 removed | 48 fields added, 0 removed | 0 type changed | 0 descriptions changed | 0 lengths changed

#### Traffic

##### 10_-_LOG_ID_TRAFFIC_EXPLICIT_PROXY
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 11_-_LOG_ID_TRAFFIC_FAIL_CONN
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 12_-_LOG_ID_TRAFFIC_MULTICAST
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 13_-_LOG_ID_TRAFFIC_END_FORWARD
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 14_-_LOG_ID_TRAFFIC_END_LOCAL
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 15_-_LOG_ID_TRAFFIC_START_FORWARD
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 16_-_LOG_ID_TRAFFIC_START_LOCAL
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 17_-_LOG_ID_TRAFFIC_SNIFFER
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 19_-_LOG_ID_TRAFFIC_BROADCAST
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 20_-_LOG_ID_TRAFFIC_STAT
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 21_-_LOG_ID_TRAFFIC_SNIFFER_STAT
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 22_-_LOG_ID_TRAFFIC_UTM_CORRELATION
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 24_-_LOG_ID_TRAFFIC_ZTNA
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 2_-_LOG_ID_TRAFFIC_ALLOW
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 3_-_LOG_ID_TRAFFIC_DENY
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 4_-_LOG_ID_TRAFFIC_OTHER_START
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 5_-_LOG_ID_TRAFFIC_OTHER_ICMP_ALLOW
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 6_-_LOG_ID_TRAFFIC_OTHER_ICMP_DENY
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 7_-_LOG_ID_TRAFFIC_OTHER_INVALID
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 8_-_LOG_ID_TRAFFIC_WANOPT
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 9_-_LOG_ID_TRAFFIC_WEBCACHE
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

#### Event

##### 22906_-_LOG_ID_SECURITY_LEVEL_CHANGE *(new)*

##### 53402_-_LOG_ID_FGFM_RECOVERY *(new)*

#### UTM

##### 41231_-_LOGID_PFCP_FORWARD
- Field added: `end-usr-address` (ip, len: 39) — "End user IP Address"
- Field added: `endusraddress6` (ip, len: 39) — ""

##### 41232_-_LOGID_PFCP_DENY
- Field added: `end-usr-address` (ip, len: 39) — "End user IP Address"
- Field added: `endusraddress6` (ip, len: 39) — ""

##### 41233_-_LOGID_PFCP_TRAFFIC_COUNT
- Field added: `end-usr-address` (ip, len: 39) — "End user IP Address"
- Field added: `endusraddress6` (ip, len: 39) — ""

---

### 7.2.9 → 7.2.10

*(no changes)*

---

### 7.2.10 → 7.2.11

**Summary:** 3 LOGID added, 0 removed | 2 fields added, 0 removed | 0 type changed | 0 descriptions changed | 0 lengths changed

#### Traffic

*(no changes)*

#### Event

##### 44559_-_LOGID_EVENT_INSTALL_IPROPE *(new)*

#### UTM

##### 61014_-_LOG_ID_SSH_UNSUPPORT_PROTO_BLOCK *(new)*

##### 61015_-_LOG_ID_SSH_UNSUPPORT_PROTO_PASS *(new)*

##### 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING
- Field added: `attack` (string, len: 256) — ""
- Field added: `attackid` (uint32, len: 10) — ""

---

### 7.2.11 → 7.2.12

**Summary:** 0 LOGID added, 0 removed | 4 fields added, 0 removed | 0 type changed | 0 descriptions changed | 0 lengths changed

#### Traffic

*(no changes)*

#### Event

*(no changes)*

#### UTM

##### 44032_-_LOGID_EVENT_VOIP_SIP
- Field added: `attack` (string, len: 256) — ""
- Field added: `attackid` (uint32, len: 10) — ""

##### 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK
- Field added: `attack` (string, len: 256) — ""
- Field added: `attackid` (uint32, len: 10) — ""

---

### 7.2.12 → 7.2.13

*(no changes)*

---


## 7.4

### 7.4.0 → 7.4.1

**Summary:** 20 LOGID added, 5 removed | 133 fields added, 1 removed | 0 type changed | 0 descriptions changed | 7 lengths changed

#### Traffic

##### 10_-_LOG_ID_TRAFFIC_EXPLICIT_PROXY
- Field added: `countcasb` (uint32, len: 10) — ""
- Field added: `countvpatch` (uint32, len: 10) — ""
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 11_-_LOG_ID_TRAFFIC_FAIL_CONN
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 12_-_LOG_ID_TRAFFIC_MULTICAST
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 13_-_LOG_ID_TRAFFIC_END_FORWARD
- Field added: `countcasb` (uint32, len: 10) — ""
- Field added: `countvpatch` (uint32, len: 10) — ""
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 14_-_LOG_ID_TRAFFIC_END_LOCAL
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 15_-_LOG_ID_TRAFFIC_START_FORWARD
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 16_-_LOG_ID_TRAFFIC_START_LOCAL
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 17_-_LOG_ID_TRAFFIC_SNIFFER
- Field added: `countcasb` (uint32, len: 10) — ""
- Field added: `countvpatch` (uint32, len: 10) — ""
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 19_-_LOG_ID_TRAFFIC_BROADCAST
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 20_-_LOG_ID_TRAFFIC_STAT
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 21_-_LOG_ID_TRAFFIC_SNIFFER_STAT
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 22_-_LOG_ID_TRAFFIC_UTM_CORRELATION
- Field added: `countcasb` (uint32, len: 10) — ""
- Field added: `countvpatch` (uint32, len: 10) — ""
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 24_-_LOG_ID_TRAFFIC_ZTNA
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 2_-_LOG_ID_TRAFFIC_ALLOW
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 3_-_LOG_ID_TRAFFIC_DENY
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 4_-_LOG_ID_TRAFFIC_OTHER_START
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 5_-_LOG_ID_TRAFFIC_OTHER_ICMP_ALLOW
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 6_-_LOG_ID_TRAFFIC_OTHER_ICMP_DENY
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 7_-_LOG_ID_TRAFFIC_OTHER_INVALID
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 8_-_LOG_ID_TRAFFIC_WANOPT
- Field added: `countcasb` (uint32, len: 10) — ""
- Field added: `countvpatch` (uint32, len: 10) — ""
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

##### 9_-_LOG_ID_TRAFFIC_WEBCACHE
- Field added: `countcasb` (uint32, len: 10) — ""
- Field added: `countvpatch` (uint32, len: 10) — ""
- Field added: `replydstintf` (string, len: 32) — ""
- Field added: `replysrcintf` (string, len: 32) — ""

#### Event

##### 20137_-_LOG_ID_FGSA_LIC_EXPIRE *(new)*

##### 20138_-_LOG_ID_SWOS_LIC_EXPIRE *(new)*

##### 20235_-_LOG_ID_SYS_SECURITY_MOUNT_VIOLATION *(new)*

##### 22939_-_LOG_ID_EVENT_VWL_FAIL_DETECT *(new)*

##### 22940_-_LOG_ID_EVENT_LINK_MONITOR_FAIL_DETECT *(new)*

##### 32055_-_LOG_ID_CC_KAT_SUCCESS *(new)*

##### 32264_-_LOG_ID_BLE_FIRMWARE_CHECK *(new)*

##### 32265_-_LOG_ID_BLE_FIRMWARE_UPDATE *(new)*

##### 46522_-_LOG_ID_INTERNAL_LTE_MODEM_BILLING_DATA_ALERT *(new)*

##### 46523_-_LOG_ID_INTERNAL_LTE_MODEM_BILLING_TIME_REFRESH *(new)*

##### 46524_-_LOG_ID_INTERNAL_LTE_MODEM_SIM_SWITCH_DATA_PLAN *(new)*

##### 46525_-_LOG_ID_INTERNAL_LTE_MODEM_BILLING_STOP_NETWORK *(new)*

##### 46526_-_LOG_ID_INTERNAL_LTE_MODEM_BILLING_DATA_PLAN_OVER *(new)*

##### 53406_-_LOG_ID_2GB_CSF_UPGRADE *(new)*

##### 32019_-_LOG_ID_CC_ENTER_ERR_MOD *(removed)*

##### 45057_-_LOG_ID_FCC_ADD *(removed)*

##### 45058_-_LOG_ID_FCC_CLOSE *(removed)*

##### 45061_-_LOG_ID_FCC_CLOSE_BY_TYPE *(removed)*

##### 46506_-_LOG_ID_INTERNAL_LTE_MODEM_BILLING_DAILY_LOG *(removed)*

##### 22938_-_LOG_ID_EVENT_VWL_WAN_SPEEDTEST_RESULT
- Field added: `latency` (string, len: 24) — ""
- Field added: `mode` (string, len: 12) — "Mode"
- Field added: `protocol` (string, len: 128) — ""

##### 43574_-_LOG_ID_EVENT_WIRELESS_STA_DASS
- Field added: `snprev` (string, len: 36) — ""

##### 43575_-_LOG_ID_EVENT_WIRELESS_STA_DAUT
- Field added: `snprev` (string, len: 36) — ""

##### 43577_-_LOG_ID_EVENT_WIRELESS_STA_DENY
- Field added: `snprev` (string, len: 36) — ""

##### 43629_-_LOG_ID_EVENT_WIRELESS_STA_RADIUS_AUTH_FAILURE
- Field added: `snprev` (string, len: 36) — ""

##### 43630_-_LOG_ID_EVENT_WIRELESS_STA_RADIUS_AUTH_SUCCESS
- Field added: `snprev` (string, len: 36) — ""

##### 43631_-_LOG_ID_EVENT_WIRELESS_STA_RADIUS_AUTH_NO_RESP
- Field added: `snprev` (string, len: 36) — ""

##### 43632_-_LOG_ID_EVENT_WIRELESS_STA_RADIUS_MAC_AUTH_FAILURE
- Field added: `snprev` (string, len: 36) — ""

##### 43633_-_LOG_ID_EVENT_WIRELESS_STA_RADIUS_MAC_AUTH_SUCCESS
- Field added: `snprev` (string, len: 36) — ""

##### 43634_-_LOG_ID_EVENT_WIRELESS_STA_RADIUS_MAC_AUTH_NO_RESP
- Field added: `snprev` (string, len: 36) — ""

##### 43635_-_LOG_ID_EVENT_WIRELESS_STA_OKC_NO_MATCH
- Field added: `snprev` (string, len: 36) — ""

##### 43636_-_LOG_ID_EVENT_WIRELESS_STA_OKC_LOCAL_MATCH
- Field added: `snprev` (string, len: 36) — ""

##### 43637_-_LOG_ID_EVENT_WIRELESS_STA_OKC_INTER_AC_MATCH
- Field added: `snprev` (string, len: 36) — ""

##### 43638_-_LOG_ID_EVENT_WIRELESS_STA_OKC_INTER_AP_MATCH
- Field added: `snprev` (string, len: 36) — ""

##### 43639_-_LOG_ID_EVENT_WIRELESS_STA_FT_INVALID_ACTION_REQ
- Field added: `snprev` (string, len: 36) — ""

##### 43640_-_LOG_ID_EVENT_WIRELESS_STA_FT_INVALID_AUTH_REQ
- Field added: `snprev` (string, len: 36) — ""

##### 43641_-_LOG_ID_EVENT_WIRELESS_STA_FT_INVALID_REASSOC_REQ
- Field added: `snprev` (string, len: 36) — ""

##### 43642_-_LOG_ID_EVENT_WIRELESS_STA_FT_ACTION_REQ
- Field added: `snprev` (string, len: 36) — ""

##### 43643_-_LOG_ID_EVENT_WIRELESS_STA_FT_ACTION_RESP
- Field added: `snprev` (string, len: 36) — ""

##### 43644_-_LOG_ID_EVENT_WIRELESS_STA_FT_AUTH_REQ
- Field added: `snprev` (string, len: 36) — ""

##### 43645_-_LOG_ID_EVENT_WIRELESS_STA_FT_AUTH_RESP
- Field added: `snprev` (string, len: 36) — ""

##### 43646_-_LOG_ID_EVENT_WIRELESS_STA_FT_REASSOC_REQ
- Field added: `snprev` (string, len: 36) — ""

##### 43647_-_LOG_ID_EVENT_WIRELESS_STA_FT_REASSOC_RESP
- Field added: `snprev` (string, len: 36) — ""

##### 43648_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_INVALID_SECOND_MSG
- Field added: `snprev` (string, len: 36) — ""

##### 43649_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_INVALID_FOURTH_MSG
- Field added: `snprev` (string, len: 36) — ""

##### 43650_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_FIRST_MSG
- Field added: `snprev` (string, len: 36) — ""

##### 43651_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_SECOND_MSG
- Field added: `snprev` (string, len: 36) — ""

##### 43652_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_THIRD_MSG
- Field added: `snprev` (string, len: 36) — ""

##### 43653_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_FOURTH_MSG
- Field added: `snprev` (string, len: 36) — ""

##### 43654_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_FIRST_GROUP_MSG
- Field added: `snprev` (string, len: 36) — ""

##### 43655_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_SECOND_GROUP_MSG
- Field added: `snprev` (string, len: 36) — ""

##### 43656_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_MAX_STA_CNT
- Field added: `snprev` (string, len: 36) — ""

##### 43657_-_LOG_ID_EVENT_WIRELESS_STA_ASSOC_FAIL
- Field added: `snprev` (string, len: 36) — ""

##### 43658_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_NO_RESP
- Field added: `snprev` (string, len: 36) — ""

##### 43659_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_DIFF_OFFER
- Field added: `snprev` (string, len: 36) — ""

##### 43660_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_NO_ACK
- Field added: `snprev` (string, len: 36) — ""

##### 43661_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_NAK
- Field added: `snprev` (string, len: 36) — ""

##### 43662_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_DUP_IP
- Field added: `snprev` (string, len: 36) — ""

##### 43663_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_DISCOVER
- Field added: `snprev` (string, len: 36) — ""

##### 43664_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_OFFER
- Field added: `snprev` (string, len: 36) — ""

##### 43665_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_DECLINE
- Field added: `snprev` (string, len: 36) — ""

##### 43666_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_REQUEST
- Field added: `snprev` (string, len: 36) — ""

##### 43667_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_ACK
- Field added: `snprev` (string, len: 36) — ""

##### 43668_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_RELEASE
- Field added: `snprev` (string, len: 36) — ""

##### 43669_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_INFORM
- Field added: `snprev` (string, len: 36) — ""

##### 43670_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_SELF_ASSIGNED
- Field added: `snprev` (string, len: 36) — ""

##### 43674_-_LOG_ID_EVENT_WIRELESS_STA_WPA_KRACK_FT_REASSOC
- Field added: `snprev` (string, len: 36) — ""

##### 43675_-_LOG_ID_EVENT_WIRELESS_STA_AUTH_REQ
- Field added: `snprev` (string, len: 36) — ""

##### 43676_-_LOG_ID_EVENT_WIRELESS_STA_AUTH_RESP
- Field added: `snprev` (string, len: 36) — ""

##### 43677_-_LOG_ID_EVENT_WIRELESS_STA_ASSOC_REQ
- Field added: `snprev` (string, len: 36) — ""

##### 43678_-_LOG_ID_EVENT_WIRELESS_STA_REASSOC_REQ
- Field added: `snprev` (string, len: 36) — ""

##### 43679_-_LOG_ID_EVENT_WIRELESS_STA_ASSOC_RESP
- Field added: `snprev` (string, len: 36) — ""

##### 43680_-_LOG_ID_EVENT_WIRELESS_STA_REASSOC_RESP
- Field added: `snprev` (string, len: 36) — ""

##### 43681_-_LOG_ID_EVENT_WIRELESS_STA_PROBE_REQ
- Field added: `snprev` (string, len: 36) — ""

##### 43682_-_LOG_ID_EVENT_WIRELESS_STA_PROBE_RESP
- Field added: `snprev` (string, len: 36) — ""

##### 43686_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_INVALID_SCHEDULE
- Field added: `snprev` (string, len: 36) — ""

##### 43693_-_LOG_ID_EVENT_WIRELESS_STA_WNM_ACTION_BSTM_REQ
- Field added: `snprev` (string, len: 36) — ""

##### 43694_-_LOG_ID_EVENT_WIRELESS_STA_WNM_ACTION_BSTM_RESP_ACCEPT
- Field added: `snprev` (string, len: 36) — ""

##### 43695_-_LOG_ID_EVENT_WIRELESS_STA_WNM_ACTION_BSTM_RESP_REJECT
- Field added: `snprev` (string, len: 36) — ""

##### 43699_-_LOG_ID_EVENT_WIRELESS_STA_DHCP6_SOLICIT
- Field added: `snprev` (string, len: 36) — ""

##### 43700_-_LOG_ID_EVENT_WIRELESS_STA_DHCP6_ADVERTISE
- Field added: `snprev` (string, len: 36) — ""

##### 43701_-_LOG_ID_EVENT_WIRELESS_STA_DHCP6_REQUEST
- Field added: `snprev` (string, len: 36) — ""

##### 43702_-_LOG_ID_EVENT_WIRELESS_STA_DHCP6_CONFIRM
- Field added: `snprev` (string, len: 36) — ""

##### 43703_-_LOG_ID_EVENT_WIRELESS_STA_DHCP6_RENEW
- Field added: `snprev` (string, len: 36) — ""

##### 43704_-_LOG_ID_EVENT_WIRELESS_STA_DHCP6_REPLY
- Field added: `snprev` (string, len: 36) — ""

##### 43705_-_LOG_ID_EVENT_WIRELESS_STA_DHCP6_RELEASE
- Field added: `snprev` (string, len: 36) — ""

##### 43706_-_LOG_ID_EVENT_WIRELESS_STA_DHCP6_RECONFIGURE
- Field added: `snprev` (string, len: 36) — ""

##### 43709_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_ENFORCEMENT
- Field added: `snprev` (string, len: 36) — ""

##### 46000_-_LOG_ID_VIP_REAL_SVR_ENA
- Length changed: `vip` 64 → 80

##### 46001_-_LOG_ID_VIP_REAL_SVR_DISA
- Length changed: `vip` 64 → 80

##### 46002_-_LOG_ID_VIP_REAL_SVR_UP
- Length changed: `vip` 64 → 80

##### 46003_-_LOG_ID_VIP_REAL_SVR_DOWN
- Length changed: `vip` 64 → 80

##### 46004_-_LOG_ID_VIP_REAL_SVR_ENT_HOLDDOWN
- Length changed: `vip` 64 → 80

##### 46005_-_LOG_ID_VIP_REAL_SVR_FAIL_HOLDDOWN
- Length changed: `vip` 64 → 80

##### 46006_-_LOG_ID_VIP_REAL_SVR_FAIL
- Length changed: `vip` 64 → 80

##### 51000_-_LOG_ID_NB_TBL_CHG
- Field added: `devintfname` (string, len: 32) — "HA device interface name"

##### 53202_-_LOG_ID_CONNECTOR_API_FAILED
- Field removed: `fctemssn` (string)

#### UTM — new subtypes: casb, virtual-patch | removed subtypes: *(none)*

##### 10000_-_LOG_ID_CASB_ACCESS_BLOCKED *(new)*

##### 10001_-_LOG_ID_CASB_ACCESS_BYPASS *(new)*

##### 10002_-_LOG_ID_CASB_ACCESS_MONITOR *(new)*

##### 62308_-_LOG_ID_SSL_ANOMALY_HANDSHAKE_FAILURE *(new)*

##### 64600_-_LOG_ID_VPATCH_BLOCK *(new)*

##### 64601_-_LOG_ID_VPATCH_LOG *(new)*

##### 61000_-_LOG_ID_SSH_COMMAND_BLOCK
- Field added: `poluuid` (string, len: 37) — ""

##### 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT
- Field added: `poluuid` (string, len: 37) — ""

##### 61002_-_LOG_ID_SSH_COMMAND_PASS
- Field added: `poluuid` (string, len: 37) — ""

##### 61003_-_LOG_ID_SSH_COMMAND_PASS_ALERT
- Field added: `poluuid` (string, len: 37) — ""

##### 61010_-_LOG_ID_SSH_CHANNEL_BLOCK
- Field added: `poluuid` (string, len: 37) — ""

##### 61011_-_LOG_ID_SSH_CHANNEL_PASS
- Field added: `poluuid` (string, len: 37) — ""

##### 61012_-_LOG_ID_SSH_HOST_KEY_WARNING
- Field added: `poluuid` (string, len: 37) — ""

##### 61013_-_LOG_ID_SSH_HOST_KEY_NOTIF
- Field added: `poluuid` (string, len: 37) — ""

---

### 7.4.1 → 7.4.2

**Summary:** 30 LOGID added, 4 removed | 246 fields added, 8 removed | 0 type changed | 0 descriptions changed | 16 lengths changed

#### Traffic

##### 10_-_LOG_ID_TRAFFIC_EXPLICIT_PROXY
- Field added: `clientcert` (string, len: 10) — ""
- Field added: `clientdeviceems` (string, len: 16) — ""
- Field added: `durationdelta` (uint32, len: 20) — ""
- Field added: `rcvdpktdelta` (uint32, len: 20) — ""
- Field added: `sentpktdelta` (uint32, len: 20) — ""

##### 11_-_LOG_ID_TRAFFIC_FAIL_CONN
- Field added: `clientcert` (string, len: 10) — ""
- Field added: `clientdeviceems` (string, len: 16) — ""
- Field added: `durationdelta` (uint32, len: 20) — ""
- Field added: `rcvdpktdelta` (uint32, len: 20) — ""
- Field added: `sentpktdelta` (uint32, len: 20) — ""

##### 12_-_LOG_ID_TRAFFIC_MULTICAST
- Field added: `clientcert` (string, len: 10) — ""
- Field added: `clientdeviceems` (string, len: 16) — ""
- Field added: `durationdelta` (uint32, len: 20) — ""
- Field added: `rcvdpktdelta` (uint32, len: 20) — ""
- Field added: `sentpktdelta` (uint32, len: 20) — ""

##### 13_-_LOG_ID_TRAFFIC_END_FORWARD
- Field added: `clientcert` (string, len: 10) — ""
- Field added: `clientdeviceems` (string, len: 16) — ""
- Field added: `durationdelta` (uint32, len: 20) — ""
- Field added: `rcvdpktdelta` (uint32, len: 20) — ""
- Field added: `sentpktdelta` (uint32, len: 20) — ""

##### 14_-_LOG_ID_TRAFFIC_END_LOCAL
- Field added: `clientcert` (string, len: 10) — ""
- Field added: `clientdeviceems` (string, len: 16) — ""
- Field added: `durationdelta` (uint32, len: 20) — ""
- Field added: `rcvdpktdelta` (uint32, len: 20) — ""
- Field added: `sentpktdelta` (uint32, len: 20) — ""

##### 15_-_LOG_ID_TRAFFIC_START_FORWARD
- Field added: `clientcert` (string, len: 10) — ""
- Field added: `clientdeviceems` (string, len: 16) — ""
- Field added: `durationdelta` (uint32, len: 20) — ""
- Field added: `rcvdpktdelta` (uint32, len: 20) — ""
- Field added: `sentpktdelta` (uint32, len: 20) — ""

##### 16_-_LOG_ID_TRAFFIC_START_LOCAL
- Field added: `clientcert` (string, len: 10) — ""
- Field added: `clientdeviceems` (string, len: 16) — ""
- Field added: `durationdelta` (uint32, len: 20) — ""
- Field added: `rcvdpktdelta` (uint32, len: 20) — ""
- Field added: `sentpktdelta` (uint32, len: 20) — ""

##### 17_-_LOG_ID_TRAFFIC_SNIFFER
- Field added: `clientcert` (string, len: 10) — ""
- Field added: `clientdeviceems` (string, len: 16) — ""
- Field added: `durationdelta` (uint32, len: 20) — ""
- Field added: `rcvdpktdelta` (uint32, len: 20) — ""
- Field added: `sentpktdelta` (uint32, len: 20) — ""

##### 19_-_LOG_ID_TRAFFIC_BROADCAST
- Field added: `clientcert` (string, len: 10) — ""
- Field added: `clientdeviceems` (string, len: 16) — ""
- Field added: `durationdelta` (uint32, len: 20) — ""
- Field added: `rcvdpktdelta` (uint32, len: 20) — ""
- Field added: `sentpktdelta` (uint32, len: 20) — ""

##### 20_-_LOG_ID_TRAFFIC_STAT
- Field added: `clientcert` (string, len: 10) — ""
- Field added: `clientdeviceems` (string, len: 16) — ""
- Field added: `durationdelta` (uint32, len: 20) — ""
- Field added: `rcvdpktdelta` (uint32, len: 20) — ""
- Field added: `sentpktdelta` (uint32, len: 20) — ""

##### 21_-_LOG_ID_TRAFFIC_SNIFFER_STAT
- Field added: `clientcert` (string, len: 10) — ""
- Field added: `clientdeviceems` (string, len: 16) — ""
- Field added: `durationdelta` (uint32, len: 20) — ""
- Field added: `rcvdpktdelta` (uint32, len: 20) — ""
- Field added: `sentpktdelta` (uint32, len: 20) — ""

##### 22_-_LOG_ID_TRAFFIC_UTM_CORRELATION
- Field added: `clientcert` (string, len: 10) — ""
- Field added: `clientdeviceems` (string, len: 16) — ""
- Field added: `durationdelta` (uint32, len: 20) — ""
- Field added: `rcvdpktdelta` (uint32, len: 20) — ""
- Field added: `sentpktdelta` (uint32, len: 20) — ""

##### 24_-_LOG_ID_TRAFFIC_ZTNA
- Field added: `clientcert` (string, len: 10) — ""
- Field added: `clientdeviceems` (string, len: 16) — ""
- Field added: `durationdelta` (uint32, len: 20) — ""
- Field added: `rcvdpktdelta` (uint32, len: 20) — ""
- Field added: `sentpktdelta` (uint32, len: 20) — ""

##### 2_-_LOG_ID_TRAFFIC_ALLOW
- Field added: `clientcert` (string, len: 10) — ""
- Field added: `clientdeviceems` (string, len: 16) — ""
- Field added: `durationdelta` (uint32, len: 20) — ""
- Field added: `rcvdpktdelta` (uint32, len: 20) — ""
- Field added: `sentpktdelta` (uint32, len: 20) — ""

##### 3_-_LOG_ID_TRAFFIC_DENY
- Field added: `clientcert` (string, len: 10) — ""
- Field added: `clientdeviceems` (string, len: 16) — ""
- Field added: `durationdelta` (uint32, len: 20) — ""
- Field added: `rcvdpktdelta` (uint32, len: 20) — ""
- Field added: `sentpktdelta` (uint32, len: 20) — ""

##### 4_-_LOG_ID_TRAFFIC_OTHER_START
- Field added: `clientcert` (string, len: 10) — ""
- Field added: `clientdeviceems` (string, len: 16) — ""
- Field added: `durationdelta` (uint32, len: 20) — ""
- Field added: `rcvdpktdelta` (uint32, len: 20) — ""
- Field added: `sentpktdelta` (uint32, len: 20) — ""

##### 5_-_LOG_ID_TRAFFIC_OTHER_ICMP_ALLOW
- Field added: `clientcert` (string, len: 10) — ""
- Field added: `clientdeviceems` (string, len: 16) — ""
- Field added: `durationdelta` (uint32, len: 20) — ""
- Field added: `rcvdpktdelta` (uint32, len: 20) — ""
- Field added: `sentpktdelta` (uint32, len: 20) — ""

##### 6_-_LOG_ID_TRAFFIC_OTHER_ICMP_DENY
- Field added: `clientcert` (string, len: 10) — ""
- Field added: `clientdeviceems` (string, len: 16) — ""
- Field added: `durationdelta` (uint32, len: 20) — ""
- Field added: `rcvdpktdelta` (uint32, len: 20) — ""
- Field added: `sentpktdelta` (uint32, len: 20) — ""

##### 7_-_LOG_ID_TRAFFIC_OTHER_INVALID
- Field added: `clientcert` (string, len: 10) — ""
- Field added: `clientdeviceems` (string, len: 16) — ""
- Field added: `durationdelta` (uint32, len: 20) — ""
- Field added: `rcvdpktdelta` (uint32, len: 20) — ""
- Field added: `sentpktdelta` (uint32, len: 20) — ""

##### 8_-_LOG_ID_TRAFFIC_WANOPT
- Field added: `clientcert` (string, len: 10) — ""
- Field added: `clientdeviceems` (string, len: 16) — ""
- Field added: `durationdelta` (uint32, len: 20) — ""
- Field added: `rcvdpktdelta` (uint32, len: 20) — ""
- Field added: `sentpktdelta` (uint32, len: 20) — ""

##### 9_-_LOG_ID_TRAFFIC_WEBCACHE
- Field added: `clientcert` (string, len: 10) — ""
- Field added: `clientdeviceems` (string, len: 16) — ""
- Field added: `durationdelta` (uint32, len: 20) — ""
- Field added: `rcvdpktdelta` (uint32, len: 20) — ""
- Field added: `sentpktdelta` (uint32, len: 20) — ""

#### Event

##### 20139_-_LOG_ID_FGCS_ACC_LIC_EXPIRE *(new)*

##### 20140_-_LOG_ID_FSPA_LIC_EXPIRE *(new)*

##### 20141_-_LOG_ID_FSFG_LIC_EXPIRE *(new)*

##### 22022_-_LOG_ID_ENTER_EXTREME_LOW_MEM_MODE *(new)*

##### 22023_-_LOG_ID_LEAVE_EXTREME_LOW_MEM_MODE *(new)*

##### 22817_-_LOG_ID_SCANUNIT_DLP_SIGNATURE_REMOVE *(new)*

##### 22874_-_LOG_ID_FLTUND_NEW_CONN *(new)*

##### 22875_-_LOG_ID_FLTUND_CONN_DOWN *(new)*

##### 22876_-_LOG_ID_FLTUND_RCV_BOOTSTRAP *(new)*

##### 22877_-_LOG_ID_FLTUND_CONN_ONLINE *(new)*

##### 22878_-_LOG_ID_FLTUND_CONN_OFFLINE *(new)*

##### 34420_-_LOG_ID_NP6XLITE_HPE_PACKET_DROP *(new)*

##### 34421_-_LOG_ID_NP6XLITE_HPE_PACKET_FLOOD *(new)*

##### 45101_-_LOG_ID_EC_REG_SUCCEED *(new)*

##### 45132_-_LOG_ID_EC_EMS_UPGRADE_FAIL *(new)*

##### 45133_-_LOG_ID_EC_SHM_MISSING_QUERY *(new)*

##### 22104_-_LOG_ID_POWER_RESTORE *(removed)*

##### 20232_-_LOG_ID_SYS_SECURITY_LOAD_MODULE_VIOLATION
- Field removed: `severity` (string)

##### 22105_-_LOG_ID_POWER_FAILURE
- Field removed: `unit` (uint32)

##### 22923_-_LOG_ID_EVENT_VWL_LQTY_STATUS
- Length changed: `eventtype` 32 → 48

##### 22924_-_LOG_ID_EVENT_VWL_VOLUME_STATUS
- Length changed: `eventtype` 32 → 48

##### 22925_-_LOG_ID_EVENT_VWL_SLA_INFO
- Length changed: `eventtype` 32 → 48

##### 22926_-_LOG_ID_EVENT_VWL_NEIGHBOR_STATUS
- Length changed: `eventtype` 32 → 48

##### 22927_-_LOG_ID_EVENT_VWL_NEIGHBOR_STANDALONE
- Length changed: `eventtype` 32 → 48

##### 22928_-_LOG_ID_EVENT_VWL_NEIGHBOR_PRIMARY
- Length changed: `eventtype` 32 → 48

##### 22929_-_LOG_ID_EVENT_VWL_NEIGHBOR_SECONDARY
- Length changed: `eventtype` 32 → 48

##### 22930_-_LOG_ID_EVENT_VWL_LQTY_STATUS_WARNING
- Length changed: `eventtype` 32 → 48

##### 22931_-_LOG_ID_EVENT_VWL_SLA_INFO_WARNING
- Length changed: `eventtype` 32 → 48

##### 22933_-_LOG_ID_EVENT_VWL_SLA_INFO_NOTIF
- Length changed: `eventtype` 32 → 48

##### 22934_-_LOG_ID_EVENT_VWL_LQTY_STATUS_INFO
- Length changed: `eventtype` 32 → 48

##### 22935_-_LOG_ID_EVENT_VWL_LQTY_STATUS_DEBUG
- Length changed: `eventtype` 32 → 48

##### 22936_-_LOG_ID_EVENT_VWL_INET_SVC_PQTY_STATUS_INFO
- Length changed: `eventtype` 32 → 48

##### 22937_-_LOG_ID_EVENT_VWL_APP_PERF_METRICS
- Length changed: `eventtype` 32 → 48

##### 22938_-_LOG_ID_EVENT_VWL_WAN_SPEEDTEST_RESULT
- Length changed: `eventtype` 32 → 48

##### 22939_-_LOG_ID_EVENT_VWL_FAIL_DETECT
- Length changed: `eventtype` 32 → 48

##### 32099_-_LOG_ID_CHG_CONFIG_INFO
- Field added: `action` (string, len: 65) — "Policy Action"
- Field added: `desc` (string, len: 128) — "Description"
- Field added: `informationsource` (string, len: 4096) — "Information Source"
- Field added: `status` (string, len: 23) — "Status"

##### 32569_-_LOG_ID_FSW_SWITCH_LOG_EVENT
- Field added: `action` (string, len: 65) — ""
- Field added: `cert` (string, len: 36) — "Certificate"
- Field added: `eventtype` (string, len: 48) — ""
- Field added: `reason` (string, len: 256) — "Reason"
- Field added: `srcip` (ip, len: 39) — ""
- Field added: `srcmac` (string, len: 17) — ""
- Field added: `status` (string, len: 23) — "Status"
- Field added: `switchaclid` (uint32, len: 10) — ""
- Field added: `switchautoip` (ip, len: 39) — ""
- Field added: `switchinterface` (string, len: 16) — ""
- Field added: `switchl2capacity` (uint32, len: 10) — ""
- Field added: `switchl2count` (uint32, len: 10) — ""
- Field added: `switchmirrorsession` (string, len: 16) — ""
- Field added: `switchphysicalport` (string, len: 16) — ""
- Field added: `switchsysteminterface` (string, len: 16) — ""
- Field added: `switchtrunk` (string, len: 16) — ""
- Field added: `switchtrunkinterface` (string, len: 16) — ""
- Field added: `vlan` (uint32, len: 10) — ""

##### 39425_-_LOG_ID_EVENT_SSL_VPN_USER_TUNNEL_DOWN
- Field added: `srccountry` (string, len: 64) — ""

##### 39936_-_LOG_ID_EVENT_SSL_VPN_SESSION_WEB_TUNNEL_STATS
- Field added: `srccountry` (string, len: 64) — ""

##### 39937_-_LOG_ID_EVENT_SSL_VPN_SESSION_WEBAPP_DENY
- Field added: `srccountry` (string, len: 64) — ""

##### 39938_-_LOG_ID_EVENT_SSL_VPN_SESSION_WEBAPP_PASS
- Field added: `srccountry` (string, len: 64) — ""

##### 39939_-_LOG_ID_EVENT_SSL_VPN_SESSION_WEBAPP_TIMEOUT
- Field added: `srccountry` (string, len: 64) — ""

##### 39940_-_LOG_ID_EVENT_SSL_VPN_SESSION_WEBAPP_CLOSE
- Field added: `srccountry` (string, len: 64) — ""

##### 39944_-_LOG_ID_EVENT_SSL_VPN_SESSION_ALERT
- Field added: `srccountry` (string, len: 64) — ""

##### 39948_-_LOG_ID_EVENT_SSL_VPN_SESSION_TUNNEL_DOWN
- Field added: `srccountry` (string, len: 64) — ""

##### 39949_-_LOG_ID_EVENT_SSL_VPN_SESSION_TUNNEL_STATS
- Field added: `srccountry` (string, len: 64) — ""

##### 43629_-_LOG_ID_EVENT_WIRELESS_STA_RADIUS_AUTH_FAILURE
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43630_-_LOG_ID_EVENT_WIRELESS_STA_RADIUS_AUTH_SUCCESS
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43631_-_LOG_ID_EVENT_WIRELESS_STA_RADIUS_AUTH_NO_RESP
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43632_-_LOG_ID_EVENT_WIRELESS_STA_RADIUS_MAC_AUTH_FAILURE
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43633_-_LOG_ID_EVENT_WIRELESS_STA_RADIUS_MAC_AUTH_SUCCESS
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43634_-_LOG_ID_EVENT_WIRELESS_STA_RADIUS_MAC_AUTH_NO_RESP
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43635_-_LOG_ID_EVENT_WIRELESS_STA_OKC_NO_MATCH
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43636_-_LOG_ID_EVENT_WIRELESS_STA_OKC_LOCAL_MATCH
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43637_-_LOG_ID_EVENT_WIRELESS_STA_OKC_INTER_AC_MATCH
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43638_-_LOG_ID_EVENT_WIRELESS_STA_OKC_INTER_AP_MATCH
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43639_-_LOG_ID_EVENT_WIRELESS_STA_FT_INVALID_ACTION_REQ
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43640_-_LOG_ID_EVENT_WIRELESS_STA_FT_INVALID_AUTH_REQ
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43641_-_LOG_ID_EVENT_WIRELESS_STA_FT_INVALID_REASSOC_REQ
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43642_-_LOG_ID_EVENT_WIRELESS_STA_FT_ACTION_REQ
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43643_-_LOG_ID_EVENT_WIRELESS_STA_FT_ACTION_RESP
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43644_-_LOG_ID_EVENT_WIRELESS_STA_FT_AUTH_REQ
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43645_-_LOG_ID_EVENT_WIRELESS_STA_FT_AUTH_RESP
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43646_-_LOG_ID_EVENT_WIRELESS_STA_FT_REASSOC_REQ
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43647_-_LOG_ID_EVENT_WIRELESS_STA_FT_REASSOC_RESP
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43648_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_INVALID_SECOND_MSG
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43649_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_INVALID_FOURTH_MSG
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43650_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_FIRST_MSG
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43651_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_SECOND_MSG
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43652_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_THIRD_MSG
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43653_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_FOURTH_MSG
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43654_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_FIRST_GROUP_MSG
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43655_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_SECOND_GROUP_MSG
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43656_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_MAX_STA_CNT
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43657_-_LOG_ID_EVENT_WIRELESS_STA_ASSOC_FAIL
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43674_-_LOG_ID_EVENT_WIRELESS_STA_WPA_KRACK_FT_REASSOC
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43675_-_LOG_ID_EVENT_WIRELESS_STA_AUTH_REQ
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43676_-_LOG_ID_EVENT_WIRELESS_STA_AUTH_RESP
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43677_-_LOG_ID_EVENT_WIRELESS_STA_ASSOC_REQ
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43678_-_LOG_ID_EVENT_WIRELESS_STA_REASSOC_REQ
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43679_-_LOG_ID_EVENT_WIRELESS_STA_ASSOC_RESP
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43680_-_LOG_ID_EVENT_WIRELESS_STA_REASSOC_RESP
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43681_-_LOG_ID_EVENT_WIRELESS_STA_PROBE_REQ
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43682_-_LOG_ID_EVENT_WIRELESS_STA_PROBE_RESP
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43686_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_INVALID_SCHEDULE
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43693_-_LOG_ID_EVENT_WIRELESS_STA_WNM_ACTION_BSTM_REQ
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43694_-_LOG_ID_EVENT_WIRELESS_STA_WNM_ACTION_BSTM_RESP_ACCEPT
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

##### 43695_-_LOG_ID_EVENT_WIRELESS_STA_WNM_ACTION_BSTM_RESP_REJECT
- Field added: `signal` (int8, len: 4) — "The signal value of SSID or client"
- Field added: `snr` (int8, len: 4) — ""

#### UTM

##### 13617_-_LOG_ID_CONTENT_TYPE_EXEMPT *(new)*

##### 13712_-_LOG_ID_VIDEOFILTER_TITLE_BLOCK *(new)*

##### 13713_-_LOG_ID_VIDEOFILTER_TITLE_MONITOR *(new)*

##### 13714_-_LOG_ID_VIDEOFILTER_TITLE_ALLOW *(new)*

##### 13728_-_LOG_ID_VIDEOFILTER_DESCRIPTION_BLOCK *(new)*

##### 13729_-_LOG_ID_VIDEOFILTER_DESCRIPTION_MONITOR *(new)*

##### 13730_-_LOG_ID_VIDEOFILTER_DESCRIPTION_ALLOW *(new)*

##### 60002_-_LOG_ID_ICAP_CONN_ERROR *(new)*

##### 62309_-_LOG_ID_SSL_ANOMALY_CERT_INVALID *(new)*

##### 64600_-_LOG_ID_OT_VPATCH_BLOCK *(new)*

##### 64601_-_LOG_ID_OT_VPATCH_LOG *(new)*

##### 64610_-_LOG_ID_LOCALIN_VPATCH_BLOCK *(new)*

##### 64611_-_LOG_ID_LOCALIN_VPATCH_LOG *(new)*

##### 8982_-_MESGID_SCAN_AV_MAX_MEMORY_REACHED_ERROR *(new)*

##### 60002_-_LOG_ID_ICAP_SERVER_CLOSE_CONN *(removed)*

##### 64600_-_LOG_ID_VPATCH_BLOCK *(removed)*

##### 64601_-_LOG_ID_VPATCH_LOG *(removed)*

##### 10000_-_LOG_ID_CASB_ACCESS_BLOCKED
- Field added: `dstuuid` (string, len: 37) — ""
- Field added: `srcuuid` (string, len: 37) — ""

##### 10001_-_LOG_ID_CASB_ACCESS_BYPASS
- Field added: `dstuuid` (string, len: 37) — ""
- Field added: `srcuuid` (string, len: 37) — ""

##### 10002_-_LOG_ID_CASB_ACCESS_MONITOR
- Field added: `dstuuid` (string, len: 37) — ""
- Field added: `srcuuid` (string, len: 37) — ""

##### 13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK
- Field added: `videodesc` (string, len: 64) — ""
- Field added: `videotitle` (string, len: 512) — ""

##### 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR
- Field added: `videodesc` (string, len: 64) — ""
- Field added: `videotitle` (string, len: 512) — ""

##### 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW
- Field added: `videodesc` (string, len: 64) — ""
- Field added: `videotitle` (string, len: 512) — ""

##### 13680_-_LOG_ID_VIDEOFILTER_CHANNEL_BLOCK
- Field added: `videodesc` (string, len: 64) — ""
- Field added: `videotitle` (string, len: 512) — ""

##### 13681_-_LOG_ID_VIDEOFILTER_CHANNEL_MONITOR
- Field added: `videodesc` (string, len: 64) — ""
- Field added: `videotitle` (string, len: 512) — ""

##### 13682_-_LOG_ID_VIDEOFILTER_CHANNEL_ALLOW
- Field added: `videodesc` (string, len: 64) — ""
- Field added: `videotitle` (string, len: 512) — ""

##### 24576_-_LOG_ID_DLP_WARN
- Field added: `ruleid` (uint32, len: 10) — ""
- Field added: `rulename` (string, len: 128) — ""
- Field removed: `filteridx` (uint32)
- Field removed: `filtername` (string)

##### 24577_-_LOG_ID_DLP_NOTIF
- Field added: `ruleid` (uint32, len: 10) — ""
- Field added: `rulename` (string, len: 128) — ""
- Field removed: `filteridx` (uint32)
- Field removed: `filtername` (string)

##### 60000_-_LOG_ID_ICAP_SERVER_ERROR
- Field added: `reason` (string, len: 4096) — ""

##### 60001_-_LOG_ID_ICAP_INFECTION_BLOCK
- Field added: `reason` (string, len: 4096) — ""

##### 64000_-_LOG_ID_FILE_FILTER_BLOCK
- Field added: `rulename` (string, len: 36) — ""
- Field removed: `filtername` (string)

##### 64001_-_LOG_ID_FILE_FILTER_LOG
- Field added: `rulename` (string, len: 36) — ""
- Field removed: `filtername` (string)

---

### 7.4.2 → 7.4.3

*(no changes)*

---

### 7.4.3 → 7.4.4

**Summary:** 21 LOGID added, 2 removed | 41 fields added, 0 removed | 0 type changed | 2 descriptions changed | 0 lengths changed

#### Traffic

##### 10_-_LOG_ID_TRAFFIC_EXPLICIT_PROXY
- Field added: `srcremote` (ip, len: 39) — ""

##### 11_-_LOG_ID_TRAFFIC_FAIL_CONN
- Field added: `srcremote` (ip, len: 39) — ""

##### 12_-_LOG_ID_TRAFFIC_MULTICAST
- Field added: `srcremote` (ip, len: 39) — ""

##### 13_-_LOG_ID_TRAFFIC_END_FORWARD
- Field added: `srcremote` (ip, len: 39) — ""

##### 14_-_LOG_ID_TRAFFIC_END_LOCAL
- Field added: `srcremote` (ip, len: 39) — ""

##### 15_-_LOG_ID_TRAFFIC_START_FORWARD
- Field added: `srcremote` (ip, len: 39) — ""

##### 16_-_LOG_ID_TRAFFIC_START_LOCAL
- Field added: `srcremote` (ip, len: 39) — ""

##### 17_-_LOG_ID_TRAFFIC_SNIFFER
- Field added: `srcremote` (ip, len: 39) — ""

##### 19_-_LOG_ID_TRAFFIC_BROADCAST
- Field added: `srcremote` (ip, len: 39) — ""

##### 20_-_LOG_ID_TRAFFIC_STAT
- Field added: `srcremote` (ip, len: 39) — ""

##### 21_-_LOG_ID_TRAFFIC_SNIFFER_STAT
- Field added: `srcremote` (ip, len: 39) — ""

##### 22_-_LOG_ID_TRAFFIC_UTM_CORRELATION
- Field added: `srcremote` (ip, len: 39) — ""

##### 24_-_LOG_ID_TRAFFIC_ZTNA
- Field added: `srcremote` (ip, len: 39) — ""

##### 2_-_LOG_ID_TRAFFIC_ALLOW
- Field added: `srcremote` (ip, len: 39) — ""

##### 3_-_LOG_ID_TRAFFIC_DENY
- Field added: `srcremote` (ip, len: 39) — ""

##### 4_-_LOG_ID_TRAFFIC_OTHER_START
- Field added: `srcremote` (ip, len: 39) — ""

##### 5_-_LOG_ID_TRAFFIC_OTHER_ICMP_ALLOW
- Field added: `srcremote` (ip, len: 39) — ""

##### 6_-_LOG_ID_TRAFFIC_OTHER_ICMP_DENY
- Field added: `srcremote` (ip, len: 39) — ""

##### 7_-_LOG_ID_TRAFFIC_OTHER_INVALID
- Field added: `srcremote` (ip, len: 39) — ""

##### 8_-_LOG_ID_TRAFFIC_WANOPT
- Field added: `srcremote` (ip, len: 39) — ""

##### 9_-_LOG_ID_TRAFFIC_WEBCACHE
- Field added: `srcremote` (ip, len: 39) — ""

#### Event

##### 22024_-_LOG_ID_IPPOOLPBA_INTERIM *(new)*

##### 22070_-_LOG_ID_FORTIGSLB_COMMUNICATION_ERROR *(new)*

##### 22071_-_LOG_ID_FORTIGSLB_CLOUD_CONFIG_UPDATED *(new)*

##### 22224_-_LOG_ID_EXT_RESOURCE_OVERFLOW *(new)*

##### 22750_-_LOG_ID_METERED_BILLING_ACCEPTED *(new)*

##### 22751_-_LOG_ID_METERED_BILLING_FAIL *(new)*

##### 22752_-_LOG_ID_METERED_BILLING_VALID *(new)*

##### 22753_-_LOG_ID_METERED_BILLING_INVALID *(new)*

##### 32618_-_LOG_ID_FGT_SWITCH_EXPORT_POOL_UNDO *(new)*

##### 32619_-_LOG_ID_FGT_SWITCH_EXPORT_VDOM_UNDO *(new)*

##### 32620_-_LOG_ID_FGT_SWITCH_GROUP_ADD_MEMBER *(new)*

##### 32621_-_LOG_ID_FGT_SWITCH_GROUP_DEL_MEMBER *(new)*

##### 32622_-_LOG_ID_FGT_SWITCH_FORTILINK_CONNECTED *(new)*

##### 32623_-_LOG_ID_FGT_SWITCH_LOCATION_CHANGE *(new)*

##### 32624_-_LOG_ID_FGT_SWITCH_NEW_PEER_DETECT *(new)*

##### 43720_-_LOG_ID_EVENT_WIRELESS_FIPS *(new)*

##### 43721_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_EXT_MPSK_RESULT *(new)*

##### 43778_-_LOG_ID_EVENT_NAC_QUARANTINE_EXPIRY *(new)*

##### 53010_-_LOG_ID_INTERNAL_FDS_FTC *(new)*

#### UTM

##### 9241_-_LOG_ID_UNKNOWN_CE_BLOCK *(new)*

##### 9242_-_LOG_ID_UNKNOWN_CE_BYPASS *(new)*

##### 13696_-_LOG_ID_UNKNOWN_CE_BLOCK *(removed)*

##### 13697_-_LOG_ID_UNKNOWN_CE_BYPASS *(removed)*

##### 10000_-_LOG_ID_CASB_ACCESS_BLOCKED
- Field added: `operation` (string, len: 80) — ""
- Field added: `policytype` (string, len: 24) — ""

##### 10001_-_LOG_ID_CASB_ACCESS_BYPASS
- Field added: `operation` (string, len: 80) — ""
- Field added: `policytype` (string, len: 24) — ""

##### 10002_-_LOG_ID_CASB_ACCESS_MONITOR
- Field added: `operation` (string, len: 80) — ""
- Field added: `policytype` (string, len: 24) — ""

##### 13632_-_LOGID_HTTP_HDR_CHG_REQ
- Field added: `action` (string, len: 11) — "Security action performed by WF:  blocked - url is blocked by webfilter  passthrough - url is allowed by webfilter"

##### 13633_-_LOGID_HTTP_HDR_CHG_RESP
- Field added: `action` (string, len: 11) — "Security action performed by WF:  blocked - url is blocked by webfilter  passthrough - url is allowed by webfilter"

##### 13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK
- Field added: `policytype` (string, len: 24) — ""

##### 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR
- Field added: `policytype` (string, len: 24) — ""

##### 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW
- Field added: `policytype` (string, len: 24) — ""

##### 13680_-_LOG_ID_VIDEOFILTER_CHANNEL_BLOCK
- Field added: `policytype` (string, len: 24) — ""

##### 13681_-_LOG_ID_VIDEOFILTER_CHANNEL_MONITOR
- Field added: `policytype` (string, len: 24) — ""

##### 13682_-_LOG_ID_VIDEOFILTER_CHANNEL_ALLOW
- Field added: `policytype` (string, len: 24) — ""

##### 13712_-_LOG_ID_VIDEOFILTER_TITLE_BLOCK
- Field added: `policytype` (string, len: 24) — ""

##### 13713_-_LOG_ID_VIDEOFILTER_TITLE_MONITOR
- Field added: `policytype` (string, len: 24) — ""

##### 13714_-_LOG_ID_VIDEOFILTER_TITLE_ALLOW
- Field added: `policytype` (string, len: 24) — ""

##### 13728_-_LOG_ID_VIDEOFILTER_DESCRIPTION_BLOCK
- Field added: `policytype` (string, len: 24) — ""

##### 13729_-_LOG_ID_VIDEOFILTER_DESCRIPTION_MONITOR
- Field added: `policytype` (string, len: 24) — ""

##### 13730_-_LOG_ID_VIDEOFILTER_DESCRIPTION_ALLOW
- Field added: `policytype` (string, len: 24) — ""

##### 8720_-_MESGID_SWITCH_PROTO_WARNING
- Description changed: `switchproto`
  - Before: "Protocol used on the switch"
  - After:  ""

##### 8721_-_MESGID_SWITCH_PROTO_NOTIF
- Description changed: `switchproto`
  - Before: "Protocol used on the switch"
  - After:  ""

---

### 7.4.4 → 7.4.5

**Summary:** 8 LOGID added, 0 removed | 6 fields added, 0 removed | 0 type changed | 0 descriptions changed | 0 lengths changed

#### Traffic

*(no changes)*

#### Event

##### 22905_-_LOG_ID_LOGDEV_STATUS_CHANGE *(new)*

##### 22906_-_LOG_ID_SECURITY_LEVEL_CHANGE *(new)*

##### 46527_-_LOG_ID_INTERNAL_LTE_MODEM_SIM_SWITCH_SIM_STATE *(new)*

##### 53050_-_LOG_ID_FTC_AUTH_FAILED *(new)*

##### 53402_-_LOG_ID_FGFM_RECOVERY *(new)*

##### 53407_-_LOG_ID_FABRIC_VPN_PSK_SECRET_UPG_SET *(new)*

#### UTM

##### 61014_-_LOG_ID_SSH_UNSUPPORT_PROTO_BLOCK *(new)*

##### 61015_-_LOG_ID_SSH_UNSUPPORT_PROTO_PASS *(new)*

##### 41231_-_LOGID_PFCP_FORWARD
- Field added: `end-usr-address` (ip, len: 39) — "End user IP Address"
- Field added: `endusraddress6` (ip, len: 39) — ""

##### 41232_-_LOGID_PFCP_DENY
- Field added: `end-usr-address` (ip, len: 39) — "End user IP Address"
- Field added: `endusraddress6` (ip, len: 39) — ""

##### 41233_-_LOGID_PFCP_TRAFFIC_COUNT
- Field added: `end-usr-address` (ip, len: 39) — "End user IP Address"
- Field added: `endusraddress6` (ip, len: 39) — ""

---

### 7.4.5 → 7.4.6

**Summary:** 2 LOGID added, 0 removed | 4 fields added, 0 removed | 0 type changed | 0 descriptions changed | 0 lengths changed

#### Traffic

*(no changes)*

#### Event

##### 22907_-_LOG_ID_INPUT_DETECTION *(new)*

##### 22908_-_LOG_ID_OUTPUT_DETECTION *(new)*

#### UTM

##### 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK
- Field added: `attack` (string, len: 256) — ""
- Field added: `attackid` (uint32, len: 10) — ""

##### 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING
- Field added: `attack` (string, len: 256) — ""
- Field added: `attackid` (uint32, len: 10) — ""

---

### 7.4.6 → 7.4.7

*(no changes)*

---

### 7.4.7 → 7.4.8

**Summary:** 11 LOGID added, 0 removed | 0 fields added, 0 removed | 0 type changed | 0 descriptions changed | 7 lengths changed

#### Traffic

*(no changes)*

#### Event

##### 32625_-_LOG_ID_FGT_SWITCH_IMG_VERIFICATION *(new)*

##### 32701_-_LOG_ID_FGT_INTF_IP_CONFLICT *(new)*

##### 43723_-_LOG_ID_EVENT_WIRELESS_SYS_AC_DOWN *(new)*

##### 44559_-_LOGID_EVENT_INSTALL_IPROPE *(new)*

##### 46703_-_LOG_ID_INTERNAL_5G_MODEM_IPV4_LINK_STATE *(new)*

##### 46705_-_LOG_ID_INTERNAL_5G_MODEM_FW_UPGRADE *(new)*

##### 46708_-_LOG_ID_INTERNAL_5G_MODEM_MODE *(new)*

##### 46709_-_LOG_ID_INTERNAL_5G_MODEM_SIM_STATE *(new)*

##### 46710_-_LOG_ID_INTERNAL_5G_MODEM_SIM_SWITCH *(new)*

##### 46711_-_LOG_ID_INTERNAL_5G_MODEM_AUTO_SIM_SWITCH_REASON *(new)*

##### 46713_-_LOG_ID_INTERNAL_5G_MODEM_SIGNAL_MODE *(new)*

##### 22800_-_LOG_ID_SCAN_SERV_FAIL
- Length changed: `mode` 12 → 32

##### 22907_-_LOG_ID_INPUT_DETECTION
- Length changed: `mode` 12 → 32

##### 22938_-_LOG_ID_EVENT_VWL_WAN_SPEEDTEST_RESULT
- Length changed: `mode` 12 → 32

##### 37127_-_MESGID_NEG_PROGRESS_P1_NOTIF
- Length changed: `mode` 12 → 32

##### 37128_-_MESGID_NEG_PROGRESS_P1_ERROR
- Length changed: `mode` 12 → 32

##### 37129_-_MESGID_NEG_PROGRESS_P2_NOTIF
- Length changed: `mode` 12 → 32

##### 37130_-_MESGID_NEG_PROGRESS_P2_ERROR
- Length changed: `mode` 12 → 32

#### UTM

*(no changes)*

---

### 7.4.8 → 7.4.9

**Summary:** 3 LOGID added, 0 removed | 0 fields added, 2 removed | 0 type changed | 0 descriptions changed | 0 lengths changed

#### Traffic

*(no changes)*

#### Event

##### 22118_-_LOG_ID_HW_MONITOR_EMERGENCY *(new)*

##### 22119_-_LOG_ID_HW_MONITOR_WARNING *(new)*

##### 22120_-_LOG_ID_HW_MONITOR_NOTIF *(new)*

#### UTM

##### 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK
- Field removed: `attack` (string)
- Field removed: `attackid` (uint32)

---

### 7.4.9 → 7.4.10

**Summary:** 6 LOGID added, 0 removed | 2 fields added, 0 removed | 0 type changed | 0 descriptions changed | 0 lengths changed

#### Traffic

*(no changes)*

#### Event

##### 20262_-_LOG_ID_SYS_SECURITY_WEB_SVC_EVAL_VIOLATION *(new)*

##### 38420_-_LOGID_EVENT_HTTPS_CONNECTION_ERROR *(new)*

##### 44558_-_LOGID_EVENT_NEWCLI_SPAWN_ATTEMPT *(new)*

##### 47400_-_LOG_ID_WEB_SVC_MEMORY_PROFILE *(new)*

##### 47401_-_LOG_ID_WEB_SVC_RESTART *(new)*

##### 52002_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_RESULT *(new)*

#### UTM

##### 44032_-_LOGID_EVENT_VOIP_SIP
- Field added: `attack` (string, len: 256) — ""
- Field added: `attackid` (uint32, len: 10) — ""

---

### 7.4.10 → 7.4.11

*(no changes)*

---


## 7.6

### 7.6.0 → 7.6.1

**Summary:** 22 LOGID added, 1 removed | 189 fields added, 2 removed | 215 type changed | 0 descriptions changed | 0 lengths changed

#### Traffic

##### 10_-_LOG_ID_TRAFFIC_EXPLICIT_PROXY
- Field added: `tcpnrt` (uint32, len: 10) — ""
- Field added: `tcporgrtrs` (uint32, len: 10) — ""
- Field added: `tcprplrtrs` (uint32, len: 10) — ""
- Field added: `tcprst` (string, len: 6) — ""
- Field added: `tcpsrt` (uint32, len: 10) — ""
- Field added: `tcpsynackrtrs` (uint32, len: 10) — ""
- Field added: `tcpsynrtrs` (uint32, len: 10) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 11_-_LOG_ID_TRAFFIC_FAIL_CONN
- Field added: `tcpnrt` (uint32, len: 10) — ""
- Field added: `tcporgrtrs` (uint32, len: 10) — ""
- Field added: `tcprplrtrs` (uint32, len: 10) — ""
- Field added: `tcprst` (string, len: 6) — ""
- Field added: `tcpsrt` (uint32, len: 10) — ""
- Field added: `tcpsynackrtrs` (uint32, len: 10) — ""
- Field added: `tcpsynrtrs` (uint32, len: 10) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 12_-_LOG_ID_TRAFFIC_MULTICAST
- Field added: `tcpnrt` (uint32, len: 10) — ""
- Field added: `tcporgrtrs` (uint32, len: 10) — ""
- Field added: `tcprplrtrs` (uint32, len: 10) — ""
- Field added: `tcprst` (string, len: 6) — ""
- Field added: `tcpsrt` (uint32, len: 10) — ""
- Field added: `tcpsynackrtrs` (uint32, len: 10) — ""
- Field added: `tcpsynrtrs` (uint32, len: 10) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 13_-_LOG_ID_TRAFFIC_END_FORWARD
- Field added: `tcpnrt` (uint32, len: 10) — ""
- Field added: `tcporgrtrs` (uint32, len: 10) — ""
- Field added: `tcprplrtrs` (uint32, len: 10) — ""
- Field added: `tcprst` (string, len: 6) — ""
- Field added: `tcpsrt` (uint32, len: 10) — ""
- Field added: `tcpsynackrtrs` (uint32, len: 10) — ""
- Field added: `tcpsynrtrs` (uint32, len: 10) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 14_-_LOG_ID_TRAFFIC_END_LOCAL
- Field added: `tcpnrt` (uint32, len: 10) — ""
- Field added: `tcporgrtrs` (uint32, len: 10) — ""
- Field added: `tcprplrtrs` (uint32, len: 10) — ""
- Field added: `tcprst` (string, len: 6) — ""
- Field added: `tcpsrt` (uint32, len: 10) — ""
- Field added: `tcpsynackrtrs` (uint32, len: 10) — ""
- Field added: `tcpsynrtrs` (uint32, len: 10) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 15_-_LOG_ID_TRAFFIC_START_FORWARD
- Field added: `tcpnrt` (uint32, len: 10) — ""
- Field added: `tcporgrtrs` (uint32, len: 10) — ""
- Field added: `tcprplrtrs` (uint32, len: 10) — ""
- Field added: `tcprst` (string, len: 6) — ""
- Field added: `tcpsrt` (uint32, len: 10) — ""
- Field added: `tcpsynackrtrs` (uint32, len: 10) — ""
- Field added: `tcpsynrtrs` (uint32, len: 10) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 16_-_LOG_ID_TRAFFIC_START_LOCAL
- Field added: `tcpnrt` (uint32, len: 10) — ""
- Field added: `tcporgrtrs` (uint32, len: 10) — ""
- Field added: `tcprplrtrs` (uint32, len: 10) — ""
- Field added: `tcprst` (string, len: 6) — ""
- Field added: `tcpsrt` (uint32, len: 10) — ""
- Field added: `tcpsynackrtrs` (uint32, len: 10) — ""
- Field added: `tcpsynrtrs` (uint32, len: 10) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 17_-_LOG_ID_TRAFFIC_SNIFFER
- Field added: `tcpnrt` (uint32, len: 10) — ""
- Field added: `tcporgrtrs` (uint32, len: 10) — ""
- Field added: `tcprplrtrs` (uint32, len: 10) — ""
- Field added: `tcprst` (string, len: 6) — ""
- Field added: `tcpsrt` (uint32, len: 10) — ""
- Field added: `tcpsynackrtrs` (uint32, len: 10) — ""
- Field added: `tcpsynrtrs` (uint32, len: 10) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 19_-_LOG_ID_TRAFFIC_BROADCAST
- Field added: `tcpnrt` (uint32, len: 10) — ""
- Field added: `tcporgrtrs` (uint32, len: 10) — ""
- Field added: `tcprplrtrs` (uint32, len: 10) — ""
- Field added: `tcprst` (string, len: 6) — ""
- Field added: `tcpsrt` (uint32, len: 10) — ""
- Field added: `tcpsynackrtrs` (uint32, len: 10) — ""
- Field added: `tcpsynrtrs` (uint32, len: 10) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 20_-_LOG_ID_TRAFFIC_STAT
- Field added: `tcpnrt` (uint32, len: 10) — ""
- Field added: `tcporgrtrs` (uint32, len: 10) — ""
- Field added: `tcprplrtrs` (uint32, len: 10) — ""
- Field added: `tcprst` (string, len: 6) — ""
- Field added: `tcpsrt` (uint32, len: 10) — ""
- Field added: `tcpsynackrtrs` (uint32, len: 10) — ""
- Field added: `tcpsynrtrs` (uint32, len: 10) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 21_-_LOG_ID_TRAFFIC_SNIFFER_STAT
- Field added: `tcpnrt` (uint32, len: 10) — ""
- Field added: `tcporgrtrs` (uint32, len: 10) — ""
- Field added: `tcprplrtrs` (uint32, len: 10) — ""
- Field added: `tcprst` (string, len: 6) — ""
- Field added: `tcpsrt` (uint32, len: 10) — ""
- Field added: `tcpsynackrtrs` (uint32, len: 10) — ""
- Field added: `tcpsynrtrs` (uint32, len: 10) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 22_-_LOG_ID_TRAFFIC_UTM_CORRELATION
- Field added: `tcpnrt` (uint32, len: 10) — ""
- Field added: `tcporgrtrs` (uint32, len: 10) — ""
- Field added: `tcprplrtrs` (uint32, len: 10) — ""
- Field added: `tcprst` (string, len: 6) — ""
- Field added: `tcpsrt` (uint32, len: 10) — ""
- Field added: `tcpsynackrtrs` (uint32, len: 10) — ""
- Field added: `tcpsynrtrs` (uint32, len: 10) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 24_-_LOG_ID_TRAFFIC_ZTNA
- Field added: `tcpnrt` (uint32, len: 10) — ""
- Field added: `tcporgrtrs` (uint32, len: 10) — ""
- Field added: `tcprplrtrs` (uint32, len: 10) — ""
- Field added: `tcprst` (string, len: 6) — ""
- Field added: `tcpsrt` (uint32, len: 10) — ""
- Field added: `tcpsynackrtrs` (uint32, len: 10) — ""
- Field added: `tcpsynrtrs` (uint32, len: 10) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 26_-_LOG_ID_TRAFFIC_HTTP_TRANSACTION
- Field added: `countapp` (uint32, len: 10) — "Number of App Ctrl logs associated with the session"
- Field added: `countav` (uint32, len: 10) — "Number of AV logs associated with the session"
- Field added: `countcasb` (uint32, len: 10) — ""
- Field added: `countcifs` (uint32, len: 10) — ""
- Field added: `countdlp` (uint32, len: 10) — "Number of DLP logs associated with the session"
- Field added: `countdns` (uint32, len: 10) — "Number of DNS Query logs associated with the session"
- Field added: `countemail` (uint32, len: 10) — "Number of Email logs associated with the session"
- Field added: `countff` (uint32, len: 10) — ""
- Field added: `counticap` (uint32, len: 10) — ""
- Field added: `countips` (uint32, len: 10) — "Number of IPS logs associated with the session"
- Field added: `countsctpf` (uint32, len: 10) — ""
- Field added: `countssh` (uint32, len: 10) — "Number of SSH logs associated with the session"
- Field added: `countssl` (uint32, len: 10) — ""
- Field added: `countvpatch` (uint32, len: 10) — ""
- Field added: `countwaf` (uint32, len: 10) — "Number of WAF logs associated with the session"
- Field added: `countweb` (uint32, len: 10) — "Number of Web Filter logs associated with the session"

##### 2_-_LOG_ID_TRAFFIC_ALLOW
- Field added: `tcpnrt` (uint32, len: 10) — ""
- Field added: `tcporgrtrs` (uint32, len: 10) — ""
- Field added: `tcprplrtrs` (uint32, len: 10) — ""
- Field added: `tcprst` (string, len: 6) — ""
- Field added: `tcpsrt` (uint32, len: 10) — ""
- Field added: `tcpsynackrtrs` (uint32, len: 10) — ""
- Field added: `tcpsynrtrs` (uint32, len: 10) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 3_-_LOG_ID_TRAFFIC_DENY
- Field added: `tcpnrt` (uint32, len: 10) — ""
- Field added: `tcporgrtrs` (uint32, len: 10) — ""
- Field added: `tcprplrtrs` (uint32, len: 10) — ""
- Field added: `tcprst` (string, len: 6) — ""
- Field added: `tcpsrt` (uint32, len: 10) — ""
- Field added: `tcpsynackrtrs` (uint32, len: 10) — ""
- Field added: `tcpsynrtrs` (uint32, len: 10) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 4_-_LOG_ID_TRAFFIC_OTHER_START
- Field added: `tcpnrt` (uint32, len: 10) — ""
- Field added: `tcporgrtrs` (uint32, len: 10) — ""
- Field added: `tcprplrtrs` (uint32, len: 10) — ""
- Field added: `tcprst` (string, len: 6) — ""
- Field added: `tcpsrt` (uint32, len: 10) — ""
- Field added: `tcpsynackrtrs` (uint32, len: 10) — ""
- Field added: `tcpsynrtrs` (uint32, len: 10) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 5_-_LOG_ID_TRAFFIC_OTHER_ICMP_ALLOW
- Field added: `tcpnrt` (uint32, len: 10) — ""
- Field added: `tcporgrtrs` (uint32, len: 10) — ""
- Field added: `tcprplrtrs` (uint32, len: 10) — ""
- Field added: `tcprst` (string, len: 6) — ""
- Field added: `tcpsrt` (uint32, len: 10) — ""
- Field added: `tcpsynackrtrs` (uint32, len: 10) — ""
- Field added: `tcpsynrtrs` (uint32, len: 10) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 6_-_LOG_ID_TRAFFIC_OTHER_ICMP_DENY
- Field added: `tcpnrt` (uint32, len: 10) — ""
- Field added: `tcporgrtrs` (uint32, len: 10) — ""
- Field added: `tcprplrtrs` (uint32, len: 10) — ""
- Field added: `tcprst` (string, len: 6) — ""
- Field added: `tcpsrt` (uint32, len: 10) — ""
- Field added: `tcpsynackrtrs` (uint32, len: 10) — ""
- Field added: `tcpsynrtrs` (uint32, len: 10) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 7_-_LOG_ID_TRAFFIC_OTHER_INVALID
- Field added: `tcpnrt` (uint32, len: 10) — ""
- Field added: `tcporgrtrs` (uint32, len: 10) — ""
- Field added: `tcprplrtrs` (uint32, len: 10) — ""
- Field added: `tcprst` (string, len: 6) — ""
- Field added: `tcpsrt` (uint32, len: 10) — ""
- Field added: `tcpsynackrtrs` (uint32, len: 10) — ""
- Field added: `tcpsynrtrs` (uint32, len: 10) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 8_-_LOG_ID_TRAFFIC_WANOPT
- Field added: `tcpnrt` (uint32, len: 10) — ""
- Field added: `tcporgrtrs` (uint32, len: 10) — ""
- Field added: `tcprplrtrs` (uint32, len: 10) — ""
- Field added: `tcprst` (string, len: 6) — ""
- Field added: `tcpsrt` (uint32, len: 10) — ""
- Field added: `tcpsynackrtrs` (uint32, len: 10) — ""
- Field added: `tcpsynrtrs` (uint32, len: 10) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 9_-_LOG_ID_TRAFFIC_WEBCACHE
- Field added: `tcpnrt` (uint32, len: 10) — ""
- Field added: `tcporgrtrs` (uint32, len: 10) — ""
- Field added: `tcprplrtrs` (uint32, len: 10) — ""
- Field added: `tcprst` (string, len: 6) — ""
- Field added: `tcpsrt` (uint32, len: 10) — ""
- Field added: `tcpsynackrtrs` (uint32, len: 10) — ""
- Field added: `tcpsynrtrs` (uint32, len: 10) — ""
- Type changed: `vrf` `uint8` → `uint16`

#### Event

##### 22818_-_LOG_ID_SCANUNIT_DLP_BUILDER_TIMEOUT *(new)*

##### 22906_-_LOG_ID_SECURITY_LEVEL_CHANGE *(new)*

##### 22907_-_LOG_ID_INPUT_DETECTION *(new)*

##### 22908_-_LOG_ID_OUTPUT_DETECTION *(new)*

##### 22957_-_LOG_ID_SANDBOX_CLOUD_ERRCON *(new)*

##### 32310_-_LOG_ID_USB_DEVICE_DETECTED *(new)*

##### 32311_-_LOG_ID_USB_DEVICE_MOUNTED *(new)*

##### 32312_-_LOG_ID_USB_DEVICE_EJECTED *(new)*

##### 32625_-_LOG_ID_FGT_SWITCH_IMG_VERIFICATION *(new)*

##### 37142_-_MESGID_TRANSPORT_SWITCH *(new)*

##### 43536_-_LOG_ID_EVENT_WIRELESS_WIDS_GENERAL *(new)*

##### 43537_-_LOG_ID_EVENT_WIRELESS_WIDS_RISKY_ENCRYPTION *(new)*

##### 43538_-_LOG_ID_EVENT_WIRELESS_WIDS_VALID_STA_MISASSOC *(new)*

##### 43723_-_LOG_ID_EVENT_WIRELESS_SYS_AC_DOWN *(new)*

##### 45134_-_LOG_ID_EC_SHM_ENDPOINT_UPDATE *(new)*

##### 45135_-_LOG_ID_EC_SHM_ENDPOINT_DELETE *(new)*

##### 46527_-_LOG_ID_INTERNAL_LTE_MODEM_SIM_SWITCH_SIM_STATE *(new)*

##### 53407_-_LOG_ID_FABRIC_VPN_PSK_SECRET_UPG_SET *(new)*

##### 40708_-_LOG_ID_EVENT_SYS_FTGD_RESOURCE_FAIL *(removed)*

##### 20007_-_LOG_ID_SOCKET_EXHAUSTED
- Type changed: `vrf` `uint8` → `uint16`

##### 32119_-_LOG_ID_UPD_SCANUNIT_AV_DB
- Field removed: `ui` (string)
- Field removed: `user` (string)

##### 43025_-_LOG_ID_EVENT_AUTH_PROXY_SUCCESS
- Field added: `url` (string, len: 512) — "URL"

##### 43026_-_LOG_ID_EVENT_AUTH_PROXY_FAILED
- Field added: `url` (string, len: 512) — "URL"

##### 43028_-_LOG_ID_EVENT_AUTH_PROXY_GROUP_INFO_FAILED
- Field added: `url` (string, len: 512) — "URL"

##### 43032_-_LOG_ID_EVENT_AUTH_PROXY_USER_LIMIT_REACHED
- Field added: `url` (string, len: 512) — "URL"

##### 43033_-_LOG_ID_EVENT_AUTH_PROXY_MULTIPLE_LOGIN
- Field added: `url` (string, len: 512) — "URL"

#### UTM

##### 13058_-_LOG_ID_WEB_FTGD_RISK_BLK *(new)*

##### 13313_-_LOG_ID_WEB_FTGD_RISK_ALLOW *(new)*

##### 61014_-_LOG_ID_SSH_UNSUPPORT_PROTO_BLOCK *(new)*

##### 61015_-_LOG_ID_SSH_UNSUPPORT_PROTO_PASS *(new)*

##### 10000_-_LOG_ID_CASB_ACCESS_BLOCKED
- Field added: `subaction` (string, len: 80) — ""
- Field added: `tenantmatch` (string, len: 80) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 10001_-_LOG_ID_CASB_ACCESS_BYPASS
- Field added: `subaction` (string, len: 80) — ""
- Field added: `tenantmatch` (string, len: 80) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 10002_-_LOG_ID_CASB_ACCESS_MONITOR
- Field added: `subaction` (string, len: 80) — ""
- Field added: `tenantmatch` (string, len: 80) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 12288_-_LOG_ID_WEB_CONTENT_BANWORD
- Type changed: `vrf` `uint8` → `uint16`

##### 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD
- Type changed: `vrf` `uint8` → `uint16`

##### 12292_-_LOG_ID_WEB_CONTENT_KEYWORD
- Type changed: `vrf` `uint8` → `uint16`

##### 12293_-_LOG_ID_WEB_CONTENT_SEARCH
- Type changed: `vrf` `uint8` → `uint16`

##### 12544_-_LOG_ID_URL_FILTER_BLOCK
- Type changed: `vrf` `uint8` → `uint16`

##### 12545_-_LOG_ID_URL_FILTER_EXEMPT
- Type changed: `vrf` `uint8` → `uint16`

##### 12546_-_LOG_ID_URL_FILTER_ALLOW
- Type changed: `vrf` `uint8` → `uint16`

##### 12547_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_HTTP_BLK
- Type changed: `vrf` `uint8` → `uint16`

##### 12548_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_HTTPS_BLK
- Type changed: `vrf` `uint8` → `uint16`

##### 12549_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_HTTP_PASS
- Type changed: `vrf` `uint8` → `uint16`

##### 12550_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_HTTPS_PASS
- Type changed: `vrf` `uint8` → `uint16`

##### 12551_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_SNI_BLK
- Type changed: `vrf` `uint8` → `uint16`

##### 12552_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_SNI_PASS
- Type changed: `vrf` `uint8` → `uint16`

##### 12553_-_LOG_ID_URL_FILTER_INVALID_CERT
- Type changed: `vrf` `uint8` → `uint16`

##### 12554_-_LOG_ID_URL_FILTER_INVALID_SESSION
- Type changed: `vrf` `uint8` → `uint16`

##### 12555_-_LOG_ID_URL_FILTER_SRV_CERT_ERR_BLK
- Type changed: `vrf` `uint8` → `uint16`

##### 12556_-_LOG_ID_URL_FILTER_SRV_CERT_ERR_PASS
- Type changed: `vrf` `uint8` → `uint16`

##### 12559_-_LOG_ID_URL_FILTER_PASS
- Type changed: `vrf` `uint8` → `uint16`

##### 12560_-_LOG_ID_URL_WISP_BLOCK
- Type changed: `vrf` `uint8` → `uint16`

##### 12561_-_LOG_ID_URL_WISP_REDIR
- Type changed: `vrf` `uint8` → `uint16`

##### 12562_-_LOG_ID_URL_WISP_ALLOW
- Type changed: `vrf` `uint8` → `uint16`

##### 12688_-_LOG_ID_WEB_SSL_EXEMPT
- Field added: `urlrisk` (uint8, len: 3) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 12800_-_LOG_ID_WEB_FTGD_ERR
- Type changed: `vrf` `uint8` → `uint16`

##### 12801_-_LOG_ID_WEB_FTGD_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 13056_-_LOG_ID_WEB_FTGD_CAT_BLK
- Field added: `urlrisk` (uint8, len: 3) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 13057_-_LOG_ID_WEB_FTGD_CAT_WARN
- Field added: `urlrisk` (uint8, len: 3) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 13312_-_LOG_ID_WEB_FTGD_CAT_ALLOW
- Field added: `urlrisk` (uint8, len: 3) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 13315_-_LOG_ID_WEB_FTGD_QUOTA_COUNTING
- Field added: `urlrisk` (uint8, len: 3) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 13316_-_LOG_ID_WEB_FTGD_QUOTA_EXPIRED
- Field added: `urlrisk` (uint8, len: 3) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 13317_-_LOG_ID_WEB_URL
- Field added: `urlrisk` (uint8, len: 3) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 13318_-_LOG_ID_WEB_DOMAIN_FRONTING
- Type changed: `vrf` `uint8` → `uint16`

##### 13568_-_LOG_ID_WEB_SCRIPTFILTER_ACTIVEX
- Type changed: `vrf` `uint8` → `uint16`

##### 13573_-_LOG_ID_WEB_SCRIPTFILTER_COOKIE
- Type changed: `vrf` `uint8` → `uint16`

##### 13584_-_LOG_ID_WEB_SCRIPTFILTER_APPLET
- Type changed: `vrf` `uint8` → `uint16`

##### 13600_-_LOG_ID_WEB_SCRIPTFILTER_OTHER
- Type changed: `vrf` `uint8` → `uint16`

##### 13601_-_LOG_ID_WEB_WF_COOKIE
- Type changed: `vrf` `uint8` → `uint16`

##### 13602_-_LOG_ID_WEB_WF_REFERER
- Type changed: `vrf` `uint8` → `uint16`

##### 13603_-_LOG_ID_WEB_WF_COMMAND_BLOCK
- Type changed: `vrf` `uint8` → `uint16`

##### 13616_-_LOG_ID_CONTENT_TYPE_BLOCK
- Type changed: `vrf` `uint8` → `uint16`

##### 13617_-_LOG_ID_CONTENT_TYPE_EXEMPT
- Type changed: `vrf` `uint8` → `uint16`

##### 13648_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_URL_ALLOW
- Type changed: `vrf` `uint8` → `uint16`

##### 13649_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_FTGD_ALLOW
- Type changed: `vrf` `uint8` → `uint16`

##### 13650_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_DEFAULT_ALLOW
- Type changed: `vrf` `uint8` → `uint16`

##### 13651_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_URL_BLOCK
- Type changed: `vrf` `uint8` → `uint16`

##### 13652_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_FTGD_BLOCK
- Type changed: `vrf` `uint8` → `uint16`

##### 13653_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_DEFAULT_BLOCK
- Type changed: `vrf` `uint8` → `uint16`

##### 13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK
- Type changed: `vrf` `uint8` → `uint16`

##### 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR
- Type changed: `vrf` `uint8` → `uint16`

##### 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW
- Type changed: `vrf` `uint8` → `uint16`

##### 13680_-_LOG_ID_VIDEOFILTER_CHANNEL_BLOCK
- Type changed: `vrf` `uint8` → `uint16`

##### 13681_-_LOG_ID_VIDEOFILTER_CHANNEL_MONITOR
- Type changed: `vrf` `uint8` → `uint16`

##### 13682_-_LOG_ID_VIDEOFILTER_CHANNEL_ALLOW
- Type changed: `vrf` `uint8` → `uint16`

##### 13712_-_LOG_ID_VIDEOFILTER_TITLE_BLOCK
- Type changed: `vrf` `uint8` → `uint16`

##### 13713_-_LOG_ID_VIDEOFILTER_TITLE_MONITOR
- Type changed: `vrf` `uint8` → `uint16`

##### 13714_-_LOG_ID_VIDEOFILTER_TITLE_ALLOW
- Type changed: `vrf` `uint8` → `uint16`

##### 13728_-_LOG_ID_VIDEOFILTER_DESCRIPTION_BLOCK
- Type changed: `vrf` `uint8` → `uint16`

##### 13729_-_LOG_ID_VIDEOFILTER_DESCRIPTION_MONITOR
- Type changed: `vrf` `uint8` → `uint16`

##### 13730_-_LOG_ID_VIDEOFILTER_DESCRIPTION_ALLOW
- Type changed: `vrf` `uint8` → `uint16`

##### 16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP
- Type changed: `vrf` `uint8` → `uint16`

##### 16385_-_LOGID_ATTCK_SIGNATURE_ICMP
- Type changed: `vrf` `uint8` → `uint16`

##### 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS
- Type changed: `vrf` `uint8` → `uint16`

##### 16399_-_LOGID_ATTACK_MALICIOUS_URL
- Type changed: `vrf` `uint8` → `uint16`

##### 16400_-_LOGID_ATTACK_BOTNET_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 16401_-_LOGID_ATTACK_BOTNET_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP
- Type changed: `vrf` `uint8` → `uint16`

##### 18433_-_LOGID_ATTCK_ANOMALY_ICMP
- Type changed: `vrf` `uint8` → `uint16`

##### 18434_-_LOGID_ATTCK_ANOMALY_OTHERS
- Type changed: `vrf` `uint8` → `uint16`

##### 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 20481_-_LOGID_EMAIL_GENERAL_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 20509_-_LOGID_ANTISPAM_FTGD_ERR
- Type changed: `vrf` `uint8` → `uint16`

##### 20510_-_LOGID_ANTISPAM_EMAIL_WEBMAIL_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 24576_-_LOG_ID_DLP_WARN
- Type changed: `vrf` `uint8` → `uint16`

##### 24577_-_LOG_ID_DLP_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 28672_-_LOGID_APP_CTRL_IM_BASIC
- Type changed: `vrf` `uint8` → `uint16`

##### 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS
- Type changed: `vrf` `uint8` → `uint16`

##### 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT
- Type changed: `vrf` `uint8` → `uint16`

##### 28675_-_LOGID_APP_CTRL_IM_FILE
- Type changed: `vrf` `uint8` → `uint16`

##### 28676_-_LOGID_APP_CTRL_IM_CHAT
- Type changed: `vrf` `uint8` → `uint16`

##### 28677_-_LOGID_APP_CTRL_IM_CHAT_BLOCK
- Type changed: `vrf` `uint8` → `uint16`

##### 28678_-_LOGID_APP_CTRL_IM_BLOCK
- Type changed: `vrf` `uint8` → `uint16`

##### 28704_-_LOGID_APP_CTRL_IPS_PASS
- Type changed: `vrf` `uint8` → `uint16`

##### 28705_-_LOGID_APP_CTRL_IPS_BLOCK
- Type changed: `vrf` `uint8` → `uint16`

##### 28706_-_LOGID_APP_CTRL_IPS_RESET
- Type changed: `vrf` `uint8` → `uint16`

##### 28720_-_LOGID_APP_CTRL_SSH_PASS
- Type changed: `vrf` `uint8` → `uint16`

##### 28721_-_LOGID_APP_CTRL_SSH_BLOCK
- Type changed: `vrf` `uint8` → `uint16`

##### 28736_-_LOGID_APP_CTRL_PORT_ENF
- Type changed: `vrf` `uint8` → `uint16`

##### 28737_-_LOGID_APP_CTRL_PROTO_ENF
- Type changed: `vrf` `uint8` → `uint16`

##### 44032_-_LOGID_EVENT_VOIP_SIP
- Field added: `attack` (string, len: 256) — ""
- Field added: `attackid` (uint32, len: 10) — ""

##### 44034_-_LOGID_EVENT_VOIP_SIP_FUZZING
- Field added: `attack` (string, len: 256) — ""
- Field added: `attackid` (uint32, len: 10) — ""

##### 60000_-_LOG_ID_ICAP_SERVER_ERROR
- Type changed: `vrf` `uint8` → `uint16`

##### 60001_-_LOG_ID_ICAP_INFECTION_BLOCK
- Type changed: `vrf` `uint8` → `uint16`

##### 60002_-_LOG_ID_ICAP_CONN_ERROR
- Type changed: `vrf` `uint8` → `uint16`

##### 62004_-_LOG_ID_SSL_EXEMPT_ADDR
- Type changed: `vrf` `uint8` → `uint16`

##### 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST
- Type changed: `vrf` `uint8` → `uint16`

##### 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY
- Type changed: `vrf` `uint8` → `uint16`

##### 62008_-_LOG_ID_SSL_EXEMPT_LOCAL_CATEGORY
- Type changed: `vrf` `uint8` → `uint16`

##### 62009_-_LOG_ID_SSL_EXEMPT_USER_CATEGORY
- Type changed: `vrf` `uint8` → `uint16`

##### 62100_-_LOG_ID_SSL_NEGOTIATION_INSPECT
- Type changed: `vrf` `uint8` → `uint16`

##### 62101_-_LOG_ID_SSL_NEGOTIATION_BLOCK
- Type changed: `vrf` `uint8` → `uint16`

##### 62102_-_LOG_ID_SSL_NEGOTIATION_BYPASS
- Type changed: `vrf` `uint8` → `uint16`

##### 62103_-_LOG_ID_SSL_NEGOTIATION_INFO
- Type changed: `vrf` `uint8` → `uint16`

##### 62200_-_LOG_ID_SSL_SERVER_CERT_INFO
- Type changed: `vrf` `uint8` → `uint16`

##### 62220_-_LOG_ID_SSL_HANDSHAKE_INFO
- Type changed: `vrf` `uint8` → `uint16`

##### 62300_-_LOG_ID_SSL_ANOMALY_CERT_BLOCKLISTED
- Type changed: `vrf` `uint8` → `uint16`

##### 62301_-_LOG_ID_SSL_ANOMALY_CERT_RESIGN_TRUSTED
- Type changed: `vrf` `uint8` → `uint16`

##### 62302_-_LOG_ID_SSL_ANOMALY_CERT_RESIGN_UNTRUSTED
- Type changed: `vrf` `uint8` → `uint16`

##### 62303_-_LOG_ID_SSL_ANOMALY_CERT_BLOCKED
- Type changed: `vrf` `uint8` → `uint16`

##### 62304_-_LOG_ID_SSL_ANOMALY_CERT_SNI_MISMATCHED
- Type changed: `vrf` `uint8` → `uint16`

##### 62305_-_LOG_ID_SSL_ANOMALY_CERT_PROBE_FAILURE_BLOCK
- Type changed: `vrf` `uint8` → `uint16`

##### 62306_-_LOG_ID_SSL_ANOMALY_CERT_PROBE_FAILURE_PASS
- Type changed: `vrf` `uint8` → `uint16`

##### 62307_-_LOG_ID_SSL_ANOMALY_CERT_SNI_MISMATCHED_INFO
- Type changed: `vrf` `uint8` → `uint16`

##### 62308_-_LOG_ID_SSL_ANOMALY_HANDSHAKE_FAILURE
- Type changed: `vrf` `uint8` → `uint16`

##### 62309_-_LOG_ID_SSL_ANOMALY_CERT_INVALID
- Type changed: `vrf` `uint8` → `uint16`

##### 64000_-_LOG_ID_FILE_FILTER_BLOCK
- Type changed: `vrf` `uint8` → `uint16`

##### 64001_-_LOG_ID_FILE_FILTER_LOG
- Type changed: `vrf` `uint8` → `uint16`

##### 64600_-_LOG_ID_OT_VPATCH_BLOCK
- Field added: `msg` (string, len: 518) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 64601_-_LOG_ID_OT_VPATCH_LOG
- Field added: `msg` (string, len: 518) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 64610_-_LOG_ID_LOCALIN_VPATCH_BLOCK
- Field added: `msg` (string, len: 518) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 64611_-_LOG_ID_LOCALIN_VPATCH_LOG
- Field added: `msg` (string, len: 518) — ""
- Type changed: `vrf` `uint8` → `uint16`

##### 8192_-_MESGID_INFECT_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8193_-_MESGID_INFECT_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8194_-_MESGID_INFECT_MIME_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8195_-_MESGID_INFECT_MIME_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8200_-_MESGID_MIME_FILETYPE_EXE_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8201_-_MESGID_MIME_FILETYPE_EXE_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8202_-_MESGID_AVQUERY_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8203_-_MESGID_AVQUERY_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8204_-_MESGID_MIME_AVQUERY_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8205_-_MESGID_MIME_AVQUERY_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8206_-_MESGID_AV_EXEMPT_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8207_-_MESGID_MIME_AV_EXEMPT_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8212_-_MESGID_MALWARE_LIST_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8213_-_MESGID_MALWARE_LIST_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8214_-_MESGID_MIME_MALWARE_LIST_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8215_-_MESGID_MIME_MALWARE_LIST_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8216_-_MESGID_FILE_HASH_EMS_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8217_-_MESGID_FILE_HASH_EMS_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8219_-_MESGID_MIME_FILE_HASH_EMS_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8220_-_MESGID_ICB_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8221_-_MESGID_ICB_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8222_-_MESGID_MIME_ICB_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8223_-_MESGID_MIME_ICB_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8224_-_MESGID_ICB_TIMEOUT_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8225_-_MESGID_ICB_TIMEOUT_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8226_-_MESGID_MIME_ICB_TIMEOUT_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8227_-_MESGID_MIME_ICB_TIMEOUT_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8228_-_MESGID_ICB_ERROR_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8229_-_MESGID_ICB_ERROR_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8230_-_MESGID_MIME_ICB_ERROR_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8231_-_MESGID_MIME_ICB_ERROR_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8448_-_MESGID_BLOCK_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8450_-_MESGID_BLOCK_MIME_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8451_-_MESGID_BLOCK_MIME_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8452_-_MESGID_BLOCK_COMMAND
- Type changed: `vrf` `uint8` → `uint16`

##### 8704_-_MESGID_OVERSIZE_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8705_-_MESGID_OVERSIZE_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8708_-_MESGID_OVERSIZE_STREAM_UNCOMP_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8709_-_MESGID_OVERSIZE_STREAM_UNCOMP_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8720_-_MESGID_SWITCH_PROTO_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8721_-_MESGID_SWITCH_PROTO_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8960_-_MESGID_SCAN_UNCOMPSIZELIMIT_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8961_-_MESGID_SCAN_UNCOMPSIZELIMIT_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8962_-_MESGID_SCAN_ARCHIVE_ENCRYPTED_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8963_-_MESGID_SCAN_ARCHIVE_ENCRYPTED_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8964_-_MESGID_SCAN_ARCHIVE_CORRUPTED_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8965_-_MESGID_SCAN_ARCHIVE_CORRUPTED_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8966_-_MESGID_SCAN_ARCHIVE_MULTIPART_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8967_-_MESGID_SCAN_ARCHIVE_MULTIPART_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8968_-_MESGID_SCAN_ARCHIVE_NESTED_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8969_-_MESGID_SCAN_ARCHIVE_NESTED_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8970_-_MESGID_SCAN_ARCHIVE_OVERSIZE_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8971_-_MESGID_SCAN_ARCHIVE_OVERSIZE_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8972_-_MESGID_SCAN_ARCHIVE_UNHANDLED_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8973_-_MESGID_SCAN_ARCHIVE_UNHANDLED_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8974_-_MESGID_SCAN_AV_ENGINE_LOAD_FAILED_ERROR
- Type changed: `vrf` `uint8` → `uint16`

##### 8975_-_MESGID_SCAN_ARCHIVE_PARTIALLYCORRUPTED_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8976_-_MESGID_SCAN_ARCHIVE_PARTIALLYCORRUPTED_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8979_-_MESGID_SCAN_ARCHIVE_TIMEOUT_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 8980_-_MESGID_SCAN_ARCHIVE_TIMEOUT_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 8981_-_MESGID_SCAN_AV_CDR_INTERNAL_ERROR
- Type changed: `vrf` `uint8` → `uint16`

##### 8982_-_MESGID_SCAN_AV_MAX_MEMORY_REACHED_ERROR
- Type changed: `vrf` `uint8` → `uint16`

##### 9233_-_MESGID_ANALYTICS_SUBMITTED
- Type changed: `vrf` `uint8` → `uint16`

##### 9234_-_MESGID_ANALYTICS_INFECT_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 9235_-_MESGID_ANALYTICS_INFECT_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 9236_-_MESGID_ANALYTICS_INFECT_MIME_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 9237_-_MESGID_ANALYTICS_INFECT_MIME_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 9239_-_MESGID_CONTENT_DISARM_NOTIF
- Type changed: `vrf` `uint8` → `uint16`

##### 9240_-_MESGID_CONTENT_DISARM_WARNING
- Type changed: `vrf` `uint8` → `uint16`

##### 9241_-_LOG_ID_UNKNOWN_CE_BLOCK
- Type changed: `vrf` `uint8` → `uint16`

##### 9242_-_LOG_ID_UNKNOWN_CE_BYPASS
- Type changed: `vrf` `uint8` → `uint16`

---

### 7.6.1 → 7.6.2

**Summary:** 0 LOGID added, 0 removed | 2 fields added, 0 removed | 0 type changed | 0 descriptions changed | 0 lengths changed

#### Traffic

*(no changes)*

#### Event

*(no changes)*

#### UTM

##### 44033_-_LOGID_EVENT_VOIP_SIP_BLOCK
- Field added: `attack` (string, len: 256) — ""
- Field added: `attackid` (uint32, len: 10) — ""

---

### 7.6.2 → 7.6.3

**Summary:** 25 LOGID added, 0 removed | 317 fields added, 328 removed | 0 type changed | 0 descriptions changed | 64 lengths changed

#### Traffic

##### 10_-_LOG_ID_TRAFFIC_EXPLICIT_PROXY
- Field added: `tunneldstip` (ip, len: 39) — ""
- Field added: `tunnelproto` (string, len: 10) — ""
- Field added: `tunnelsessionid` (uint32, len: 10) — ""
- Field added: `tunnelsrcip` (ip, len: 39) — ""
- Field added: `vipincomingip` (ip, len: 39) — ""

##### 11_-_LOG_ID_TRAFFIC_FAIL_CONN
- Field added: `tunneldstip` (ip, len: 39) — ""
- Field added: `tunnelproto` (string, len: 10) — ""
- Field added: `tunnelsessionid` (uint32, len: 10) — ""
- Field added: `tunnelsrcip` (ip, len: 39) — ""
- Field added: `vipincomingip` (ip, len: 39) — ""

##### 12_-_LOG_ID_TRAFFIC_MULTICAST
- Field added: `tunneldstip` (ip, len: 39) — ""
- Field added: `tunnelproto` (string, len: 10) — ""
- Field added: `tunnelsessionid` (uint32, len: 10) — ""
- Field added: `tunnelsrcip` (ip, len: 39) — ""
- Field added: `vipincomingip` (ip, len: 39) — ""

##### 13_-_LOG_ID_TRAFFIC_END_FORWARD
- Field added: `tunneldstip` (ip, len: 39) — ""
- Field added: `tunnelproto` (string, len: 10) — ""
- Field added: `tunnelsessionid` (uint32, len: 10) — ""
- Field added: `tunnelsrcip` (ip, len: 39) — ""
- Field added: `vipincomingip` (ip, len: 39) — ""

##### 14_-_LOG_ID_TRAFFIC_END_LOCAL
- Field added: `tunneldstip` (ip, len: 39) — ""
- Field added: `tunnelproto` (string, len: 10) — ""
- Field added: `tunnelsessionid` (uint32, len: 10) — ""
- Field added: `tunnelsrcip` (ip, len: 39) — ""
- Field added: `vipincomingip` (ip, len: 39) — ""

##### 15_-_LOG_ID_TRAFFIC_START_FORWARD
- Field added: `tunneldstip` (ip, len: 39) — ""
- Field added: `tunnelproto` (string, len: 10) — ""
- Field added: `tunnelsessionid` (uint32, len: 10) — ""
- Field added: `tunnelsrcip` (ip, len: 39) — ""
- Field added: `vipincomingip` (ip, len: 39) — ""

##### 16_-_LOG_ID_TRAFFIC_START_LOCAL
- Field added: `tunneldstip` (ip, len: 39) — ""
- Field added: `tunnelproto` (string, len: 10) — ""
- Field added: `tunnelsessionid` (uint32, len: 10) — ""
- Field added: `tunnelsrcip` (ip, len: 39) — ""
- Field added: `vipincomingip` (ip, len: 39) — ""

##### 17_-_LOG_ID_TRAFFIC_SNIFFER
- Field added: `tunneldstip` (ip, len: 39) — ""
- Field added: `tunnelproto` (string, len: 10) — ""
- Field added: `tunnelsessionid` (uint32, len: 10) — ""
- Field added: `tunnelsrcip` (ip, len: 39) — ""
- Field added: `vipincomingip` (ip, len: 39) — ""

##### 19_-_LOG_ID_TRAFFIC_BROADCAST
- Field added: `tunneldstip` (ip, len: 39) — ""
- Field added: `tunnelproto` (string, len: 10) — ""
- Field added: `tunnelsessionid` (uint32, len: 10) — ""
- Field added: `tunnelsrcip` (ip, len: 39) — ""
- Field added: `vipincomingip` (ip, len: 39) — ""

##### 20_-_LOG_ID_TRAFFIC_STAT
- Field added: `tunneldstip` (ip, len: 39) — ""
- Field added: `tunnelproto` (string, len: 10) — ""
- Field added: `tunnelsessionid` (uint32, len: 10) — ""
- Field added: `tunnelsrcip` (ip, len: 39) — ""
- Field added: `vipincomingip` (ip, len: 39) — ""

##### 21_-_LOG_ID_TRAFFIC_SNIFFER_STAT
- Field added: `tunneldstip` (ip, len: 39) — ""
- Field added: `tunnelproto` (string, len: 10) — ""
- Field added: `tunnelsessionid` (uint32, len: 10) — ""
- Field added: `tunnelsrcip` (ip, len: 39) — ""
- Field added: `vipincomingip` (ip, len: 39) — ""

##### 22_-_LOG_ID_TRAFFIC_UTM_CORRELATION
- Field added: `tunneldstip` (ip, len: 39) — ""
- Field added: `tunnelproto` (string, len: 10) — ""
- Field added: `tunnelsessionid` (uint32, len: 10) — ""
- Field added: `tunnelsrcip` (ip, len: 39) — ""
- Field added: `vipincomingip` (ip, len: 39) — ""

##### 24_-_LOG_ID_TRAFFIC_ZTNA
- Field added: `tunneldstip` (ip, len: 39) — ""
- Field added: `tunnelproto` (string, len: 10) — ""
- Field added: `tunnelsessionid` (uint32, len: 10) — ""
- Field added: `tunnelsrcip` (ip, len: 39) — ""
- Field added: `vipincomingip` (ip, len: 39) — ""

##### 2_-_LOG_ID_TRAFFIC_ALLOW
- Field added: `tunneldstip` (ip, len: 39) — ""
- Field added: `tunnelproto` (string, len: 10) — ""
- Field added: `tunnelsessionid` (uint32, len: 10) — ""
- Field added: `tunnelsrcip` (ip, len: 39) — ""
- Field added: `vipincomingip` (ip, len: 39) — ""

##### 3_-_LOG_ID_TRAFFIC_DENY
- Field added: `tunneldstip` (ip, len: 39) — ""
- Field added: `tunnelproto` (string, len: 10) — ""
- Field added: `tunnelsessionid` (uint32, len: 10) — ""
- Field added: `tunnelsrcip` (ip, len: 39) — ""
- Field added: `vipincomingip` (ip, len: 39) — ""

##### 4_-_LOG_ID_TRAFFIC_OTHER_START
- Field added: `tunneldstip` (ip, len: 39) — ""
- Field added: `tunnelproto` (string, len: 10) — ""
- Field added: `tunnelsessionid` (uint32, len: 10) — ""
- Field added: `tunnelsrcip` (ip, len: 39) — ""
- Field added: `vipincomingip` (ip, len: 39) — ""

##### 5_-_LOG_ID_TRAFFIC_OTHER_ICMP_ALLOW
- Field added: `tunneldstip` (ip, len: 39) — ""
- Field added: `tunnelproto` (string, len: 10) — ""
- Field added: `tunnelsessionid` (uint32, len: 10) — ""
- Field added: `tunnelsrcip` (ip, len: 39) — ""
- Field added: `vipincomingip` (ip, len: 39) — ""

##### 6_-_LOG_ID_TRAFFIC_OTHER_ICMP_DENY
- Field added: `tunneldstip` (ip, len: 39) — ""
- Field added: `tunnelproto` (string, len: 10) — ""
- Field added: `tunnelsessionid` (uint32, len: 10) — ""
- Field added: `tunnelsrcip` (ip, len: 39) — ""
- Field added: `vipincomingip` (ip, len: 39) — ""

##### 7_-_LOG_ID_TRAFFIC_OTHER_INVALID
- Field added: `tunneldstip` (ip, len: 39) — ""
- Field added: `tunnelproto` (string, len: 10) — ""
- Field added: `tunnelsessionid` (uint32, len: 10) — ""
- Field added: `tunnelsrcip` (ip, len: 39) — ""
- Field added: `vipincomingip` (ip, len: 39) — ""

##### 8_-_LOG_ID_TRAFFIC_WANOPT
- Field added: `tunneldstip` (ip, len: 39) — ""
- Field added: `tunnelproto` (string, len: 10) — ""
- Field added: `tunnelsessionid` (uint32, len: 10) — ""
- Field added: `tunnelsrcip` (ip, len: 39) — ""
- Field added: `vipincomingip` (ip, len: 39) — ""

##### 9_-_LOG_ID_TRAFFIC_WEBCACHE
- Field added: `tunneldstip` (ip, len: 39) — ""
- Field added: `tunnelproto` (string, len: 10) — ""
- Field added: `tunnelsessionid` (uint32, len: 10) — ""
- Field added: `tunnelsrcip` (ip, len: 39) — ""
- Field added: `vipincomingip` (ip, len: 39) — ""

#### Event

##### 22819_-_LOG_ID_SCANUNIT_DLP_BUILDER_PATTERN_SKIP *(new)*

##### 22941_-_LOG_ID_EVENT_VWL_PASS_APP_PERF *(new)*

##### 22942_-_LOG_ID_EVENT_LINK_MONITOR_BUILD_ERR *(new)*

##### 37143_-_MESGID_PH1_PEER_PROPOSAL *(new)*

##### 37144_-_MESGID_PH2_PEER_PROPOSAL *(new)*

##### 38422_-_LOGID_EVENT_ICBD_UPDATE_SUCCESS *(new)*

##### 38423_-_LOGID_EVENT_ICBD_UPDATE_FAILURE *(new)*

##### 43056_-_LOG_ID_EVENT_AUTH_SERVER_REACHABILITY_UPDATE *(new)*

##### 44559_-_LOGID_EVENT_INSTALL_IPROPE *(new)*

##### 44560_-_LOGID_EVENT_CONFIG_ACCPROFILE_SUPER_ADMIN *(new)*

##### 44561_-_LOGID_EVENT_CONFIG_REQUEST_UNAUTH *(new)*

##### 47005_-_LOG_ID_MALWARE_STREAM_TRUNCATED_ENTER *(new)*

##### 47006_-_LOG_ID_MALWARE_STREAM_TRUNCATED_EXIT *(new)*

##### 52002_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_RESULT *(new)*

##### 53326_-_LOG_ID_NPU_HEALTH_INFO *(new)*

##### 53327_-_LOG_ID_NPU_HEALTH_WARNING *(new)*

##### 53328_-_LOG_ID_NPU_HEALTH_ERROR *(new)*

##### 37120_-_MESGID_NEG_GENERIC_P1_NOTIF
- Field added: `eapauthgroup` (string, len: 128) — ""
- Field added: `eapuser` (string, len: 256) — ""

##### 37121_-_MESGID_NEG_GENERIC_P1_ERROR
- Field added: `eapauthgroup` (string, len: 128) — ""
- Field added: `eapuser` (string, len: 256) — ""

##### 37122_-_MESGID_NEG_GENERIC_P2_NOTIF
- Field added: `eapauthgroup` (string, len: 128) — ""
- Field added: `eapuser` (string, len: 256) — ""

##### 37123_-_MESGID_NEG_GENERIC_P2_ERROR
- Field added: `eapauthgroup` (string, len: 128) — ""
- Field added: `eapuser` (string, len: 256) — ""

##### 37124_-_MESGID_NEG_I_P1_ERROR
- Field added: `eapauthgroup` (string, len: 128) — ""
- Field added: `eapuser` (string, len: 256) — ""

##### 37125_-_MESGID_NEG_I_P2_ERROR
- Field added: `eapauthgroup` (string, len: 128) — ""
- Field added: `eapuser` (string, len: 256) — ""

##### 37126_-_MESGID_NEG_NO_STATE_ERROR
- Field added: `eapauthgroup` (string, len: 128) — ""
- Field added: `eapuser` (string, len: 256) — ""

##### 37127_-_MESGID_NEG_PROGRESS_P1_NOTIF
- Field added: `eapauthgroup` (string, len: 128) — ""
- Field added: `eapuser` (string, len: 256) — ""

##### 37128_-_MESGID_NEG_PROGRESS_P1_ERROR
- Field added: `eapauthgroup` (string, len: 128) — ""
- Field added: `eapuser` (string, len: 256) — ""

##### 37129_-_MESGID_NEG_PROGRESS_P2_NOTIF
- Field added: `eapauthgroup` (string, len: 128) — ""
- Field added: `eapuser` (string, len: 256) — ""

##### 37130_-_MESGID_NEG_PROGRESS_P2_ERROR
- Field added: `eapauthgroup` (string, len: 128) — ""
- Field added: `eapuser` (string, len: 256) — ""

##### 37131_-_MESGID_ESP_ERROR
- Field added: `eapauthgroup` (string, len: 128) — ""
- Field added: `eapuser` (string, len: 256) — ""

##### 37132_-_MESGID_ESP_CRITICAL
- Field added: `eapauthgroup` (string, len: 128) — ""
- Field added: `eapuser` (string, len: 256) — ""

##### 37133_-_MESGID_INSTALL_SA
- Field added: `eapauthgroup` (string, len: 128) — ""
- Field added: `eapuser` (string, len: 256) — ""

##### 37134_-_MESGID_DELETE_P1_SA
- Field added: `eapauthgroup` (string, len: 128) — ""
- Field added: `eapuser` (string, len: 256) — ""

##### 37135_-_MESGID_DELETE_P2_SA
- Field added: `eapauthgroup` (string, len: 128) — ""
- Field added: `eapuser` (string, len: 256) — ""

##### 37136_-_MESGID_DPD_FAILURE
- Field added: `eapauthgroup` (string, len: 128) — ""
- Field added: `eapuser` (string, len: 256) — ""

##### 37137_-_MESGID_CONN_FAILURE
- Field added: `eapauthgroup` (string, len: 128) — ""
- Field added: `eapuser` (string, len: 256) — ""

##### 37138_-_MESGID_CONN_UPDOWN
- Field added: `eapauthgroup` (string, len: 128) — ""
- Field added: `eapuser` (string, len: 256) — ""

##### 37139_-_MESGID_P2_UPDOWN
- Field added: `eapauthgroup` (string, len: 128) — ""
- Field added: `eapuser` (string, len: 256) — ""

##### 37141_-_MESGID_CONN_STATS
- Field added: `eapauthgroup` (string, len: 128) — ""
- Field added: `eapuser` (string, len: 256) — ""

##### 37142_-_MESGID_TRANSPORT_SWITCH
- Field added: `eapauthgroup` (string, len: 128) — ""
- Field added: `eapuser` (string, len: 256) — ""
- Field removed: `xauthgroup` (string)
- Field removed: `xauthuser` (string)

##### 41984_-_LOG_ID_EVENT_VPN_CERT_LOAD
- Length changed: `cert-type` 6 → 9

##### 41985_-_LOG_ID_EVENT_VPN_CERT_REMOVAL
- Length changed: `cert-type` 6 → 9

##### 41986_-_LOG_ID_EVENT_VPN_CERT_REGEN
- Length changed: `cert-type` 6 → 9

##### 41987_-_LOG_ID_EVENT_VPN_CERT_UPDATE
- Length changed: `cert-type` 6 → 9

##### 41989_-_LOG_ID_EVENT_VPN_CERT_ERR
- Length changed: `cert-type` 6 → 9

##### 41990_-_LOG_ID_EVENT_VPN_CERT_UPDATE_FAILED
- Length changed: `cert-type` 6 → 9

##### 41991_-_LOG_ID_EVENT_VPN_CERT_EXPORT
- Length changed: `cert-type` 6 → 9

##### 41992_-_LOG_ID_EVENT_VPN_CERT_CRL_EXPIRED
- Length changed: `cert-type` 6 → 9

##### 43025_-_LOG_ID_EVENT_AUTH_PROXY_SUCCESS
- Field added: `method` (string, len: 64) — "Method"

##### 43026_-_LOG_ID_EVENT_AUTH_PROXY_FAILED
- Field added: `method` (string, len: 64) — "Method"

##### 43028_-_LOG_ID_EVENT_AUTH_PROXY_GROUP_INFO_FAILED
- Field added: `method` (string, len: 64) — "Method"

##### 43032_-_LOG_ID_EVENT_AUTH_PROXY_USER_LIMIT_REACHED
- Field added: `method` (string, len: 64) — "Method"

##### 43033_-_LOG_ID_EVENT_AUTH_PROXY_MULTIPLE_LOGIN
- Field added: `method` (string, len: 64) — "Method"

##### 43524_-_LOG_ID_EVENT_WIRELESS_STA
- Field added: `trafficmode` (string, len: 8) — ""

##### 43526_-_LOG_ID_EVENT_WIRELESS_WTPR
- Field added: `trafficmode` (string, len: 8) — ""

##### 43528_-_LOG_ID_EVENT_WIRELESS_WTPR_ERROR
- Field added: `trafficmode` (string, len: 8) — ""

##### 43572_-_LOG_ID_EVENT_WIRELESS_STA_ASSO
- Field added: `trafficmode` (string, len: 8) — ""

##### 43573_-_LOG_ID_EVENT_WIRELESS_STA_AUTH
- Field added: `trafficmode` (string, len: 8) — ""

##### 43574_-_LOG_ID_EVENT_WIRELESS_STA_DASS
- Field added: `trafficmode` (string, len: 8) — ""

##### 43575_-_LOG_ID_EVENT_WIRELESS_STA_DAUT
- Field added: `trafficmode` (string, len: 8) — ""

##### 43576_-_LOG_ID_EVENT_WIRELESS_STA_IDLE
- Field added: `trafficmode` (string, len: 8) — ""

##### 43577_-_LOG_ID_EVENT_WIRELESS_STA_DENY
- Field added: `trafficmode` (string, len: 8) — ""

##### 43578_-_LOG_ID_EVENT_WIRELESS_STA_KICK
- Field added: `trafficmode` (string, len: 8) — ""

##### 43579_-_LOG_ID_EVENT_WIRELESS_STA_IP
- Field added: `trafficmode` (string, len: 8) — ""

##### 43580_-_LOG_ID_EVENT_WIRELESS_STA_LEAVE_WTP
- Field added: `trafficmode` (string, len: 8) — ""

##### 43581_-_LOG_ID_EVENT_WIRELESS_STA_WTP_DISCONN
- Field added: `trafficmode` (string, len: 8) — ""

##### 43586_-_LOG_ID_EVENT_WIRELESS_WTPR_DARRP_CHAN
- Field added: `trafficmode` (string, len: 8) — ""

##### 43587_-_LOG_ID_EVENT_WIRELESS_WTPR_DARRP_START
- Field added: `trafficmode` (string, len: 8) — ""

##### 43588_-_LOG_ID_EVENT_WIRELESS_WTPR_OPER_CHAN
- Field added: `trafficmode` (string, len: 8) — ""

##### 43589_-_LOG_ID_EVENT_WIRELESS_WTPR_RADAR
- Field added: `trafficmode` (string, len: 8) — ""

##### 43590_-_LOG_ID_EVENT_WIRELESS_WTPR_NOL
- Field added: `trafficmode` (string, len: 8) — ""

##### 43591_-_LOG_ID_EVENT_WIRELESS_WTPR_COUNTRY_CFG_SUCCESS
- Field added: `trafficmode` (string, len: 8) — ""

##### 43592_-_LOG_ID_EVENT_WIRELESS_WTPR_OPER_COUNTRY
- Field added: `trafficmode` (string, len: 8) — ""

##### 43593_-_LOG_ID_EVENT_WIRELESS_WTPR_CFG_TXPOWER
- Field added: `trafficmode` (string, len: 8) — ""

##### 43594_-_LOG_ID_EVENT_WIRELESS_WTPR_OPER_TXPOWER
- Field added: `trafficmode` (string, len: 8) — ""

##### 43600_-_LOG_ID_EVENT_WIRELESS_WTPR_DARRP_STOP
- Field added: `trafficmode` (string, len: 8) — ""

##### 43601_-_LOG_ID_EVENT_WIRELESS_STA_CAP_SIGNON
- Field added: `trafficmode` (string, len: 8) — ""

##### 43602_-_LOG_ID_EVENT_WIRELESS_STA_CAP_SIGNON_SUCCESS
- Field added: `trafficmode` (string, len: 8) — ""

##### 43603_-_LOG_ID_EVENT_WIRELESS_STA_CAP_SIGNON_FAILURE
- Field added: `trafficmode` (string, len: 8) — ""

##### 43604_-_LOG_ID_EVENT_WIRELESS_STA_CAP_EMAIL_REQUEST
- Field added: `trafficmode` (string, len: 8) — ""

##### 43605_-_LOG_ID_EVENT_WIRELESS_STA_CAP_EMAIL_SUCCESS
- Field added: `trafficmode` (string, len: 8) — ""

##### 43606_-_LOG_ID_EVENT_WIRELESS_STA_CAP_EMAIL_FAILURE
- Field added: `trafficmode` (string, len: 8) — ""

##### 43607_-_LOG_ID_EVENT_WIRELESS_STA_CAP_DISCLAIMER_CHECK
- Field added: `trafficmode` (string, len: 8) — ""

##### 43608_-_LOG_ID_EVENT_WIRELESS_STA_CAP_DISCLAIMER_DECLINE
- Field added: `trafficmode` (string, len: 8) — ""

##### 43609_-_LOG_ID_EVENT_WIRELESS_WTPR_DARRP_OPTIMIZATION_START
- Field added: `trafficmode` (string, len: 8) — ""

##### 43610_-_LOG_ID_EVENT_WIRELESS_WTPR_DARRP_OPTIMIZATION_STOP
- Field added: `trafficmode` (string, len: 8) — ""

##### 43616_-_LOG_ID_EVENT_WIRELESS_WTPR_NOL_ADD
- Field added: `trafficmode` (string, len: 8) — ""

##### 43625_-_LOG_ID_EVENT_WIRELESS_STA_CAP_CMCC_SUCCESS
- Field added: `trafficmode` (string, len: 8) — ""

##### 43626_-_LOG_ID_EVENT_WIRELESS_STA_CAP_CMCC_FAILURE
- Field added: `trafficmode` (string, len: 8) — ""

##### 43627_-_LOG_ID_EVENT_WIRELESS_STA_CAP_CMCC_TIMEOUT
- Field added: `trafficmode` (string, len: 8) — ""

##### 43628_-_LOG_ID_EVENT_WIRELESS_STA_CAP_CMCC_MAC_AUTH_SUCCESS
- Field added: `trafficmode` (string, len: 8) — ""

##### 43629_-_LOG_ID_EVENT_WIRELESS_STA_RADIUS_AUTH_FAILURE
- Field added: `trafficmode` (string, len: 8) — ""

##### 43630_-_LOG_ID_EVENT_WIRELESS_STA_RADIUS_AUTH_SUCCESS
- Field added: `trafficmode` (string, len: 8) — ""

##### 43631_-_LOG_ID_EVENT_WIRELESS_STA_RADIUS_AUTH_NO_RESP
- Field added: `trafficmode` (string, len: 8) — ""

##### 43632_-_LOG_ID_EVENT_WIRELESS_STA_RADIUS_MAC_AUTH_FAILURE
- Field added: `trafficmode` (string, len: 8) — ""

##### 43633_-_LOG_ID_EVENT_WIRELESS_STA_RADIUS_MAC_AUTH_SUCCESS
- Field added: `trafficmode` (string, len: 8) — ""

##### 43634_-_LOG_ID_EVENT_WIRELESS_STA_RADIUS_MAC_AUTH_NO_RESP
- Field added: `trafficmode` (string, len: 8) — ""

##### 43635_-_LOG_ID_EVENT_WIRELESS_STA_OKC_NO_MATCH
- Field added: `trafficmode` (string, len: 8) — ""

##### 43636_-_LOG_ID_EVENT_WIRELESS_STA_OKC_LOCAL_MATCH
- Field added: `trafficmode` (string, len: 8) — ""

##### 43637_-_LOG_ID_EVENT_WIRELESS_STA_OKC_INTER_AC_MATCH
- Field added: `trafficmode` (string, len: 8) — ""

##### 43638_-_LOG_ID_EVENT_WIRELESS_STA_OKC_INTER_AP_MATCH
- Field added: `trafficmode` (string, len: 8) — ""

##### 43639_-_LOG_ID_EVENT_WIRELESS_STA_FT_INVALID_ACTION_REQ
- Field added: `trafficmode` (string, len: 8) — ""

##### 43640_-_LOG_ID_EVENT_WIRELESS_STA_FT_INVALID_AUTH_REQ
- Field added: `trafficmode` (string, len: 8) — ""

##### 43641_-_LOG_ID_EVENT_WIRELESS_STA_FT_INVALID_REASSOC_REQ
- Field added: `trafficmode` (string, len: 8) — ""

##### 43642_-_LOG_ID_EVENT_WIRELESS_STA_FT_ACTION_REQ
- Field added: `trafficmode` (string, len: 8) — ""

##### 43643_-_LOG_ID_EVENT_WIRELESS_STA_FT_ACTION_RESP
- Field added: `trafficmode` (string, len: 8) — ""

##### 43644_-_LOG_ID_EVENT_WIRELESS_STA_FT_AUTH_REQ
- Field added: `trafficmode` (string, len: 8) — ""

##### 43645_-_LOG_ID_EVENT_WIRELESS_STA_FT_AUTH_RESP
- Field added: `trafficmode` (string, len: 8) — ""

##### 43646_-_LOG_ID_EVENT_WIRELESS_STA_FT_REASSOC_REQ
- Field added: `trafficmode` (string, len: 8) — ""

##### 43647_-_LOG_ID_EVENT_WIRELESS_STA_FT_REASSOC_RESP
- Field added: `trafficmode` (string, len: 8) — ""

##### 43648_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_INVALID_SECOND_MSG
- Field added: `trafficmode` (string, len: 8) — ""

##### 43649_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_INVALID_FOURTH_MSG
- Field added: `trafficmode` (string, len: 8) — ""

##### 43650_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_FIRST_MSG
- Field added: `trafficmode` (string, len: 8) — ""

##### 43651_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_SECOND_MSG
- Field added: `trafficmode` (string, len: 8) — ""

##### 43652_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_THIRD_MSG
- Field added: `trafficmode` (string, len: 8) — ""

##### 43653_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_FOURTH_MSG
- Field added: `trafficmode` (string, len: 8) — ""

##### 43654_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_FIRST_GROUP_MSG
- Field added: `trafficmode` (string, len: 8) — ""

##### 43655_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_SECOND_GROUP_MSG
- Field added: `trafficmode` (string, len: 8) — ""

##### 43656_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_MAX_STA_CNT
- Field added: `trafficmode` (string, len: 8) — ""

##### 43657_-_LOG_ID_EVENT_WIRELESS_STA_ASSOC_FAIL
- Field added: `trafficmode` (string, len: 8) — ""

##### 43658_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_NO_RESP
- Field added: `trafficmode` (string, len: 8) — ""

##### 43659_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_DIFF_OFFER
- Field added: `trafficmode` (string, len: 8) — ""

##### 43660_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_NO_ACK
- Field added: `trafficmode` (string, len: 8) — ""

##### 43661_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_NAK
- Field added: `trafficmode` (string, len: 8) — ""

##### 43662_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_DUP_IP
- Field added: `trafficmode` (string, len: 8) — ""

##### 43663_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_DISCOVER
- Field added: `trafficmode` (string, len: 8) — ""

##### 43664_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_OFFER
- Field added: `trafficmode` (string, len: 8) — ""

##### 43665_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_DECLINE
- Field added: `trafficmode` (string, len: 8) — ""

##### 43666_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_REQUEST
- Field added: `trafficmode` (string, len: 8) — ""

##### 43667_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_ACK
- Field added: `trafficmode` (string, len: 8) — ""

##### 43668_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_RELEASE
- Field added: `trafficmode` (string, len: 8) — ""

##### 43669_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_INFORM
- Field added: `trafficmode` (string, len: 8) — ""

##### 43670_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_SELF_ASSIGNED
- Field added: `trafficmode` (string, len: 8) — ""

##### 43671_-_LOG_ID_EVENT_WIRELESS_STA_DNS_NO_RESP
- Field added: `trafficmode` (string, len: 8) — ""

##### 43672_-_LOG_ID_EVENT_WIRELESS_STA_DNS_SERVER_FAILURE
- Field added: `trafficmode` (string, len: 8) — ""

##### 43673_-_LOG_ID_EVENT_WIRELESS_STA_DNS_NO_DOMAIN
- Field added: `trafficmode` (string, len: 8) — ""

##### 43674_-_LOG_ID_EVENT_WIRELESS_STA_WPA_KRACK_FT_REASSOC
- Field added: `trafficmode` (string, len: 8) — ""

##### 43675_-_LOG_ID_EVENT_WIRELESS_STA_AUTH_REQ
- Field added: `trafficmode` (string, len: 8) — ""

##### 43676_-_LOG_ID_EVENT_WIRELESS_STA_AUTH_RESP
- Field added: `trafficmode` (string, len: 8) — ""

##### 43677_-_LOG_ID_EVENT_WIRELESS_STA_ASSOC_REQ
- Field added: `trafficmode` (string, len: 8) — ""

##### 43678_-_LOG_ID_EVENT_WIRELESS_STA_REASSOC_REQ
- Field added: `trafficmode` (string, len: 8) — ""

##### 43679_-_LOG_ID_EVENT_WIRELESS_STA_ASSOC_RESP
- Field added: `trafficmode` (string, len: 8) — ""

##### 43680_-_LOG_ID_EVENT_WIRELESS_STA_REASSOC_RESP
- Field added: `trafficmode` (string, len: 8) — ""

##### 43681_-_LOG_ID_EVENT_WIRELESS_STA_PROBE_REQ
- Field added: `trafficmode` (string, len: 8) — ""

##### 43682_-_LOG_ID_EVENT_WIRELESS_STA_PROBE_RESP
- Field added: `trafficmode` (string, len: 8) — ""

##### 43686_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_INVALID_SCHEDULE
- Field added: `trafficmode` (string, len: 8) — ""

##### 43687_-_LOG_ID_EVENT_WIRELESS_STA_WL_BRIDGE_TRAFFIC_STATS
- Field added: `trafficmode` (string, len: 8) — ""

##### 43692_-_LOG_ID_EVENT_WIRELESS_WTPR_ANTENNA_DEFECT_DETECT
- Field added: `trafficmode` (string, len: 8) — ""

##### 43693_-_LOG_ID_EVENT_WIRELESS_STA_WNM_ACTION_BSTM_REQ
- Field added: `trafficmode` (string, len: 8) — ""

##### 43694_-_LOG_ID_EVENT_WIRELESS_STA_WNM_ACTION_BSTM_RESP_ACCEPT
- Field added: `trafficmode` (string, len: 8) — ""

##### 43695_-_LOG_ID_EVENT_WIRELESS_STA_WNM_ACTION_BSTM_RESP_REJECT
- Field added: `trafficmode` (string, len: 8) — ""

##### 43696_-_LOG_ID_EVENT_WIRELESS_WTPR_DRMA_START
- Field added: `trafficmode` (string, len: 8) — ""

##### 43697_-_LOG_ID_EVENT_WIRELESS_WTPR_DRMA_STOP
- Field added: `trafficmode` (string, len: 8) — ""

##### 43698_-_LOG_ID_EVENT_WIRELESS_WTPR_DRMA_MODE
- Field added: `trafficmode` (string, len: 8) — ""

##### 43699_-_LOG_ID_EVENT_WIRELESS_STA_DHCP6_SOLICIT
- Field added: `trafficmode` (string, len: 8) — ""

##### 43700_-_LOG_ID_EVENT_WIRELESS_STA_DHCP6_ADVERTISE
- Field added: `trafficmode` (string, len: 8) — ""

##### 43701_-_LOG_ID_EVENT_WIRELESS_STA_DHCP6_REQUEST
- Field added: `trafficmode` (string, len: 8) — ""

##### 43702_-_LOG_ID_EVENT_WIRELESS_STA_DHCP6_CONFIRM
- Field added: `trafficmode` (string, len: 8) — ""

##### 43703_-_LOG_ID_EVENT_WIRELESS_STA_DHCP6_RENEW
- Field added: `trafficmode` (string, len: 8) — ""

##### 43704_-_LOG_ID_EVENT_WIRELESS_STA_DHCP6_REPLY
- Field added: `trafficmode` (string, len: 8) — ""

##### 43705_-_LOG_ID_EVENT_WIRELESS_STA_DHCP6_RELEASE
- Field added: `trafficmode` (string, len: 8) — ""

##### 43706_-_LOG_ID_EVENT_WIRELESS_STA_DHCP6_RECONFIGURE
- Field added: `trafficmode` (string, len: 8) — ""

##### 43707_-_LOG_ID_EVENT_WIRELESS_WTPR_SSID_UP
- Field added: `trafficmode` (string, len: 8) — ""

##### 43708_-_LOG_ID_EVENT_WIRELESS_WTPR_SSID_DOWN
- Field added: `trafficmode` (string, len: 8) — ""

##### 43709_-_LOG_ID_EVENT_WIRELESS_STA_DHCP_ENFORCEMENT
- Field added: `trafficmode` (string, len: 8) — ""

##### 43710_-_LOG_ID_EVENT_WIRELESS_SAM_IPERF
- Field added: `trafficmode` (string, len: 8) — ""

##### 43711_-_LOG_ID_EVENT_WIRELESS_SAM_PING
- Field added: `trafficmode` (string, len: 8) — ""

##### 43712_-_LOG_ID_EVENT_WIRELESS_SAM_AUTH_FAILED
- Field added: `trafficmode` (string, len: 8) — ""

##### 43713_-_LOG_ID_EVENT_WIRELESS_SAM_CWP_AUTH_FAILED
- Field added: `trafficmode` (string, len: 8) — ""

##### 43715_-_LOG_ID_EVENT_WIRELESS_WTPR_BSS_COLOR_COLLISION
- Field added: `trafficmode` (string, len: 8) — ""

##### 43717_-_LOG_ID_EVENT_WIRELESS_STA_L3R_REHOME
- Field added: `trafficmode` (string, len: 8) — ""

##### 43719_-_LOG_ID_EVENT_WIRELESS_STA_PROBE_LOW_RSSI
- Field added: `trafficmode` (string, len: 8) — ""

##### 43721_-_LOG_ID_EVENT_WIRELESS_STA_WPA_MSG_EXT_MPSK_RESULT
- Field added: `trafficmode` (string, len: 8) — ""

#### UTM — new subtypes: Debug | removed subtypes: *(none)*

##### 16402_-_LOGID_ATTACK_SIGNATURE_L2 *(new)*

##### 28738_-_LOGID_APP_CTRL_DETECT_L2 *(new)*

##### 54806_-_LOG_ID_DNS_SVCPARAM_ECH *(new)*

##### 65290_-_LOG_ID_DEBUG_PRINT *(new)*

##### 8244_-_MESGID_MALWARE_STREAM_WARNING *(new)*

##### 8245_-_MESGID_MALWARE_STREAM_NOTIF *(new)*

##### 8246_-_MESGID_MIME_MALWARE_STREAM_WARNING *(new)*

##### 8247_-_MESGID_MIME_MALWARE_STREAM_NOTIF *(new)*

##### 12688_-_LOG_ID_WEB_SSL_EXEMPT
- Field added: `risklevel` (string, len: 36) — ""

##### 13056_-_LOG_ID_WEB_FTGD_CAT_BLK
- Field added: `risklevel` (string, len: 36) — ""

##### 13057_-_LOG_ID_WEB_FTGD_CAT_WARN
- Field added: `risklevel` (string, len: 36) — ""

##### 13058_-_LOG_ID_WEB_FTGD_RISK_BLK
- Field added: `risklevel` (string, len: 36) — ""

##### 13312_-_LOG_ID_WEB_FTGD_CAT_ALLOW
- Field added: `risklevel` (string, len: 36) — ""

##### 13313_-_LOG_ID_WEB_FTGD_RISK_ALLOW
- Field added: `risklevel` (string, len: 36) — ""

##### 13315_-_LOG_ID_WEB_FTGD_QUOTA_COUNTING
- Field added: `risklevel` (string, len: 36) — ""

##### 13316_-_LOG_ID_WEB_FTGD_QUOTA_EXPIRED
- Field added: `risklevel` (string, len: 36) — ""

##### 13317_-_LOG_ID_WEB_URL
- Field added: `risklevel` (string, len: 36) — ""

##### 44032_-_LOGID_EVENT_VOIP_SIP
- Field removed: `attack` (string)
- Field removed: `attackid` (uint32)

##### 54200_-_LOG_ID_DNS_RESOLV_ERROR
- Field added: `echmsg` (string, len: 64) — ""

##### 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK
- Field added: `echmsg` (string, len: 64) — ""

##### 54401_-_LOG_ID_DNS_URL_FILTER_ALLOW
- Field added: `echmsg` (string, len: 64) — ""

##### 54600_-_LOG_ID_DNS_BOTNET_IP
- Field added: `echmsg` (string, len: 64) — ""

##### 54601_-_LOG_ID_DNS_BOTNET_DOMAIN
- Field added: `echmsg` (string, len: 64) — ""

##### 54800_-_LOG_ID_DNS_FTGD_WARNING
- Field added: `echmsg` (string, len: 64) — ""

##### 54801_-_LOG_ID_DNS_FTGD_ERROR
- Field added: `echmsg` (string, len: 64) — ""

##### 54802_-_LOG_ID_DNS_FTGD_CAT_ALLOW
- Field added: `echmsg` (string, len: 64) — ""

##### 54803_-_LOG_ID_DNS_FTGD_CAT_BLOCK
- Field added: `echmsg` (string, len: 64) — ""

##### 54804_-_LOG_ID_DNS_SAFE_SEARCH
- Field added: `echmsg` (string, len: 64) — ""

##### 54805_-_LOG_ID_DNS_LOCAL
- Field added: `echmsg` (string, len: 64) — ""

##### 60000_-_LOG_ID_ICAP_SERVER_ERROR
- Field added: `poluuid` (string, len: 37) — ""

##### 60001_-_LOG_ID_ICAP_INFECTION_BLOCK
- Field added: `poluuid` (string, len: 37) — ""

##### 60002_-_LOG_ID_ICAP_CONN_ERROR
- Field added: `poluuid` (string, len: 37) — ""

##### 8192_-_MESGID_INFECT_WARNING
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8193_-_MESGID_INFECT_NOTIF
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8194_-_MESGID_INFECT_MIME_WARNING
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8195_-_MESGID_INFECT_MIME_NOTIF
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8202_-_MESGID_AVQUERY_WARNING
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8203_-_MESGID_AVQUERY_NOTIF
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8204_-_MESGID_MIME_AVQUERY_WARNING
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8205_-_MESGID_MIME_AVQUERY_NOTIF
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8206_-_MESGID_AV_EXEMPT_NOTIF
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8207_-_MESGID_MIME_AV_EXEMPT_NOTIF
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8212_-_MESGID_MALWARE_LIST_WARNING
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8213_-_MESGID_MALWARE_LIST_NOTIF
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8214_-_MESGID_MIME_MALWARE_LIST_WARNING
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8215_-_MESGID_MIME_MALWARE_LIST_NOTIF
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8216_-_MESGID_FILE_HASH_EMS_WARNING
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8217_-_MESGID_FILE_HASH_EMS_NOTIF
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8219_-_MESGID_MIME_FILE_HASH_EMS_NOTIF
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8220_-_MESGID_ICB_WARNING
- Field added: `icberror` (string, len: 32) — ""
- Field removed: `analyticscksum` (string)
- Field removed: `cdrcontent` (string)
- Field removed: `contentdisarmed` (string)
- Field removed: `filehash` (string)
- Field removed: `filehashsrc` (string)
- Length changed: `itype` 16 → 32

##### 8221_-_MESGID_ICB_NOTIF
- Field added: `icberror` (string, len: 32) — ""
- Field removed: `analyticscksum` (string)
- Field removed: `cdrcontent` (string)
- Field removed: `contentdisarmed` (string)
- Field removed: `filehash` (string)
- Field removed: `filehashsrc` (string)
- Length changed: `itype` 16 → 32

##### 8222_-_MESGID_MIME_ICB_WARNING
- Field added: `icberror` (string, len: 32) — ""
- Field removed: `analyticscksum` (string)
- Field removed: `cdrcontent` (string)
- Field removed: `contentdisarmed` (string)
- Field removed: `filehash` (string)
- Field removed: `filehashsrc` (string)
- Length changed: `itype` 16 → 32

##### 8223_-_MESGID_MIME_ICB_NOTIF
- Field added: `icberror` (string, len: 32) — ""
- Field removed: `analyticscksum` (string)
- Field removed: `cdrcontent` (string)
- Field removed: `contentdisarmed` (string)
- Field removed: `filehash` (string)
- Field removed: `filehashsrc` (string)
- Length changed: `itype` 16 → 32

##### 8224_-_MESGID_ICB_TIMEOUT_WARNING
- Field added: `icberror` (string, len: 32) — ""
- Field removed: `analyticscksum` (string)
- Field removed: `cdrcontent` (string)
- Field removed: `contentdisarmed` (string)
- Field removed: `filehash` (string)
- Field removed: `filehashsrc` (string)
- Length changed: `itype` 16 → 32

##### 8225_-_MESGID_ICB_TIMEOUT_NOTIF
- Field added: `icberror` (string, len: 32) — ""
- Field removed: `analyticscksum` (string)
- Field removed: `cdrcontent` (string)
- Field removed: `contentdisarmed` (string)
- Field removed: `filehash` (string)
- Field removed: `filehashsrc` (string)
- Length changed: `itype` 16 → 32

##### 8226_-_MESGID_MIME_ICB_TIMEOUT_WARNING
- Field added: `icberror` (string, len: 32) — ""
- Field removed: `analyticscksum` (string)
- Field removed: `cdrcontent` (string)
- Field removed: `contentdisarmed` (string)
- Field removed: `filehash` (string)
- Field removed: `filehashsrc` (string)
- Length changed: `itype` 16 → 32

##### 8227_-_MESGID_MIME_ICB_TIMEOUT_NOTIF
- Field added: `icberror` (string, len: 32) — ""
- Field removed: `analyticscksum` (string)
- Field removed: `cdrcontent` (string)
- Field removed: `contentdisarmed` (string)
- Field removed: `filehash` (string)
- Field removed: `filehashsrc` (string)
- Length changed: `itype` 16 → 32

##### 8228_-_MESGID_ICB_ERROR_WARNING
- Field added: `icberror` (string, len: 32) — ""
- Field removed: `analyticscksum` (string)
- Field removed: `cdrcontent` (string)
- Field removed: `contentdisarmed` (string)
- Field removed: `filehash` (string)
- Field removed: `filehashsrc` (string)
- Length changed: `itype` 16 → 32

##### 8229_-_MESGID_ICB_ERROR_NOTIF
- Field added: `icberror` (string, len: 32) — ""
- Field removed: `analyticscksum` (string)
- Field removed: `cdrcontent` (string)
- Field removed: `contentdisarmed` (string)
- Field removed: `filehash` (string)
- Field removed: `filehashsrc` (string)
- Length changed: `itype` 16 → 32

##### 8230_-_MESGID_MIME_ICB_ERROR_WARNING
- Field added: `icberror` (string, len: 32) — ""
- Field removed: `analyticscksum` (string)
- Field removed: `cdrcontent` (string)
- Field removed: `contentdisarmed` (string)
- Field removed: `filehash` (string)
- Field removed: `filehashsrc` (string)
- Length changed: `itype` 16 → 32

##### 8231_-_MESGID_MIME_ICB_ERROR_NOTIF
- Field added: `icberror` (string, len: 32) — ""
- Field removed: `analyticscksum` (string)
- Field removed: `cdrcontent` (string)
- Field removed: `contentdisarmed` (string)
- Field removed: `filehash` (string)
- Field removed: `filehashsrc` (string)
- Length changed: `itype` 16 → 32

##### 8960_-_MESGID_SCAN_UNCOMPSIZELIMIT_WARNING
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8961_-_MESGID_SCAN_UNCOMPSIZELIMIT_NOTIF
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8962_-_MESGID_SCAN_ARCHIVE_ENCRYPTED_WARNING
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8963_-_MESGID_SCAN_ARCHIVE_ENCRYPTED_NOTIF
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8964_-_MESGID_SCAN_ARCHIVE_CORRUPTED_WARNING
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8965_-_MESGID_SCAN_ARCHIVE_CORRUPTED_NOTIF
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8966_-_MESGID_SCAN_ARCHIVE_MULTIPART_WARNING
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8967_-_MESGID_SCAN_ARCHIVE_MULTIPART_NOTIF
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8968_-_MESGID_SCAN_ARCHIVE_NESTED_WARNING
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8969_-_MESGID_SCAN_ARCHIVE_NESTED_NOTIF
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8970_-_MESGID_SCAN_ARCHIVE_OVERSIZE_WARNING
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8971_-_MESGID_SCAN_ARCHIVE_OVERSIZE_NOTIF
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8972_-_MESGID_SCAN_ARCHIVE_UNHANDLED_WARNING
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8973_-_MESGID_SCAN_ARCHIVE_UNHANDLED_NOTIF
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8974_-_MESGID_SCAN_AV_ENGINE_LOAD_FAILED_ERROR
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8975_-_MESGID_SCAN_ARCHIVE_PARTIALLYCORRUPTED_WARNING
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8976_-_MESGID_SCAN_ARCHIVE_PARTIALLYCORRUPTED_NOTIF
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8979_-_MESGID_SCAN_ARCHIVE_TIMEOUT_WARNING
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8980_-_MESGID_SCAN_ARCHIVE_TIMEOUT_NOTIF
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8981_-_MESGID_SCAN_AV_CDR_INTERNAL_ERROR
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 8982_-_MESGID_SCAN_AV_MAX_MEMORY_REACHED_ERROR
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 9233_-_MESGID_ANALYTICS_SUBMITTED
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 9234_-_MESGID_ANALYTICS_INFECT_WARNING
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 9235_-_MESGID_ANALYTICS_INFECT_NOTIF
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 9236_-_MESGID_ANALYTICS_INFECT_MIME_WARNING
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 9237_-_MESGID_ANALYTICS_INFECT_MIME_NOTIF
- Field removed: `icbaction` (string)
- Field removed: `icbconfidence` (string)
- Field removed: `icbfileid` (string)
- Field removed: `icbfiletype` (string)
- Field removed: `icbseverity` (string)
- Field removed: `icbverdict` (string)
- Length changed: `itype` 16 → 32

##### 9241_-_LOG_ID_UNKNOWN_CE_BLOCK
- Field added: `agent` (string, len: 1024) — "User agent - eg. agent="Mozilla/5.0""
- Field added: `direction` (string, len: 8) — "Message/packets direction"
- Field added: `httpmethod` (string, len: 20) — ""
- Field added: `policytype` (string, len: 24) — ""

##### 9242_-_LOG_ID_UNKNOWN_CE_BYPASS
- Field added: `agent` (string, len: 1024) — "User agent - eg. agent="Mozilla/5.0""
- Field added: `direction` (string, len: 8) — "Message/packets direction"
- Field added: `httpmethod` (string, len: 20) — ""
- Field added: `policytype` (string, len: 24) — ""

---

### 7.6.3 → 7.6.4

**Summary:** 17 LOGID added, 2 removed | 554 fields added, 8 removed | 0 type changed | 0 descriptions changed | 7 lengths changed

#### Traffic

##### 10_-_LOG_ID_TRAFFIC_EXPLICIT_PROXY
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 11_-_LOG_ID_TRAFFIC_FAIL_CONN
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12_-_LOG_ID_TRAFFIC_MULTICAST
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13_-_LOG_ID_TRAFFIC_END_FORWARD
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 14_-_LOG_ID_TRAFFIC_END_LOCAL
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 15_-_LOG_ID_TRAFFIC_START_FORWARD
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 16_-_LOG_ID_TRAFFIC_START_LOCAL
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 17_-_LOG_ID_TRAFFIC_SNIFFER
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 19_-_LOG_ID_TRAFFIC_BROADCAST
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 20_-_LOG_ID_TRAFFIC_STAT
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 21_-_LOG_ID_TRAFFIC_SNIFFER_STAT
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 22_-_LOG_ID_TRAFFIC_UTM_CORRELATION
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 24_-_LOG_ID_TRAFFIC_ZTNA
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 2_-_LOG_ID_TRAFFIC_ALLOW
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 3_-_LOG_ID_TRAFFIC_DENY
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 4_-_LOG_ID_TRAFFIC_OTHER_START
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 5_-_LOG_ID_TRAFFIC_OTHER_ICMP_ALLOW
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 6_-_LOG_ID_TRAFFIC_OTHER_ICMP_DENY
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 7_-_LOG_ID_TRAFFIC_OTHER_INVALID
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8_-_LOG_ID_TRAFFIC_WANOPT
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 9_-_LOG_ID_TRAFFIC_WEBCACHE
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

#### Event

##### 22096_-_LOG_ID_AUTOMATIC_UPGRADE_SUCCEEDED *(new)*

##### 22097_-_LOG_ID_AUTOMATIC_UPGRADE_FAILED *(new)*

##### 22920_-_LOG_ID_SVR_STATUS_CHANGED *(new)*

##### 43724_-_LOG_ID_EVENT_WIRELESS_WTPR_SKIP_CAC *(new)*

##### 46703_-_LOG_ID_INTERNAL_5G_MODEM_IPV4_LINK_STATE *(new)*

##### 46705_-_LOG_ID_INTERNAL_5G_MODEM_FW_UPGRADE *(new)*

##### 46708_-_LOG_ID_INTERNAL_5G_MODEM_MODE *(new)*

##### 46709_-_LOG_ID_INTERNAL_5G_MODEM_SIM_STATE *(new)*

##### 46710_-_LOG_ID_INTERNAL_5G_MODEM_SIM_SWITCH *(new)*

##### 46711_-_LOG_ID_INTERNAL_5G_MODEM_AUTO_SIM_SWITCH_REASON *(new)*

##### 46713_-_LOG_ID_INTERNAL_5G_MODEM_SIGNAL_MODE *(new)*

##### 53412_-_LOG_ID_EVENT_TELEMETRY_AGENT_ONLINE *(new)*

##### 53413_-_LOG_ID_EVENT_TELEMETRY_AGENT_OFFLINE *(new)*

##### 53414_-_LOG_ID_EVENT_TELEMETRY_AGENT_ADD *(new)*

##### 53415_-_LOG_ID_EVENT_TELEMETRY_AGENT_DELETE *(new)*

##### 20235_-_LOG_ID_SYS_SECURITY_MOUNT_VIOLATION *(removed)*

##### 32018_-_LOG_ID_FIPS_ENTER_ERR_MOD *(removed)*

##### 22090_-_LOG_ID_FEDERATED_UPGRADE_CANCELLED
- Field added: `upgradesource` (string, len: 80) — ""

##### 22091_-_LOG_ID_FEDERATED_UPGRADE_SUCCEEDED
- Field added: `upgradesource` (string, len: 80) — ""

##### 22092_-_LOG_ID_FEDERATED_UPGRADE_FAILED
- Field added: `upgradesource` (string, len: 80) — ""

##### 22094_-_LOG_ID_FEDERATED_UPGRADE_ROOT_COMPLETED
- Field added: `fgtcount` (uint32, len: 5) — ""
- Field added: `nodecount` (uint32, len: 5) — ""

##### 22095_-_LOG_ID_FEDERATED_UPGRADE_ROOT_NOT_COMPLETED
- Field added: `fgtcount` (uint32, len: 5) — ""
- Field added: `nodecount` (uint32, len: 5) — ""
- Field added: `upgradesource` (string, len: 80) — ""

##### 22800_-_LOG_ID_SCAN_SERV_FAIL
- Length changed: `mode` 12 → 32

##### 22907_-_LOG_ID_INPUT_DETECTION
- Length changed: `mode` 12 → 32

##### 22938_-_LOG_ID_EVENT_VWL_WAN_SPEEDTEST_RESULT
- Length changed: `mode` 12 → 32

##### 37127_-_MESGID_NEG_PROGRESS_P1_NOTIF
- Length changed: `mode` 12 → 32

##### 37128_-_MESGID_NEG_PROGRESS_P1_ERROR
- Length changed: `mode` 12 → 32

##### 37129_-_MESGID_NEG_PROGRESS_P2_NOTIF
- Length changed: `mode` 12 → 32

##### 37130_-_MESGID_NEG_PROGRESS_P2_ERROR
- Length changed: `mode` 12 → 32

##### 38422_-_LOGID_EVENT_ICBD_UPDATE_SUCCESS
- Field added: `server` (string, len: 64) — "Server IP Address"
- Field removed: `dstip` (ip)

##### 38423_-_LOGID_EVENT_ICBD_UPDATE_FAILURE
- Field added: `server` (string, len: 64) — "Server IP Address"
- Field removed: `dstip` (ip)

##### 47301_-_LOG_ID_EVENT_REST_API_OK
- Field added: `auditreporttype` (string, len: 20) — ""
- Field added: `audittime` (uint64, len: 20) — ""
- Field added: `criticalcount` (int32, len: 10) — ""
- Field added: `highcount` (int32, len: 10) — ""
- Field added: `lowcount` (int32, len: 10) — ""
- Field added: `mediumcount` (int32, len: 10) — ""
- Field added: `passedcount` (int32, len: 10) — ""

##### 47302_-_LOG_ID_EVENT_REST_API_ERR
- Field added: `auditreporttype` (string, len: 20) — ""
- Field added: `audittime` (uint64, len: 20) — ""
- Field added: `criticalcount` (int32, len: 10) — ""
- Field added: `highcount` (int32, len: 10) — ""
- Field added: `lowcount` (int32, len: 10) — ""
- Field added: `mediumcount` (int32, len: 10) — ""
- Field added: `passedcount` (int32, len: 10) — ""

##### 52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY
- Field removed: `auditid` (uint64)
- Field removed: `auditscore` (string)

##### 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE
- Field removed: `auditid` (uint64)
- Field removed: `auditscore` (string)

##### 52002_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_RESULT
- Field removed: `auditid` (uint64)
- Field removed: `auditscore` (string)

#### UTM

##### 24580_-_LOG_ID_DLP_FORTIDATA_ERROR_NOTIF *(new)*

##### 24581_-_LOG_ID_DLP_FORTIDATA_ERROR_WARNING *(new)*

##### 10000_-_LOG_ID_CASB_ACCESS_BLOCKED
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 10001_-_LOG_ID_CASB_ACCESS_BYPASS
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 10002_-_LOG_ID_CASB_ACCESS_MONITOR
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12288_-_LOG_ID_WEB_CONTENT_BANWORD
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12292_-_LOG_ID_WEB_CONTENT_KEYWORD
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12293_-_LOG_ID_WEB_CONTENT_SEARCH
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12544_-_LOG_ID_URL_FILTER_BLOCK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12545_-_LOG_ID_URL_FILTER_EXEMPT
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12546_-_LOG_ID_URL_FILTER_ALLOW
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12547_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_HTTP_BLK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12548_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_HTTPS_BLK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12549_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_HTTP_PASS
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12550_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_HTTPS_PASS
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12551_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_SNI_BLK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12552_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_SNI_PASS
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12553_-_LOG_ID_URL_FILTER_INVALID_CERT
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12554_-_LOG_ID_URL_FILTER_INVALID_SESSION
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12555_-_LOG_ID_URL_FILTER_SRV_CERT_ERR_BLK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12556_-_LOG_ID_URL_FILTER_SRV_CERT_ERR_PASS
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12559_-_LOG_ID_URL_FILTER_PASS
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12560_-_LOG_ID_URL_WISP_BLOCK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12561_-_LOG_ID_URL_WISP_REDIR
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12562_-_LOG_ID_URL_WISP_ALLOW
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12688_-_LOG_ID_WEB_SSL_EXEMPT
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12800_-_LOG_ID_WEB_FTGD_ERR
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 12801_-_LOG_ID_WEB_FTGD_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13056_-_LOG_ID_WEB_FTGD_CAT_BLK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13057_-_LOG_ID_WEB_FTGD_CAT_WARN
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13058_-_LOG_ID_WEB_FTGD_RISK_BLK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13312_-_LOG_ID_WEB_FTGD_CAT_ALLOW
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13313_-_LOG_ID_WEB_FTGD_RISK_ALLOW
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13315_-_LOG_ID_WEB_FTGD_QUOTA_COUNTING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13316_-_LOG_ID_WEB_FTGD_QUOTA_EXPIRED
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13317_-_LOG_ID_WEB_URL
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13318_-_LOG_ID_WEB_DOMAIN_FRONTING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13568_-_LOG_ID_WEB_SCRIPTFILTER_ACTIVEX
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13573_-_LOG_ID_WEB_SCRIPTFILTER_COOKIE
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13584_-_LOG_ID_WEB_SCRIPTFILTER_APPLET
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13600_-_LOG_ID_WEB_SCRIPTFILTER_OTHER
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13601_-_LOG_ID_WEB_WF_COOKIE
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13602_-_LOG_ID_WEB_WF_REFERER
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13603_-_LOG_ID_WEB_WF_COMMAND_BLOCK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13616_-_LOG_ID_CONTENT_TYPE_BLOCK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13617_-_LOG_ID_CONTENT_TYPE_EXEMPT
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13632_-_LOGID_HTTP_HDR_CHG_REQ
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13633_-_LOGID_HTTP_HDR_CHG_RESP
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13648_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_URL_ALLOW
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13649_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_FTGD_ALLOW
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13650_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_DEFAULT_ALLOW
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13651_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_URL_BLOCK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13652_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_FTGD_BLOCK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13653_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_DEFAULT_BLOCK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13680_-_LOG_ID_VIDEOFILTER_CHANNEL_BLOCK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13681_-_LOG_ID_VIDEOFILTER_CHANNEL_MONITOR
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13682_-_LOG_ID_VIDEOFILTER_CHANNEL_ALLOW
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13712_-_LOG_ID_VIDEOFILTER_TITLE_BLOCK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13713_-_LOG_ID_VIDEOFILTER_TITLE_MONITOR
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13714_-_LOG_ID_VIDEOFILTER_TITLE_ALLOW
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13728_-_LOG_ID_VIDEOFILTER_DESCRIPTION_BLOCK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13729_-_LOG_ID_VIDEOFILTER_DESCRIPTION_MONITOR
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 13730_-_LOG_ID_VIDEOFILTER_DESCRIPTION_ALLOW
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 16385_-_LOGID_ATTCK_SIGNATURE_ICMP
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 16399_-_LOGID_ATTACK_MALICIOUS_URL
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 16400_-_LOGID_ATTACK_BOTNET_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 16401_-_LOGID_ATTACK_BOTNET_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 16402_-_LOGID_ATTACK_SIGNATURE_L2
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 18433_-_LOGID_ATTCK_ANOMALY_ICMP
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 18434_-_LOGID_ATTCK_ANOMALY_OTHERS
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 20481_-_LOGID_EMAIL_GENERAL_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 20509_-_LOGID_ANTISPAM_FTGD_ERR
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 20510_-_LOGID_ANTISPAM_EMAIL_WEBMAIL_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 24576_-_LOG_ID_DLP_WARN
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `error` (string, len: 20) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 24577_-_LOG_ID_DLP_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `error` (string, len: 20) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 28704_-_LOGID_APP_CTRL_IPS_PASS
- Field added: `aiuser` (string, len: 64) — ""
- Field added: `cloudgenai` (string, len: 1024) — ""
- Field added: `dcgeo` (string, len: 64) — ""
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `model` (string, len: 64) — ""
- Field added: `prompt` (string, len: 512) — ""
- Field added: `srczone` (string, len: 32) — ""
- Field added: `usecase` (string, len: 64) — ""

##### 28705_-_LOGID_APP_CTRL_IPS_BLOCK
- Field added: `aiuser` (string, len: 64) — ""
- Field added: `cloudgenai` (string, len: 1024) — ""
- Field added: `dcgeo` (string, len: 64) — ""
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `model` (string, len: 64) — ""
- Field added: `prompt` (string, len: 512) — ""
- Field added: `srczone` (string, len: 32) — ""
- Field added: `usecase` (string, len: 64) — ""

##### 28706_-_LOGID_APP_CTRL_IPS_RESET
- Field added: `aiuser` (string, len: 64) — ""
- Field added: `cloudgenai` (string, len: 1024) — ""
- Field added: `dcgeo` (string, len: 64) — ""
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `model` (string, len: 64) — ""
- Field added: `prompt` (string, len: 512) — ""
- Field added: `srczone` (string, len: 32) — ""
- Field added: `usecase` (string, len: 64) — ""

##### 28736_-_LOGID_APP_CTRL_PORT_ENF
- Field added: `aiuser` (string, len: 64) — ""
- Field added: `cloudgenai` (string, len: 1024) — ""
- Field added: `dcgeo` (string, len: 64) — ""
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `model` (string, len: 64) — ""
- Field added: `prompt` (string, len: 512) — ""
- Field added: `srczone` (string, len: 32) — ""
- Field added: `usecase` (string, len: 64) — ""

##### 28737_-_LOGID_APP_CTRL_PROTO_ENF
- Field added: `aiuser` (string, len: 64) — ""
- Field added: `cloudgenai` (string, len: 1024) — ""
- Field added: `dcgeo` (string, len: 64) — ""
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `model` (string, len: 64) — ""
- Field added: `prompt` (string, len: 512) — ""
- Field added: `srczone` (string, len: 32) — ""
- Field added: `usecase` (string, len: 64) — ""

##### 28738_-_LOGID_APP_CTRL_DETECT_L2
- Field added: `aiuser` (string, len: 64) — ""
- Field added: `cloudgenai` (string, len: 1024) — ""
- Field added: `dcgeo` (string, len: 64) — ""
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `model` (string, len: 64) — ""
- Field added: `prompt` (string, len: 512) — ""
- Field added: `srczone` (string, len: 32) — ""
- Field added: `usecase` (string, len: 64) — ""

##### 30248_-_LOGID_WAF_SIGNATURE_BLOCK
- Field added: `srczone` (string, len: 32) — ""

##### 30249_-_LOGID_WAF_SIGNATURE_PASS
- Field added: `srczone` (string, len: 32) — ""

##### 30250_-_LOGID_WAF_SIGNATURE_ERASE
- Field added: `srczone` (string, len: 32) — ""

##### 30251_-_LOGID_WAF_CUSTOM_SIGNATURE_BLOCK
- Field added: `srczone` (string, len: 32) — ""

##### 30252_-_LOGID_WAF_CUSTOM_SIGNATURE_PASS
- Field added: `srczone` (string, len: 32) — ""

##### 30253_-_LOGID_WAF_METHOD_BLOCK
- Field added: `srczone` (string, len: 32) — ""

##### 30255_-_LOGID_WAF_ADDRESS_LIST_BLOCK
- Field added: `srczone` (string, len: 32) — ""

##### 30257_-_LOGID_WAF_CONSTRAINTS_BLOCK
- Field added: `srczone` (string, len: 32) — ""

##### 30258_-_LOGID_WAF_CONSTRAINTS_PASS
- Field added: `srczone` (string, len: 32) — ""

##### 30259_-_LOGID_WAF_URL_ACCESS_PERMIT
- Field added: `srczone` (string, len: 32) — ""

##### 30260_-_LOGID_WAF_URL_ACCESS_BYPASS
- Field added: `srczone` (string, len: 32) — ""

##### 30261_-_LOGID_WAF_URL_ACCESS_BLOCK
- Field added: `srczone` (string, len: 32) — ""

##### 44032_-_LOGID_EVENT_VOIP_SIP
- Field added: `attack` (string, len: 256) — ""
- Field added: `attackid` (uint32, len: 10) — ""

##### 54000_-_LOG_ID_DNS_QUERY
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 54200_-_LOG_ID_DNS_RESOLV_ERROR
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 54401_-_LOG_ID_DNS_URL_FILTER_ALLOW
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 54600_-_LOG_ID_DNS_BOTNET_IP
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 54601_-_LOG_ID_DNS_BOTNET_DOMAIN
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 54800_-_LOG_ID_DNS_FTGD_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 54801_-_LOG_ID_DNS_FTGD_ERROR
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 54802_-_LOG_ID_DNS_FTGD_CAT_ALLOW
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 54803_-_LOG_ID_DNS_FTGD_CAT_BLOCK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 54804_-_LOG_ID_DNS_SAFE_SEARCH
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 54805_-_LOG_ID_DNS_LOCAL
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 54806_-_LOG_ID_DNS_SVCPARAM_ECH
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 60000_-_LOG_ID_ICAP_SERVER_ERROR
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 60001_-_LOG_ID_ICAP_INFECTION_BLOCK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 60002_-_LOG_ID_ICAP_CONN_ERROR
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 61000_-_LOG_ID_SSH_COMMAND_BLOCK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 61002_-_LOG_ID_SSH_COMMAND_PASS
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 61003_-_LOG_ID_SSH_COMMAND_PASS_ALERT
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 61010_-_LOG_ID_SSH_CHANNEL_BLOCK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 61011_-_LOG_ID_SSH_CHANNEL_PASS
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 61012_-_LOG_ID_SSH_HOST_KEY_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 61013_-_LOG_ID_SSH_HOST_KEY_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 61014_-_LOG_ID_SSH_UNSUPPORT_PROTO_BLOCK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 61015_-_LOG_ID_SSH_UNSUPPORT_PROTO_PASS
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 62004_-_LOG_ID_SSL_EXEMPT_ADDR
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 62008_-_LOG_ID_SSL_EXEMPT_LOCAL_CATEGORY
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 62009_-_LOG_ID_SSL_EXEMPT_USER_CATEGORY
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 62100_-_LOG_ID_SSL_NEGOTIATION_INSPECT
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 62101_-_LOG_ID_SSL_NEGOTIATION_BLOCK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 62102_-_LOG_ID_SSL_NEGOTIATION_BYPASS
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 62103_-_LOG_ID_SSL_NEGOTIATION_INFO
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 62200_-_LOG_ID_SSL_SERVER_CERT_INFO
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 62220_-_LOG_ID_SSL_HANDSHAKE_INFO
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 62300_-_LOG_ID_SSL_ANOMALY_CERT_BLOCKLISTED
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 62301_-_LOG_ID_SSL_ANOMALY_CERT_RESIGN_TRUSTED
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 62302_-_LOG_ID_SSL_ANOMALY_CERT_RESIGN_UNTRUSTED
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 62303_-_LOG_ID_SSL_ANOMALY_CERT_BLOCKED
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 62304_-_LOG_ID_SSL_ANOMALY_CERT_SNI_MISMATCHED
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 62305_-_LOG_ID_SSL_ANOMALY_CERT_PROBE_FAILURE_BLOCK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 62306_-_LOG_ID_SSL_ANOMALY_CERT_PROBE_FAILURE_PASS
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 62307_-_LOG_ID_SSL_ANOMALY_CERT_SNI_MISMATCHED_INFO
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 62308_-_LOG_ID_SSL_ANOMALY_HANDSHAKE_FAILURE
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 62309_-_LOG_ID_SSL_ANOMALY_CERT_INVALID
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 64000_-_LOG_ID_FILE_FILTER_BLOCK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 64001_-_LOG_ID_FILE_FILTER_LOG
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 64600_-_LOG_ID_OT_VPATCH_BLOCK
- Field added: `dstzone` (string, len: 64) — ""
- Field added: `srczone` (string, len: 64) — ""

##### 64601_-_LOG_ID_OT_VPATCH_LOG
- Field added: `dstzone` (string, len: 64) — ""
- Field added: `srczone` (string, len: 64) — ""

##### 64610_-_LOG_ID_LOCALIN_VPATCH_BLOCK
- Field added: `dstzone` (string, len: 64) — ""
- Field added: `srczone` (string, len: 64) — ""

##### 64611_-_LOG_ID_LOCALIN_VPATCH_LOG
- Field added: `dstzone` (string, len: 64) — ""
- Field added: `srczone` (string, len: 64) — ""

##### 8192_-_MESGID_INFECT_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8193_-_MESGID_INFECT_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8194_-_MESGID_INFECT_MIME_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8195_-_MESGID_INFECT_MIME_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8200_-_MESGID_MIME_FILETYPE_EXE_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8201_-_MESGID_MIME_FILETYPE_EXE_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8202_-_MESGID_AVQUERY_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8203_-_MESGID_AVQUERY_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8204_-_MESGID_MIME_AVQUERY_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8205_-_MESGID_MIME_AVQUERY_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8206_-_MESGID_AV_EXEMPT_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8207_-_MESGID_MIME_AV_EXEMPT_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8212_-_MESGID_MALWARE_LIST_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8213_-_MESGID_MALWARE_LIST_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8214_-_MESGID_MIME_MALWARE_LIST_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8215_-_MESGID_MIME_MALWARE_LIST_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8216_-_MESGID_FILE_HASH_EMS_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8217_-_MESGID_FILE_HASH_EMS_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8219_-_MESGID_MIME_FILE_HASH_EMS_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8220_-_MESGID_ICB_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8221_-_MESGID_ICB_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8222_-_MESGID_MIME_ICB_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8223_-_MESGID_MIME_ICB_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8224_-_MESGID_ICB_TIMEOUT_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8225_-_MESGID_ICB_TIMEOUT_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8226_-_MESGID_MIME_ICB_TIMEOUT_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8227_-_MESGID_MIME_ICB_TIMEOUT_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8228_-_MESGID_ICB_ERROR_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8229_-_MESGID_ICB_ERROR_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8230_-_MESGID_MIME_ICB_ERROR_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8231_-_MESGID_MIME_ICB_ERROR_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8244_-_MESGID_MALWARE_STREAM_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8245_-_MESGID_MALWARE_STREAM_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8246_-_MESGID_MIME_MALWARE_STREAM_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8247_-_MESGID_MIME_MALWARE_STREAM_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8448_-_MESGID_BLOCK_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8450_-_MESGID_BLOCK_MIME_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8451_-_MESGID_BLOCK_MIME_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8452_-_MESGID_BLOCK_COMMAND
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8704_-_MESGID_OVERSIZE_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8705_-_MESGID_OVERSIZE_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8708_-_MESGID_OVERSIZE_STREAM_UNCOMP_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8709_-_MESGID_OVERSIZE_STREAM_UNCOMP_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8720_-_MESGID_SWITCH_PROTO_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8721_-_MESGID_SWITCH_PROTO_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8960_-_MESGID_SCAN_UNCOMPSIZELIMIT_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8961_-_MESGID_SCAN_UNCOMPSIZELIMIT_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8962_-_MESGID_SCAN_ARCHIVE_ENCRYPTED_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8963_-_MESGID_SCAN_ARCHIVE_ENCRYPTED_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8964_-_MESGID_SCAN_ARCHIVE_CORRUPTED_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8965_-_MESGID_SCAN_ARCHIVE_CORRUPTED_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8966_-_MESGID_SCAN_ARCHIVE_MULTIPART_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8967_-_MESGID_SCAN_ARCHIVE_MULTIPART_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8968_-_MESGID_SCAN_ARCHIVE_NESTED_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8969_-_MESGID_SCAN_ARCHIVE_NESTED_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8970_-_MESGID_SCAN_ARCHIVE_OVERSIZE_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8971_-_MESGID_SCAN_ARCHIVE_OVERSIZE_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8972_-_MESGID_SCAN_ARCHIVE_UNHANDLED_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8973_-_MESGID_SCAN_ARCHIVE_UNHANDLED_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8974_-_MESGID_SCAN_AV_ENGINE_LOAD_FAILED_ERROR
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8975_-_MESGID_SCAN_ARCHIVE_PARTIALLYCORRUPTED_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8976_-_MESGID_SCAN_ARCHIVE_PARTIALLYCORRUPTED_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8979_-_MESGID_SCAN_ARCHIVE_TIMEOUT_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8980_-_MESGID_SCAN_ARCHIVE_TIMEOUT_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8981_-_MESGID_SCAN_AV_CDR_INTERNAL_ERROR
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 8982_-_MESGID_SCAN_AV_MAX_MEMORY_REACHED_ERROR
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 9233_-_MESGID_ANALYTICS_SUBMITTED
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 9234_-_MESGID_ANALYTICS_INFECT_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 9235_-_MESGID_ANALYTICS_INFECT_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 9236_-_MESGID_ANALYTICS_INFECT_MIME_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 9237_-_MESGID_ANALYTICS_INFECT_MIME_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 9239_-_MESGID_CONTENT_DISARM_NOTIF
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 9240_-_MESGID_CONTENT_DISARM_WARNING
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `srczone` (string, len: 32) — ""

##### 9241_-_LOG_ID_UNKNOWN_CE_BLOCK
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `filename` (string, len: 256) — "File name"
- Field added: `srczone` (string, len: 32) — ""

##### 9242_-_LOG_ID_UNKNOWN_CE_BYPASS
- Field added: `dstzone` (string, len: 32) — ""
- Field added: `filename` (string, len: 256) — "File name"
- Field added: `srczone` (string, len: 32) — ""

---

### 7.6.4 → 7.6.5

**Summary:** 14 LOGID added, 0 removed | 289 fields added, 2 removed | 0 type changed | 0 descriptions changed | 0 lengths changed

#### Traffic

##### 26_-_LOG_ID_TRAFFIC_HTTP_TRANSACTION
- Field added: `msg` (string, len: 512) — "Log message"

#### Event

##### 20142_-_LOG_ID_SSFL_LIC_EXPIRE *(new)*

##### 22118_-_LOG_ID_HW_MONITOR_EMERGENCY *(new)*

##### 22119_-_LOG_ID_HW_MONITOR_WARNING *(new)*

##### 22120_-_LOG_ID_HW_MONITOR_NOTIF *(new)*

##### 43725_-_LOG_ID_EVENT_WIRELESS_WTPR_AI_DARRP_SUPPORT_START *(new)*

##### 43726_-_LOG_ID_EVENT_WIRELESS_WTPR_AI_DARRP_SUPPORT_STOP *(new)*

##### 43727_-_LOG_ID_EVENT_WIRELESS_WTPR_AI_DARRP_CHAN *(new)*

##### 43728_-_LOG_ID_EVENT_WIRELESS_WTPR_AI_DARRP_OPTIMIZATION_TRIGGER *(new)*

##### 43729_-_LOG_ID_EVENT_WIRELESS_WTP_AUTO_GEN_CERT_SUCC *(new)*

##### 43730_-_LOG_ID_EVENT_WIRELESS_WTP_AUTO_GEN_CERT_FAIL *(new)*

##### 43731_-_LOG_ID_EVENT_WIRELESS_STA_USERGROUP_UPDATE *(new)*

##### 46714_-_LOG_ID_INTERNAL_5G_MODEM_IPV6_LINK_STATE *(new)*

##### 47400_-_LOG_ID_WEB_SVC_MEMORY_PROFILE *(new)*

##### 47401_-_LOG_ID_WEB_SVC_RESTART *(new)*

##### 47301_-_LOG_ID_EVENT_REST_API_OK
- Field added: `durationtotal` (string, len: 10) — ""
- Field added: `endtime` (uint64, len: 16) — ""
- Field added: `membytes` (uint64, len: 16) — ""
- Field added: `memchange` (int32, len: 10) — ""
- Field added: `rss` (uint32, len: 16) — ""
- Field added: `starttime` (uint64, len: 16) — ""
- Field added: `subtask` (string, len: 256) — ""
- Field added: `task` (uint16, len: 5) — ""
- Field added: `totalsession` (uint32, len: 10) — "Total Number of Sessions"

##### 47302_-_LOG_ID_EVENT_REST_API_ERR
- Field added: `durationtotal` (string, len: 10) — ""
- Field added: `endtime` (uint64, len: 16) — ""
- Field added: `membytes` (uint64, len: 16) — ""
- Field added: `memchange` (int32, len: 10) — ""
- Field added: `rss` (uint32, len: 16) — ""
- Field added: `starttime` (uint64, len: 16) — ""
- Field added: `subtask` (string, len: 256) — ""
- Field added: `task` (uint16, len: 5) — ""
- Field added: `totalsession` (uint32, len: 10) — "Total Number of Sessions"

##### 52000_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_SUMMARY
- Field added: `durationtotal` (string, len: 10) — ""
- Field added: `endtime` (uint64, len: 16) — ""
- Field added: `membytes` (uint64, len: 16) — ""
- Field added: `memchange` (int32, len: 10) — ""
- Field added: `rss` (uint32, len: 16) — ""
- Field added: `starttime` (uint64, len: 16) — ""
- Field added: `subtask` (string, len: 256) — ""
- Field added: `task` (uint16, len: 5) — ""
- Field added: `totalsession` (uint32, len: 10) — "Total Number of Sessions"

##### 52001_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_CHANGE
- Field added: `durationtotal` (string, len: 10) — ""
- Field added: `endtime` (uint64, len: 16) — ""
- Field added: `membytes` (uint64, len: 16) — ""
- Field added: `memchange` (int32, len: 10) — ""
- Field added: `rss` (uint32, len: 16) — ""
- Field added: `starttime` (uint64, len: 16) — ""
- Field added: `subtask` (string, len: 256) — ""
- Field added: `task` (uint16, len: 5) — ""
- Field added: `totalsession` (uint32, len: 10) — "Total Number of Sessions"

##### 52002_-_LOG_ID_EVENT_SECURITY_AUDIT_FABRIC_RESULT
- Field added: `durationtotal` (string, len: 10) — ""
- Field added: `endtime` (uint64, len: 16) — ""
- Field added: `membytes` (uint64, len: 16) — ""
- Field added: `memchange` (int32, len: 10) — ""
- Field added: `rss` (uint32, len: 16) — ""
- Field added: `starttime` (uint64, len: 16) — ""
- Field added: `subtask` (string, len: 256) — ""
- Field added: `task` (uint16, len: 5) — ""
- Field added: `totalsession` (uint32, len: 10) — "Total Number of Sessions"

#### UTM

##### 10000_-_LOG_ID_CASB_ACCESS_BLOCKED
- Field added: `profilegroup` (string, len: 48) — ""

##### 10001_-_LOG_ID_CASB_ACCESS_BYPASS
- Field added: `profilegroup` (string, len: 48) — ""

##### 10002_-_LOG_ID_CASB_ACCESS_MONITOR
- Field added: `profilegroup` (string, len: 48) — ""

##### 12288_-_LOG_ID_WEB_CONTENT_BANWORD
- Field added: `profilegroup` (string, len: 48) — ""

##### 12290_-_LOG_ID_WEB_CONTENT_EXEMPTWORD
- Field added: `profilegroup` (string, len: 48) — ""

##### 12292_-_LOG_ID_WEB_CONTENT_KEYWORD
- Field added: `profilegroup` (string, len: 48) — ""

##### 12293_-_LOG_ID_WEB_CONTENT_SEARCH
- Field added: `profilegroup` (string, len: 48) — ""

##### 12544_-_LOG_ID_URL_FILTER_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 12545_-_LOG_ID_URL_FILTER_EXEMPT
- Field added: `profilegroup` (string, len: 48) — ""

##### 12546_-_LOG_ID_URL_FILTER_ALLOW
- Field added: `profilegroup` (string, len: 48) — ""

##### 12547_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_HTTP_BLK
- Field added: `profilegroup` (string, len: 48) — ""

##### 12548_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_HTTPS_BLK
- Field added: `profilegroup` (string, len: 48) — ""

##### 12549_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_HTTP_PASS
- Field added: `profilegroup` (string, len: 48) — ""

##### 12550_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_HTTPS_PASS
- Field added: `profilegroup` (string, len: 48) — ""

##### 12551_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_SNI_BLK
- Field added: `profilegroup` (string, len: 48) — ""

##### 12552_-_LOG_ID_URL_FILTER_INVALID_HOSTNAME_SNI_PASS
- Field added: `profilegroup` (string, len: 48) — ""

##### 12553_-_LOG_ID_URL_FILTER_INVALID_CERT
- Field added: `profilegroup` (string, len: 48) — ""

##### 12554_-_LOG_ID_URL_FILTER_INVALID_SESSION
- Field added: `profilegroup` (string, len: 48) — ""

##### 12555_-_LOG_ID_URL_FILTER_SRV_CERT_ERR_BLK
- Field added: `profilegroup` (string, len: 48) — ""

##### 12556_-_LOG_ID_URL_FILTER_SRV_CERT_ERR_PASS
- Field added: `profilegroup` (string, len: 48) — ""

##### 12558_-_LOG_ID_URL_FILTER_RATING_ERR
- Field added: `profilegroup` (string, len: 48) — ""

##### 12559_-_LOG_ID_URL_FILTER_PASS
- Field added: `profilegroup` (string, len: 48) — ""

##### 12560_-_LOG_ID_URL_WISP_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 12561_-_LOG_ID_URL_WISP_REDIR
- Field added: `profilegroup` (string, len: 48) — ""

##### 12562_-_LOG_ID_URL_WISP_ALLOW
- Field added: `profilegroup` (string, len: 48) — ""

##### 12688_-_LOG_ID_WEB_SSL_EXEMPT
- Field added: `profilegroup` (string, len: 48) — ""

##### 12800_-_LOG_ID_WEB_FTGD_ERR
- Field added: `profilegroup` (string, len: 48) — ""

##### 12801_-_LOG_ID_WEB_FTGD_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 13056_-_LOG_ID_WEB_FTGD_CAT_BLK
- Field added: `profilegroup` (string, len: 48) — ""

##### 13057_-_LOG_ID_WEB_FTGD_CAT_WARN
- Field added: `profilegroup` (string, len: 48) — ""

##### 13058_-_LOG_ID_WEB_FTGD_RISK_BLK
- Field added: `profilegroup` (string, len: 48) — ""

##### 13312_-_LOG_ID_WEB_FTGD_CAT_ALLOW
- Field added: `profilegroup` (string, len: 48) — ""

##### 13313_-_LOG_ID_WEB_FTGD_RISK_ALLOW
- Field added: `profilegroup` (string, len: 48) — ""

##### 13315_-_LOG_ID_WEB_FTGD_QUOTA_COUNTING
- Field added: `profilegroup` (string, len: 48) — ""

##### 13316_-_LOG_ID_WEB_FTGD_QUOTA_EXPIRED
- Field added: `profilegroup` (string, len: 48) — ""

##### 13317_-_LOG_ID_WEB_URL
- Field added: `profilegroup` (string, len: 48) — ""

##### 13318_-_LOG_ID_WEB_DOMAIN_FRONTING
- Field added: `profilegroup` (string, len: 48) — ""

##### 13568_-_LOG_ID_WEB_SCRIPTFILTER_ACTIVEX
- Field added: `profilegroup` (string, len: 48) — ""

##### 13573_-_LOG_ID_WEB_SCRIPTFILTER_COOKIE
- Field added: `profilegroup` (string, len: 48) — ""

##### 13584_-_LOG_ID_WEB_SCRIPTFILTER_APPLET
- Field added: `profilegroup` (string, len: 48) — ""

##### 13600_-_LOG_ID_WEB_SCRIPTFILTER_OTHER
- Field added: `profilegroup` (string, len: 48) — ""

##### 13601_-_LOG_ID_WEB_WF_COOKIE
- Field added: `profilegroup` (string, len: 48) — ""

##### 13602_-_LOG_ID_WEB_WF_REFERER
- Field added: `profilegroup` (string, len: 48) — ""

##### 13603_-_LOG_ID_WEB_WF_COMMAND_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 13616_-_LOG_ID_CONTENT_TYPE_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 13617_-_LOG_ID_CONTENT_TYPE_EXEMPT
- Field added: `profilegroup` (string, len: 48) — ""

##### 13632_-_LOGID_HTTP_HDR_CHG_REQ
- Field added: `profilegroup` (string, len: 48) — ""

##### 13633_-_LOGID_HTTP_HDR_CHG_RESP
- Field added: `profilegroup` (string, len: 48) — ""

##### 13648_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_URL_ALLOW
- Field added: `profilegroup` (string, len: 48) — ""

##### 13649_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_FTGD_ALLOW
- Field added: `profilegroup` (string, len: 48) — ""

##### 13650_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_DEFAULT_ALLOW
- Field added: `profilegroup` (string, len: 48) — ""

##### 13651_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_URL_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 13652_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_FTGD_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 13653_-_LOG_ID_WEB_WF_ANTIPHISH_MATCH_DEFAULT_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 13664_-_LOG_ID_VIDEOFILTER_CATEGORY_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 13665_-_LOG_ID_VIDEOFILTER_CATEGORY_MONITOR
- Field added: `profilegroup` (string, len: 48) — ""

##### 13666_-_LOG_ID_VIDEOFILTER_CATEGORY_ALLOW
- Field added: `profilegroup` (string, len: 48) — ""

##### 13680_-_LOG_ID_VIDEOFILTER_CHANNEL_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 13681_-_LOG_ID_VIDEOFILTER_CHANNEL_MONITOR
- Field added: `profilegroup` (string, len: 48) — ""

##### 13682_-_LOG_ID_VIDEOFILTER_CHANNEL_ALLOW
- Field added: `profilegroup` (string, len: 48) — ""

##### 13712_-_LOG_ID_VIDEOFILTER_TITLE_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 13713_-_LOG_ID_VIDEOFILTER_TITLE_MONITOR
- Field added: `profilegroup` (string, len: 48) — ""

##### 13714_-_LOG_ID_VIDEOFILTER_TITLE_ALLOW
- Field added: `profilegroup` (string, len: 48) — ""

##### 13728_-_LOG_ID_VIDEOFILTER_DESCRIPTION_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 13729_-_LOG_ID_VIDEOFILTER_DESCRIPTION_MONITOR
- Field added: `profilegroup` (string, len: 48) — ""

##### 13730_-_LOG_ID_VIDEOFILTER_DESCRIPTION_ALLOW
- Field added: `profilegroup` (string, len: 48) — ""

##### 16384_-_LOGID_ATTCK_SIGNATURE_TCP_UDP
- Field added: `profilegroup` (string, len: 48) — ""

##### 16385_-_LOGID_ATTCK_SIGNATURE_ICMP
- Field added: `profilegroup` (string, len: 48) — ""

##### 16386_-_LOGID_ATTCK_SIGNATURE_OTHERS
- Field added: `profilegroup` (string, len: 48) — ""

##### 16399_-_LOGID_ATTACK_MALICIOUS_URL
- Field added: `profilegroup` (string, len: 48) — ""

##### 16400_-_LOGID_ATTACK_BOTNET_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 16401_-_LOGID_ATTACK_BOTNET_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 16402_-_LOGID_ATTACK_SIGNATURE_L2
- Field added: `profilegroup` (string, len: 48) — ""

##### 18432_-_LOGID_ATTCK_ANOMALY_TCP_UDP
- Field added: `profilegroup` (string, len: 48) — ""

##### 18433_-_LOGID_ATTCK_ANOMALY_ICMP
- Field added: `profilegroup` (string, len: 48) — ""

##### 18434_-_LOGID_ATTCK_ANOMALY_OTHERS
- Field added: `profilegroup` (string, len: 48) — ""

##### 20480_-_LOGID_ANTISPAM_EMAIL_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 20481_-_LOGID_EMAIL_GENERAL_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 20482_-_LOGID_ANTISPAM_EMAIL_BWORD_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 20509_-_LOGID_ANTISPAM_FTGD_ERR
- Field added: `profilegroup` (string, len: 48) — ""

##### 20510_-_LOGID_ANTISPAM_EMAIL_WEBMAIL_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 24576_-_LOG_ID_DLP_WARN
- Field added: `profilegroup` (string, len: 48) — ""

##### 24577_-_LOG_ID_DLP_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 24578_-_LOG_ID_DLP_DOC_SOURCE
- Field added: `profilegroup` (string, len: 48) — ""

##### 24579_-_LOG_ID_DLP_DOC_SOURCE_ERROR
- Field added: `profilegroup` (string, len: 48) — ""

##### 24580_-_LOG_ID_DLP_FORTIDATA_ERROR_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 24581_-_LOG_ID_DLP_FORTIDATA_ERROR_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 28672_-_LOGID_APP_CTRL_IM_BASIC
- Field added: `profilegroup` (string, len: 48) — ""

##### 28673_-_LOGID_APP_CTRL_IM_BASIC_WITH_STATUS
- Field added: `profilegroup` (string, len: 48) — ""

##### 28674_-_LOGID_APP_CTRL_IM_BASIC_WITH_COUNT
- Field added: `profilegroup` (string, len: 48) — ""

##### 28675_-_LOGID_APP_CTRL_IM_FILE
- Field added: `profilegroup` (string, len: 48) — ""

##### 28676_-_LOGID_APP_CTRL_IM_CHAT
- Field added: `profilegroup` (string, len: 48) — ""

##### 28677_-_LOGID_APP_CTRL_IM_CHAT_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 28678_-_LOGID_APP_CTRL_IM_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 28704_-_LOGID_APP_CTRL_IPS_PASS
- Field added: `profilegroup` (string, len: 48) — ""

##### 28705_-_LOGID_APP_CTRL_IPS_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 28706_-_LOGID_APP_CTRL_IPS_RESET
- Field added: `profilegroup` (string, len: 48) — ""

##### 28720_-_LOGID_APP_CTRL_SSH_PASS
- Field added: `profilegroup` (string, len: 48) — ""

##### 28721_-_LOGID_APP_CTRL_SSH_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 28736_-_LOGID_APP_CTRL_PORT_ENF
- Field added: `profilegroup` (string, len: 48) — ""

##### 28737_-_LOGID_APP_CTRL_PROTO_ENF
- Field added: `profilegroup` (string, len: 48) — ""

##### 28738_-_LOGID_APP_CTRL_DETECT_L2
- Field added: `profilegroup` (string, len: 48) — ""

##### 30248_-_LOGID_WAF_SIGNATURE_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 30249_-_LOGID_WAF_SIGNATURE_PASS
- Field added: `profilegroup` (string, len: 48) — ""

##### 30250_-_LOGID_WAF_SIGNATURE_ERASE
- Field added: `profilegroup` (string, len: 48) — ""

##### 30251_-_LOGID_WAF_CUSTOM_SIGNATURE_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 30252_-_LOGID_WAF_CUSTOM_SIGNATURE_PASS
- Field added: `profilegroup` (string, len: 48) — ""

##### 30253_-_LOGID_WAF_METHOD_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 30255_-_LOGID_WAF_ADDRESS_LIST_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 30257_-_LOGID_WAF_CONSTRAINTS_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 30258_-_LOGID_WAF_CONSTRAINTS_PASS
- Field added: `profilegroup` (string, len: 48) — ""

##### 30259_-_LOGID_WAF_URL_ACCESS_PERMIT
- Field added: `profilegroup` (string, len: 48) — ""

##### 30260_-_LOGID_WAF_URL_ACCESS_BYPASS
- Field added: `profilegroup` (string, len: 48) — ""

##### 30261_-_LOGID_WAF_URL_ACCESS_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 44032_-_LOGID_EVENT_VOIP_SIP
- Field removed: `attack` (string)
- Field removed: `attackid` (uint32)

##### 54000_-_LOG_ID_DNS_QUERY
- Field added: `profilegroup` (string, len: 48) — ""

##### 54200_-_LOG_ID_DNS_RESOLV_ERROR
- Field added: `profilegroup` (string, len: 48) — ""

##### 54400_-_LOG_ID_DNS_URL_FILTER_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 54401_-_LOG_ID_DNS_URL_FILTER_ALLOW
- Field added: `profilegroup` (string, len: 48) — ""

##### 54600_-_LOG_ID_DNS_BOTNET_IP
- Field added: `profilegroup` (string, len: 48) — ""

##### 54601_-_LOG_ID_DNS_BOTNET_DOMAIN
- Field added: `profilegroup` (string, len: 48) — ""

##### 54800_-_LOG_ID_DNS_FTGD_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 54801_-_LOG_ID_DNS_FTGD_ERROR
- Field added: `profilegroup` (string, len: 48) — ""

##### 54802_-_LOG_ID_DNS_FTGD_CAT_ALLOW
- Field added: `profilegroup` (string, len: 48) — ""

##### 54803_-_LOG_ID_DNS_FTGD_CAT_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 54804_-_LOG_ID_DNS_SAFE_SEARCH
- Field added: `profilegroup` (string, len: 48) — ""

##### 54805_-_LOG_ID_DNS_LOCAL
- Field added: `profilegroup` (string, len: 48) — ""

##### 54806_-_LOG_ID_DNS_SVCPARAM_ECH
- Field added: `profilegroup` (string, len: 48) — ""

##### 60000_-_LOG_ID_ICAP_SERVER_ERROR
- Field added: `profilegroup` (string, len: 48) — ""

##### 60001_-_LOG_ID_ICAP_INFECTION_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 60002_-_LOG_ID_ICAP_CONN_ERROR
- Field added: `profilegroup` (string, len: 48) — ""

##### 61000_-_LOG_ID_SSH_COMMAND_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 61001_-_LOG_ID_SSH_COMMAND_BLOCK_ALERT
- Field added: `profilegroup` (string, len: 48) — ""

##### 61002_-_LOG_ID_SSH_COMMAND_PASS
- Field added: `profilegroup` (string, len: 48) — ""

##### 61003_-_LOG_ID_SSH_COMMAND_PASS_ALERT
- Field added: `profilegroup` (string, len: 48) — ""

##### 61010_-_LOG_ID_SSH_CHANNEL_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 61011_-_LOG_ID_SSH_CHANNEL_PASS
- Field added: `profilegroup` (string, len: 48) — ""

##### 61012_-_LOG_ID_SSH_HOST_KEY_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 61013_-_LOG_ID_SSH_HOST_KEY_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 61014_-_LOG_ID_SSH_UNSUPPORT_PROTO_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 61015_-_LOG_ID_SSH_UNSUPPORT_PROTO_PASS
- Field added: `profilegroup` (string, len: 48) — ""

##### 62004_-_LOG_ID_SSL_EXEMPT_ADDR
- Field added: `profilegroup` (string, len: 48) — ""

##### 62006_-_LOG_ID_SSL_EXEMPT_ALLOWLIST
- Field added: `profilegroup` (string, len: 48) — ""

##### 62007_-_LOG_ID_SSL_EXEMPT_FTGD_CATEGORY
- Field added: `profilegroup` (string, len: 48) — ""

##### 62008_-_LOG_ID_SSL_EXEMPT_LOCAL_CATEGORY
- Field added: `profilegroup` (string, len: 48) — ""

##### 62009_-_LOG_ID_SSL_EXEMPT_USER_CATEGORY
- Field added: `profilegroup` (string, len: 48) — ""

##### 62100_-_LOG_ID_SSL_NEGOTIATION_INSPECT
- Field added: `profilegroup` (string, len: 48) — ""

##### 62101_-_LOG_ID_SSL_NEGOTIATION_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 62102_-_LOG_ID_SSL_NEGOTIATION_BYPASS
- Field added: `profilegroup` (string, len: 48) — ""

##### 62103_-_LOG_ID_SSL_NEGOTIATION_INFO
- Field added: `profilegroup` (string, len: 48) — ""

##### 62200_-_LOG_ID_SSL_SERVER_CERT_INFO
- Field added: `profilegroup` (string, len: 48) — ""

##### 62220_-_LOG_ID_SSL_HANDSHAKE_INFO
- Field added: `profilegroup` (string, len: 48) — ""

##### 62300_-_LOG_ID_SSL_ANOMALY_CERT_BLOCKLISTED
- Field added: `profilegroup` (string, len: 48) — ""

##### 62301_-_LOG_ID_SSL_ANOMALY_CERT_RESIGN_TRUSTED
- Field added: `profilegroup` (string, len: 48) — ""

##### 62302_-_LOG_ID_SSL_ANOMALY_CERT_RESIGN_UNTRUSTED
- Field added: `profilegroup` (string, len: 48) — ""

##### 62303_-_LOG_ID_SSL_ANOMALY_CERT_BLOCKED
- Field added: `profilegroup` (string, len: 48) — ""

##### 62304_-_LOG_ID_SSL_ANOMALY_CERT_SNI_MISMATCHED
- Field added: `profilegroup` (string, len: 48) — ""

##### 62305_-_LOG_ID_SSL_ANOMALY_CERT_PROBE_FAILURE_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 62306_-_LOG_ID_SSL_ANOMALY_CERT_PROBE_FAILURE_PASS
- Field added: `profilegroup` (string, len: 48) — ""

##### 62307_-_LOG_ID_SSL_ANOMALY_CERT_SNI_MISMATCHED_INFO
- Field added: `profilegroup` (string, len: 48) — ""

##### 62308_-_LOG_ID_SSL_ANOMALY_HANDSHAKE_FAILURE
- Field added: `profilegroup` (string, len: 48) — ""

##### 62309_-_LOG_ID_SSL_ANOMALY_CERT_INVALID
- Field added: `profilegroup` (string, len: 48) — ""

##### 64000_-_LOG_ID_FILE_FILTER_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 64001_-_LOG_ID_FILE_FILTER_LOG
- Field added: `profilegroup` (string, len: 48) — ""

##### 64600_-_LOG_ID_OT_VPATCH_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 64601_-_LOG_ID_OT_VPATCH_LOG
- Field added: `profilegroup` (string, len: 48) — ""

##### 64610_-_LOG_ID_LOCALIN_VPATCH_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 64611_-_LOG_ID_LOCALIN_VPATCH_LOG
- Field added: `profilegroup` (string, len: 48) — ""

##### 8192_-_MESGID_INFECT_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8193_-_MESGID_INFECT_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8194_-_MESGID_INFECT_MIME_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8195_-_MESGID_INFECT_MIME_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8200_-_MESGID_MIME_FILETYPE_EXE_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8201_-_MESGID_MIME_FILETYPE_EXE_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8202_-_MESGID_AVQUERY_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8203_-_MESGID_AVQUERY_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8204_-_MESGID_MIME_AVQUERY_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8205_-_MESGID_MIME_AVQUERY_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8206_-_MESGID_AV_EXEMPT_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8207_-_MESGID_MIME_AV_EXEMPT_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8212_-_MESGID_MALWARE_LIST_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8213_-_MESGID_MALWARE_LIST_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8214_-_MESGID_MIME_MALWARE_LIST_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8215_-_MESGID_MIME_MALWARE_LIST_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8216_-_MESGID_FILE_HASH_EMS_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8217_-_MESGID_FILE_HASH_EMS_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8218_-_MESGID_MIME_FILE_HASH_EMS_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8219_-_MESGID_MIME_FILE_HASH_EMS_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8220_-_MESGID_ICB_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8221_-_MESGID_ICB_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8222_-_MESGID_MIME_ICB_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8223_-_MESGID_MIME_ICB_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8224_-_MESGID_ICB_TIMEOUT_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8225_-_MESGID_ICB_TIMEOUT_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8226_-_MESGID_MIME_ICB_TIMEOUT_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8227_-_MESGID_MIME_ICB_TIMEOUT_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8228_-_MESGID_ICB_ERROR_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8229_-_MESGID_ICB_ERROR_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8230_-_MESGID_MIME_ICB_ERROR_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8231_-_MESGID_MIME_ICB_ERROR_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8244_-_MESGID_MALWARE_STREAM_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8245_-_MESGID_MALWARE_STREAM_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8246_-_MESGID_MIME_MALWARE_STREAM_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8247_-_MESGID_MIME_MALWARE_STREAM_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8448_-_MESGID_BLOCK_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8450_-_MESGID_BLOCK_MIME_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8451_-_MESGID_BLOCK_MIME_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8452_-_MESGID_BLOCK_COMMAND
- Field added: `profilegroup` (string, len: 48) — ""

##### 8704_-_MESGID_OVERSIZE_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8705_-_MESGID_OVERSIZE_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8708_-_MESGID_OVERSIZE_STREAM_UNCOMP_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8709_-_MESGID_OVERSIZE_STREAM_UNCOMP_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8720_-_MESGID_SWITCH_PROTO_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8721_-_MESGID_SWITCH_PROTO_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8960_-_MESGID_SCAN_UNCOMPSIZELIMIT_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8961_-_MESGID_SCAN_UNCOMPSIZELIMIT_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8962_-_MESGID_SCAN_ARCHIVE_ENCRYPTED_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8963_-_MESGID_SCAN_ARCHIVE_ENCRYPTED_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8964_-_MESGID_SCAN_ARCHIVE_CORRUPTED_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8965_-_MESGID_SCAN_ARCHIVE_CORRUPTED_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8966_-_MESGID_SCAN_ARCHIVE_MULTIPART_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8967_-_MESGID_SCAN_ARCHIVE_MULTIPART_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8968_-_MESGID_SCAN_ARCHIVE_NESTED_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8969_-_MESGID_SCAN_ARCHIVE_NESTED_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8970_-_MESGID_SCAN_ARCHIVE_OVERSIZE_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8971_-_MESGID_SCAN_ARCHIVE_OVERSIZE_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8972_-_MESGID_SCAN_ARCHIVE_UNHANDLED_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8973_-_MESGID_SCAN_ARCHIVE_UNHANDLED_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8974_-_MESGID_SCAN_AV_ENGINE_LOAD_FAILED_ERROR
- Field added: `profilegroup` (string, len: 48) — ""

##### 8975_-_MESGID_SCAN_ARCHIVE_PARTIALLYCORRUPTED_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8976_-_MESGID_SCAN_ARCHIVE_PARTIALLYCORRUPTED_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8979_-_MESGID_SCAN_ARCHIVE_TIMEOUT_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 8980_-_MESGID_SCAN_ARCHIVE_TIMEOUT_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 8981_-_MESGID_SCAN_AV_CDR_INTERNAL_ERROR
- Field added: `profilegroup` (string, len: 48) — ""

##### 8982_-_MESGID_SCAN_AV_MAX_MEMORY_REACHED_ERROR
- Field added: `profilegroup` (string, len: 48) — ""

##### 9233_-_MESGID_ANALYTICS_SUBMITTED
- Field added: `profilegroup` (string, len: 48) — ""

##### 9234_-_MESGID_ANALYTICS_INFECT_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 9235_-_MESGID_ANALYTICS_INFECT_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 9236_-_MESGID_ANALYTICS_INFECT_MIME_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 9237_-_MESGID_ANALYTICS_INFECT_MIME_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 9239_-_MESGID_CONTENT_DISARM_NOTIF
- Field added: `profilegroup` (string, len: 48) — ""

##### 9240_-_MESGID_CONTENT_DISARM_WARNING
- Field added: `profilegroup` (string, len: 48) — ""

##### 9241_-_LOG_ID_UNKNOWN_CE_BLOCK
- Field added: `profilegroup` (string, len: 48) — ""

##### 9242_-_LOG_ID_UNKNOWN_CE_BYPASS
- Field added: `profilegroup` (string, len: 48) — ""

---

### 7.6.5 → 7.6.6

*(no changes)*

---

