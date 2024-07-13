

# CloudNS SDK Documentation

Welcome to the CloudNS SDK documentation repository! This repository contains the Python SDK for interacting with the CloudNS API. It provides convenient methods to manage DNS records, zones, notifications, and more.

## Installation

To install the CloudNS SDK, you can use pip:

```bash
pip install cloudns-sdk
```

## Usage

The CloudNS SDK allows you to programmatically interact with the CloudNS API. Below are some examples of its usage:

```python
from cloudns_sdk import ClouDNSAPI

# Initialize the API client
api = ClouDNSAPI(auth_id, auth_password)

# Example: Check login status
response = api.login()
print(response)
```
Replace `auth-id` and `auth-password` with actual values from your CloudNS account. 

For detailed usage instructions and API reference, please refer to the [full documentation](https://lively-ops.github.io/cloudns_sdk/cloudns_sdk.html).

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

## Author

This SDK is maintained by [Komal Paudyal](mailto:komal.paudyal@icloud.com).

---

