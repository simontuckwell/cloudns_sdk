class DNSSECAPI:
    """
    Provides methods for managing DNSSEC settings and operations for domain/zone.

    This class allows checking DNSSEC availability, activating and deactivating DNSSEC,
    retrieving DS records, and changing DNSSEC opt-out status for domains.

    Args:
        auth_params (callable): Function or callable object that provides authentication parameters for API requests.
        make_request (callable): Function or callable object that executes HTTP requests to the API.

    Methods:
        is_dnssec_available(domain_name):
            Checks if DNSSEC is available for a specified domain.

        activate_dnssec(domain_name):
            Activates DNSSEC for a specified domain.

        deactivate_dnssec(domain_name):
            Deactivates DNSSEC for a specified domain.

        get_ds_records(domain_name):
            Retrieves DS (Delegation Signer) records for a specified domain.

        change_dnssec_optout(domain_name, status=True):
            Changes the DNSSEC opt-out status for a specified domain.

    """
    def __init__(self, auth_params, make_request):
        self._auth_params = auth_params
        self.make_request = make_request

    def is_dnssec_available(self, domain_name):
        """
        Checks if DNSSEC is available for a specified domain.

        Args:
            domain_name (str): Domain name for which to check DNSSEC availability.

        Returns:
            dict: Response from the API indicating DNSSEC availability.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/is-dnssec-available.json', method='GET', params=params)

    def activate_dnssec(self, domain_name):
        """
        Activates DNSSEC for a specified domain.

        Args:
            domain_name (str): Domain name for which to activate DNSSEC.

        Returns:
            dict: Response from the API confirming the activation of DNSSEC.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/activate-dnssec.json', method='POST', data=params)

    def deactivate_dnssec(self, domain_name):
        """
        Deactivates DNSSEC for a specified domain.

        Args:
            domain_name (str): Domain name for which to deactivate DNSSEC.

        Returns:
            dict: Response from the API confirming the deactivation of DNSSEC.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/deactivate-dnssec.json', method='POST', data=params)

    def get_ds_records(self, domain_name):
        """
        Retrieves DS (Delegation Signer) records for a specified domain.

        Args:
            domain_name (str): Domain name for which to retrieve DS records.

        Returns:
            dict: Response from the API containing DS records for the domain.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/get-dnssec-ds-records.json', method='GET', params=params)

    def change_dnssec_optout(self, domain_name, status=True):
        """
        Changes the DNSSEC opt-out status for a specified domain.

        Args:
            domain_name (str): Domain name for which to change DNSSEC opt-out status.
            status (bool): Desired status of DNSSEC opt-out (True for opt-out, False for opt-in).

        Returns:
            dict: Response from the API confirming the change of DNSSEC opt-out status.
        """
        params = self._auth_params({'domain-name': domain_name, 'status': 1 if status else 0})
        return self.make_request('dns/set-dnssec-optout.json', method='POST', data=params)