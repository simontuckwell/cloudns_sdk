class TransferAPI:
    """
    Provides methods for zone transfers using AXFR, importing/exporting records in BIND format,
    and sharing zones with another ClouDNS user.

    Attributes:
        _auth_params (callable): Function to retrieve authentication parameters.
        make_request (callable): Function to make HTTP requests to the ClouDNS API.
        auth_id (str): Authentication ID for the ClouDNS API.
        auth_password (str): Authentication password for the ClouDNS API.
    """

    def __init__(self, auth_params, make_request, auth_id, auth_password):
        """
        Initializes the TransferAPI instance with authentication parameters,
        request function, and ClouDNS authentication credentials.

        Args:
            auth_params (callable): Function that returns authentication parameters.
            make_request (callable): Function that makes HTTP requests to the ClouDNS API.
            auth_id (str): Authentication ID for the ClouDNS API.
            auth_password (str): Authentication password for the ClouDNS API.
        """
        self._auth_params = auth_params
        self.make_request = make_request
        self.auth_id = auth_id
        self.auth_password = auth_password

    def import_via_axfr(self, domain_name, server):
        """
        Imports zone data using AXFR (DNS zone transfer) from a specified server.

        Args:
            domain_name (str): Domain name or reverse zone name to import via AXFR.
            server (str): IP address or hostname of the server to import from.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'server': server
        })
        return self.make_request('dns/axfr-import.json', method='GET', params=params)

    def axfr_add_ip(self, domain_name, ip):
        """
        Adds an IP address to allow AXFR zone transfers from for a specific domain.

        Args:
            domain_name (str): Domain name to add IP for AXFR.
            ip (str): IP address of the server to add for AXFR.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name, 'ip': ip})
        return self.make_request('dns/axfr-add.json', method='POST', data=params)

    def axfr_delete_ip(self, domain_name, id):
        """
        Deletes an IP address used for AXFR zone transfers from a specific domain.

        Args:
            domain_name (str): Domain name to delete IP from AXFR.
            id (str): ID of the IP address entry to delete.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name, 'id': id})
        return self.make_request('dns/axfr-remove.json', method='POST', data=params)

    def axfr_list_ips(self, domain_name):
        """
        Lists IP addresses allowed for AXFR zone transfers for a specific domain.

        Args:
            domain_name (str): Domain name to list AXFR IPs.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/axfr-list.json', method='GET', params=params)

    def import_records(self, domain_name, format='bind', content='', delete_existing_records=False, record_types=None):
        """
        Imports DNS records for a domain in BIND or TinyDNS format.

        Args:
            domain_name (str): Domain name to import records for.
            format (str): Format of the records ('bind' or 'tinydns'). Default is 'bind'.
            content (str): Content of the records in the chosen format.
            delete_existing_records (bool): Whether to delete existing records before importing. Default is False.
            record_types (list): Optional list of record types to import.

        Returns:
            dict: JSON response from the API.
        """
        params = [
            ('auth-id', self.auth_id),
            ('auth-password', self.auth_password),
            ('domain-name', domain_name),
            ('format', format),
            ('content', content)
        ]

        if record_types:
            for type in record_types:
                params.append(('record-types[]', type))

        if delete_existing_records:
            params.append(('delete-existing-records', 1))
        else:
            params.append(('delete-existing-records', 0))

        return self.make_request('dns/records-import.json', method='POST', data=params)

    def export_records_in_bind(self, domain_name):
        """
        Exports DNS records for a domain in BIND format.

        Args:
            domain_name (str): Domain name to export records for.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/records-export.json', method='POST', data=params)

    def list_shared_accounts(self, domain_name):
        """
        Lists shared accounts for a specific domain.

        Args:
            domain_name (str): Domain name to list shared accounts.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/list-shared-accounts.json', method='GET', params=params)

    def add_shared_account(self, domain_name, mail):
        """
        Adds a shared account (user) for a specific domain.

        Args:
            domain_name (str): Domain name to add shared account to.
            mail (str): Email address of the shared account.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name, 'mail': mail})
        return self.make_request('dns/add-shared-account.json', method='POST', data=params)

    def remove_shared_account(self, domain_name, mail):
        """
        Removes a shared account (user) from a specific domain.

        Args:
            domain_name (str): Domain name to remove shared account from.
            mail (str): Email address of the shared account.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name, 'mail': mail})
        return self.make_request('dns/remove-shared-account.json', method='POST', data=params)