from .mail import MailForwardingAPI
from .records import RecordsAPI
from .transfer import TransferAPI
from .stats import StatsAPI
from .slave import SlaveZoneAPI
from .parked import ParkedAPI
from .cloud import CloudDomainAPI
from .geodns import GeoDNSAPI
from .groups import GroupsAPI
from .dnssec import DNSSECAPI
from .ssl import SSLAPI
from .notes import NotesAPI

class DNSZoneAPI:
    """
    Provides methods for managing DNS zones and associated functionalities.

    This class aggregates various API functionalities related to DNS management,
    including zone registration, deletion, listing, updating, and obtaining zone statistics.

    Attributes:
        forward (MailForwardingAPI): Instance of MailForwardingAPI for managing mail forwarding settings.
        records (RecordsAPI): Instance of RecordsAPI for managing DNS records.
        transfer (TransferAPI): Instance of TransferAPI for managing zone transfers.
        stats (StatsAPI): Instance of StatsAPI for retrieving zone statistics.
        slaves (SlaveZoneAPI): Instance of SlaveZoneAPI for managing slave zones.
        park (ParkedAPI): Instance of ParkedAPI for managing parked zone settings.
        cloud (CloudDomainAPI): Instance of CloudDomainAPI for managing cloud domain settings.
        geodns (GeoDNSAPI): Instance of GeoDNSAPI for managing GeoDNS settings.
        groups (GroupsAPI): Instance of GroupsAPI for managing groups of zones.
        dnssec (DNSSECAPI): Instance of DNSSECAPI for managing DNSSEC settings.
        ssl (SSLAPI): Instance of SSLAPI for managing SSL certificates.
        notes (NotesAPI): Instance of NotesAPI for managing notes associated with zones.

    Args:
        auth_params (callable): Function or callable object that provides authentication parameters for API requests.
        make_request (callable): Function or callable object that executes HTTP requests to the API.
        auth_id (str): Authentication ID required for certain API operations.
        auth_password (str): Authentication password associated with auth_id.

    Methods:
        get_available_name_servers(detailed_info=0):
            Retrieves available name servers.

        register_domain_zone(domain_name, zone_type, ns=None, master_ip=None):
            Registers a new DNS zone.

        delete_domain_zone(domain_name):
            Deletes a DNS zone.

        list_zones(page=1, rows_per_page=20, search=None, group_id=None, has_cloud_domains=None):
            Lists DNS zones with optional filters.

        get_pages_count(rows_per_page=10, search=None, group_id=None, has_cloud_domains=None):
            Retrieves the number of pages of DNS zones.

        get_zones_stats():
            Retrieves statistics for all zones.

        get_zone_info(domain_name):
            Retrieves information about a specific DNS zone.

        update_zone(domain_name):
            Updates an existing DNS zone.

        get_update_status(domain_name):
            Retrieves the update status of a DNS zone.

        is_updated(domain_name):
            Checks if a DNS zone is updated.

        change_zone_status(domain_name, status=True):
            Changes the status of a DNS zone.

        get_records_stats():
            Retrieves statistics for DNS records across all zones.

    """
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
        self.groups = GroupsAPI(self._auth_params, self.make_request)
        self.dnssec = DNSSECAPI(self._auth_params, self.make_request)
        self.ssl = SSLAPI(self._auth_params, self.make_request)
        self.notes = NotesAPI(self._auth_params, self.make_request)

    def get_available_name_servers(self, detailed_info=0):
        """
        Retrieves available name servers.

        Args:
            detailed_info (int, optional): Flag to indicate whether to include detailed information. Defaults to 0.

        Returns:
            dict: Response from the API containing available name server information.
        """
        params = self._auth_params({'detailed-info': detailed_info})
        return self.make_request('dns/available-name-servers.json', method='GET', params=params)

    def register_domain_zone(self, domain_name, zone_type, ns=None, master_ip=None):
        """
        Registers a new DNS zone.

        Args:
            domain_name (str): Domain name or reverse zone name to register.
            zone_type (str): Type of DNS zone ('master', 'slave', 'parked', 'geodns').
            ns (list, optional): List of name servers for the zone. Required for 'master' zones.
            master_ip (str, optional): Master server IP address. Required for 'slave' zones.

        Returns:
            dict: Response from the API indicating success or failure of the registration.
        """
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
        """
        Deletes a DNS zone.

        Args:
            domain_name (str): Domain name or reverse zone name to delete.

        Returns:
            dict: Response from the API indicating success or failure of the deletion.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/delete.json', method='POST', data=params)

    def list_zones(self, page=1, rows_per_page=20, search=None, group_id=None, has_cloud_domains=None):
        """
        Lists DNS zones with optional filters.

        Args:
            page (int, optional): Page number of the results. Defaults to 1.
            rows_per_page (int, optional): Number of results per page. Can be 10, 20, 30, 50, or 100. Defaults to 20.
            search (str, optional): Domain name, reverse zone name, or keyword to search for.
            group_id (int, optional): ID of the group to filter zones by.
            has_cloud_domains (int, optional): Flag to filter zones that have cloud domains.

        Returns:
            dict: Response from the API containing the list of DNS zones based on the filters.
        """
        params = self._auth_params({
            'page': page,
            'rows-per-page': rows_per_page,
            'search': search,
            'group-id': group_id,
            'has-cloud-domains': has_cloud_domains
        })
        return self.make_request('dns/list-zones.json', method='GET', params=params)

    def get_pages_count(self, rows_per_page=10, search=None, group_id=None, has_cloud_domains=None):
        """
        Retrieves the number of pages of DNS zones based on optional filters.

        Args:
            rows_per_page (int, optional): Number of results per page. Can be 10, 20, 30, 50, or 100. Defaults to 10.
            search (str, optional): Domain name, reverse zone name, or keyword to search for.
            group_id (int, optional): ID of the group to filter zones by.
            has_cloud_domains (int, optional): Flag to filter zones that have cloud domains.

        Returns:
            dict: Response from the API containing the number of pages of DNS zones.
        """
        params = self._auth_params({
            'rows-per-page': rows_per_page,
            'search': search,
            'group-id': group_id,
            'has-cloud-domains': has_cloud_domains
        })
        return self.make_request('dns/get-pages-count.json', method='GET', params=params)

    def get_zones_stats(self):
        """
        Retrieves statistics for all DNS zones.

        Returns:
            dict: Response from the API containing statistics for all DNS zones.
        """
        return self.make_request('dns/get-zones-stats.json', method='GET', params=self._auth_params())

    def get_zone_info(self, domain_name):
        """
        Retrieves information about a specific DNS zone.

        Args:
            domain_name (str): Domain name or reverse zone name to retrieve information for.

        Returns:
            dict: Response from the API containing information about the specified DNS zone.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/get-zone-info.json', method='GET', params=params)

    def update_zone(self, domain_name):
        """
        Updates an existing DNS zone.

        Args:
            domain_name (str): Domain name or reverse zone name to update.

        Returns:
            dict: Response from the API indicating success or failure of the update.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/update-zone.json', method='POST', data=params)

    def get_update_status(self, domain_name):
        """
        Retrieves the update status of a DNS zone.

        Args:
            domain_name (str): Domain name or reverse zone name to check update status for.

        Returns:
            dict: Response from the API containing the update status of the specified DNS zone.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/update-status.json', method='GET', params=params)

    def is_updated(self, domain_name):
        """
        Checks if a DNS zone is updated.

        Args:
            domain_name (str): Domain name or reverse zone name to check update status for.

        Returns:
            dict: Response from the API indicating whether the DNS zone is updated or not.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/is-updated.json', method='GET', params=params)

    def change_zone_status(self, domain_name, status=True):
        """
        Changes the status of a DNS zone.

        Args:
            domain_name (str): Domain name or reverse zone name to change status for.
            status (bool, optional): Desired status of the zone. Defaults to True (active).

        Returns:
            dict: Response from the API indicating success or failure of changing the zone status.
        """
        params = self._auth_params({'domain-name': domain_name, 'status': 1 if status else 0})
        return self.make_request('dns/change-status.json', method='POST', data=params)

    def get_records_stats(self):
        """
        Retrieves statistics for DNS records across all zones.

        Returns:
            dict: Response from the API containing statistics for DNS records across all zones.
        """
        return self.make_request('dns/get-records-stats.json', method='GET', params=self._auth_params())
