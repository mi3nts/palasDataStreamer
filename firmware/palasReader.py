# ***************************************************************************
#  mintsXU4
#   ---------------------------------
#   Written by: Lakitha Omal Harindha Wijeratne
#   - for -
#   Mints: Multi-scale Integrated Sensing and Simulation
#   ---------------------------------
#   Date: February 4th, 2019
#   ---------------------------------
#   This module is written for generic implimentation of MINTS projects
#   --------------------------------------------------------------------------
#   https://github.com/mi3nts
#   http://utdmints.info/
#  ***************************************************************************


import datetime
import os
import csv
from mintsXU4 import mintsLatest as mL
from mintsXU4 import mintsDefinitions as mD
import time
from collections import OrderedDict
import netifaces as ni
import math



with open("201209_044918_Log.txt", "r") as f1:
    last_line = f1.readlines()[-1]


print(last_line.replace('Inf','-1').split())
dateTime =pd.to_datetime(df['Date'].astype(str) + ' ' + df['Time'])