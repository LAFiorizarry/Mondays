# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 16:20:57 2026

@author: Laura.Fiorentino
"""
import pandas as pd

met = pd.read_csv(r'C:\Users\Laura.Fiorentino\Documents\UsefulScripts\MetFetch\Data\8652226_20250814_20260127_data.csv')
wind = met.iloc[:,0:4].copy()
wind['wind_date_time'] = pd.to_datetime(wind['wind_date_time'])
wind = wind.set_index('wind_date_time')
wind = wind[~wind.index.isnan()]
wind = wind.sort_index().loc[~wind.index.duplicated(keep='first')]



baro = met.iloc[:,0:2].copy()
wt = met.iloc[:,2:4].copy()
batt = met.iloc[:,4:6].copy()

baro['baro_date_time'] = pd.to_datetime(baro['baro_date_time'])
wt['wt_date_time'] = pd.to_datetime(wt['wt_date_time'])
batt['battery_date_time'] = pd.to_datetime(batt['battery_date_time'])

baro = baro.set_index('baro_date_time')
wt   = wt.set_index('wt_date_time')
batt = batt.set_index('battery_date_time')


baro = baro[~baro.index.isna()]
wt   = wt[~wt.index.isna()]
batt = batt[~batt.index.isna()]

baro = baro.resample('6min').mean()
wt   = wt.resample('6min').mean()
batt = batt.resample('6min').mean()

MetNew = (
    baro
    .join(wt, how='outer')
    .join(batt, how='outer')
)
MetNew.to_csv('G:\My Drive\Projects\CurrentMeasurementSystems\Curby\FieldTests\JennettesPier2025\WeeklyReports\Met.csv')