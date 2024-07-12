from cloudns_sdk import ClouDNSAPI
from cloudns_sdk.validations import validate

id = 22889
key = 'srizana'

domain_name = "demosrizana.dns-dynamic.net"
zone_type = "master"
name_servers = ["pns1.cloudns.net", "pns2.cloudns.net"]
# api = ClouDNSAPI(id, key)
# response = api.get_record(domain_name, record_id='509121146')
#
# print("Response:", response)


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

def mock_dns_record(domain_name, record_type, host, record, ttl, priority=None, **kwargs):


    # Prepare the DNS record data
    record_data = {key: value for key, value in locals().items() if key != 'kwargs' and value is not None}
    record_data.update(kwargs)

    result, msg = validate(record_data)

    if (result):
        print('Success')
    else:
        print(msg)



mock_dns_record(
    domain_name="example.com",
    record_type="TLSA",
    host="_443._tcp.example.com",
    record="1 1 1 abcdef",
    ttl=3600,
    priority=10,
    tlsa_usage=0,
    tlsa_selector=1,
    tlsa_matching_type=2,
    algorithm="RSA",
    fptype=1,
    caa_type='issuewild',  # Corrected CAA type
    comment="This is a mock DNS record",
    enabled=True
)






