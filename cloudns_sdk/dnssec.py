

class DNSSECAPI:

    def __init__(self, auth_params, make_request):
        self._auth_params = auth_params
        self.make_request = make_request

    def is_dnssec_available(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/is-dnssec-available.json', method='GET', params=params)


    def activate_dnssec(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/activate-dnssec.json', method='POST', data=params)

    def deactivate_dnssec(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/deactivate-dnssec.json', method='POST', data=params)

    def get_ds_records(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/get-dnssec-ds-records.json', method='GET', params=params)


    def change_dnssec_optout(self, domain_name, status=True):
        params = self._auth_params({'domain-name': domain_name, 'status': 1 if status else 0})
        return self.make_request('dns/set-dnssec-optout.json', method='POST', data=params)

