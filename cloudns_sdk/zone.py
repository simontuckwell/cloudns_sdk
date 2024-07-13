from .mail import MailForwardingAPI
from .records import RecordsAPI
from .transfer import TransferAPI
from .stats import StatsAPI
from .slave import SlaveZoneAPI
from .parked import ParkedAPI
from .cloud import CloudDomainAPI
from .geodns import GeoDNSAPI

class DNSZoneAPI:

    def __init__(self, auth_params, make_request, auth_id, auth_password):
        self._auth_params = auth_params
        self.make_request = make_request
        self.auth_id = auth_id
        self.auth_password = auth_password

        self.forward = MailForwardingAPI(self._auth_params, self.make_request)
        self.records = RecordsAPI(self._auth_params, self.make_request, self.auth_id, self.auth_password)
        self.transfer = TransferAPI(self._auth_params, self.make_request, self.auth_id, self.auth_password)
        self.stats = StatsAPI(self._auth_params, self.make_request)
        self.slaves = SlaveZoneAPI(self._auth_params, self.make_request)
        self.park = ParkedAPI(self._auth_params, self.make_request)
        self.cloud = CloudDomainAPI(self._auth_params, self.make_request)
        self.geodns = GeoDNSAPI(self._auth_params, self.make_request)


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

        return self.make_request('dns/register.json', method='POST', data=params)

    def delete_domain_zone(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/delete.json', method='POST', data=params)

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
        return self.make_request('dns/update-zone.json', method='POST', data=params)

    def get_update_status(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/update-status.json', method='GET', params=params)

    def is_updated(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/is-updated.json', method='GET', params=params)

    def change_zone_status(self, domain_name, status=True):
        params = self._auth_params({'domain-name': domain_name, 'status': 1 if status else 0})
        return self.make_request('dns/change-status.json', method='POST', data=params)

    def get_records_stats(self):
        return self.make_request('dns/get-records-stats.json', method='GET', params=self._auth_params())