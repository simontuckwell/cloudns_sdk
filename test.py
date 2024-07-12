from cloudns_sdk import ClouDNSAPI
from cloudns_sdk.validations import validate

id = 22889
key = 'srizana'

domain_name = "demosrizana.dns-dynamic.net"
zone_type = "master"
name_servers = ["pns1.cloudns.net", "pns2.cloudns.net"]
api = ClouDNSAPI(id, key)





params = {

    "domain_name": "example.com",
    "record_type": "TLSA",
    "host": "_443._tcp.example.com",
    "record": "1 1 1 abcdef",
    "ttl": 3600,
    "priority": 10,
    "tlsa_usage": 0,
    "tlsa_selector": 1,
    "tlsa_matching_type": 2,
    "algorithm": "RSA",
    "fptype": 1,
    "caa_type": 'issuekl',
}





res = api.add_record(
    domain_name="demosrizana.dns-dynamic.net",
    record_type="A",
    host="test",
    record="1.1.1.1",
    ttl=3600,
    enabled=True
)


print(res)





