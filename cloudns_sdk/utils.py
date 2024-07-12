

def process_params(record_data, params):
    keys_to_check = ['domain_name', 'record_type', 'record_id', 'record', 'host', 'ttl', 'priority', 'weight', 'port',
                     'frame', 'frame_title', 'frame_keywords',
                     'frame_description', 'mobile_meta', 'save_path', 'redirect_type', 'mail', 'txt',
                     'algorithm', 'fptype', 'status', 'geodns_location', 'geodns_code', 'caa_flag',
                     'caa_type', 'caa_value', 'tlsa_selector', 'tlsa_usage', 'tlsa_matching_type',
                     'key_tag', 'digest_type', 'order', 'pref', 'flag', 'params', 'regexp', 'replace',
                     'cert_type', 'cert_key_tag', 'cert_algorithm', 'lat_deg', 'lat_min', 'lat_sec',
                     'lat_dir', 'long_deg', 'long_min', 'long_sec', 'long_dir', 'altitude', 'size',
                     'h_precision', 'v_precision', 'cpu', 'os']

    keys_to_retain_underscore = {'caa_flag', 'caa_type', 'caa_value', 'tlsa_selector', 'tlsa_usage',
                                 'tlsa_matching_type'}

    for key in keys_to_check:
        if key in record_data and record_data[key] is not None:
            if key in keys_to_retain_underscore:
                params[key] = record_data[key]
            else:
                params[key.replace('_', '-')] = record_data[key]

    return params