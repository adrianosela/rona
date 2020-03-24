#!/usr/bin/env python

import datasets
import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce

# download latest version of dataset
dsets = datasets.load()

# data comes in "wide" format, reshape to “long” format with 
# one country-date combination per row and counts in a single column
ids = ["Province/State", "Country/Region", "Lat", "Long"]
for dset in dsets:
    dsets[dset] = dsets[dset].melt(id_vars=ids, var_name="Date", value_name=dset)

# merge all the dataframes on date
covid = reduce(lambda x, y: pd.merge(x, y, on=ids.append("Date")), list(dsets.values()))

# format date and populate empty cells
covid["Date"] = pd.to_datetime(covid["Date"])
covid["Province/State"] = covid["Province/State"].fillna("")

# dataframe for specific country
country = covid.groupby("Country/Region").get_group("Canada") # FIXME: make variable

# plot confirmed cases data for country per province/state
fig, ax = plt.subplots(figsize=(10,6))
for prov, df in country.reset_index().groupby("Province/State"):
    df.plot(x="Date", y=datasets.CONFIRMED, ax=ax, label=prov)
ax.set_title("Cases by Province")

plt.show()
