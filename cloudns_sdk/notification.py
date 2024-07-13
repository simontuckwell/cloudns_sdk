class FailoverNotificationAPI:
    """
    Provides methods to manage notifications for zone failover situations.

    Attributes:
        _auth_params (callable): Function to retrieve authentication parameters.
        make_request (callable): Function to make HTTP requests to the ClouDNS API.
    """

    def __init__(self, auth_params, make_request):
        """
        Initializes the FailoverNotificationAPI instance with authentication parameters and request function.

        Args:
            auth_params (callable): Function that returns authentication parameters.
            make_request (callable): Function that makes HTTP requests to the ClouDNS API.
        """
        self._auth_params = auth_params
        self.make_request = make_request

    def create_failover_notification(self, domain_name, record_id, type, code, value, chat_id):
        """
        Creates a new failover notification for a specific domain and record.

        Args:
            domain_name (str): The domain where the failover notification is applied.
            record_id (int): Record ID of the DNS record. Obtain this ID from the list of records.
            type (str): Type of notification ('webhook-up', 'webhook-down', 'mail', 'sms', 'telegram', 'discord').
            code (str): Phone code for SMS notifications, or BotToken for Telegram or Discord notifications.
            value (str): Notification email, URL address, phone number, or custom message.
            chat_id (str): Chat ID for Telegram, or channel ID for Discord.

        Returns:
            dict: JSON response from the API.
        """
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
        """
        Retrieves failover notifications paginated for a specific domain and record.

        Args:
            domain_name (str): The domain where the failover notification is applied.
            record_id (int): Record ID of the DNS record. Obtain this ID from the list of records.
            rows_per_page (int): Number of notifications per page (default is 20).

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name, 'record-id': record_id, 'rows-per-page': rows_per_page})
        return self.make_request('dns/get-failover-notifications-pages.json', method='GET', params=params)

    def list_failover_notifications(self, domain_name, record_id, rows_per_page=20, page=1):
        """
        Lists all failover notifications for a specific domain and record.

        Args:
            domain_name (str): The domain where the failover notification is applied.
            record_id (int): Record ID of the DNS record. Obtain this ID from the list of records.
            rows_per_page (int): Number of notifications per page (default is 20).
            page (int): Page number to fetch (default is 1).

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name, 'record-id': record_id, 'rows-per-page': rows_per_page, 'page': page})
        return self.make_request('dns/list-failover-notifications.json', method='GET', params=params)

    def delete_failover_notification(self, domain_name, record_id, notification_id):
        """
        Deletes a failover notification for a specific domain, record, and notification ID.

        Args:
            domain_name (str): The domain where the failover notification is applied.
            record_id (int): Record ID of the DNS record. Obtain this ID from the list of records.
            notification_id (str): ID of the failover notification to delete.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name, 'record-id': record_id, 'notification-id': notification_id})
        return self.make_request('dns/delete-failover-notification.json', method='GET', params=params)