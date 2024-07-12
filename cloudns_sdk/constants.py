# constants.py

KEYS_TO_CHECK = [
    'domain_name', 'record_id', 'record', 'host', 'ttl', 'priority', 'weight', 'port',
    'frame', 'frame_title', 'frame_keywords', 'frame_description', 'mobile_meta',
    'save_path', 'redirect_type', 'mail', 'txt', 'algorithm', 'fptype', 'status',
    'geodns_location', 'geodns_code', 'caa_flag', 'caa_type', 'caa_value',
    'tlsa_selector', 'tlsa_usage', 'tlsa_matching_type', 'key_tag', 'digest_type',
    'order', 'pref', 'flag', 'params', 'regexp', 'replace', 'cert_type',
    'cert_key_tag', 'cert_algorithm', 'lat_deg', 'lat_min', 'lat_sec', 'lat_dir',
    'long_deg', 'long_min', 'long_sec', 'long_dir', 'altitude', 'size', 'h_precision',
    'v_precision', 'cpu', 'os'
]

KEYS_TO_RETAIN_UNDERSCORE = {
    'caa_flag', 'caa_type', 'caa_value', 'tlsa_selector', 'tlsa_usage', 'tlsa_matching_type'
}