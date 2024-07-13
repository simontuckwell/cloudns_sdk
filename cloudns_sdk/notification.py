

class FailoverNotificationAPI:

    def __init__(self, auth_params, make_request):
        self._auth_params = auth_params
        self.make_request = make_request


    def create_failover_notification(self, domain_name, record_id, type, code, value, chat_id):
        params = self._auth_params({
            'domain-name': domain_name,
            'record-id': record_id,
            'type': type,
            'code': code,
            'value': value,
            'chat-id': chat_id
        })
        return self.make_request('dns/create-failover-notification.json', method='POST', data=params)


    def get_failover_notifications_pages(self, domain_name, record_id, rows_per_page=20):
        params = self._auth_params({'domain-name': domain_name, 'record-id': record_id, 'rows-per-page': rows_per_page})
        return self.make_request('dns/get-failover-notifications-pages.json', method='GET', params=params)

    def list_failover_notifications(self, domain_name, record_id, rows_per_page=20, page=1):
        params = self._auth_params({'domain-name': domain_name, 'record-id': record_id, 'rows-per-page': rows_per_page, 'page': page})
        return self.make_request('dns/list-failover-notifications.json', method='GET', params=params)

    def delete_failover_notification(self, domain_name, record_id, notification_id):
        params = self._auth_params({'domain-name': domain_name, 'record-id': record_id, 'notification-id': notification_id})
        return self.make_request('dns/delete-failover-notification.json', method='GET', params=params)


