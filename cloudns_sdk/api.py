"""
ClouDNSAPI: Python wrapper for the ClouDNS API.

Author: Komal Paudyal ||
Email: komal.paudyal@icloud.com

This module provides a Python interface to interact with the ClouDNS API.
"""

import requests
from .rate_limit import rate_limited
from .exceptions import ClouDNSAPIException
from .failover import FailoverAPI
from .zone import DNSZoneAPI

class ClouDNSAPI:
    BASE_URL = "https://api.cloudns.net"
    RATE_LIMIT_PER_SECOND = 20

    def __init__(self, auth_id=None, auth_password=None):
        """
        Initializes the ClouDNSAPI instance with authentication credentials.

        Args:
            auth_id (int or str): The authentication ID for accessing the ClouDNS API.
            auth_password (str): The authentication password associated with the auth_id.
        """
        self.auth_id = auth_id
        self.auth_password = auth_password
        self.failover = FailoverAPI(self._auth_params, self.make_request)
        self.zone = DNSZoneAPI(self._auth_params, self.make_request, self.auth_id, self.auth_password)

    @rate_limited(RATE_LIMIT_PER_SECOND)
    def make_request(self, endpoint, method='GET', params=None, data=None):
        """
        Makes an HTTP request to the ClouDNS API.

        Args:
            endpoint (str): The API endpoint to send the request to (e.g., 'ip/get-my-ip.json').
            method (str): The HTTP method to use ('GET' or 'POST'). Default is 'GET'.
            params (dict): Optional. Query parameters for the request.
            data (dict): Optional. Data to send as the body of the request for POST methods.

        Returns:
            dict: JSON response from the API.

        Raises:
            ValueError: If an unsupported HTTP method is provided.
            ClouDNSAPIException: If the API responds with an error status code.
        """
        url = f"{self.BASE_URL}/{endpoint}"
        params = params or {}
        if method == 'GET':
            response = requests.get(url, params=params)
        elif method == 'POST':
            response = requests.post(url, data=data or {})
        else:
            raise ValueError("Unsupported HTTP method")

        if response.status_code != 200:
            raise ClouDNSAPIException(response.json())

        return response.json()

    def _auth_params(self, additional_params=None):
        """
        Constructs authentication parameters with optional additional parameters.

        Args:
            additional_params (dict): Optional. Additional parameters to include in the authentication.

        Returns:
            dict: Authentication parameters dictionary.
        """
        params = {
            'auth-id': self.auth_id,
            'auth-password': self.auth_password,
        }
        if additional_params:
            params.update(additional_params)
        return params

    def login(self):
        """
        Logs into the ClouDNS API using provided authentication credentials.

        Returns:
            dict: JSON response containing login status.
        """
        params = {
            'auth-id': self.auth_id,
            'auth-password': self.auth_password
        }
        return self.make_request('login/login.json', method='POST', data=params)

    def get_current_ip(self):
        """
        Retrieves the current IP address associated with the authenticated account.

        Returns:
            dict: JSON response containing the current IP address information.
        """
        return self.make_request('ip/get-my-ip.json', method='GET', params=self._auth_params())

    def get_account_balance(self):
        """
        Retrieves the account balance for the authenticated account.

        Returns:
            dict: JSON response containing the account balance information.
        """
        return self.make_request('account/get-balance.json', method='GET', params=self._auth_params())