#!/usr/bin/env python

import pandas as pd

CONFIRMED = 'confirmed'
RECOVERIES = 'recoveries'
DEATHS = 'deaths'

dataset_urls = {
    CONFIRMED:'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv',
    RECOVERIES: 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv',
    DEATHS: 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv'
}

def download():
    dsets = dict()
    for dset in dataset_urls:
        dsets[dset] = pd.read_csv(dataset_urls[dset])
    return dsets
