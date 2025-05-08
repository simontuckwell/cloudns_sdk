class DomainsGroupsAPI:
    """
    Provides methods for managing groups of domains.

    This class allows adding, deleting, listing, renaming, and changing groups for domains.

    Args:
        auth_params (callable): Function or callable object that provides authentication parameters for API requests.
        make_request (callable): Function or callable object that executes HTTP requests to the API.

    Methods:
        add_group(domain_name, name):
            Adds a new group for domains.

        delete_group(group_id):
            Deletes a group of domains by its ID.

        list_groups():
            Retrieves a list of all groups of domains.

        rename_group(group_id, new_name):
            Renames an existing group of domains.

        change_group(domain_name, group_id):
            Changes the group of a specified domains.

    """
    def __init__(self, auth_params, make_request):
        self._auth_params = auth_params
        self.make_request = make_request

    def add_group(self, domain_name, name):
        """
        Adds a new group for domains.

        Args:
            domain_name (str): Domain name to associate with the new group.
            name (str): Name of the new group.

        Returns:
            dict: Response from the API indicating success or failure of adding the group.
        """
        params = self._auth_params({'domain-name': domain_name, 'name': name})
        return self.make_request('domains/add-group.json', method='POST', data=params)

    def delete_group(self, group_id):
        """
        Deletes a group of domains by its ID.

        Args:
            group_id (int): ID of the group to delete.

        Returns:
            dict: Response from the API indicating success or failure of deleting the group.
        """
        params = self._auth_params({'group-id': group_id})
        return self.make_request('domains/delete-group.json', method='POST', data=params)

    def list_groups(self):
        """
        Retrieves a list of all groups of domains.

        Returns:
            dict: Response from the API containing a list of all groups of domains.
        """
        params = self._auth_params()
        return self.make_request('domains/list-groups.json', method='GET', params=params)

    def rename_group(self, group_id, new_name):
        """
        Renames an existing group of domains.

        Args:
            group_id (int): ID of the group to rename.
            new_name (str): New name for the group.

        Returns:
            dict: Response from the API indicating success or failure of renaming the group.
        """
        params = self._auth_params({'group-id': group_id, 'new-name': new_name})
        return self.make_request('domains/rename-group.json', method='POST', data=params)

    def change_group(self, domain_name, group_id):
        """
        Changes the group of a specified domains.

        Args:
            domain_name (str): Domain name to change its group.
            group_id (int): ID of the new group to assign to the domain.

        Returns:
            dict: Response from the API indicating success or failure of changing the group.
        """
        params = self._auth_params({'domain-name': domain_name,'group-id': group_id})
        return self.make_request('domains/change-group.json', method='POST', data=params)