class DomainsDNSSECAPI:
    """
    Provides methods for managing the DNSSEC records and operations for a domain.

    Args:
        auth_params (callable): Function or callable object that provides authentication parameters for API requests.
        make_request (callable): Function or callable object that executes HTTP requests to the API.

    Methods:
        add_dnssec_record(domain_name, record):
            Create a DNSSEC record for a specified domain.

        delete_dnssec_record(domain_name, record):
            Delete a DNSSEC record from a specified domain.

        list_dnssec_records(domain_name):
            List the DNSSEC records for a specified domain.


    """
    def __init__(self, auth_params, make_request):
        self._auth_params = auth_params
        self.make_request = make_request

    def add_dnssec_record(self, domain_name, record):
        """
        Add a DNSSEC record for a specified domain.

        Args:
            domain_name (str): Domain name to add a DNSSEC record to.
            record (str): The DNSSEC record you wish to apply for your domain name.
        Returns:
            dict: Response from the API confirming the addition of the DNSSEC record.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'record': record
        })
        return self.make_request('domains/add-dnssec-record.json', method='POST', data=params)

    def delete_dnssec_record(self, domain_name, record):
        """
        Delete a DNSSEC record from a specified domain.

        Args:
            domain_name (str): Domain name to delete a DNSSEC record from.
            record (str): The DNSSEC record you wish to remove from your domain name.

        Returns:
            dict: Response from the API confirming the deletion of the DNSSEC record.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'record': record
        })
        return self.make_request('domains/delete-dnssec-record.json', method='POST', data=params)

    def list_dnssec_records(self, domain_name):
        """
        Retrieves DNSSEC records for a specified domain.

        Args:
            domain_name (str): Domain name for which to retrieve DNSSEC records.

        Returns:
            list: List of DNSSEC Records for your domain name.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('domains/list-dnssec-records.json', method='GET', params=params)
