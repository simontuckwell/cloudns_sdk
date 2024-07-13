

class ParkedAPI():

    def __init__(self, auth_params, make_request):
        self._auth_params = auth_params
        self.make_request = make_request

    def get_parked_templates(self):
        params = self._auth_params()
        return self.make_request('dns/get-parked-templates.json', method='GET', params=params)

    def get_parked_zone_settings(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/get-parked-settings.json', method='GET', params=params)

    def set_parked_zone_settings(self, domain_name, template=3, title='', description='', keywords='', contact_form=0):
        params = self._auth_params(
            {'domain-name': domain_name,
             'title': domain_name if title == '' else title,
             'description': description,
             'keywords': keywords,
             'contact-form': contact_form,
             'template': template, })
        return self.make_request('dns/set-parked-settings.json', method='POST', data=params)