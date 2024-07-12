from constants import KEYS_TO_CHECK, KEYS_TO_RETAIN_UNDERSCORE

def process_params(record_data):
    params = {}
    for key in KEYS_TO_CHECK:
        if key in record_data and record_data[key] is not None:
            if key in KEYS_TO_RETAIN_UNDERSCORE:
                params[key] = record_data[key]
            else:
                params[key.replace('_', '-')] = record_data[key]
    return params