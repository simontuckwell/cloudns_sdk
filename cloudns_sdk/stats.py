class StatsAPI:
    """
    Provides methods to retrieve zone statistics.

    Attributes:
        _auth_params (callable): Function to retrieve authentication parameters.
        make_request (callable): Function to make HTTP requests to the ClouDNS API.
    """

    def __init__(self, auth_params, make_request):
        """
        Initializes the StatsAPI instance with authentication parameters and request function.

        Args:
            auth_params (callable): Function that returns authentication parameters.
            make_request (callable): Function that makes HTTP requests to the ClouDNS API.
        """
        self._auth_params = auth_params
        self.make_request = make_request

    def get_hourly_stats(self, domain_name, day, month, year):
        """
        Retrieves hourly statistics for a domain on a specific day, month, and year.

        Args:
            domain_name (str): Domain name or reverse zone name to retrieve hourly statistics for.
            day (int): Day of the month (1-31).
            month (int): Month (1-12).
            year (int): Year.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name, 'day': day, 'month': month, 'year': year})
        return self.make_request('dns/statistics-hourly.json', method='GET', params=params)

    def get_daily_stats(self, domain_name, month, year):
        """
        Retrieves daily statistics for a domain in a specific month and year.

        Args:
            domain_name (str): Domain name or reverse zone name to retrieve daily statistics for.
            month (int): Month (1-12).
            year (int): Year.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name, 'month': month, 'year': year})
        return self.make_request('dns/statistics-daily.json', method='GET', params=params)

    def get_monthly_stats(self, domain_name, year):
        """
        Retrieves monthly statistics for a domain in a specific year.

        Args:
            domain_name (str): Domain name or reverse zone name to retrieve monthly statistics for.
            year (int): Year.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name, 'year': year})
        return self.make_request('dns/statistics-monthly.json', method='GET', params=params)

    def get_yearly_stats(self, domain_name):
        """
        Retrieves yearly statistics for a domain.

        Args:
            domain_name (str): Domain name or reverse zone name to retrieve yearly statistics for.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/statistics-yearly.json', method='GET', params=params)

    def get_last_30_days_stats(self, domain_name):
        """
        Retrieves statistics for the last 30 days for a domain.

        Args:
            domain_name (str): Domain name or reverse zone name to retrieve last 30 days statistics for.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/statistics-last-30-days.json', method='GET', params=params)