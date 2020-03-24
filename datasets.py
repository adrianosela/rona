#!/usr/bin/env python

import pandas as pd
import requests

CONFIRMED = 'confirmed'
RECOVERIES = 'recoveries'
DEATHS = 'deaths'

DATASET_URLS = {
    CONFIRMED:'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv',
    RECOVERIES: 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv',
    DEATHS: 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv'
}

def load():
    dsets = dict()
    for dset in DATASET_URLS:
        dsets[dset] = pd.read_csv(DATASET_URLS[dset])
    return dsets

def download():
    for dset in DATASET_URLS:
        resp = requests.get(DATASET_URLS[dset])
        with open("%s.csv" % dset, 'w') as f:
            f.write(resp.text)
        f.close()
