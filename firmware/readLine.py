from collections import OrderedDict
from mintsXU4 import mintsLatest as mL
from mintsXU4 import mintsDefinitions as mD
from mintsXU4 import mintsSensorReader as mSR

with open("201209_044918_Log.txt", "r") as f1:
    lastLine = f1.readlines()[-1]


dataOut  = lastLine.replace('Inf','-1').split()



# def FRG001Write(sensorData,dateTime):
#     dataOut    = sensorData.split(':')
#     sensorName = "FRG001"
#     dataLength = 100
#     if(len(dataOut) == (dataLength +1)):
#         sensorDictionary =  OrderedDict([
#                 ("dateTime"     , str(dateTime)), # always the same
#         		("temperature"  ,dataOut[0]), # check with arduino code
#             	("pressure"     ,dataOut[1]),
#                 ("humidity"     ,dataOut[2]),
#             	("altitude"     ,dataOut[3])
#                 ])
#         mSR.sensorFinisher(dateTime,sensorName,sensorDictionary)