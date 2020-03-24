#!/usr/bin/env python

import pandas as pd
import sys
from functools import reduce

CONFIRMED = 'confirmed'
RECOVERIES = 'recoveries'
DEATHS = 'deaths'

DATASET_URLS = {
    CONFIRMED:'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv',
    RECOVERIES: 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv',
    DEATHS: 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv'
}

PROVINCE_ID = 'Province/State'
COUNTRY_ID = 'Country/Region'
LATITUDE_ID = 'Lat'
LONGITUDE_ID = 'Long'
DATE_ID = 'Date'

COLUMN_IDS = [
    PROVINCE_ID,
    COUNTRY_ID,
    LATITUDE_ID,
    LONGITUDE_ID
]

# returns a dict of dataset name to pandas dataframe
def load():
    dsets = dict()
    for dset in DATASET_URLS:
        dsets[dset] = pd.read_csv(DATASET_URLS[dset])
    return dsets

# returns a pandas dataframe of all datasets combined
def combine(dsets):
    # data comes in "wide" format, reshape to “long” format with
    # one country-date combination per row and counts in a single column
    for dset in dsets:
        dsets[dset] = dsets[dset].melt(id_vars=COLUMN_IDS, var_name=DATE_ID, value_name=dset)
    # merge all the dataframes on date
    combined = reduce(lambda x, y: pd.merge(x, y, on=COLUMN_IDS.append(DATE_ID)), list(dsets.values()))
    # format date and populate empty cells
    combined[DATE_ID] = pd.to_datetime(combined[DATE_ID])
    combined[PROVINCE_ID] = combined[PROVINCE_ID].fillna("")
    return combined

if __name__ == "__main__":
    path = "."
    if len(sys.argv) > 1:
        path = sys.argv[1]
    combine(load()).to_csv(f'{path}/covid.csv', index=False)
