from .domains_dnssec import DomainsDNSSECAPI
from .domains_groups import DomainsGroupsAPI

class DomainNameAPI:
    """
    Provides methods for managing domain names and associated functionalities.

    This class aggregates various API functionalities related to domain name management,
    including registration, deletion, listing, updating and statistics.

    Attributes:
        dnssec (DomainsDNSSECAPI): Instance of DomainsDNSSECAPI for managing DNSSEC settings.
        groups (DomainsGroupsAPI): Instance of DomainsGroupsAPI for managing groups of domains.

    Args:
        auth_params (callable): Function or callable object that provides authentication parameters for API requests.
        make_request (callable): Function or callable object that executes HTTP requests to the API.
        auth_id (str): Authentication ID required for certain API operations.
        auth_password (str): Authentication password associated with auth_id.

    Methods:
        check_domain_available(name, tld):
            Retrieves domain name availability.

        pricing_list():
            Retrieves domain name pricing information.

        register_domain(domain_name, tld, period, mail,
                        name, address, city, state, zip, country, telnocc, telno,
                        nameservers, intended_use=None, company=None, faxnocc=None, faxno=None,
                        registrant_type=None, registrant_type_id=None, registrant_policy=None,
                        birth_date=None, birth_cc=None, birth_city=None, birth_zip=None,
                        publication=None, vat=None, siren=None, duns=None, trademark=None,
                        waldec=None, registrant_type_other=None, privacy_protection=None,
                        code=None, publicity=None, kpp=None, passport_number=None,
                        passport_issued_by=None, passport_issued_on=None,
                        organization_authority=None, organization_create_date=None,
                        aero_id=None, aero_key=None, registrant_title=None,
                        bank_bic=None, bank_name=None, bank_iban=None):
            Registers a new domain name.

        renew_domain(domain_name, period):
            Renews a DNS zone.

        transfer_domain(domain_name, tld, period, mail,
                        name, address, city, state, zip, country, telnocc, telno,
                        nameservers, intended_use=None, company=None, faxnocc=None, faxno=None,
                        registrant_type=None, registrant_type_id=None, registrant_policy=None,
                        birth_date=None, birth_cc=None, birth_city=None, birth_zip=None,
                        publication=None, vat=None, siren=None, duns=None, trademark=None,
                        waldec=None, registrant_type_other=None, privacy_protection=None,
                        code=None, publicity=None, kpp=None, passport_number=None,
                        passport_issued_by=None, passport_issued_on=None,
                        organization_authority=None, organization_create_date=None,
                        aero_id=None, aero_key=None, registrant_title=None,
                        bank_bic=None, bank_name=None, bank_iban=None):
            Transfers domain name.

        list_domains(page=1, rows_per_page=10, search=None, order_by=None):
            List registered domains with optional filters.

        get_pages_count(rows_per_page=10, search=None):
            Retrieves the number of pages of registered domains based on optional filters.

        get_domain_info(domain_name):
            Retrieves information about a specific domain name.

        get_domain_contacts(domain_name):
            Retrieves a specific domain name's contacts.

        modify_domain_contact(domain_name, type, mail, name, company,
                              address, city, state, zip, country,
                              telnocc, telno, faxnocc=None, faxno=None):
            Changes a specific domain name's contacts.

        get_domain_nameservers(domain_name):
            Retrieves a specific domain name's name servers.

        set_domain_nameservers(domain_name, nameservers):
            Retrieves a specific domain name's name servers.

        get_domain_child_nameservers(domain_name):
            Retrieves a domain name's child name servers.

        add_domain_child_nameserver(domain_name, host, ip):
            Adds a child name server (Glue record) to a domain name.

        delete_domain_child_nameserver(domain_name, host, ip):
            Deletes a child name server from a domain name.

        modify_domain_child_nameserver(domain_name, host, old_ip, new_ip):
            Update a child name server for a domain name.

        modify_domain_privacy_protection(domain_name, status):
            Modifies the privacy protection of the domain.

        modify_domain_transfer_lock(domain_name, status):
            Modifies the transfer lock of the domain.

        get_domain_transfer_code(domain_name):
            Retrieves a specific domain name's transfer code.

        get_domain_raa_status(domain_name):
            Retrieves a specific domain name's RAA contact information status.

        resend_domain_raa_verification(domain_name):
            Resend the verification e-mail to the domain's administrative contact.

    """
    def __init__(self, auth_params, make_request, auth_id, auth_password):
        self._auth_params = auth_params
        self.make_request = make_request
        self.auth_id = auth_id
        self.auth_password = auth_password

        self.groups = DomainsGroupsAPI(self._auth_params, self.make_request)
        self.dnssec = DomainsDNSSECAPI(self._auth_params, self.make_request)

    def check_domain_available(self, name, tld):
        """
        Retrieves domain name availability.

        Args:
            name (str): Domain name to check (e.g. 'example').
            tld (str): array of TLDs to check (e.g. ['com', 'uk']).

        Returns:
            dict: Response from the API containing availability information.
        """
        params = self._auth_params({'name': name, 'tld[]': tld})
        return self.make_request('domains/check-available.json', method='GET', params=params)

    def pricing_list(self):
        """
        Retrieves domain name pricing information.

        Returns:
            dict: Response from the API containing domain name pricing information.
        """
        params = self._auth_params({})
        return self.make_request('domains/pricing-list.json', method='GET', params=params)

    def register_domain(self, domain_name, tld, period, mail,
                        name, address, city, state, zip, country, telnocc, telno,
                        nameservers, intended_use=None, company=None, faxnocc=None, faxno=None,
                        registrant_type=None, registrant_type_id=None, registrant_policy=None,
                        birth_date=None, birth_cc=None, birth_city=None, birth_zip=None,
                        publication=None, vat=None, siren=None, duns=None, trademark=None,
                        waldec=None, registrant_type_other=None, privacy_protection=None,
                        code=None, publicity=None, kpp=None, passport_number=None,
                        passport_issued_by=None, passport_issued_on=None,
                        organization_authority=None, organization_create_date=None,
                        aero_id=None, aero_key=None, registrant_title=None,
                        bank_bic=None, bank_name=None, bank_iban=None):
        """
        Registers a new domain name.

        Args:
            domain_name (str): The name to register without TLD.
            tld (str): The TLD the domain name will be registered with (com, net, org, etc)
            period (int): Registration period in years.
            mail (str): Email address
            name (str): First and last name of the person
            address (str): Address of the company/person(street, number, etc)
            city (str): Example: Dallas
            state (str): Example: Texas
            zip (int or str): ZIP code
            country (str): 2 letters country code according to ISO 3166
            telnocc (int): Phone number calling code. Between 1 and 3 digits.
            telno (int): Phone number
            nameservers ([str]): Array with name servers.
            intended_use (str, optional): For example, commercial use, statistic website, cultural, blog, etc.
            company (str, optional): Name of the company.
            faxnocc (int, optional): Fax number calling code. Between 1 and 3 digits.
            faxno (int, optional): Fax number.
            registrant_type (str, optional): Optional field for specific TLDs.
            registrant_type_id (str, optional): Optional field for specific TLDs.
            registrant_policy (int, optional): Optional field for specific TLDs.
            birth_date (str, optional): Optional Birth date.
            birth_cc (str, optional): Optional Birth country code.
            birth_city (str, optional): Optional Birth city name.
            birth_zip (str, optional): Optional Postal code of the birth city.
            publication (str, optional): Restricted or Non-Restricted publication of the individual details.
            vat (str, optional): EU VAT number.
            siren (str, optional): Siren number of the company (organization).
            duns (str, optional): DUNS number of the company (organization).
            trademark (str, optional): field for specific TLDs.
            waldec (str, optional): Waldec number of the association.
            registrant_type_other (str, optional): Type of the organization.
            privacy_protection (int, optional): Enabling/disabling Privacy Protection for the domain.
            code (int, optional): Identification code.
            publicity (int, optional): Consent to the processing of personal data for registration)
            kpp (int, optional): Territory-linked Taxpayer number when the Country is Russia.
            passport_number (str, optional): Document Number.
            passport_issued_by (str, optional): Document details.
            passport_issued_on (str, optional): Document details.
            organization_authority (str, optional): Document details.
            organization_create_date (str, optional): Document details.
            aero_id (str, optional): Required for *.aero domain names.
            aero_key (str, optional): Required for *.aero domain names.
            registrant_title (str, optional): Required for *.ga domain names.
            bank_bic (str, optional): Required for *.md domain names.
            bank_name (str, optional): Required for *.md domain names.
            bank_iban (str, optional): Required for *.md domain names.

        Returns:
            dict: Response from the API indicating success or failure of the registration.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'tld': tld,
            'period': period,
            'mail': mail,
            'name': name,
            'address': address,
            'city': city,
            'state': state,
            'zip': zip,
            'country': country,
            'telnocc': telnocc,
            'telno': telno,
            'ns[]': nameservers,
            'intended_use': intended_use,
            'company': company,
            'faxnocc': faxnocc,
            'faxno': faxno,
            'registrant_type': registrant_type,
            'registrant_type_id': registrant_type_id,
            'registrant_policy': registrant_policy,
            'birth_date': birth_date,
            'birth_cc': birth_cc,
            'birth_city': birth_city,
            'birth_zip': birth_zip,
            'publication': publication,
            'vat': vat,
            'siren': siren,
            'duns': duns,
            'trademark': trademark,
            'waldec': waldec,
            'registrant_type_other': registrant_type_other,
            'privacy_protection': privacy_protection,
            'code': code,
            'publicity': publicity,
            'kpp': kpp,
            'passport_number': passport_number,
            'passport_issued_by': passport_issued_by,
            'passport_issued_on': passport_issued_on,
            'organization_authority': organization_authority,
            'organization_create_date': organization_create_date,
            'aero_id': aero_id,
            'aero_key': aero_key,
            'registrant_title': registrant_title,
            'bank_bic': bank_bic,
            'bank_name': bank_name,
            'bank_iban': bank_iban
        })

        return self.make_request('domains/order-new-domain.json', method='POST', data=params)

    def renew_domain(self, domain_name, period):
        """
        Renews a DNS zone.

        Args:
            domain_name (str): Domain name to renew (with TLD).
            period (int): Registration period in years.

        Returns:
            dict: Response from the API indicating success or failure of the renewal.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'period': period
        })
        return self.make_request('domains/order-renew-domain', method='POST', data=params)

    def transfer_domain(self, domain_name, tld, period, mail,
                        name, address, city, state, zip, country, telnocc, telno,
                        nameservers, intended_use=None, company=None, faxnocc=None, faxno=None,
                        registrant_type=None, registrant_type_id=None, registrant_policy=None,
                        birth_date=None, birth_cc=None, birth_city=None, birth_zip=None,
                        publication=None, vat=None, siren=None, duns=None, trademark=None,
                        waldec=None, registrant_type_other=None, privacy_protection=None,
                        code=None, publicity=None, kpp=None, passport_number=None,
                        passport_issued_by=None, passport_issued_on=None,
                        organization_authority=None, organization_create_date=None,
                        aero_id=None, aero_key=None, registrant_title=None,
                        bank_bic=None, bank_name=None, bank_iban=None):
        """
        Transfers domain name.

        Args:
            domain_name (str): The name to register without TLD.
            tld (str): The TLD the domain name will be registered with (com, net, org, etc)
            period (int): Registration period in years.
            mail (str): Email address
            name (str): First and last name of the person
            address (str): Address of the company/person(street, number, etc)
            city (str): Example: Dallas
            state (str): Example: Texas
            zip (int or str): ZIP code
            country (str): 2 letters country code according to ISO 3166
            telnocc (int): Phone number calling code. Between 1 and 3 digits.
            telno (int): Phone number
            nameservers ([str]): Array with name servers.
            intended_use (str, optional): For example, commercial use, statistic website, cultural, blog, etc.
            company (str, optional): Name of the company.
            faxnocc (int, optional): Fax number calling code. Between 1 and 3 digits.
            faxno (int, optional): Fax number.
            registrant_type (str, optional): Optional field for specific TLDs.
            registrant_type_id (str, optional): Optional field for specific TLDs.
            registrant_policy (int, optional): Optional field for specific TLDs.
            birth_date (str, optional): Optional Birth date.
            birth_cc (str, optional): Optional Birth country code.
            birth_city (str, optional): Optional Birth city name.
            birth_zip (str, optional): Optional Postal code of the birth city.
            publication (str, optional): Restricted or Non-Restricted publication of the individual details.
            vat (str, optional): EU VAT number.
            siren (str, optional): Siren number of the company (organization).
            duns (str, optional): DUNS number of the company (organization).
            trademark (str, optional): field for specific TLDs.
            waldec (str, optional): Waldec number of the association.
            registrant_type_other (str, optional): Type of the organization.
            privacy_protection (int, optional): Enabling/disabling Privacy Protection for the domain.
            code (int, optional): Identification code.
            publicity (int, optional): Consent to the processing of personal data for registration)
            kpp (int, optional): Territory-linked Taxpayer number when the Country is Russia.
            passport_number (str, optional): Document Number.
            passport_issued_by (str, optional): Document details.
            passport_issued_on (str, optional): Document details.
            organization_authority (str, optional): Document details.
            organization_create_date (str, optional): Document details.
            aero_id (str, optional): Required for *.aero domain names.
            aero_key (str, optional): Required for *.aero domain names.
            registrant_title (str, optional): Required for *.ga domain names.
            bank_bic (str, optional): Required for *.md domain names.
            bank_name (str, optional): Required for *.md domain names.
            bank_iban (str, optional): Required for *.md domain names.

        Returns:
            dict: Response from the API indicating success or failure of the transfer.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'tld': tld,
            'period': period,
            'mail': mail,
            'name': name,
            'address': address,
            'city': city,
            'state': state,
            'zip': zip,
            'country': country,
            'telnocc': telnocc,
            'telno': telno,
            'ns[]': nameservers,
            'intended_use': intended_use,
            'company': company,
            'faxnocc': faxnocc,
            'faxno': faxno,
            'registrant_type': registrant_type,
            'registrant_type_id': registrant_type_id,
            'registrant_policy': registrant_policy,
            'birth_date': birth_date,
            'birth_cc': birth_cc,
            'birth_city': birth_city,
            'birth_zip': birth_zip,
            'publication': publication,
            'vat': vat,
            'siren': siren,
            'duns': duns,
            'trademark': trademark,
            'waldec': waldec,
            'registrant_type_other': registrant_type_other,
            'privacy_protection': privacy_protection,
            'code': code,
            'publicity': publicity,
            'kpp': kpp,
            'passport_number': passport_number,
            'passport_issued_by': passport_issued_by,
            'passport_issued_on': passport_issued_on,
            'organization_authority': organization_authority,
            'organization_create_date': organization_create_date,
            'aero_id': aero_id,
            'aero_key': aero_key,
            'registrant_title': registrant_title,
            'bank_bic': bank_bic,
            'bank_name': bank_name,
            'bank_iban': bank_iban
        })

        return self.make_request('domains/order-transfer-domain.json', method='POST', data=params)

    def list_domains(self, page=1, rows_per_page=10, search=None, order_by=None):
        """
        List registered domains with optional filters.

        Args:
            page (int, optional): Page number of the results. Defaults to 1.
            rows_per_page (int, optional): Number of results per page. Can be 10, 20, 30, 50, 100 or 250. Defaults to 250.
            search (str, optional): Domain name, reverse zone name, or keyword to search for.
            order_by (str, optional): Sorting. Can be name (default), expire or registered.

        Returns:
            dict: Response from the API containing the list of domains based on the filters.
        """
        params = self._auth_params({
            'page': page,
            'rows-per-page': rows_per_page,
            'search': search,
            'order_by': order_by
        })
        return self.make_request('domains/list-domains.json', method='GET', params=params)

    def get_pages_count(self, rows_per_page=10, search=None):
        """
        Retrieves the number of pages of registered domains based on optional filters.

        Args:
            rows_per_page (int, optional): Number of results per page. Can be 10, 20, 30, 50, 100 or 250. Defaults to 10.
            search (str, optional): Domain name, reverse zone name, or keyword to search for.

        Returns:
            dict: Response from the API containing the number of pages of DNS zones.
        """
        params = self._auth_params({
            'rows-per-page': rows_per_page,
            'search': search
        })
        return self.make_request('domains/get-pages-count.json', method='GET', params=params)

    def get_domain_info(self, domain_name):
        """
        Retrieves information about a specific domain name.

        Args:
            domain_name (str): Domain name to retrieve information for.

        Returns:
            dict: Response from the API containing information about the specified domain.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('domains/domain-info.json', method='GET', params=params)

    def get_domain_contacts(self, domain_name):
        """
        Retrieves a specific domain name's contacts.

        Args:
            domain_name (str): Domain name to retrieve contacts for.

        Returns:
            dict: Response from the API containing information about the specified domain.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('domains/get-contacts.json', method='GET', params=params)

    def modify_domain_contact(self, domain_name, type, mail, name, company,
                              address, city, state, zip, country,
                              telnocc, telno, faxnocc=None, faxno=None):
        """
        Changes a specific domain name's contacts.

        Args:
            domain_name (str): Domain name to modify a contact for.
            type (str): The type of contact you want to change.
            mail (str): Email address
            name (str): First and last name of the person
            company (str): Name of the company.
            address (str): Address of the company/person(street, number, etc)
            city (str): Example: Dallas
            state (str): Example: Texas
            zip (int or str): ZIP code
            country (str): 2 letters country code according to ISO 3166
            telnocc (int): Phone number calling code. Between 1 and 3 digits.
            telno (int): Phone number
            faxnocc (int, optional): Fax number calling code. Between 1 and 3 digits.
            faxno (int, optional): Fax number.

        Returns:
            dict: Response from the API indicating success or failure of the update.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'type': type,
            'mail': mail,
            'name': name,
            'company': company,
            'address': address,
            'city': city,
            'state': state,
            'zip': zip,
            'country': country,
            'telnocc': telnocc,
            'telno': telno,
            'faxnocc': faxnocc,
            'faxno': faxno
        })
        return self.make_request('domains/set-contacts.json', method='POST', params=params)

    def get_domain_nameservers(self, domain_name):
        """
        Retrieves a specific domain name's name servers.

        Args:
            domain_name (str): Domain name to retrieve information for.

        Returns:
            dict: Response from the API containing information about the specified domain.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('domains/get-nameservers.json', method='GET', params=params)

    def set_domain_nameservers(self, domain_name, nameservers):
        """
        Retrieves a specific domain name's name servers.

        Args:
            domain_name (str): Domain name to retrieve information for.
            nameservers ([str]): Array containing the domain's new name servers.

        Returns:
            dict: Response from the API indicating success or failure of the update.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'ns[]': nameservers
        })
        return self.make_request('domains/get-nameservers.json', method='POST', params=params)

    def get_domain_child_nameservers(self, domain_name):
        """
        Retrieves a domain name's child name servers.

        Args:
            domain_name (str): Domain name to retrieve information for.

        Returns:
            dict: Response from the API containing information about the specified domain.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('domains/get-child-nameservers.json', method='GET', params=params)

    def add_domain_child_nameserver(self, domain_name, host, ip):
        """
        Adds a child name server (Glue record) to a domain name.

        Args:
            domain_name (str): Domain name to add the child name server to.
            host (str): Host of the child name server.
            ip (str): IP address of the child name server.

        Returns:
            dict: Response from the API indicating success or failure of the operation.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'host': host,
            'ip': ip
        })
        return self.make_request('domains/add-child-nameservers.json', method='POST', params=params)

    def delete_domain_child_nameserver(self, domain_name, host, ip):
        """
        Deletes a child name server from a domain name.

        Args:
            domain_name (str): Domain name to add the child name server to.
            host (str): Host of the child name server.
            ip (str): IP address of the child name server.

        Returns:
            dict: Response from the API indicating success or failure of the operation.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'host': host,
            'ip': ip
        })
        return self.make_request('domains/delete-child-nameservers.json', method='POST', params=params)

    def modify_domain_child_nameserver(self, domain_name, host, old_ip, new_ip):
        """
        Update a child name server for a domain name.

        Args:
            domain_name (str): Domain name to add the child name server to.
            host (str): Host of the child name server.
            old_ip (str): Old IP address of the child name server.
            new_ip (str): New IP address of the child name server.

        Returns:
            dict: Response from the API indicating success or failure of the operation.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'host': host,
            'old-ip': old_ip,
            'new-ip': new_ip
        })
        return self.make_request('domains/modify-child-nameservers.json', method='POST', params=params)

    def modify_domain_privacy_protection(self, domain_name, status):
        """
        Modifies the privacy protection of the domain.

        Args:
            domain_name (str): Domain name to change privacy protection for.
            status (int): 1 or 0 for enable or disable.

        Returns:
            dict: Response from the API indicating success or failure of the operation.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'status': status
        })
        return self.make_request('domains/edit-privacy-protection.json', method='POST', params=params)

    def modify_domain_transfer_lock(self, domain_name, status):
        """
        Modifies the transfer lock of the domain.

        Args:
            domain_name (str): Domain name to change the transfer lock for.
            status (int): 1 or 0 for enable or disable.

        Returns:
            dict: Response from the API indicating success or failure of the operation.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'status': status
        })
        return self.make_request('domains/edit-transfer-lock.json', method='POST', params=params)

    def get_domain_transfer_code(self, domain_name):
        """
        Retrieves a specific domain name's transfer code.

        Args:
            domain_name (str): Domain name to retrieve information for.

        Returns:
            dict: Response from the API containing information about the specified domain.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('domains/get-transfer-code.json', method='GET', params=params)

    def get_domain_raa_status(self, domain_name):
        """
        Retrieves a specific domain name's RAA contact information status.

        Args:
            domain_name (str): Domain name to retrieve information for.

        Returns:
            dict: Response from the API containing information about the specified domain.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('domains/get-raa-status.json', method='GET', params=params)

    def resend_domain_raa_verification(self, domain_name):
        """
        Resend the verification e-mail to the domain's administrative contact.

        Args:
            domain_name (str): Domain name to resend verification for.

        Returns:
            dict: Response from the API containing information about the specified domain.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('domains/resend-raa-verification.json', method='POST', params=params)
