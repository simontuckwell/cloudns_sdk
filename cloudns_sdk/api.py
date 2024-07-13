import requests
from .rate_limit import rate_limited
from .exceptions import ClouDNSAPIException
from .failover import FailoverAPI
from .zone import DNSZoneAPI


class ClouDNSAPI:
    BASE_URL = "https://api.cloudns.net"
    RATE_LIMIT_PER_SECOND = 20

    def __init__(self, auth_id=None, auth_password=None):
        self.auth_id = auth_id
        self.auth_password = auth_password
        self.failover = FailoverAPI(self._auth_params, self.make_request)
        self.zone = DNSZoneAPI(self._auth_params, self.make_request, self.auth_id, self.auth_password)


    @rate_limited(RATE_LIMIT_PER_SECOND)
    def make_request(self, endpoint, method='GET', params=None, data=None):
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
        params = {
            'auth-id': self.auth_id,
            'auth-password': self.auth_password,
        }
        if additional_params:
            params.update(additional_params)
        return params

    def login(self):
        params = {
            'auth-id': self.auth_id,
            'auth-password': self.auth_password
        }
        return self.make_request('login/login.json', method='POST', data=params)

    def get_current_ip(self):
        return self.make_request('ip/get-my-ip.json', method='GET', params=self._auth_params())

    def get_account_balance(self):
        return self.make_request('account/get-balance.json', method='GET', params=self._auth_params())






