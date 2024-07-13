

class MailForwardingAPI:
    def __init__(self, auth_params, make_request):
        self._auth_params = auth_params
        self.make_request = make_request

    def get_mail_forward_stats(self):
        params = self._auth_params()
        return self.make_request('dns/get-mail-forwards-stats.json', method='GET', params=params)

    def get_mail_forward_servers(self):
        params = self._auth_params()
        return self.make_request('dns/get-mailforward-servers.json', method='GET', params=params)

    def add_mail_forward(self, domain_name, box='', host='', destination=''):
        params = self._auth_params({'domain-name': domain_name, 'box': box, 'host': host, 'destination': destination})
        return self.make_request('dns/add-mail-forward.json', method='POST', data=params)

    def modify_mail_forward(self, domain_name, box='', host='', destination='', mail_forward_id=None):
        params = self._auth_params({'domain-name': domain_name, 'box': box, 'host': host, 'destination': destination,
                                    'mail-forward-id': mail_forward_id})
        return self.make_request('dns/modify-mail-forward.json', method='POST', data=params)

    def delete_mail_forward(self, domain_name, mail_forward_id):
        params = self._auth_params({'domain-name': domain_name, 'mail-forward-id': mail_forward_id})
        return self.make_request('dns/delete-mail-forward.json', method='POST', data=params)

    def list_mail_forwards(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/mail-forwards.json', method='GET', data=params)

    def change_mail_forward_status(self, domain_name, mail_forward_id, status=True):
        params = self._auth_params(
            {'domain-name': domain_name, 'mail-forward-id': mail_forward_id, 'status': 1 if status else 0})
        return self.make_request('dns/modify-mail-forward-status.json', method='POST', data=params)