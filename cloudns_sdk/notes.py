
class NotesAPI:

    def __init__(self, auth_params, make_request):
        self._auth_params = auth_params
        self.make_request = make_request


    def add_note(self, domain_name, note):
        params = self._auth_params({'domain-name': domain_name, 'note': note})
        return self.make_request('dns/set-note.json', method='POST', data=params)

    def delete_note(self, domain_name):
        note = ''
        params = self._auth_params({'domain-name': domain_name, 'note': note})
        return self.make_request('dns/set-note.json', method='POST', data=params)

    def get_note(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/get-note.json', method='POST', data=params)