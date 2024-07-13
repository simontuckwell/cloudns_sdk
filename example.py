
from cloudns_sdk import ClouDNSAPI
from cloudns_sdk.validations import validate

id = 22969
key = '152207'

api = ClouDNSAPI(id, key)


res = api.zone.records.add_record('jointcove.com', 'A', '1.3.3.1')

print(res)






