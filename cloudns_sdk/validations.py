import re
import ipaddress

# Constants
ALGORITHMS = {'RSA', 'DSA', 'ECDSA', 'ED25519'}
CAA_TYPES = {'issue', 'issuewild', 'iodef'}
FP_TYPES = {'SHA-1', 'SHA-256'}
TTLS = {60, 300, 900, 1800, 3600, 21600, 43200, 86400, 172800, 259200, 604800,
        1209600, 2592000}
ZONE_TYPES = {'master', 'slave', 'parked', 'geodns', 'domain', 'reverse'}

RECORD_TYPES = {'A', 'AAAA', 'MX', 'CNAME', 'TXT', 'SPF', 'NS', 'SRV', 'WR',
                'RP', 'SSHFP', 'ALIAS', 'CAA', 'TLSA', 'CERT', 'DS', 'PTR',
                'NAPTR', 'HINFO', 'LOC', 'DNAME', 'SMIMEA', 'OPENPGPKEY'}
DIRECTIONS = {'N', 'S', 'W', 'E'}

def validate_integer(value, name):
    if not isinstance(value, int):
        raise ValueError(f"{name} must be an integer.")

def validate_string(value, name):
    if not isinstance(value, str):
        raise ValueError(f"{name} must be a string.")

def validate_domain_name(value):
    validate_string(value, "domain-name")
    pattern = r'^((?=[a-z0-9-]{1,63}\.)(xn--)?[a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,63}$'
    if not re.match(pattern, value):
        raise ValueError("Invalid domain name.")

def validate_record_type(value):
    validate_string(value, "record-type")
    if value not in RECORD_TYPES:
        raise ValueError("Invalid record type.")

def validate_host(value):
    validate_string(value, "host")
    # Additional validation rules for host can be added here

def validate_redirect_type(value):
    validate_integer(value, "redirect-type")
    if value not in {301, 302}:
        raise ValueError("Redirect type must be 301 or 302.")

def validate_ipv4_address(value, name):
    try:
        ipaddress.IPv4Address(value)
    except ipaddress.AddressValueError:
        raise ValueError(f"{name} must be a valid IPv4 address.")

def validate_ipv6_address(value, name):
    try:
        ipaddress.IPv6Address(value)
    except ipaddress.AddressValueError:
        raise ValueError(f"{name} must be a valid IPv6 address.")

def validate_record(value, params):
    if value is None:
        raise ValueError("Record cannot be empty.")
    validate_string(value, "record")
    if params.get("record-type") == "A":
        validate_ipv4_address(value, "record")
    elif params.get("record-type") == "AAAA":
        validate_ipv6_address(value, "record")

def validate_ttl(value):
    validate_integer(value, "ttl")
    if value not in TTLS:
        raise ValueError("Invalid TTL value.")

def validate_priority(value):
    validate_integer(value, "priority")

def validate_weight(value):
    validate_integer(value, "weight")

def validate_port(value):
    validate_integer(value, "port")

def validate_frame(value):
    validate_integer(value, "frame")
    if value not in {0, 1}:
        raise ValueError("frame must be 0 or 1.")

def validate_status(value):
    validate_integer(value, "status")
    if value not in {0, 1}:
        raise ValueError("status must be 0 or 1.")

def validate_email(value, name):
    validate_string(value, name)
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(pattern, value):
        raise ValueError(f"Invalid email format for {name}.")

def validate_geodns_code(value):
    validate_string(value, "geodns-code")
    # Additional validation rules for geodns-code can be added here

def validate_caa_flag(value):
    validate_integer(value, "caa_flag")
    if value not in {0, 128}:
        raise ValueError("CAA Flag must be 0 or 128.")

def validate_caa_type(value):
    validate_string(value, "caa_type")
    if value not in CAA_TYPES:
        raise ValueError("Invalid CAA Type.")

def validate_lat_long_direction(value, name):
    validate_string(value, name)
    if value not in DIRECTIONS:
        raise ValueError(f"{name} must be one of {DIRECTIONS}.")

def validate_lat_long_value(value, name, min_val, max_val):
    validate_integer(value, name)
    if not (min_val <= value <= max_val):
        raise ValueError(f"{name} must be between {min_val} and {max_val}.")

def validate_optional_integer(value, name, min_val=None, max_val=None):
    if value is not None:
        validate_integer(value, name)
        if min_val is not None and value < min_val:
            raise ValueError(f"{name} must be greater than or equal to {min_val}.")
        if max_val is not None and value > max_val:
            raise ValueError(f"{name} must be less than or equal to {max_val}.")

def validate_optional_string(value, name):
    if value is not None:
        validate_string(value, name)

def validate_algorithm(value):
    validate_string(value, "algorithm")
    if value not in ALGORITHMS:
        raise ValueError("Invalid algorithm.")

def validate_fptype(value):
    validate_integer(value, "fptype")
    if (value not in FP_TYPES and value not in [1, 2]):
        raise ValueError(f"Invalid fptype value. Valid values are: {FP_TYPES}")

def validate_tlsa_selection(value):
    validate_integer(value, "tlsa_selector")
    if value not in {0, 1}:
        raise ValueError("tlsa_selector must be 0 or 1.")

def validate_refresh(value):
    validate_optional_integer(value, "refresh", 1200, 43200)

def validate_retry(value):
    validate_optional_integer(value, "retry", 180, 2419200)

def validate_expiry(value):
    validate_optional_integer(value, "expiry", 1209600, 2419200)

def validate_default_ttl(value):
    validate_optional_integer(value, "default_ttl", 60, 2419200)

def validate_tlsa_usage(value):
    validate_integer(value, "tlsa_usage")
    if value not in {0, 1, 2, 3}:
        raise ValueError("tlsa_usage must be between 0 and 3.")

def validate_tlsa_matching_type(value):
    validate_integer(value, "tlsa_matching_type")
    if value not in {0, 1, 2}:
        raise ValueError("tlsa_matching_type must be between 0 and 2.")

def validate(params):
    validators = {
        "domain_name": validate_domain_name,
        "record_type": validate_record_type,
        "host": validate_host,
        "record": lambda v: validate_record(v, params),
        "ttl": validate_ttl,
        "priority": validate_priority,
        "weight": validate_weight,
        "port": validate_port,
        "frame": validate_frame,
        "frame_title": lambda v: validate_optional_string(v, "frame-title"),
        "redirect_type": validate_redirect_type,
        "admin_email": lambda v: validate_email(v, "admin_email"),
        "txt": lambda v: validate_optional_string(v, "txt"),
        "algorithm": validate_algorithm,
        "fptype": validate_fptype,
        "status": validate_status,
        "geodns-code": validate_geodns_code,
        "caa_flag": validate_caa_flag,
        "caa_type": validate_caa_type,
        "caa_value": lambda v: validate_optional_string(v, "caa_value"),
        "tlsa_usage": validate_tlsa_usage,
        "tlsa_selector": validate_tlsa_selection,
        "tlsa_matching_type": validate_tlsa_matching_type,
        "refresh": validate_refresh,
        "retry": validate_retry,
        "expiry": validate_expiry,
        "default_ttl": validate_default_ttl,
        "primary_ns": validate_domain_name
    }

    error_messages = []
    for key, validator in validators.items():
        if key in params:
            try:
                validator(params[key])
            except ValueError as e:
                error_messages.append(str(e))

    if error_messages:
        return False, error_messages
    else:
        return True, None
