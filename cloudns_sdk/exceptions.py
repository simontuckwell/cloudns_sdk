class ClouDNSAPIException(Exception):
    def __init__(self, response):
        self.status = response.get('status')
        self.description = response.get('statusDescription')
        super().__init__(self.description)

    def __str__(self):
        return f"ClouDNSAPIException: {self.status} - {self.description}"