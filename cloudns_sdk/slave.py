class SlaveZoneAPI:
    """
    Provides methods to manage slave zones.

    Attributes:
        _auth_params (callable): Function to retrieve authentication parameters.
        make_request (callable): Function to make HTTP requests to the ClouDNS API.
    """

    def __init__(self, auth_params, make_request):
        """
        Initializes the SlaveZoneAPI instance with authentication parameters and request function.

        Args:
            auth_params (callable): Function that returns authentication parameters.
            make_request (callable): Function that makes HTTP requests to the ClouDNS API.
        """
        self._auth_params = auth_params
        self.make_request = make_request

    def add_master_server(self, domain_name, master_ip):
        """
        Adds a master server to a slave zone.

        Args:
            domain_name (str): Domain name or reverse zone name where the master server is to be added.
            master_ip (str): IP address of the master server.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name, 'master-ip': master_ip})
        return self.make_request('dns/add-master-server.json', method='GET', params=params)

    def delete_master_server(self, domain_name, master_id):
        """
        Deletes a master server from a slave zone.

        Args:
            domain_name (str): Domain name or reverse zone name from where the master server is to be deleted.
            master_id (int): ID of the master server, obtained from `list_master_servers`.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name, 'master-id': master_id})
        return self.make_request('dns/delete-master-server.json', method='GET', params=params)

    def list_master_servers(self, domain_name):
        """
        Lists all master servers associated with a slave zone.

        Args:
            domain_name (str): Domain name or reverse zone name to list master servers for.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/master-servers.json', method='GET', params=params)

    def list_transfer_servers(self, domain_name):
        """
        Lists available secondary servers for transferring a slave zone.

        Args:
            domain_name (str): Domain name or reverse zone name to list available secondary servers for.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/available-secondary-servers.json', method='GET', params=params)

    def get_soa_of_server(self, domain_name, server_id):
        """
        Retrieves SOA details of a secondary server for a slave zone.

        Args:
            domain_name (str): Domain name or reverse zone name to retrieve SOA details for.
            server_id (int): ID of the server, obtained from `list_transfer_servers`.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name, 'server-id': server_id})
        return self.make_request('dns/get-soa-secondary-zone.json', method='GET', params=params)

    def export_slave_zone(self, domain_name):
        """
        Exports the configuration of a slave zone.

        Args:
            domain_name (str): Domain name or reverse zone name to export configuration for.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/export-secondary-zone.json', method='GET', params=params)