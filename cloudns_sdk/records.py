from .validations import validate
from .utils import process_params


class RecordsAPI:
    """
    Provides methods to manage DNS records for a zone.

    Attributes:
        VALID_ZONE_TYPES (list): List of valid zone types supported by the API.

    Args:
        auth_params (callable): Function that returns authentication parameters for API requests.
        make_request (callable): Function to make HTTP requests to the API.
        auth_id (str): Authentication ID for API access.
        auth_password (str): Authentication password for API access.
    """

    VALID_ZONE_TYPES = ['domain', 'reverse', 'parked', 'master', 'slave', 'geodns']

    def __init__(self, auth_params, make_request, auth_id, auth_password):
        self._auth_params = auth_params
        self.make_request = make_request
        self.auth_id = auth_id
        self.auth_password = auth_password

    def is_valid_zone_type(self, zone_type):
        """
        Checks if the provided zone type is valid.

        Args:
            zone_type (str): Type of the DNS zone.

        Returns:
            bool: True if the zone type is valid, False otherwise.
        """
        return zone_type in self.VALID_ZONE_TYPES

    def get_record(self, domain_name, record_id):
        """
        Retrieves details of a specific DNS record.

        Args:
            domain_name (str): Domain name or reverse zone name.
            record_id (int): ID of the record to retrieve.

        Returns:
            dict: Response from the API containing record details.
        """
        params = self._auth_params({'domain-name': domain_name, 'record-id': record_id})
        return self.make_request('dns/get-record.json', method='GET', params=params)

    def list_records(self, domain_name, host=None, host_like=None, record_type=None,
                     rows_per_page=20, page=1, order_by=None):
        """
        Lists DNS records for a given domain with optional filters.

        Args:
            domain_name (str): Domain name or reverse zone name.
            host (str, optional): Hostname of the records to list.
            host_like (str, optional): Partial match for hostname.
            record_type (str, optional): Type of the records to list.
            rows_per_page (int, optional): Number of records per page (default 20).
            page (int, optional): Page number to fetch (default 1).
            order_by (str, optional): Field to order records by.

        Returns:
            dict: Response from the API containing list of records.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'host': host,
            'host-like': host_like,
            'type': record_type,
            'rows-per-page': rows_per_page,
            'page': page,
            'order-by': order_by
        })
        return self.make_request('dns/records.json', method='GET', params=params)

    def get_records_pages_count(self, domain_name, host=None, record_type=None, rows_per_page=20):
        """
        Retrieves the number of pages available for DNS records.

        Args:
            domain_name (str): Domain name or reverse zone name.
            host (str, optional): Hostname of the records to count.
            record_type (str, optional): Type of the records to count.
            rows_per_page (int, optional): Number of records per page.

        Returns:
            dict: Response from the API containing the number of pages.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'host': host,
            'type': record_type,
            'rows-per-page': rows_per_page
        })
        return self.make_request('dns/get-records-pages-count.json', method='GET', params=params)

    def add_record(self, domain_name, record_type, record=None, host='', ttl=3600, **kwargs):
        """
        Adds a new DNS record to the specified domain.

        Args:
        domain_name (str): The name of the domain.
        record_type (str): Type of the record (e.g., A, AAAA, MX, CNAME, etc.).
        host (str): Host or subdomain.
        record (str): Record value (e.g., 10.10.10.10 or cname.cloudns.net).
        ttl (int): Time-to-live value. Available values are:
            60 = 1 minute,
            300 = 5 minutes,
            900 = 15 minutes,
            1800 = 30 minutes,
            3600 = 1 hour,
            21600 = 6 hours,
            43200 = 12 hours,
            86400 = 1 day,
            172800 = 2 days,
            259200 = 3 days,
            604800 = 1 week,
            1209600 = 2 weeks,
            2592000 = 1 month.
        priority (int, optional): Priority for MX or SRV record.
        weight (int, optional): Weight for SRV record.
        port (int, optional): Port for SRV record.
        frame (int, optional): 0 or 1 to disable or enable frame for Web redirects.
        frame_title (str, optional): Title if frame is enabled in Web redirects.
        frame_keywords (str, optional): Keywords if frame is enabled in Web redirects.
        frame_description (str, optional): Description if frame is enabled in Web redirects.
        mobile_meta (int, optional): Mobile responsive meta tags if Web redirects with frame is enabled. Default is 0.
        save_path (int, optional): 0 or 1 for Web redirects.
        redirect_type (int, optional): 301 or 302 for Web redirects if frame is disabled.
        mail (str, optional): E-mail address for RP records.
        txt (str, optional): Domain name for TXT record used in RP records.
        algorithm (int, optional): Algorithm used to create the SSHFP fingerprint. Required for SSHFP records only. Supported values are 'RSA', 'DSA', 'ECDSA', 'ED25519'
        fptype (int, optional): Type of the SSHFP algorithm. Required for SSHFP records only. 'SHA-1' and 'SHA-256' are supported.
        status (int, optional): Set to 1 to create the record active or 0 to create it inactive. If omitted, the record will be created active.
        geodns_location (int, optional): ID of a GeoDNS location for A, AAAA, CNAME, NAPTR, or SRV record.
        geodns_code (str, optional): Code of a GeoDNS location for A, AAAA, CNAME, NAPTR, or SRV record.
        caa_flag (int, optional): 0 for Non-critical or 128 for Critical.
        caa_type (str, optional): Type of CAA record. The available flags are issue, issuewild, iodef.
        caa_value (str, optional): Value for CAA record based on caa_type.
        tlsa_selector (str, optional): Specifies which part of the TLS certificate presented by the server will be matched against the association data.
        tlsa_usage (str, optional): Specifies the provided association that will be used.
        tlsa_matching_type (str, optional): Specifies how the certificate association is presented.
        key_tag (int, optional): Numeric value used for identifying the referenced DS record.
        digest_type (int, optional): Cryptographic hash algorithm used to create the Digest value.
        order (str, optional): Specifies the order in which multiple NAPTR records must be processed (low to high).
        pref (str, optional): Specifies the order (low to high) in which NAPTR records with equal Order values should be processed.
        flag (int, optional): Controls aspects of the rewriting and interpretation of the fields in the record.
        params (str, optional): Specifies the service parameters applicable to this delegation path.
        regexp (str, optional): Contains a substitution expression applied to the original string to construct the next domain name to look up.
        replace (int, optional): Specifies the next domain name (fully qualified) to query for depending on the potential values found in the flags field.
        cert_type (str, optional): Type of the Certificate/CRL.
        cert_key_tag (int, optional): Numeric value (0-65535) used to efficiently pick a CERT record.
        cert_algorithm (int, optional): Identifies the algorithm used to produce a legitimate signature.
        lat_deg (int, optional): Latitude degrees (0-90).
        lat_min (int, optional): Latitude minutes (0-59). Default is 0.
        lat_sec (int, optional): Latitude seconds (0-59). Default is 0.
        lat_dir (str, optional): Latitude direction (N for North, S for South).
        long_deg (int, optional): Longitude degrees (0-180).
        long_min (int, optional): Longitude minutes (0-59). Default is 0.
        long_sec (int, optional): Longitude seconds (0-59). Default is 0.
        long_dir (str, optional): Longitude direction (W for West, E for East).
        altitude (int, optional): Altitude in meters (-100000.00 to 42849672.95).
        size (int, optional): Size in meters (0 to 90000000.00). Default is 0.
        h_precision (int, optional): Horizontal precision in meters (0 to 90000000.00). Default is 10000.
        v_precision (int, optional): Vertical precision in meters (0 to 90000000.00). Default is 10.
        cpu (str, optional): CPU of the server.
        os (str, optional): Operating system of the server.

        Returns:
            dict: Response from the API confirming the record addition.

        Raises:
            ValueError: If validation of record data fails.
        """
        record_data = {key: value for key, value in locals().items() if key != 'kwargs' and value is not None}
        record_data.update(kwargs)

        valid, error = validate(record_data)

        if valid:
            cred = self._auth_params()
            params = process_params(record_data, cred)
            return self.make_request('dns/add-record.json', method='POST', data=params)
        else:
            raise ValueError(f"Error: {error}")

    def delete_record(self, domain_name, record_id):
        """
        Deletes a specific DNS record from the domain.

        Args:
            domain_name (str): Domain name to delete the record.
            record_id (int): ID of the record to delete.

        Returns:
            dict: Response from the API confirming the record deletion.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'record-id': record_id
        })
        return self.make_request('dns/delete-record.json', method='POST', data=params)

    def modify_record(self, domain_name, record_id, host='', record=None, ttl=3600, **kwargs):
        """
        Modifies an existing DNS record in the specified domain.

        Args:
        domain_name (str): The name of the domain.
        record_type (str): Type of the record (e.g., A, AAAA, MX, CNAME, etc.).
        host (str): Host or subdomain.
        record (str): Record value (e.g., 10.10.10.10 or cname.cloudns.net).
        ttl (int): Time-to-live value. Available values are:
            60 = 1 minute,
            300 = 5 minutes,
            900 = 15 minutes,
            1800 = 30 minutes,
            3600 = 1 hour,
            21600 = 6 hours,
            43200 = 12 hours,
            86400 = 1 day,
            172800 = 2 days,
            259200 = 3 days,
            604800 = 1 week,
            1209600 = 2 weeks,
            2592000 = 1 month.
        priority (int, optional): Priority for MX or SRV record.
        weight (int, optional): Weight for SRV record.
        port (int, optional): Port for SRV record.
        frame (int, optional): 0 or 1 to disable or enable frame for Web redirects.
        frame_title (str, optional): Title if frame is enabled in Web redirects.
        frame_keywords (str, optional): Keywords if frame is enabled in Web redirects.
        frame_description (str, optional): Description if frame is enabled in Web redirects.
        mobile_meta (int, optional): Mobile responsive meta tags if Web redirects with frame is enabled. Default is 0.
        save_path (int, optional): 0 or 1 for Web redirects.
        redirect_type (int, optional): 301 or 302 for Web redirects if frame is disabled.
        mail (str, optional): E-mail address for RP records.
        txt (str, optional): Domain name for TXT record used in RP records.
        algorithm (int, optional): Algorithm used to create the SSHFP fingerprint. Required for SSHFP records only. Supported values are 'RSA', 'DSA', 'ECDSA', 'ED25519'
        fptype (int, optional): Type of the SSHFP algorithm. Required for SSHFP records only. 'SHA-1' and 'SHA-256' are supported.
        status (int, optional): Set to 1 to create the record active or 0 to create it inactive. If omitted, the record will be created active.
        geodns_location (int, optional): ID of a GeoDNS location for A, AAAA, CNAME, NAPTR, or SRV record.
        geodns_code (str, optional): Code of a GeoDNS location for A, AAAA, CNAME, NAPTR, or SRV record.
        caa_flag (int, optional): 0 for Non-critical or 128 for Critical.
        caa_type (str, optional): Type of CAA record. The available flags are issue, issuewild, iodef.
        caa_value (str, optional): Value for CAA record based on caa_type.
        tlsa_selector (str, optional): Specifies which part of the TLS certificate presented by the server will be matched against the association data.
        tlsa_usage (str, optional): Specifies the provided association that will be used.
        tlsa_matching_type (str, optional): Specifies how the certificate association is presented.
        key_tag (int, optional): Numeric value used for identifying the referenced DS record.
        digest_type (int, optional): Cryptographic hash algorithm used to create the Digest value.
        order (str, optional): Specifies the order in which multiple NAPTR records must be processed (low to high).
        pref (str, optional): Specifies the order (low to high) in which NAPTR records with equal Order values should be processed.
        flag (int, optional): Controls aspects of the rewriting and interpretation of the fields in the record.
        params (str, optional): Specifies the service parameters applicable to this delegation path.
        regexp (str, optional): Contains a substitution expression applied to the original string to construct the next domain name to look up.
        replace (int, optional): Specifies the next domain name (fully qualified) to query for depending on the potential values found in the flags field.
        cert_type (str, optional): Type of the Certificate/CRL.
        cert_key_tag (int, optional): Numeric value (0-65535) used to efficiently pick a CERT record.
        cert_algorithm (int, optional): Identifies the algorithm used to produce a legitimate signature.
        lat_deg (int, optional): Latitude degrees (0-90).
        lat_min (int, optional): Latitude minutes (0-59). Default is 0.
        lat_sec (int, optional): Latitude seconds (0-59). Default is 0.
        lat_dir (str, optional): Latitude direction (N for North, S for South).
        long_deg (int, optional): Longitude degrees (0-180).
        long_min (int, optional): Longitude minutes (0-59). Default is 0.
        long_sec (int, optional): Longitude seconds (0-59). Default is 0.
        long_dir (str, optional): Longitude direction (W for West, E for East).
        altitude (int, optional): Altitude in meters (-100000.00 to 42849672.95).
        size (int, optional): Size in meters (0 to 90000000.00). Default is 0.
        h_precision (int, optional): Horizontal precision in meters (0 to 90000000.00). Default is 10000.
        v_precision (int, optional): Vertical precision in meters (0 to 90000000.00). Default is 10.
        cpu (str, optional): CPU of the server.
        os (str, optional): Operating system of the server.

        Returns:
            dict: Response from the API confirming the record modification.

        Raises:
            ValueError: If validation of record data fails.
        """
        record_data = {key: value for key, value in locals().items() if key != 'kwargs' and value is not None}
        record_data.update(kwargs)

        valid, error = validate(record_data)

        if valid:
            cred = self._auth_params()
            params = process_params(record_data, cred)
            return self.make_request('dns/mod-record.json', method='POST', data=params)
        else:
            raise ValueError(f"Error: {error}")

    def copy_records(self, domain_name, from_domain, delete_current_records=False):
        """
        Copies DNS records from one domain to another.

        Args:
            domain_name (str): Destination domain to copy records into.
            from_domain (str): Source domain to copy records from.
            delete_current_records (bool, optional): Whether to delete existing records in the destination domain.

        Returns:
            dict: Response from the API confirming the record copy.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'from-domain': from_domain,
            'delete-current-records': 1 if delete_current_records else 0
        })

        return self.make_request('dns/copy-records.json', method='POST', data=params)

    def get_available_record_types(self, zone_type):
        """
        Retrieves available DNS record types for a specific zone type.

        Args:
            zone_type (str): Type of the DNS zone.

        Returns:
            dict: Response from the API containing available record types.

        Raises:
            ValueError: If an invalid zone type is provided.
        """
        if not self.is_valid_zone_type(zone_type):
            raise ValueError(f"Invalid zone type: {zone_type}. Expected one of {', '.join(self.VALID_ZONE_TYPES)}.")

        params = self._auth_params({'zone-type': zone_type})
        return self.make_request('dns/get-available-record-types.json', method='GET', params=params)

    def get_available_ttl(self, domain_name):
        """
        Retrieves available TTL values for records in a domain.

        Args:
            domain_name (str): Domain name to retrieve TTL values.

        Returns:
            dict: Response from the API containing available TTL values.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/get-available-ttl.json', method='GET', params=params)

    def get_records_count(self, domain_name):
        """
        Retrieves the total count of DNS records in a domain.

        Args:
            domain_name (str): Domain name to retrieve records count.

        Returns:
            dict: Response from the API containing total records count.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/get-records-count.json', method='GET', params=params)

    def get_soa_details(self, domain_name):
        """
        Retrieves the SOA (Start of Authority) details for a domain.

        Args:
            domain_name (str): Domain name to retrieve SOA details.

        Returns:
            dict: Response from the API containing SOA details.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/soa-details.json', method='GET', params=params)

    def modify_soa_details(self, domain_name, primary_ns, admin_email='', refresh=7200, retry=7200, expire=2419200,
                           default_ttl=3600):
        """
        Modifies the SOA (Start of Authority) details for a domain.

        Args:
            domain_name (str): Domain name to modify SOA details.
            primary_ns (str): Primary nameserver hostname.
            admin_email (str, optional): DNS admin's email address.
            refresh (int, optional): Refresh rate in seconds (default 7200).
            retry (int, optional): Retry rate in seconds (default 7200).
            expire (int, optional): Expiry time in seconds (default 2419200).
            default_ttl (int, optional): Default TTL in seconds (default 3600).

        Returns:
            dict: Response from the API confirming SOA modification.

        Raises:
            ValueError: If validation of SOA details fails.
        """
        record_data = {key: value for key, value in locals().items() if key != 'kwargs' and value is not None}

        valid, error = validate(record_data)
        if valid:
            params = self._auth_params({
                'domain-name': domain_name,
                'primary-ns': primary_ns,
                'admin-email': admin_email,
                'refresh': refresh,
                'retry': retry,
                'expire': expire,
                'default-ttl': default_ttl
            })
            return self.make_request('dns/modify-soa.json', method='POST', data=params)
        else:
            raise ValueError(f"Error: {error}")

    def get_dynamic_url(self, domain_name, record_id):
        """
        Retrieves the dynamic URL details for a specific record.

        Args:
            domain_name (str): Domain name containing the record.
            record_id (int): ID of the record to retrieve dynamic URL.

        Returns:
            dict: Response from the API containing dynamic URL details.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'record-id': record_id
        })
        return self.make_request('dns/get-dynamic-url.json', method='GET', params=params)

    def disable_dynamic_url(self, domain_name, record_id):
        """
        Disables the dynamic URL for a specific record.

        Args:
            domain_name (str): Domain name containing the record.
            record_id (int): ID of the record to disable dynamic URL.

        Returns:
            dict: Response from the API confirming dynamic URL disablement.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'record-id': record_id
        })
        return self.make_request('dns/disable-dynamic-url.json', method='POST', data=params)

    def change_dynamic_url(self, domain_name, record_id):
        """
        Changes the dynamic URL for a specific record.

        Args:
            domain_name (str): Domain name containing the record.
            record_id (int): ID of the record to change dynamic URL.

        Returns:
            dict: Response from the API confirming dynamic URL change.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'record-id': record_id
        })
        return self.make_request('dns/change-dynamic-url.json', method='POST', data=params)

    def get_dynamic_url_history(self, domain_name, record_id, rows_per_page=20, page=1):
        """
        Retrieves the history of dynamic URL changes for a specific record.

        Args:
            domain_name (str): Domain name containing the record.
            record_id (int): ID of the record to retrieve dynamic URL history.
            rows_per_page (int, optional): Number of records per page (default 20).
            page (int, optional): Page number to fetch (default 1).

        Returns:
            dict: Response from the API containing dynamic URL history.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'record-id': record_id,
            'rows-per-page': rows_per_page,
            'page': page
        })
        return self.make_request('dns/get-dynamic-url-history.json', method='GET', params=params)

    def get_dynamic_url_history_pages(self, domain_name, record_id, rows_per_page=20):
        """
        Retrieves the number of pages available for dynamic URL history of a record.

        Args:
            domain_name (str): Domain name containing the record.
            record_id (int): ID of the record to retrieve dynamic URL history pages.
            rows_per_page (int, optional): Number of records per page.

        Returns:
            dict: Response from the API containing the number of pages.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'record-id': record_id,
            'rows-per-page': rows_per_page
        })
        return self.make_request('dns/get-dynamic-url-history-pages.json', method='GET', params=params)

    def change_record_status(self, domain_name, record_id, status=True):
        """
        Changes the status (active/inactive) of a specific record.

        Args:
            domain_name (str): Domain name containing the record.
            record_id (int): ID of the record to change status.
            status (bool, optional): True to activate, False to deactivate (default True).

        Returns:
            dict: Response from the API confirming the record status change.
        """
        params = self._auth_params({
            'domain-name': domain_name,
            'record-id': record_id,
            'status': 1 if status else 0
        })
        return self.make_request('dns/change-record-status.json', method='GET', params=params)

    def reset_soa_details(self, domain_name):
        """
        Resets the SOA (Start of Authority) details for a domain to default.

        Args:
            domain_name (str): Domain name to reset SOA details.

        Returns:
            dict: Response from the API confirming SOA details reset.
        """
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/reset-soa.json', method='GET', params=params)
