class CloudDomainAPI:
    """
    Provides methods to manage cloud domains associated with a master domain.

    Cloud domains act as followers, mirroring changes made to the master domain.

    Attributes:
        _auth_params (callable): Function to retrieve authentication parameters.
        make_request (callable): Function to make HTTP requests to the ClouDNS API.
    """

    def __init__(self, auth_params, make_request):
        """
        Initializes the CloudDomainAPI instance with authentication parameters and request function.

        Args:
            auth_params (callable): Function that returns authentication parameters.
            make_request (callable): Function that makes HTTP requests to the ClouDNS API.
        """
        self._auth_params = auth_params
        self.make_request = make_request

    def add_cloud_domain(self, domain_name, cloud_domain_name):
        """
        Adds a new cloud domain to mirror changes from the master domain.

        Args:
            domain_name (str): Domain name of the master domain.
            cloud_domain_name (str): Domain name of the new domain to be added as cloud domain.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name, 'cloud-domain-name': cloud_domain_name})
        return self.make_request('dns/add-cloud-domain.json', method='POST', data=params)

    def delete_cloud_domain(self, domain_name):
        """
        Deletes a cloud domain associated with the master domain.

        Args:
            domain_name (str): Domain name of the master domain.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/delete-cloud-domain.json', method='POST', data=params)

    def change_cloud_master(self, domain_name):
        """
        Changes the master domain for a cloud domain.

        Args:
            domain_name (str): Domain name of the master domain.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/set-master-cloud-domain.json', method='POST', data=params)

    def list_cloud_domains(self, domain_name):
        """
        Lists all cloud domains associated with the specified master domain.

        Args:
            domain_name (str): Domain name of the master domain.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/list-cloud-domains.json', method='POST', data=params)