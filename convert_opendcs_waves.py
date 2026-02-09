# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 16:02:12 2025

@author: Laura.Fiorentino
"""
import os
import numpy as np
from datetime import datetime
import pandas as pd

BASE_FOLDER = r"C:\OPENDCS"


def extract_data(data, psd_name, data_key):
    data = np.array(data[psd_name == data_key])
    if data_key[:3] == "PSD":
        data = data * 1e-10       
    elif data_key in ("Hm0", "H1/3", "Hmax"):
        data = data * 1e-5
    elif data_key in ("Tm01", "Tm02", "Tp", "Tzero"):
        data = data * 1e-3
    elif data_key == "BAT":
        data = data * 1e-2
    if data_key not in ("BV", "MV", "CBMV", "DATE"):
        data[data <= 0] = float("nan")
    return data

   
def get_message(file_to_use):  
    with open(file_to_use, "r") as f:
        data = f.read()
    data = np.array(data.split("\n"))
    
    remove_item = []
    for d in data:
        if 250 > len(d) > 200 and d.find("ID") == -1 and d.find("raw") == -1  and d.count('|') == 19 and len(d.split("|")[18].strip()) > 0:
            remove_item.append(True)
        else:
            remove_item.append(False)
    data = data[remove_item]
    temp = []
    station_id = None
    
    for d in data:
        d = str(d).replace("error", "nan")
        data_sample = d.split("|")
        temp.append(float(data_sample[18].strip()))
        if len(data_sample[4].strip()) > 0:
            if station_id == None:
                station_id = data_sample[4].strip()
            date_temp = data_sample[5].strip() + data_sample[6].strip()
            date_temp = "{0}/{1}/{2} {3}:00:00".format(date_temp[:2], date_temp[2:4], 
                                                       date_temp[6:8], date_temp[8:10])
            temp.append(datetime.strptime(date_temp, '%m/%d/%y %H:%M:%S'))
            data_sample = [float(ds.strip()) for ds in data_sample[7:18]]
            temp = temp + data_sample
    temp = np.array(temp)
    psd_name = []
    data_len = (len(temp) // 45)
    for pn in range(1,34):
        psd_name.append("PSD" + str(pn))
    psd_name = np.array((psd_name + ["DATE","BAT", "BV", "MV", "CBMV", "Hm0", 
                                     "Tm01", "Tm02", "Tp", "H1/3", "Hmax", 
                                     "Tzero"]) * data_len)
    psd_val = []
    for pn in psd_name[:45]:
        psd_val.append(extract_data(temp, psd_name, pn))
    
    psd_dict = {psd_name[i]: psd_val[i] for i in range(len(psd_name[:45]))}
    psd_pd = pd.DataFrame(psd_dict)
    psd_pd.index = psd_pd["DATE"]
    del psd_pd["DATE"]
    psd_pd = psd_pd.loc[:,:].apply(pd.to_numeric, errors='coerce')
    return psd_pd.resample("H").mean()

#file_name = "messages.txt"
#psd = get_message(file_name)
#psd.to_csv(file_name[:-3] + 'csv') 

def convert_opendcs_waves(filename):
    #filename = input("Enter the input filename (e.g., messages.txt): ")
    input_path = os.path.join(BASE_FOLDER, filename)
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"File not found: {input_path}")
    output_path = os.path.join(BASE_FOLDER, filename.rsplit(".", 1)[0] + ".csv")
    psd = get_message(input_path)
    psd.to_csv(output_path)
    print(f"Saved CSV to: {output_path}")
