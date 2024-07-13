class GeoDNSAPI:
    """
    Provides methods for managing GeoDNS locations and checking availability.

    This class allows listing GeoDNS locations for a domain and checking if GeoDNS is available.

    Args:
        auth_params (callable): Function or callable object that provides authentication parameters for API requests.
        make_request (callable): Function or callable object that executes HTTP requests to the API.

    Methods:
        list_geodns_locations(domain_name):
            Retrieves a list of GeoDNS locations configured for a specific domain.

        is_geodns_available():
            Checks the availability of GeoDNS for the authenticated account.

    """
    def __init__(self, auth_params, make_request):
        self._auth_params = auth_params
        self.make_request = make_request

    def list_geodns_locations(self, domain_name):
        """
        Retrieves a list of GeoDNS locations configured for a specific domain.

        Args:
            domain_name (str): Domain name for which to retrieve GeoDNS locations.

        Returns:
            dict: Response from the API containing GeoDNS locations for the domain.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/get-geodns-locations.json', method='GET', params=params)

    def is_geodns_available(self):
        """
        Checks the availability of GeoDNS for the authenticated account.

        Returns:
            dict: Response from the API indicating whether GeoDNS is available.
        """
        params = self._auth_params()
        return self.make_request('dns/is-geodns-available.json', method='GET', params=params)