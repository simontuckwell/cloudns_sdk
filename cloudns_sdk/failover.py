
from .notification import FailoverNotificationAPI


class FailoverAPI:
    def __init__(self, auth_params, make_request):
        self._auth_params = auth_params
        self.make_request = make_request

        self.notification = FailoverNotificationAPI(self._auth_params, self.make_request)



    def get_failover_settings(self, domain_name, record_id):
        params = self._auth_params({'domain-name': domain_name, 'record-id': record_id})
        return self.make_request('dns/failover-settings.json', method='GET', params=params)

    def activate_failover(self, domain_name, record_id, check_type,
                          down_event_handler, up_event_handler, main_ip,
                          backup_ip_1, backup_ip_2=None, backup_ip_3=None, backup_ip_4=None, backup_ip_5=None,
                          monitoring_region=None, host=None, port=None, path=None, content=None,
                          query_type=None, query_response=None, check_period=None, notification_mail=None,
                          deactivate_record=0, latency_limit=None, timeout=None, http_request_type=None):

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

        params.update({key: value for key,
        value in all_params.items() if
                       value is not None and key not in ['self', 'domain_name', 'record_id', 'check_type',
                                                         'down_event_handler', 'up_event_handler', 'main_ip',
                                                         'backup_ip_1']})

        return self.make_request('dns/failover-activate.json', method='POST', data=params)



    def modify_failover(self, domain_name, record_id, check_type,
                          down_event_handler, up_event_handler, main_ip,
                          backup_ip_1, backup_ip_2=None, backup_ip_3=None, backup_ip_4=None, backup_ip_5=None,
                          monitoring_region=None, host=None, port=None, path=None, content=None,
                          query_type=None, query_response=None, check_period=None, notification_mail=None,
                          deactivate_record=0, latency_limit=None, timeout=None, http_request_type=None):

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

        params.update({key: value for key,
        value in all_params.items() if
                       value is not None and key not in ['self', 'domain_name', 'record_id', 'check_type',
                                                         'down_event_handler', 'up_event_handler', 'main_ip',
                                                         'backup_ip_1']})

        return self.make_request('dns/failover-modify.json', method='POST', data=params)



    def deactivate_failover(self, domain_name, record_id):
        params = self._auth_params({'domain-name': domain_name, 'record-id': record_id})
        return self.make_request('dns/failover-deactivate.json', method='POST', data=params)


    def check_failover_history_pages(self, domain_name, record_id, rows_per_page=20):
        params = self._auth_params({'domain-name': domain_name, 'record-id': record_id, 'rows-per-page': rows_per_page})
        return self.make_request('dns/failover-check-history-pages.json', method='GET', params=params)


    def check_failover_history(self, domain_name, record_id, rows_per_page=20, page=1):
        params = self._auth_params({'domain-name': domain_name, 'record-id': record_id, 'rows-per-page': rows_per_page, 'page': page})
        return self.make_request('dns/failover-check-history.json', method='GET', params=params)


    def get_failover_action_history_pages(self, domain_name, record_id, rows_per_page=20):
        params = self._auth_params({'domain-name': domain_name, 'record-id': record_id, 'rows-per-page': rows_per_page})
        return self.make_request('dns/failover-action-history-pages.json', method='GET', params=params)


    def get_failover_action_history(self, domain_name, record_id, rows_per_page=20, page=1):
        params = self._auth_params({'domain-name': domain_name, 'record-id': record_id, 'rows-per-page': rows_per_page, 'page': page})
        return self.make_request('dns/failover-action-history.json', method='GET', params=params)


    def get_failover_limits(self):
        params = self._auth_params()
        return self.make_request('dns/get-failover-stats.json', method='GET', params=params)

    def list_failover_nodes(self):
        params = self._auth_params()
        return self.make_request('dns/get-failover-servers.json', method='GET', params=params)
