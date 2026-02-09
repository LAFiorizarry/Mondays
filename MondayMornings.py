# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 09:51:19 2025

@author: Laura.Fiorentino
"""

import shutil
import os
import convert_opendcs_waves

startdate = '20260202'
enddate = '20260209'

# =============================================================================
#            LinkComm
# =============================================================================

# Duck
prefix = '99999211_log_'
filename = prefix + startdate + '_' + enddate + '.csv'
source = r'C:\Users\Laura.Fiorentino\Documents\LinkComm\Log Files'
destination = r'G:\My Drive\Projects\MWWL_Waves\FieldTestData\Duck_RealTimeProcessing\raw_Range_CSV_originals'
destination2 = r'G:\Shared drives\NOS CO-OPS OSTEP\OSTEP_DATA\Waves\MWWL_Waves\FieldTestData\Duck\raw_Range_CSV_originals'

shutil.copy(os.path.join(source, filename), os.path.join(destination, filename))
shutil.copy(os.path.join(source, filename), os.path.join(destination2, filename))

# Duck Vega
prefix = '99999381_log_'
filename = prefix + startdate + '_' + enddate + '.csv'
source = r'C:\Users\Laura.Fiorentino\Documents\LinkComm\Log Files'
destination2 = r'G:\Shared drives\NOS CO-OPS OSTEP\OSTEP_DATA\WaterLevelSensors\Vega\Duck\FY25\FieldTestData\raw_range'
shutil.copy(os.path.join(source, filename), os.path.join(destination2, filename))


# Money Point Vega 
prefix = '99999371_log_'
filename = prefix + startdate + '_' + enddate + '.csv'
source = r'C:\Users\Laura.Fiorentino\Documents\LinkComm\Log Files'
destination2 = r'G:\Shared drives\NOS CO-OPS OSTEP\OSTEP_DATA\WaterLevelSensors\Vega\MoneyPoint\FieldTestData\raw_range'
shutil.copy(os.path.join(source, filename), os.path.join(destination2, filename))


# Holland outside
prefix = '99999281_log_'
filename = prefix + startdate + '_' + enddate + '.csv'
source = r'C:\Users\Laura.Fiorentino\Documents\LinkComm\Log Files'
destination = r'G:\My Drive\Projects\MWWL_Waves\FieldTestData\Holland\Outside\raw_range'
destination2 = r'G:\Shared drives\NOS CO-OPS OSTEP\OSTEP_DATA\Waves\MWWL_Waves\FieldTestData\Holland\Outside\raw_range'

shutil.copy(os.path.join(source, filename), os.path.join(destination, filename))
shutil.copy(os.path.join(source, filename), os.path.join(destination2, filename))


# =============================================================================
#            XTerm
# =============================================================================

# Cape Vincent CCF: 63.40.5.223 9210
# save directly to My Drive, copy to OSTEP
#G:\My Drive\Projects\CCFBubbler\TestData\CapeVincent\raw
prefix = 'SSP_'
filename = prefix + startdate + '_' + enddate + '.txt'
source = r'G:\My Drive\Projects\CCFBubbler\TestData\CapeVincent\raw'
destination2 = r'G:\Shared drives\NOS CO-OPS OSTEP\OSTEP_DATA\Bubbler\CCF_Bubbler\TestData\CapeVincent\raw'
shutil.copy(os.path.join(source, filename), os.path.join(destination2, filename))

# Holland Inside: 63.40.5.19
# save to My Drive, copy to OSTEP
#G:\My Drive\Projects\MWWL_Waves\FieldTestData\Holland\Inside\raw_range
prefix = 'Holland_'
filename = prefix + startdate + '_' + enddate + '.txt'
source = r'G:\My Drive\Projects\MWWL_Waves\FieldTestData\Holland\Inside\raw_range'
destination2 = r'G:\Shared drives\NOS CO-OPS OSTEP\OSTEP_DATA\Waves\MWWL_Waves\FieldTestData\Holland\Inside\raw_range'
shutil.copy(os.path.join(source, filename), os.path.join(destination2, filename))

# Wrightsville CCF: 63.40.5.8 9210
# save directly to My Drive, copy to OSTEP
#G:\My Drive\Projects\CCFBubbler\TestData\Wrightsville\raw
prefix = 'Wrightsville_'
filename = prefix + startdate + '_' + enddate + '.txt'
source = r'G:\My Drive\Projects\CCFBubbler\TestData\Wrightsville\raw'
destination2 = r'G:\Shared drives\NOS CO-OPS OSTEP\OSTEP_DATA\Bubbler\CCF_Bubbler\TestData\Wrightsville\raw'
shutil.copy(os.path.join(source, filename), os.path.join(destination2, filename))

# =============================================================================
#            OpenDCS
# =============================================================================

BASE_FOLDER = r"C:\OPENDCS"

# CBBT
convert_opendcs_waves.convert_opendcs_waves('cbbtmessages.txt')
new_filename = 'CBBT_' + startdate + '_' + enddate + '_waves.csv'
os.rename(os.path.join(BASE_FOLDER, 'cbbtmessages.csv'), os.path.join(BASE_FOLDER, new_filename))
mydir = r'G:\My Drive\Projects\MWWL_Waves\FieldTestData\CBBT\raw_Waves_CSV'
shutil.copyfile(os.path.join(BASE_FOLDER, new_filename), os.path.join(mydir, new_filename))
ostepdir = r'G:\Shared drives\NOS CO-OPS OSTEP\OSTEP_DATA\Waves\MWWL_Waves\FieldTestData\CBBT\raw_Waves_CSV'
shutil.copyfile(os.path.join(BASE_FOLDER, new_filename), os.path.join(ostepdir, new_filename))



# Duck 
convert_opendcs_waves.convert_opendcs_waves('duckmessages.txt')
new_filename = 'Duck_' + startdate + '_' + enddate + '_waves.csv'
os.rename(os.path.join(BASE_FOLDER, 'duckmessages.csv'), os.path.join(BASE_FOLDER, new_filename))
mydir = r'G:\My Drive\Projects\MWWL_Waves\FieldTestData\Duck_RealTimeProcessing\raw_Waves_CSV'
shutil.copyfile(os.path.join(BASE_FOLDER, new_filename), os.path.join(mydir, new_filename))
ostepdir = r'G:\Shared drives\NOS CO-OPS OSTEP\OSTEP_DATA\Waves\MWWL_Waves\FieldTestData\Duck\raw_Waves_CSV'
shutil.copyfile(os.path.join(BASE_FOLDER, new_filename), os.path.join(ostepdir, new_filename))


# Duck Vega
#convert_opendcs_waves.convert_opendcs_waves('duckvegamessages.txt')
#new_filename = 'DuckVega_' + startdate + '_' + enddate + '_waves.csv'
#os.rename(os.path.join(BASE_FOLDER, 'duckvegamessages.csv'), os.path.join(BASE_FOLDER, new_filename))
#ostepdir = r'G:\Shared drives\NOS CO-OPS OSTEP\OSTEP_DATA\WaterLevelSensors\Vega\Duck\FY25\FieldTestData\raw_waves_CSV'
#shutil.copyfile(os.path.join(BASE_FOLDER, new_filename), os.path.join(ostepdir, new_filename))


# Money Point Vega
convert_opendcs_waves.convert_opendcs_waves('mpmessages.txt')
new_filename = 'MP_' + startdate + '_' + enddate + '_waves.csv'
os.rename(os.path.join(BASE_FOLDER, 'mpmessages.csv'), os.path.join(BASE_FOLDER, new_filename))
ostepdir = r'G:\Shared drives\NOS CO-OPS OSTEP\OSTEP_DATA\WaterLevelSensors\Vega\MoneyPoint\FieldTestData\raw_waves_csv'
shutil.copyfile(os.path.join(BASE_FOLDER, new_filename), os.path.join(ostepdir, new_filename))

# Port Aransas
#convert_opendcs_waves.convert_opendcs_waves('pamessages.txt')
#new_filename = 'PA_' + startdate + '_' + enddate + '_waves.csv'
#os.rename(os.path.join(BASE_FOLDER, 'pamessages.csv'), os.path.join(BASE_FOLDER, new_filename))


# =============================================================================
#            FTP
# =============================================================================
import sys
import shutil
import os
sys.path.append(r'G:\My Drive\Projects\MWWL_Waves\FTP')
import ftp_waves_fxns
Waves = ftp_waves_fxns.import_waves()

first_time = Waves['99999291']['Sensor Time'].min().strftime("%Y%m%d")
last_time = Waves['99999291']['Sensor Time'].max().strftime("%Y%m%d")


# PA
BASE_FOLDER = r'G:\My Drive\Projects\MWWL_Waves\FTP'
filename = '99999291_' + first_time + '_' + last_time + '_summary.csv'
new_filename = 'PA_' + first_time + '_' + last_time + '_waves.csv'
mydir = r'G:\My Drive\Projects\MWWL_Waves\FieldTestData\PortAransas\raw_Waves_CSV'
ostepdir = r'G:\Shared drives\NOS CO-OPS OSTEP\OSTEP_DATA\Waves\MWWL_Waves\FieldTestData\PortAransas\raw_Waves_CSV'
shutil.copyfile(os.path.join(BASE_FOLDER, filename), os.path.join(mydir, new_filename))
shutil.copyfile(os.path.join(BASE_FOLDER, filename), os.path.join(ostepdir, new_filename))

# CBBT
first_time = Waves['99999351']['Sensor Time'].min().strftime("%Y%m%d")
last_time = Waves['99999351']['Sensor Time'].max().strftime("%Y%m%d")

BASE_FOLDER = r'G:\My Drive\Projects\MWWL_Waves\FTP'
filename = '99999351_' + first_time + '_' + last_time + '_summary.csv'
new_filename = 'CBBT_' + first_time + '_' + last_time + '_waves.csv'
mydir = r'G:\My Drive\Projects\MWWL_Waves\FieldTestData\CBBT\raw_Waves_CSV'
ostepdir = r'G:\Shared drives\NOS CO-OPS OSTEP\OSTEP_DATA\Waves\MWWL_Waves\FieldTestData\CBBT\raw_Waves_CSV'
shutil.copyfile(os.path.join(BASE_FOLDER, filename), os.path.join(mydir, new_filename))
shutil.copyfile(os.path.join(BASE_FOLDER, filename), os.path.join(ostepdir, new_filename))
