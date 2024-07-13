class ParkedAPI:
    """
    Provides methods to manage zone parking settings.

    Attributes:
        _auth_params (callable): Function to retrieve authentication parameters.
        make_request (callable): Function to make HTTP requests to the ClouDNS API.
    """

    def __init__(self, auth_params, make_request):
        """
        Initializes the ParkedAPI instance with authentication parameters and request function.

        Args:
            auth_params (callable): Function that returns authentication parameters.
            make_request (callable): Function that makes HTTP requests to the ClouDNS API.
        """
        self._auth_params = auth_params
        self.make_request = make_request

    def get_parked_templates(self):
        """
        Retrieves available templates for parking zones.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params()
        return self.make_request('dns/get-parked-templates.json', method='GET', params=params)

    def get_parked_zone_settings(self, domain_name):
        """
        Retrieves the current parked zone settings for a specific domain.

        Args:
            domain_name (str): The name of the zone to retrieve parked settings for.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/get-parked-settings.json', method='GET', params=params)

    def set_parked_zone_settings(self, domain_name, template=3, title='', description='', keywords='', contact_form=0):
        """
        Sets or updates parked zone settings for a specific domain.

        Args:
            domain_name (str): The name of the zone to modify the parked settings of.
            template (int): The ID of the template (1, 2, 3, or 4). Use `get_parked_templates` to get available IDs.
            title (str): Optional. The title of the parked page.
            description (str): Optional. The description of the parked page.
            keywords (str): Optional. The keywords of the parked page.
            contact_form (int): Optional. Whether to show a contact form (1 for enabled, 2 for disabled). Default is 0.

        Returns:
            dict: JSON response from the API.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'template': template,
            'title': domain_name if title == '' else title,
            'description': description,
            'keywords': keywords,
            'contact-form': contact_form,

        })
        return self.make_request('dns/set-parked-settings.json', method='POST', data=params)