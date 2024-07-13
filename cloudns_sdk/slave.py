

class SlaveZoneAPI:

    def __init__(self, auth_params, make_request):
        self._auth_params = auth_params
        self.make_request = make_request


    def add_master_server(self, domain_name, master_ip):
        params = self._auth_params({'domain-name': domain_name, 'master-ip': master_ip})
        return self.make_request('dns/add-master-server.json', method='GET', params=params)

    def delete_master_server(self, domain_name, master_id):
        params = self._auth_params({'domain-name': domain_name, 'master-id': master_id})
        return self.make_request('dns/delete-master-server.json', method='GET', params=params)

    def list_master_servers(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/master-servers.json', method='GET', params=params)

    def list_transfer_servers(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/available-secondary-servers.json', method='GET', params=params)

    def get_soa_of_server(self, domain_name, server_id):
        params = self._auth_params({'domain-name': domain_name, 'server-id': server_id})
        return self.make_request('dns/get-soa-secondary-zone.json', method='GET', params=params)

    def export_slave_zone(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/export-secondary-zone.json', method='GET', params=params)