#!/usr/bin/env python

import requests

CONFIRMED_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
RECOVERED_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv'
DEATHS_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv'

DATASET_URLS = {
    "confirmed": CONFIRMED_URL,
    "recovered": RECOVERED_URL,
    "dead": DEATHS_URL
}

for dset in DATASET_URLS:
    resp = requests.get(DATASET_URLS[dset])
    with open("%s.csv" % dset, 'w') as f:
        f.write(resp.text)
    f.close()
