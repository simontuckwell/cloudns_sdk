from .notification import FailoverNotificationAPI

class FailoverAPI:
    """
    Provides methods to manage DNS failover settings.

    Args:
        auth_params (callable): Function that returns authentication parameters for API requests.
        make_request (callable): Function to make HTTP requests to the API.
    """

    def __init__(self, auth_params, make_request):
        """
        Initializes the FailoverAPI with authentication parameters and a request maker.

        Args:
            auth_params (callable): Function that returns authentication parameters for API requests.
            make_request (callable): Function to make HTTP requests to the API.
        """
        self._auth_params = auth_params
        self.make_request = make_request
        self.notification = FailoverNotificationAPI(self._auth_params, self.make_request)

    def get_failover_settings(self, domain_name, record_id):
        """
        Retrieves failover settings for a specific domain and record.

        Args:
            domain_name (str): The domain name containing the record.
            record_id (str): The ID of the record.

        Returns:
            dict: Failover settings for the specified domain and record.
        """
        params = self._auth_params({'domain-name': domain_name, 'record-id': record_id})
        return self.make_request('dns/failover-settings.json', method='GET', params=params)

    def activate_failover(self, domain_name, record_id, check_type,
                          down_event_handler, up_event_handler, main_ip,
                          backup_ip_1, backup_ip_2=None, backup_ip_3=None, backup_ip_4=None, backup_ip_5=None,
                          monitoring_region=None, host=None, port=None, path=None, content=None,
                          query_type=None, query_response=None, check_period=None, notification_mail=None,
                          deactivate_record=0, latency_limit=None, timeout=None, http_request_type=None):
        """
        Activates failover for a specific domain and record.

        Args:
            domain_name (str): The domain name containing the record.
            record_id (str): The ID of the record.
            check_type (int): Monitoring check type for the failover. Possible values:
                              1 - Ping (15% threshold), 2 - Ping (25% threshold),
                              3 - Ping (50% threshold), 4 - HTTP, 5 - HTTPS,
                              6 - HTTP custom string, 7 - HTTPS custom string,
                              8 - TCP, 9 - UDP, 10 - DNS, 14 - Ping (100% threshold)
            down_event_handler (int): Event handler if Main IP is down. Possible values:
                              0 - Monitoring only, email notification
                              1 - Deactivate DNS record
                              2 - Replace with working Backup IP

            up_event_handler (int): Event handler if Main IP is up. Possible values:
                              0 - Monitoring only, email notification
                              1 - Activate the Main IP for the DNS record
                              2 - Do not monitor if it is back up
            main_ip (str): Main IP address to be monitored.
            backup_ip_1 (str): First backup IP address.
            backup_ip_2 (str, optional): Second backup IP address.
            backup_ip_3 (str, optional): Third backup IP address.
            backup_ip_4 (str, optional): Fourth backup IP address.
            backup_ip_5 (str, optional): Fifth backup IP address.
            monitoring_region (str, optional): Monitoring region or country. Possible values:
                                               global, eur, nam, asi, at, bg, br, ca, de, es, fi, hk, hu, il, in, it,
                                               jp, kr, mx, nl, pl, ro, ru, sg, tr, tw, uk, us, za. Or specify a single node.
            host (str, optional): Hostname (FQDN) for HTTP, HTTPS, Custom HTTP, Custom HTTPS, and DNS check types.
            port (int, optional): Port of the server for HTTP, HTTPS, Custom HTTP, Custom HTTPS, TCP, and UDP check types.
            path (str, optional): Path on the FQDN for HTTP, HTTPS, Custom HTTP, and Custom HTTPS check types.
            content (str, optional): Expected output for Custom HTTP and Custom HTTPS check types.
            query_type (str, optional): Record type for DNS check type.
            query_response (str, optional): Expected response for DNS check type.
            check_period (int, optional): Time-frame between each monitoring check. Default is 60 (1 minute). Possible values:
                                          60, 120, 300, 600, 900, 1200, 1800, 3600.
            notification_mail (str, optional): Email address for notifications. Use "-1" to disable.
            deactivate_record (int, optional): Deactivate the record if both Main IP and backup IPs are down. Default is 0.
                                               Possible values: 0, 1. (1 will deactivate the record)
            latency_limit (float, optional): Latency limit for Ping checks. Marks check as DOWN if latency is above limit.
            timeout (int, optional): Timeout for Ping checks. Default is 2. Must be between 1 and 5.
            http_request_type (str, optional): HTTP request type for HTTP/S checks. Default is GET. Possible values: GET, HEAD, POST, PUT, DELETE.

        Returns:
            dict: Response from the API.
        """
        all_params = locals()
        params = self._auth_params({
            'domain-name': domain_name,
            'record-id': record_id,
            'check_type': check_type,
            'down_event_handler': down_event_handler,
            'up_event_handler': up_event_handler,
            'main_ip': main_ip,
            'backup_ip_1': backup_ip_1,
        })

        params.update({key: value for key, value in all_params.items() if value is not None and key not in ['self', 'domain_name', 'record_id', 'check_type', 'down_event_handler', 'up_event_handler', 'main_ip', 'backup_ip_1']})
        return self.make_request('dns/failover-activate.json', method='POST', data=params)

    def modify_failover(self, domain_name, record_id, check_type,
                        down_event_handler, up_event_handler, main_ip,
                        backup_ip_1, backup_ip_2=None, backup_ip_3=None, backup_ip_4=None, backup_ip_5=None,
                        monitoring_region=None, host=None, port=None, path=None, content=None,
                        query_type=None, query_response=None, check_period=None, notification_mail=None,
                        deactivate_record=0, latency_limit=None, timeout=None, http_request_type=None):
        """
        Modifies failover settings for a specific domain and record.

        Args:
            domain_name (str): The domain name containing the record.
            record_id (str): The ID of the record.
            check_type (int): Monitoring check type for the failover. Possible values:
                              1 - Ping (15% threshold), 2 - Ping (25% threshold),
                              3 - Ping (50% threshold), 4 - HTTP, 5 - HTTPS,
                              6 - HTTP custom string, 7 - HTTPS custom string,
                              8 - TCP, 9 - UDP, 10 - DNS, 14 - Ping (100% threshold)
            down_event_handler (int): Event handler if Main IP is down. Possible values:
                              0 - Monitoring only, email notification
                              1 - Deactivate DNS record
                              2 - Replace with working Backup IP

            up_event_handler (int): Event handler if Main IP is up. Possible values:
                              0 - Monitoring only, email notification
                              1 - Activate the Main IP for the DNS record
                              2 - Do not monitor if it is back up
            main_ip (str): Main IP address to be monitored.
            backup_ip_1 (str): First backup IP address.
            backup_ip_2 (str, optional): Second backup IP address.
            backup_ip_3 (str, optional): Third backup IP address.
            backup_ip_4 (str, optional): Fourth backup IP address.
            backup_ip_5 (str, optional): Fifth backup IP address.
            monitoring_region (str, optional): Monitoring region or country. Possible values:
                                               global, eur, nam, asi, at, bg, br, ca, de, es, fi, hk, hu, il, in, it,
                                               jp, kr, mx, nl, pl, ro, ru, sg, tr, tw, uk, us, za. Or specify a single node.
            host (str, optional): Hostname (FQDN) for HTTP, HTTPS, Custom HTTP, Custom HTTPS, and DNS check types.
            port (int, optional): Port of the server for HTTP, HTTPS, Custom HTTP, Custom HTTPS, TCP, and UDP check types.
            path (str, optional): Path on the FQDN for HTTP, HTTPS, Custom HTTP, and Custom HTTPS check types.
            content (str, optional): Expected output for Custom HTTP and Custom HTTPS check types.
            query_type (str, optional): Record type for DNS check type.
            query_response (str, optional): Expected response for DNS check type.
            check_period (int, optional): Time-frame between each monitoring check. Default is 60 (1 minute). Possible values:
                                          60, 120, 300, 600, 900, 1200, 1800, 3600.
            notification_mail (str, optional): Email address for notifications. Use "-1" to disable.
            deactivate_record (int, optional): Deactivate the record if both Main IP and backup IPs are down. Default is 0.
                                               Possible values: 0, 1. (1 will deactivate the record)
            latency_limit (float, optional): Latency limit for Ping checks. Marks check as DOWN if latency is above limit.
            timeout (int, optional): Timeout for Ping checks. Default is 2. Must be between 1 and 5.
            http_request_type (str, optional): HTTP request type for HTTP/S checks. Default is GET. Possible values: GET, HEAD, POST, PUT, DELETE.
        Returns:
            dict: Response from the API.
        """
        all_params = locals()
        params = self._auth_params({
            'domain-name': domain_name,
            'record-id': record_id,
            'check_type': check_type,
            'down_event_handler': down_event_handler,
            'up_event_handler': up_event_handler,
            'main_ip': main_ip,
            'backup_ip_1': backup_ip_1,
        })

        params.update({key: value for key, value in all_params.items() if value is not None and key not in ['self', 'domain_name', 'record_id', 'check_type', 'down_event_handler', 'up_event_handler', 'main_ip', 'backup_ip_1']})
        return self.make_request('dns/failover-modify.json', method='POST', data=params)

    def deactivate_failover(self, domain_name, record_id):
        """
        Deactivates failover for a specific domain and record.

        Args:
            domain_name (str): The domain name containing the record.
            record_id (str): The ID of the record.

        Returns:
            dict: Response from the API.
        """
        params = self._auth_params({'domain-name': domain_name, 'record-id': record_id})
        return self.make_request('dns/failover-deactivate.json', method='POST', data=params)

    def check_failover_history_pages(self, domain_name, record_id, rows_per_page=20):
        """
        Retrieves the number of pages in the failover check history for a specific domain and record.

        Args:
            domain_name (str): The domain name containing the record.
            record_id (str): The ID of the record.
            rows_per_page (int, optional): Results per page. Default is 20. Can be 10, 20, 30, 50, or 100.

        Returns:
            dict: Number of pages in the failover check history.
        """
        params = self._auth_params({'domain-name': domain_name, 'record-id': record_id, 'rows-per-page': rows_per_page})
        return self.make_request('dns/failover-check-history-pages.json', method='GET', params=params)

    def check_failover_history(self, domain_name, record_id, rows_per_page=20, page=1):
        """
        Retrieves the failover check history for a specific domain and record.

        Args:
            domain_name (str): The domain name containing the record.
            record_id (str): The ID of the record.
            rows_per_page (int, optional): Results per page. Default is 20. Can be 10, 20, 30, 50, or 100.
            page (int, optional): Page number. Default is 1.

        Returns:
            dict: Failover check history.
        """
        params = self._auth_params({'domain-name': domain_name, 'record-id': record_id, 'rows-per-page': rows_per_page, 'page': page})
        return self.make_request('dns/failover-check-history.json', method='GET', params=params)

    def get_failover_action_history_pages(self, domain_name, record_id, rows_per_page=20):
        """
        Retrieves the number of pages in the failover action history for a specific domain and record.

        Args:
            domain_name (str): The domain name containing the record.
            record_id (str): The ID of the record.
            rows_per_page (int, optional): Results per page. Default is 20. Can be 10, 20, 30, 50, or 100.

        Returns:
            dict: Number of pages in the failover action history.
        """
        params = self._auth_params({'domain-name': domain_name, 'record-id': record_id, 'rows-per-page': rows_per_page})
        return self.make_request('dns/failover-action-history-pages.json', method='GET', params=params)

    def get_failover_action_history(self, domain_name, record_id, rows_per_page=20, page=1):
        """
        Retrieves the failover action history for a specific domain and record.

        Args:
            domain_name (str): The domain name containing the record.
            record_id (str): The ID of the record.
            rows_per_page (int, optional): Results per page. Default is 20. Can be 10, 20, 30, 50, or 100.
            page (int, optional): Page number. Default is 1.

        Returns:
            dict: Failover action history.
        """
        params = self._auth_params({'domain-name': domain_name, 'record-id': record_id, 'rows-per-page': rows_per-page, 'page': page})
        return self.make_request('dns/failover-action-history.json', method='GET', params=params)

    def get_failover_limits(self):
        """
        Retrieves the failover limits for the account.

        Returns:
            dict: Failover limits.
        """
        params = self._auth_params()
        return self.make_request('dns/get-failover-stats.json', method='GET', params=params)

    def list_failover_nodes(self):
        """
        Lists available failover nodes.

        Returns:
            dict: Available failover nodes.
        """
        params = self._auth_params()
        return self.make_request('dns/get-failover-servers.json', method='GET', params=params)
