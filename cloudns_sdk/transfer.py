
class TransferAPI:

    def __init__(self, auth_params, make_request, auth_id, auth_password):
        self._auth_params = auth_params
        self.make_request = make_request
        self.auth_id = auth_id
        self.auth_password = auth_password


    def import_via_axfr(self, domain_name, server):
        params = self._auth_params({
            'domain-name': domain_name,
            'server': server
        })
        return self.make_request('dns/axfr-import.json', method='GET', params=params)


    def axfr_add_ip(self, domain_name, ip):
        params = self._auth_params({'domain-name': domain_name, 'ip': ip})
        return self.make_request('dns/axfr-add.json', method='POST', data=params)

    def axfr_delete_ip(self, domain_name, id):
        params = self._auth_params({'domain-name': domain_name, 'id': id})
        return self.make_request('dns/axfr-remove.json', method='POST', data=params)

    def axfr_list_ips(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/axfr-list.json', method='GET', params=params)

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

        return self.make_request('dns/records-import.json', method='POST', data=params)

    def export_records_in_bind(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/records-export.json', method='POST', data=params)

    def list_shared_accounts(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/list-shared-accounts.json', method='GET', params=params)

    def add_shared_account(self, domain_name, mail):
        params = self._auth_params({'domain-name': domain_name, 'mail': mail})
        return self.make_request('dns/add-shared-account.json', method='POST', data=params)

    def remove_shared_account(self, domain_name, mail):
        params = self._auth_params({'domain-name': domain_name, 'mail': mail})
        return self.make_request('dns/remove-shared-account.json', method='POST', data=params)