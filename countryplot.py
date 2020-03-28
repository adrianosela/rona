#!/usr/bin/env python

import datasets
import pandas as pd
import matplotlib.pyplot as plt
import qeds
import sys

# activate plot theme
qeds.themes.mpl_style()

# download latest version of data
dsets = datasets.load()
covid = datasets.combine(dsets)

def plot_country(country):
    try:
        by_country = covid.groupby(datasets.COUNTRY_ID).get_group(country)
        print(by_country)
    except:
        print(f'no data for country: "{country}"')
        sys.exit(1)

    # plot confirmed cases data for country per province/state
    fig, ax = plt.subplots(figsize=(10,6))
    for prov, df in by_country.reset_index().groupby(datasets.PROVINCE_ID):
        df.plot(x="Date", y=datasets.CONFIRMED, ax=ax, label=prov)
    ax.set_title("Cases by Province/State")
    plt.show()

if __name__ == "__main__":
    plot_country(sys.argv[1])
