

from .validations import validate
from .utils import process_params


class RecordsAPI:

    VALID_ZONE_TYPES = ['domain', 'reverse', 'parked', 'master', 'slave', 'geodns']


    def __init__(self, auth_params, make_request, auth_id, auth_password):
        self._auth_params = auth_params
        self.make_request = make_request
        self.auth_id = auth_id
        self.auth_password = auth_password

    def is_valid_zone_type(self, zone_type):
        return zone_type in self.VALID_ZONE_TYPES


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
        return self.make_request('dns/delete-record.json', method='POST', data=params)

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

        return self.make_request('dns/copy-records.json', method='POST', data=params)


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

    def modify_soa_details(self, domain_name, primary_ns, admin_email='', refresh=7200, retry=7200, expire=2419200,
                           default_ttl=3600):
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

        return self.make_request('dns/disable-dynamic-url.json', method='POST', data=params)

    def change_dynamic_url(self, domain_name, record_id):
        params = self._auth_params({
            'domain-name': domain_name,
            'record-id': record_id
        })

        return self.make_request('dns/change-dynamic-url.json', method='POST', data=params)

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

