class NotesAPI:
    """
    Provides methods for managing notes associated with domains/zones.

    This class allows adding, retrieving, and deleting notes for specific domains.

    Args:
        auth_params (callable): Function or callable object that provides authentication parameters for API requests.
        make_request (callable): Function or callable object that executes HTTP requests to the API.

    Methods:
        add_note(domain_name, note):
            Adds a note to a specified domain.

        delete_note(domain_name):
            Deletes the note associated with a specified domain.

        get_note(domain_name):
            Retrieves the note associated with a specified domain.

    """
    def __init__(self, auth_params, make_request):
        self._auth_params = auth_params
        self.make_request = make_request

    def add_note(self, domain_name, note):
        """
        Adds a note to a specified domain.

        Args:
            domain_name (str): Domain name for which the note will be added.
            note (str): The note content to be added.

        Returns:
            dict: Response from the API indicating success or failure of adding the note.
        """
        params = self._auth_params({'domain-name': domain_name, 'note': note})
        return self.make_request('dns/set-note.json', method='POST', data=params)

    def delete_note(self, domain_name):
        """
        Deletes the note associated with a specified domain.

        Args:
            domain_name (str): Domain name for which the note will be deleted.

        Returns:
            dict: Response from the API indicating success or failure of deleting the note.
        """
        note = ''  # Empty note parameter signifies deletion
        params = self._auth_params({'domain-name': domain_name, 'note': note})
        return self.make_request('dns/set-note.json', method='POST', data=params)

    def get_note(self, domain_name):
        """
        Retrieves the note associated with a specified domain.

        Args:
            domain_name (str): Domain name for which to retrieve the note.

        Returns:
            dict: Response from the API containing the note associated with the domain.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/get-note.json', method='POST', data=params)