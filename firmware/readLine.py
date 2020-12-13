from collections import OrderedDict
from mintsXU4 import mintsLatest as mL
from mintsXU4 import mintsDefinitions as mD
from mintsXU4 import mintsSensorReader as mSR
import datetime
# Reading last line of code 

with open("201209_044918_Log.txt", "r") as f1:
    lastLine = f1.readlines()[-1]

dataOutPre  = lastLine.replace('Inf','-1').split()
dateTime = datetime.datetime.strptime((dataOutPre[0] + ' ' + dataOutPre[1]), '%d.%m.%y %H:%M:%S')
dataOut = dataOutPre[2:len(dataOutPre)]
mSR.FRG001Write(dataOut,dateTime)