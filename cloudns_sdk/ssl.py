


class SSLAPI:

    def __init__(self, auth_params, make_request):
        self._auth_params = auth_params
        self.make_request = make_request


    def activate_free_ssl(self, domain_name, issuer=2):
        params = self._auth_params({
            'domain-name': domain_name,
            'issuer': issuer
        })
        return self.make_request('dns/freessl-activate.json', method='POST', data=params)


    def deactivate_free_ssl(self, domain_name):
        params = self._auth_params({
            'domain-name': domain_name
        })
        return self.make_request('dns/freessl-deactivate.json', method='POST', data=params)


    def get_free_ssl_data(self, domain_name):
        params = self._auth_params({
            'domain-name': domain_name
        })
        return self.make_request('dns/freessl-get.json', method='GET', params=params)


    def change_free_ssl_issuer(self, domain_name, issuer=2):
        params = self._auth_params({
            'domain-name': domain_name,
            'issuer': issuer
        })
        return self.make_request('dns/freessl-change-issuer.json', method='POST', data=params)