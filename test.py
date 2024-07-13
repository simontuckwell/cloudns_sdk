
from cloudns_sdk import ClouDNSAPI
from cloudns_sdk.validations import validate

id = 22889
key = 'komal123'

api = ClouDNSAPI(id, key)

#here we are using the same instance of API class for both GET and POST method.
res = api.zone.ssl.activate_free_ssl()

print(res)






