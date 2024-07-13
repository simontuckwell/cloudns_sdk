
from cloudns_sdk import ClouDNSAPI
from cloudns_sdk.validations import validate

id = 111111111
key = 'yourpass'

api = ClouDNSAPI(id, key)


res = api.login()

print(res)






