#!/usr/bin/env python

import datasets
import warnings
import pandas as pd
from pandas_datareader import wb
import matplotlib.pyplot as plt
import qeds
import sys
import os

# activate plot theme
qeds.themes.mpl_style()

# World Bank data indices we'll use to predict
INDICES_USED = [
    # Population
    "SP.POP.TOTL", "SP.POP.DPND.OL",
    "SP.POP.DPND.YG", "EN.POP.DNST",
    "BG.GSR.NFSV.GD.ZS","SP.URB.GROW",
    "SP.URB.TOTL",
    # Economic
    "NY.GDP.MKTP.KD.ZG", "NY.GDP.PCAP.KD.ZG",
    # Migration & Remittances
    "SM.POP.TOTL", "BX.TRF.PWKR.CD.DT",
    "BM.TRF.PWKR.CD.DT",
    # Tourism
    "ST.INT.ARVL",
    "ST.INT.RCPT.CD",
    "ST.INT.XPND.CD",
    # Health care
    "SH.XPD.CHEX.PC.CD",
    "SH.XPD.OOPC.CH.ZS",
    "SH.MED.PHYS.ZS",
    "SH.MED.NUMW.P3",
    # Health, comorbitites
    "SH.PRV.SMOK.MA",
    "SH.PRV.SMOK.FE",
    "SH.TBS.INCD",
    "SH.STA.DIAB.ZS",
    "SP.DYN.LE00.IN",
    ]

# wdi file name (cache file)
WDI_FILE ='./wdi.pkl'

# replace dataset naming conventions with world bank's
def fixcountrynames(s):
    trans = { "Egypt, Arab Rep.":"Egypt",
        "Slovak Republic":"Slovakia",
        "Brunei Darussalam":"Brunei",
        "United States":"US",
        "Iran, Islamic Rep.":"Iran",
        "Korea, Rep.":"Korea, South",
        "Czech Republic":"Czechia",
        "Russian Federation":"Russia",
        "Congo, Dem. Rep.":"Congo (Kinshasa)",
        "Venezuela, RB":"Venezuela",
        "St. Lucia":"Saint Lucia",
        "St. Vincent and the Grenadines":"Saint Vincent and the Grenadines",
        "Congo, Rep.":"Republic of the Congo",
        "Bahamas, The":"The Bahamas",
        "Gambia, The":"The Gambia"
    }
    for t in trans :
        s["Country/Region"] = s["Country/Region"].replace(t, trans[t])
    return(s)


if __name__ == "__main__":
    dsets = datasets.load()
    covid = datasets.combine(dsets)
    if (os.path.isfile(WDI_FILE)) :
        warnings.warn("Reading cached WDI data from disk, delete file to download updated")
        wdi = pd.read_pickle(WDI_FILE)
    else :
        wdi = covid.drop(columns=["Date","Province/State","Lat","Long", datasets.CONFIRMED,"deaths","recoveries"]).drop_duplicates()
        for id in INDICES_USED:
            s = wb.download(indicator=id, country="all", start=2005, end=2019).reset_index()

            # use most recent non missing value
            s = s.dropna().groupby("country").last()
            s = s.drop(columns="year").reset_index()

            # match country names to covid data
            s = s.rename(columns={"country":"Country/Region"})
            s = fixcountrynames(s)
            wdi = pd.merge(wdi, s, how='left', on='Country/Region', validate="one_to_one")
        wdi.to_pickle(WDI_FILE)
