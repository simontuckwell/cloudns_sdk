
from cloudns_sdk import ClouDNSAPI
from cloudns_sdk.validations import validate

id = 101010
key = '1@mypass'

api = ClouDNSAPI(id, key)


res = api.zone.records.add_record('example.com', 'A', '1.3.3.1')

print(res)






