class MailForwardingAPI:
    """
    Provides methods for managing mail forwarding settings for domains.

    This class facilitates operations related to adding, modifying, deleting, listing, and
    managing the status of mail forwards for specific domains.

    Args:
        auth_params (callable): Function or callable object that provides authentication parameters for API requests.
        make_request (callable): Function or callable object that executes HTTP requests to the API.

    Methods:
        get_mail_forward_stats():
            Retrieves statistics for mail forwarding.

        get_mail_forward_servers():
            Retrieves available mail forwarding servers.

        add_mail_forward(domain_name, box='', host='', destination=''):
            Adds a new mail forward for a domain.

        modify_mail_forward(domain_name, box='', host='', destination='', mail_forward_id=None):
            Modifies an existing mail forward for a domain.

        delete_mail_forward(domain_name, mail_forward_id):
            Deletes a mail forward for a domain.

        list_mail_forwards(domain_name):
            Lists all mail forwards for a specific domain.

        change_mail_forward_status(domain_name, mail_forward_id, status=True):
            Changes the status of a mail forward for a domain.

    """
    def __init__(self, auth_params, make_request):
        self._auth_params = auth_params
        self.make_request = make_request

    def get_mail_forward_stats(self):
        """
        Retrieves statistics for mail forwarding.

        Returns:
            dict: Response from the API containing statistics for mail forwarding.
        """
        params = self._auth_params()
        return self.make_request('dns/get-mail-forwards-stats.json', method='GET', params=params)

    def get_mail_forward_servers(self):
        """
        Retrieves available mail forwarding servers.

        Returns:
            dict: Response from the API containing available mail forwarding servers.
        """
        params = self._auth_params()
        return self.make_request('dns/get-mailforward-servers.json', method='GET', params=params)

    def add_mail_forward(self, domain_name, box='', host='', destination=''):
        """
        Adds a new mail forward for a domain.

        Args:
            domain_name (str): Domain name for which the mail forward will be added.
            box (str, optional): Name of the mail box to forward.
            host (str, optional): Host of the mailbox. Should be empty for main domain name forwarding.
            destination (str, optional): Email address to which incoming mails will be forwarded.

        Returns:
            dict: Response from the API indicating success or failure of the operation.
        """
        params = self._auth_params({'domain-name': domain_name, 'box': box, 'host': host, 'destination': destination})
        return self.make_request('dns/add-mail-forward.json', method='POST', data=params)

    def modify_mail_forward(self, domain_name, box='', host='', destination='', mail_forward_id=None):
        """
        Modifies an existing mail forward for a domain.

        Args:
            domain_name (str): Domain name for which the mail forward will be modified.
            box (str, optional): Name of the mail box to forward.
            host (str, optional): Host of the mailbox. Should be empty for main domain name forwarding.
            destination (str, optional): Email address to which incoming mails will be forwarded.
            mail_forward_id (int, optional): ID of the mail forward to modify.

        Returns:
            dict: Response from the API indicating success or failure of the modification.
        """
        params = self._auth_params({'domain-name': domain_name, 'box': box, 'host': host, 'destination': destination,
                                    'mail-forward-id': mail_forward_id})
        return self.make_request('dns/modify-mail-forward.json', method='POST', data=params)

    def delete_mail_forward(self, domain_name, mail_forward_id):
        """
        Deletes a mail forward for a domain.

        Args:
            domain_name (str): Domain name for which the mail forward will be deleted.
            mail_forward_id (int): ID of the mail forward to delete.

        Returns:
            dict: Response from the API indicating success or failure of the deletion.
        """
        params = self._auth_params({'domain-name': domain_name, 'mail-forward-id': mail_forward_id})
        return self.make_request('dns/delete-mail-forward.json', method='POST', data=params)

    def list_mail_forwards(self, domain_name):
        """
        Lists all mail forwards for a specific domain.

        Args:
            domain_name (str): Domain name for which to list mail forwards.

        Returns:
            dict: Response from the API containing the list of mail forwards for the specified domain.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/mail-forwards.json', method='GET', params=params)

    def change_mail_forward_status(self, domain_name, mail_forward_id, status=True):
        """
        Changes the status of a mail forward for a domain.

        Args:
            domain_name (str): Domain name for which the mail forward status will be changed.
            mail_forward_id (int): ID of the mail forward to modify.
            status (bool, optional): Desired status of the mail forward. Defaults to True (active). Use False to pause mail forwarding.

        Returns:
            dict: Response from the API indicating success or failure of changing the mail forward status.
        """
        params = self._auth_params(
            {'domain-name': domain_name, 'mail-forward-id': mail_forward_id, 'status': 1 if status else 0})
        return self.make_request('dns/modify-mail-forward-status.json', method='POST', data=params)