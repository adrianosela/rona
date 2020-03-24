#!/usr/bin/env python

import pandas as pd

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
