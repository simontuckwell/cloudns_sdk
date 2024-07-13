
class CloudDomainAPI:

    def __init__(self, auth_params, make_request):
        self._auth_params = auth_params
        self.make_request = make_request


    def add_cloud_domain(self, domain_name, cloud_domain_name):
        params = self._auth_params({'domain-name': domain_name, 'cloud-domain-name': cloud_domain_name})
        return self.make_request('dns/add-cloud-domain.json', method='POST', data=params)

    def delete_cloud_domain(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/delete-cloud-domain.json', method='POST', data=params)

    def change_cloud_master(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/set-master-cloud-domain.json', method='POST', data=params)

    def list_cloud_domains(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/list-cloud-domains.json', method='POST', data=params)