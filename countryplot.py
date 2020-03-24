import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import qeds
from sklearn import (
    linear_model, metrics, neural_network, pipeline, model_selection, preprocessing
)

# activate plot theme
qeds.themes.mpl_style();

#!/usr/bin/env python

import requests

CONFIRMED_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
RECOVERIES_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv'
DEATHS_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv'

DATASET_URLS = {
    "confirmed": CONFIRMED_URL,
    "recoveries": RECOVERIES_URL,
    "deaths": DEATHS_URL
}

DATASETS = dict()

for dset in DATASET_URLS:
    DATASETS[dset] = pd.read_csv(DATASET_URLS[dset])

for dset in DATASET_URLS:
    print(DATASETS[dset].head())
