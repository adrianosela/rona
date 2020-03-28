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

def plot_world_by_country():
    fig, ax = plt.subplots(figsize=(10,6))
    for country, df in covid.reset_index().groupby(datasets.COUNTRY_ID):
        df.plot(x="Date", y=datasets.DEATHS, ax=ax, label=country)
    ax.set_title("Cases by Country")
    plt.show()

if __name__ == "__main__":
    plot_world_by_country()
