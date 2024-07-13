class SSLAPI:
    """
    Provides methods for issuing and managing SSL certificates.

    Attributes:
        _auth_params (callable): Function to retrieve authentication parameters.
        make_request (callable): Function to make HTTP requests to the ClouDNS API.
    """

    def __init__(self, auth_params, make_request):
        """
        Initializes the SSLAPI instance with authentication parameters and request function.

        Args:
            auth_params (callable): Function that returns authentication parameters.
            make_request (callable): Function that makes HTTP requests to the ClouDNS API.
        """
        self._auth_params = auth_params
        self.make_request = make_request

    def activate_free_ssl(self, domain_name, issuer=2):
        """
        Activates free SSL certificate for a domain using a specified issuer.

        Args:
            domain_name (str): Domain name to activate Free SSL for.
            issuer (int): Issuer ID (1 for ZeroSSL, 2 for Let's Encrypt). Default is 2.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'issuer': issuer
        })
        return self.make_request('dns/freessl-activate.json', method='POST', data=params)

    def deactivate_free_ssl(self, domain_name):
        """
        Deactivates free SSL certificate for a domain.

        Args:
            domain_name (str): Domain name to deactivate Free SSL for.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({
            'domain-name': domain_name
        })
        return self.make_request('dns/freessl-deactivate.json', method='POST', data=params)

    def get_free_ssl_data(self, domain_name):
        """
        Retrieves data of the free SSL certificate for a domain.

        Args:
            domain_name (str): Domain name to retrieve Free SSL data for.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({
            'domain-name': domain_name
        })
        return self.make_request('dns/freessl-get.json', method='GET', params=params)

    def change_free_ssl_issuer(self, domain_name, issuer=2):
        """
        Changes the issuer of the free SSL certificate for a domain.

        Args:
            domain_name (str): Domain name to change Free SSL issuer for.
            issuer (int): Issuer ID (1 for ZeroSSL, 2 for Let's Encrypt). Default is 2.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'issuer': issuer
        })
        return self.make_request('dns/freessl-change-issuer.json', method='POST', data=params)