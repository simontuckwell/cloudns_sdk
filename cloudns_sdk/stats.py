

class StatsAPI:
    def __init__(self, auth_params, make_request):
        self._auth_params = auth_params
        self.make_request = make_request



    def get_hourly_stats(self, domain_name, day, month, year):
        params = self._auth_params({'domain-name': domain_name, 'day': day, 'month': month, 'year': year})
        return self.make_request('dns/statistics-hourly.json', method='GET', params=params)

    def get_daily_stats(self, domain_name, month, year):
        params = self._auth_params({'domain-name': domain_name, 'month': month, 'year': year})
        return self.make_request('dns/statistics-daily.json', method='GET', params=params)

    def get_monthly_stats(self, domain_name, year):
        params = self._auth_params({'domain-name': domain_name, 'year': year})
        return self.make_request('dns/statistics-monthly.json', method='GET', params=params)

    def get_yearly_stats(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/statistics-yearly.json', method='GET', params=params)

    def get_last_30_days_stats(self, domain_name):
        params = self._auth_params({'domain-name': domain_name})
        return self.make_request('dns/statistics-last-30-days.json', method='GET', params=params)


