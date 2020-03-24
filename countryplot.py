#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import qeds
from sklearn import (
    linear_model, metrics, neural_network, pipeline, model_selection, preprocessing
)
from functools import reduce

DATASET_URLS = {
    'confirmed':'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv',
    'recoveries': 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv',
    'deaths': 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv'
}

# activate plot theme
qeds.themes.mpl_style();

# load CSV data to a dict of dataset name to pandas dataframe
DATASETS = dict()
for dset in DATASET_URLS:
    DATASETS[dset] = pd.read_csv(DATASET_URLS[dset])

# data comes in "wide" format, reshape to “long” format with 
# one country-date combination per row and counts in a single column
ids = ["Province/State","Country/Region", "Lat","Long"]
for dset in DATASETS:
    DATASETS[dset] = DATASETS[dset].melt(id_vars=ids, var_name="Date", value_name=dset)

# merge all the dataframes on date
covid = reduce(lambda x, y: pd.merge(x, y, on=ids.append("Date")), list(DATASETS.values()))

# format date
covid["Date"] = pd.to_datetime(covid["Date"])

# populate empty cells
covid["Province/State"]=covid["Province/State"].fillna("")

print(covid.groupby("Country/Region").get_group("Canada").groupby("Province/State").tail(1))
