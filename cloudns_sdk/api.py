import requests
from .rate_limit import rate_limited
from .exceptions import ClouDNSAPIException
from .validations import validate
from .utils import process_params

class ClouDNSAPI:
    BASE_URL = "https://api.cloudns.net"
    RATE_LIMIT_PER_SECOND = 20
    VALID_ZONE_TYPES = ['domain', 'reverse', 'parked', 'master', 'slave', 'geodns']

    def __init__(self, auth_id=None, auth_password=None):
        self.auth_id = auth_id
        self.auth_password = auth_password

    def is_valid_zone_type(self, zone_type):
        return zone_type in self.VALID_ZONE_TYPES

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

    def get_available_name_servers(self, detailed_info=0):
        params = self._auth_params({'detailed-info': detailed_info})
        return self.make_request('dns/available-name-servers.json', method='GET', params=params)

    def register_domain_zone(self, domain_name, zone_type, ns=None, master_ip=None):
        params = [
            ('auth-id', self.auth_id),
            ('auth-password', self.auth_password),
            ('domain-name', domain_name),
            ('zone-type', zone_type)
        ]

        if ns:
            for ns_server in ns:
                params.append(('ns[]', ns_server))

        if master_ip:
            params.append(('master-ip', master_ip))

        print(params)

        return self.make_request('dns/register.json', method='GET', params=params)

    def delete_domain_zone(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/delete.json', method='POST', params=params)

    def list_zones(self, page=1, rows_per_page=20, search=None, group_id=None, has_cloud_domains=None):
        params = self._auth_params({
            'page': page,
            'rows-per-page': rows_per_page,
            'search': search,
            'group-id': group_id,
            'has-cloud-domains': has_cloud_domains
        })
        return self.make_request('dns/list-zones.json', method='GET', params=params)

    def get_pages_count(self, rows_per_page=10, search=None, group_id=None, has_cloud_domains=None):
        params = self._auth_params({
            'rows-per-page': rows_per_page,
            'search': search,
            'group-id': group_id,
            'has-cloud-domains': has_cloud_domains
        })
        return self.make_request('dns/get-pages-count.json', method='GET', params=params)

    def get_zones_stats(self):
        return self.make_request('dns/get-zones-stats.json', method='GET', params=self._auth_params())

    def get_zone_info(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/get-zone-info.json', method='GET', params=params)

    def update_zone(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/update-zone.json', method='POST', params=params)

    def get_update_status(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/update-status.json', method='GET', params=params)

    def is_updated(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/is-updated.json', method='GET', params=params)

    def change_zone_status(self, domain_name, status=True):
        params = self._auth_params({'domain-name': domain_name, 'status': 1 if status else 0})
        return self.make_request('dns/change-status.json', method='POST', params=params)

    def get_records_stats(self):
        return self.make_request('dns/get-records-stats.json', method='GET', params=self._auth_params())

    def get_record(self, domain_name, record_id):
        params = self._auth_params({'domain-name': domain_name, 'record-id': record_id})
        return self.make_request('dns/get-record.json', method='GET', params=params)

    def list_records(self, domain_name, host=None, host_like=None, record_type=None,
                     rows_per_page=20, page=1, order_by=None):
        params = self._auth_params({
            'domain-name': domain_name,
            'host': host,
            'host-like': host_like,
            'type': record_type,
            'rows-per-page': rows_per_page,
            'page': page,
            'order-by': order_by
        })
        return self.make_request('dns/records.json', method='GET', params=params)

    def get_records_pages_count(self, domain_name, host=None, record_type=None, rows_per_page=20):
        params = self._auth_params({
            'domain-name': domain_name,
            'host': host,
            'type': record_type,
            'rows-per-page': rows_per_page
        })
        return self.make_request('dns/get-records-pages-count.json', method='GET', params=params)

    def add_record(self, domain_name, record_type, record=None, host='', ttl=3600, **kwargs):
        record_data = {key: value for key, value in locals().items() if key != 'kwargs' and value is not None}
        record_data.update(kwargs)

        valid, error = validate(record_data)

        if valid:

            cred = self._auth_params()
            params = process_params(record_data, cred)

            return self.make_request('dns/add-record.json', method='POST', data=params)
        else:
            raise ValueError(f"Error: {error}")

    def delete_record(self, domain_name, record_id):
        params = self._auth_params({
            'domain-name': domain_name,
            'record-id': record_id
        })
        return self.make_request('dns/delete-record.json', method='POST', params=params)

    def modify_record(self, domain_name, record_id, host='', record=None, ttl=3600, **kwargs):

        record_data = {key: value for key, value in locals().items() if key != 'kwargs' and value is not None}
        record_data.update(kwargs)

        valid, error = validate(record_data)

        if valid:

            cred = self._auth_params()
            params = process_params(record_data, cred)
            return self.make_request('dns/mod-record.json', method='POST', data=params)

        else:
            raise ValueError(f"Error: {error}")

    def copy_records(self, domain_name, from_domain, delete_current_records=False):
        params = self._auth_params({
            'domain-name': domain_name,
            'from-domain': from_domain,
            'delete-current-records': 1 if delete_current_records else 0
        })

        return self.make_request('dns/copy-records.json', method='POST', params=params)


    def import_records(self, domain_name, format='bind', content='', delete_exisiting_records=False, record_types=None):
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

        if delete_exisiting_records:
            params.append(('delete-existing-records', 1))
        else:
            params.append(('delete-existing-records', 0))

        return self.make_request('dns/records-import.json', method='POST', params=params)


    def export_records_in_bind(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/records-export.json', method='POST', params=params)

    def get_available_record_types(self, zone_type):
        if not self.is_valid_zone_type(zone_type):
            raise ValueError(f"Invalid zone type: {zone_type}. Expected one of {', '.join(self.VALID_ZONE_TYPES)}.")

        params = self._auth_params({'zone-type': zone_type})

        return self.make_request('dns/get-available-record-types.json', method='GET', params=params)


    def get_available_ttl(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/get-available-ttl.json', method='GET', params=params)


    def get_records_count(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/get-records-count.json', method='GET', params=params)


    def get_soa_details(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/soa-details.json', method='GET', params=params)


    def modify_soa_details(self, domain_name, primary_ns, admin_email='', refresh=7200, retry=7200, expire=2419200, default_ttl=3600):
        record_data = {key: value for key, value in locals().items() if key != 'kwargs' and value is not None}

        valid, error = validate(record_data)
        if valid:
            params = self._auth_params({
                'domain-name': domain_name,
                'primary-ns': primary_ns,
                'admin-email': admin_email,
                'refresh': refresh,
                'retry': retry,
                'expire': expire,
                'default-ttl': default_ttl
            })
            return self.make_request('dns/modify-soa.json', method='POST', data=params)

        else:
            raise ValueError(f"Error: {error}")



    def get_dynamic_url(self, domain_name, record_id):
        params = self._auth_params({
            'domain-name': domain_name,
            'record-id': record_id
        })

        return self.make_request('dns/get-dynamic-url.json', method='GET', params=params)


    def disable_dynamic_url(self, domain_name, record_id):
        params = self._auth_params({
            'domain-name': domain_name,
            'record-id': record_id
        })

        return self.make_request('dns/disable-dynamic-url.json', method='POST', params=params)

    def change_dynamic_url(self, domain_name, record_id):
        params = self._auth_params({
            'domain-name': domain_name,
            'record-id': record_id
        })

        return self.make_request('dns/change-dynamic-url.json', method='POST', params=params)


    def get_dynamic_url_history(self, domain_name, record_id, rows_per_page=20, page=1):
        params = self._auth_params({
            'domain-name': domain_name,
            'record-id': record_id,
            'rows-per-page': rows_per_page,
            'page': page
        })

        return self.make_request('dns/get-dynamic-url-history.json', method='GET', params=params)


    def get_dynamic_url_history_pages(self, domain_name, record_id, rows_per_page=20):
        params = self._auth_params({
            'domain-name': domain_name,
            'record-id': record_id,
            'rows-per-page': rows_per_page
        })

        return self.make_request('dns/get-dynamic-url-history-pages.json', method='GET', params=params)


    def import_via_transfer(self, domain_name, server):
        params = self._auth_params({
            'domain-name': domain_name,
            'server': server
        })
        return self.make_request('dns/axfr-import.json', method='GET', params=params)


    def change_record_status(self, domain_name, record_id, status=True):
        params = self._auth_params({
            'domain-name': domain_name,
            'record-id': record_id,
            'status': 1 if status else 0
        })
        return self.make_request('dns/change-record-status.json', method='GET', params=params)


    def reset_soa_details(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/reset-soa.json', method='GET', params=params)


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




    def get_mail_forward_stats(self):
        params = self._auth_params()
        return self.make_request('dns/get-mail-forwards-stats.json', method='GET', params=params)


    def get_mail_forward_servers(self):
        params = self._auth_params()
        return self.make_request('dns/get-mailforward-servers.json', method='GET', params=params)

    def add_mail_forward(self, domain_name, box='', host='', destination=''):
        params = self._auth_params({'domain-name': domain_name, 'box': box, 'host': host, 'destination': destination})
        return self.make_request('dns/add-mail-forward.json', method='POST', params=params)

    def modify_mail_forward(self, domain_name, box='', host='', destination='', mail_forward_id=None):
        params = self._auth_params({'domain-name': domain_name, 'box': box, 'host': host, 'destination': destination, 'mail-forward-id': mail_forward_id})
        return self.make_request('dns/modify-mail-forward.json', method='POST', params=params)

    def delete_mail_forward(self, domain_name, mail_forward_id):
        params = self._auth_params({'domain-name': domain_name, 'mail-forward-id': mail_forward_id})
        return self.make_request('dns/delete-mail-forward.json', method='POST', params=params)

    def list_mail_forwards(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/mail-forwards.json', method='GET', params=params)

    def change_mail_forward_status(self, domain_name, mail_forward_id, status=True):
        params = self._auth_params({'domain-name': domain_name, 'mail-forward-id': mail_forward_id, 'status': 1 if status else 0})
        return self.make_request('dns/modify-mail-forward-status.json', method='POST', params=params)


















