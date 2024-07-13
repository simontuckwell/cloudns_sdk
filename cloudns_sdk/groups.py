

class GroupsAPI:

    def __init__(self, auth_params, make_request):
        self._auth_params = auth_params
        self.make_request = make_request


    def add_group(self, domain_name, name):
        params = self._auth_params({'domain-name': domain_name, 'name': name})
        return self.make_request('dns/add-group.json', method='POST', data=params)


    def delete_group(self, group_id):
        params = self._auth_params({'group-id': group_id})
        return self.make_request('dns/delete-group.json', method='POST', data=params)

    def list_groups(self):
        params = self._auth_params()
        return self.make_request('dns/list-groups.json', method='GET', params=params)

    def rename_group(self, group_id, new_name):
        params = self._auth_params({'group-id': group_id, 'new-name': new_name})
        return self.make_request('dns/rename-group.json', method='POST', data=params)


    def change_group(self, domain_name, group_id):
        params = self._auth_params({'domain-name': domain_name,'group-id': group_id})
        return self.make_request('dns/change-group.json', method='POST', data=params)



