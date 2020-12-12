


# # Load the Pandas libraries with alias 'pd' 
import pandas as pd 
import datetime 
import numpy as np
import csv

clmns = ['Date','Time','PM10','PM4','PM2,5','PM1','PMtot','Cn',\
                '110','111','112','113','114','115','116','117','118','119',\
                '120','121','122','123','124','125','126','127','128','129',\
                '130','131','132','133','134','135','136','137','138','139',\
                '140','141','142','143','144','145','146','147','148','149',\
                '150','151','152','153','154','155','156','157','158','159',\
                '160','161','162','163','164','165','166','167','168','169',\
                '170','171','172','173','174','175','176','177','178','179',\
                '180','181','182','183','184','185','186','187','188','189',\
                '190','191','192','193','194','195','196','197','198','199',\
                '200','201','202','203']

# dataTypes = {'Date':str,'Time','PM10':np.float64,'PM4','PM2,5','PM1','PMtot','Cn',\
#                 '110','111','112','113','114','115','116','117','118','119',\
#                 '120','121','122','123','124','125','126','127','128','129',\
#                 '130','131','132','133','134','135','136','137','138','139',\
#                 '140','141','142','143','144','145','146','147','148','149',\
#                 '150','151','152','153','154','155','156','157','158','159',\
#                 '160','161','162','163','164','165','166','167','168','169',\
#                 '170','171','172','173','174','175','176','177','178','179',\
#                 '180','181','182','183','184','185','186','187','188','189',\
#                 '190','191','192','193','194','195','196','197','198','199',\
#                 '200','201','202','203'}                

df = pd.read_csv("201209_044918_Log.txt", usecols= clmns,delimiter='\t')
df=pd.DataFrame(df.iloc[-1:,:]) 
dateTime = df['Date'].astype(str) + ' ' + df['Time']
del df['Date']
del df['Time']

print(df.dtypes)
# df = pd.to_numeric(df)
print(df['120'])

# clmnsRr = [ 'dateTime','PM1','PM2_5','PM4','PM10','PMtot','Cn',\
#        '110','111','112','113','114','115','116','117','118','119',\
#        '120','121','122','123','124','125','126','127','128','129',\
#        '130','131','132','133','134','135','136','137','138','139',\
#        '140','141','142','143','144','145','146','147','148','149',\
#        '150','151','152','153','154','155','156','157','158','159',\
#        '160','161','162','163','164','165','166','167','168','169',\
#        '170','171','172','173','174','175','176','177','178','179',\
#        '180','181','182','183','184','185','186','187','188','189',\
#        '190','191','192','193','194','195','196','197','198','199',\
#        '200','201','202','203'\
#         ]

# # df = pd.read_csv("201209_044918_Log.txt", usecols= clms,delimiter='\t')
# df = pd.read_csv("201209_044918_Log.txt",delimiter='\t')

# # df.columns = df.columns.str.replace(',','_')
    
# # # Re-order Columns

# df = pd.read_csv("201209_044918_Log.txt",delimiter='\t')

# df=pd.DataFrame(df.iloc[-1:,:].values) 
# df.columns = clmns

# dateTime =pd.to_datetime(df['Date'].astype(str) + ' ' + df['Time'])
# del df['Date']
# del df['Time']
# df.columns = df.columns.str.replace(',','_')
# print(df.to_numpy())

# x = np.array([np.inf, -np.inf, np.nan, -128, 128])
# np.nan_to_num(x)


# a_csv_file = open("201209_044918_Log.txt", "r")
# dict_reader = csv.DictReader(a_csv_file,delimiter='\t')

# ordered_dict_from_csv = list(dict_reader)[-1]
# dict_from_csv = dict(ordered_dict_from_csv)

# print(dict_from_csv)

# df['dateTime'] = pd.to_datetime(df['dateTime'])
# print(pd.to_datetime(df['dateTime']))

# # Other Errors 
# # pd.to_numeric(df)
# df.replace([np.inf, -np.inf], np.nan, inplace=True) 
# print(df)
# print(df.dtypes)
# d =  df.to_dict('records')[0]

# d[d.values == np.inf] = -1

# print(d.values == np.inf)
# print(d)
# for k, v in d.items():
#     print(k, v)
#     print(v == np.inf)
# print(df.to_dict('records'))
# print(type(df.dtypes))

# print(df._get_numeric_data().columns)
# print(df.select_dtypes(exclude=["bool_","object_"]))


###
###

# # Load the Pandas libraries with alias 'pd' 
import pandas as pd 
import datetime 
import numpy as np
import csv
# # data = pd.read_csv("201209_044918_Log.txt",delimiter='\t') 
clmns = ['Date','Time','PM10','PM4','PM2,5','PM1','PMtot','Cn',\
                '110','111','112','113','114','115','116','117','118','119',\
                '120','121','122','123','124','125','126','127','128','129',\
                '130','131','132','133','134','135','136','137','138','139',\
                '140','141','142','143','144','145','146','147','148','149',\
                '150','151','152','153','154','155','156','157','158','159',\
                '160','161','162','163','164','165','166','167','168','169',\
                '170','171','172','173','174','175','176','177','178','179',\
                '180','181','182','183','184','185','186','187','188','189',\
                '190','191','192','193','194','195','196','197','198','199',\
                '200','201','202','203','204']
dataTypes = {'Date':str,'Time':str,'PM10':np.float,'PM4':np.float,'PM2,5':np.float,'PM1':np.float,'PMtot':np.float,'Cn':np.float,\
                '110':np.float,'111':np.float,'112':np.float,'113':np.float,'114':np.float,'115':np.float,'116':np.float,'117':np.float,'118':np.float,'119':np.float,\
                '120':np.float,'121':np.float,'122':np.float,'123':np.float,'124':np.float,'125':np.float,'126':np.float,'127':np.float,'128':np.float,'129':np.float,\
                '130':np.float,'131':np.float,'132':np.float,'133':np.float,'134':np.float,'135':np.float,'136':np.float,'137':np.float,'138':np.float,'139':np.float,\
                '140':np.float,'141':np.float,'142':np.float,'143':np.float,'144':np.float,'145':np.float,'146':np.float,'147':np.float,'148':np.float,'149':np.float,\
                '150':np.float,'151':np.float,'152':np.float,'153':np.float,'154':np.float,'155':np.float,'156':np.float,'157':np.float,'158':np.float,'159':np.float,\
                '160':np.float,'161':np.float,'162':np.float,'163':np.float,'164':np.float,'165':np.float,'166':np.float,'167':np.float,'168':np.float,'169':np.float,\
                '170':np.float,'171':np.float,'172':np.float,'173':np.float,'174':np.float,'175':np.float,'176':np.float,'177':np.float,'178':np.float,'179':np.float,\
                '180':np.float,'181':np.float,'182':np.float,'183':np.float,'184':np.float,'185':np.float,'186':np.float,'187':np.float,'188':np.float,'189':np.float,\
                '190':np.float,'191':np.float,'192':np.float,'193':np.float,'194':np.float,'195':np.float,'196':np.float,'197':np.float,'198':np.float,'199':np.float,\
                '200':np.float,'201':np.float,'202':np.float,'203':np.float}    

# clmnsRr = [ 'dateTime','PM1','PM2_5','PM4','PM10','PMtot','Cn',\
#        '110','111','112','113','114','115','116','117','118','119',\
#        '120','121','122','123','124','125','126','127','128','129',\
#        '130','131','132','133','134','135','136','137','138','139',\
#        '140','141','142','143','144','145','146','147','148','149',\
#        '150','151','152','153','154','155','156','157','158','159',\
#        '160','161','162','163','164','165','166','167','168','169',\
#        '170','171','172','173','174','175','176','177','178','179',\
#        '180','181','182','183','184','185','186','187','188','189',\
#        '190','191','192','193','194','195','196','197','198','199',\
#        '200','201','202','203'\
#         ]

# # df = pd.read_csv("201209_044918_Log.txt", usecols= cols_to_use,delimiter='\t')
# df = pd.read_csv("201209_044918_Log.txt",delimiter='\t')

# # df['dateTime'] =df['Date'].astype(str) + ' ' + df['Time']

# # del df['Date']
# # del df['Time']
# # df.columns = df.columns.str.replace(',','_')
    
# # # Re-order Columns

df = pd.read_csv("201209_044918_Log.txt",delimiter='\t')

df=pd.DataFrame(df.iloc[-1:,:].values) 
df.columns = clmns

dateTime =pd.to_datetime(df['Date'].astype(str) + ' ' + df['Time'])
del df['Date']
del df['Time']
df.columns = df.columns.str.replace(',','_')
print(df.to_numpy())

# x = np.array([np.inf, -np.inf, np.nan, -128, 128])
# np.nan_to_num(x)


# a_csv_file = open("201209_044918_Log.txt", "r")
# dict_reader = csv.DictReader(a_csv_file,delimiter='\t')

# ordered_dict_from_csv = list(dict_reader)[-1]
# dict_from_csv = dict(ordered_dict_from_csv)

# print(dict_from_csv)


# df['dateTime'] = pd.to_datetime(df['dateTime'])
# print(pd.to_datetime(df['dateTime']))


# # Other Errors 
# # pd.to_numeric(df)
# df.replace([np.inf, -np.inf], np.nan, inplace=True) 
# print(df)
# print(df.dtypes)
# d =  df.to_dict('records')[0]

# d[d.values == np.inf] = -1

# print(d.values == np.inf)
# print(d)
# for k, v in d.items():
#     print(k, v)
#     print(v == np.inf)
# print(df.to_dict('records'))
# print(type(df.dtypes))

# print(df._get_numeric_data().columns)
# print(df.select_dtypes(exclude=["bool_","object_"]))
