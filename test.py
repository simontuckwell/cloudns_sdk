from cloudns_sdk import ClouDNSAPI
from cloudns_sdk.validations import validate

id = 22889
key = 'komal123'

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



domain_name = "jointcove.com"
zone_type = "master"
server='ns1.dnsowl.com'

res1 = api.login()
print(res1)
res = api.import_via_transfer(domain_name, server)
print(res)





