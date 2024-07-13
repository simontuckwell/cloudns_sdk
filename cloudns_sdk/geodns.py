

class GeoDNSAPI:
    def __init__(self, auth_params, make_request):
        self._auth_params = auth_params
        self.make_request = make_request


    def list_geodns_locations(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/get-geodns-locations.json', method='GET', params=params)

    def is_geodns_available(self):
        params = self._auth_params()
        return self.make_request('dns/is-geodns-available.json', method='GET', params=params)