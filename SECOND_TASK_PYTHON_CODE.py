#
#With this program we have processed meteorological data
#previously extracted with the use of an API in the first task.
#The structure of our code is divided into three modules:
#1)In the first module, we processed a dataset composed of data extracted 
#  during this period, and therefore related to current weather forecasts.
#  We decided to plot them using bar graphs and line graphs.
#2)In the second module, we decided to process data extracted from an older 
#  dataset, i.e. weather forecasts made in November.
#  The graphs obtained are the same as in the first module.
#3)In the third and last module we have done the same thing as
#  the previous ones, but we have obtained graphs that are 
#  the union of the bar graphs generated previously:
#  this allows us to compare the data obtained in the extraction
#  of a month ago and that of today
#
############################################################################
#FIRST PART#################################################################
############################################################################
#
#
#The first thing done was to import the necessary libraries:
#we imported the pandas library to work with dataframes.
import pandas as pd 

#Matplotlib.pyplot is instead a library used to create plots with datasets
import matplotlib.pyplot as plt 

#We created a list with the cities names in the order witch they appear in
#the dataset
cities=['Berlin', 'Paris', 'London', 'Madrid', 'Athens', 'Rome']
#We then extracted the data from the respective csv file and converted
#it in dataframe, defining the names of the columns. 
df = pd.read_csv ("wheaterforecast_eu_capitals_13_12_21dataset.csv")
df.columns = [' city', ' time', ' temperature (C°)', ' relative humidity (%)', ' apparent temperature (C°)', ' pressure (psi)', ' precipitation (mm)']


print(df.head())
print(df.shape)

#we selected the graphic style used to plot the data
plt.style.use('seaborn') 

plt.figure (figsize=(10,5))

#we created a list of color, one for each city
c = ["red", "green", "blue", "purple", "yellow", "black", "orange"]
i=0

#we created a list with the names of the values we extracted.
# We will use this for calling the desired data and to give names to the plot created
value_str=[' temperature (C°)', ' relative humidity (%)', ' apparent temperature (C°)', ' pressure (psi)', ' precipitation (mm)']

#we created an empty list for each of the values
temperature=[] 
relative_humidity=[]
apparent_temperature=[]
pressure=[]
precipitation=[]
#then we created a list composed of empty lists
value=[ temperature, relative_humidity, apparent_temperature, pressure, precipitation]
df[' time'] = pd.to_datetime(df[' time'])#we converted the datetime in the dataframe.

#With this two for loops we firstly selected the data relative to a single city, for each loop.
#then we exctracted general informations, such as avarage, mediam, max and minimum for each city from our dataset.
#Afterwards we selected only the averages for each value in each city and put it in the relative list of the relative value.
for city in cities:
    dfa = df[df[' city']==city]
    for i in range(len(value)):
       dfb=dfa.describe()
       column=dfb[value_str[i]]
       mean=column['mean']
       value[i].append(mean)
# In this part we created a bar chart graph for each average,
# where each bin is refered to a city.

for j in range(len(value)):
#For the average pessure we created two different barcharts:
#one with the the average pressure data plotted with the normal y ax values,
#and one with the same value but in logarithmic scale.  
    if value_str[j]==' pressure (psi)':
         plt.figure(1, figsize=(10,5))
         plt.bar(cities, value[j], color=c, log=False)
         plt.title('13 to 19/12/21 '+'average '+value_str[j])
         plt.savefig('13 to 19_12_21 '+'average '+value_str[j]+'.png')
         plt.show()
         plt.figure(2, figsize=(10,5))
         plt.bar(cities, value[j], color=c, log=True)
         plt.title('13 to 19/12/21 '+'average '+value_str[j]+'in log scale')
         plt.savefig('13 to 19_12_21 '+'average '+value_str[j]+'in log scale'+'.png')
         plt.show()       
    else:
        plt.figure( figsize=(10,5))
        plt.bar(cities, value[j], color=c, log=False) 
        plt.title('13 to 19/12/21 '+'average '+value_str[j])
        plt.savefig('13 to 19_12_21 '+'average '+value_str[j]+'.png')
        plt.show()
    

        
 
#here we have created the linear graphs that trace the trend of the 
#values available to us over time
for k in range(len(value_str)):
    df[' time']=pd.to_datetime(df[' time'])
    i=0
    plt.figure(figsize=(10,5))
    c = ["red", "green", "blue", "purple", "yellow", "black", "orange"]
    for city in cities:
       dfa = df[df[' city']==city]
       plt.plot(dfa[' time'],dfa[value_str[k]],marker='.', color=c[i])
       i=i+1
    plt.legend(cities)
    plt.xlabel(" Time")
    plt.ylabel(value_str[k])
    plt.title('13 to 19/12/21 '+value_str[k])
    plt.savefig('13 to 19_12_21 '+ value_str[k]+ '.png')
    plt.show()
    


############################################################################
#SECOND PART################################################################
############################################################################
#In this second part we have basically done the same as before, but with an
#older dataset.

cities=['Berlin', 'Paris', 'London', 'Madrid', 'Athens', 'Rome']#Cities names
df = pd.read_csv ("wheaterforecast_eu_capitals_7_11_21dataset.csv")
df.columns = [' city', ' time', ' temperature (C°)', ' relative humidity (%)', ' apparent temperature (C°)', ' pressure (psi)', ' precipitation (mm)']


plt.style.use('seaborn')

#general info
c = ["red", "green", "blue", "purple", "yellow", "black", "orange"]
i=0
value_str=[' temperature (C°)', ' relative humidity (%)', ' apparent temperature (C°)', ' pressure (psi)', ' precipitation (mm)']
temperature=[] 
relative_humidity=[]
apparent_temperature=[]
pressure=[]
precipitation=[]
value=[ temperature, relative_humidity, apparent_temperature, pressure, precipitation]
df[' time'] = pd.to_datetime(df[' time'])
for city in cities:
    dfa = df[df[' city']==city]
    for i in range(len(value)):
       dfb=dfa.describe()
       column=dfb[value_str[i]]
       mean=column['mean']
       value[i].append(mean)

for j in range(len(value)):
    if value_str[j]==' pressure (psi)':
         plt.figure(1, figsize=(10,5))
         plt.bar(cities, value[j], color=c, log=False)
         plt.title('7 to 13/11/21 '+'average '+value_str[j])
         plt.savefig('7 to 13_11_21 '+'average '+value_str[j]+'.png')
         plt.show()
         plt.figure(2, figsize=(10,5))
         plt.bar(cities, value[j], color=c, log=True)
         plt.title('7 to 13/11/21 '+'average '+value_str[j]+' in log scale')
         plt.savefig('7 to 13_11_21 '+'average '+value_str[j]+ 'in log scale'+'.png')
         plt.show()
                  
    else:
         plt.figure(figsize=(10,5))
         plt.bar(cities, value[j], color=c, log=False) 
         plt.title('7 to 13/11/21 '+'average '+value_str[j])
         plt.savefig('7 to 13_11_21 '+'average '+value_str[j]+'.png')
         plt.show()

#line graphs
for k in range(len(value_str)):
    df[' time']=pd.to_datetime(df[' time'])
    i=0
    plt.figure(figsize=(10,5))
    c = ["red", "green", "blue", "purple", "yellow", "black", "orange"]
    for city in cities:
       dfa = df[df[' city']==city]
       plt.plot(dfa[' time'],dfa[value_str[k]],marker='.', color=c[i])
       i=i+1
    plt.legend(cities)
    plt.xlabel(" Time")
    plt.ylabel(value_str[k])
    plt.title('7 to 13/11/21 '+ value_str[k])
    plt.savefig('7 to 13_11_21 '+value_str[k]+ '.png')
    plt.show()

############################################################################
#THIRD PART#################################################################
############################################################################
#In this last third part we have substantially redone what we had done
#in the two previous ones, only in this case the output will be formed
#by a series of bar graphs in which are compared the averages of the 
#values extracted in two different periods in the same city.
#
#
import numpy as np


dfnew = pd.read_csv ("wheaterforecast_eu_capitals_13_12_21dataset.csv")
dfold = pd.read_csv ("wheaterforecast_eu_capitals_7_11_21dataset.csv")


dfold.columns = [' city', ' time', ' temperature (C°)', ' relative humidity (%)', ' apparent temperature (C°)', ' pressure (psi)', ' precipitation (mm)']
dfnew.columns = [' city', ' time', ' temperature (C°)', ' relative humidity (%)', ' apparent temperature (C°)', ' pressure (psi)', ' precipitation (mm)']

#empty list new
temperature_new=[] 
relative_humidity_new=[]
apparent_temperature_new=[]
pressure_new=[]
precipitation_new=[]
value_new=[ temperature_new, relative_humidity_new, apparent_temperature_new, pressure_new, precipitation_new]

#empty list old
temperature_old=[] 
relative_humidity_old=[]
apparent_temperature_old=[]
pressure_old=[]
precipitation_old=[]
value_old=[ temperature_old, relative_humidity_old, apparent_temperature_old, pressure_old, precipitation_old]

dfold[' time'] = pd.to_datetime(dfold[' time'])
dfnew[' time'] = pd.to_datetime(dfnew[' time'])

for city in cities:
    dfnewa = dfnew[dfnew[' city']==city]
    dfolda = dfold[dfold[' city']==city]
    for i in range(len(value_str)):
       dfnewb=dfnewa.describe()
       dfoldb=dfolda.describe()
       columnnew=dfnewb[value_str[i]]
       columnold=dfoldb[value_str[i]]
       meannew=columnnew['mean']
       meanold=columnold['mean']
       value_new[i].append(meannew)
       value_old[i].append(meanold)   


plt.style.use('seaborn')

p = np.arange(len(cities))  # the label locations
width = 0.30  # the width of the bars
print(p)
for j in range(len(value_str)):
  if value_str[j]==' pressure (psi)':
    #pressure 
    plt.subplots(1)
    rects1 = plt.bar(p-width/2, value_old[j], width, color='blue', label='from 07/11/21 to 13/11/21', edgecolor='white')
    rects2 = plt.bar(p+width/2, value_new[j], width, color='orange', label='from 13/12/21 to 19/12/21', edgecolor='white')
    plt.ylabel(value_str[j])
    plt.xlabel('cities')
    plt.title('comparison between the average '+value_str[j] +' of november and december')
    plt.xticks(p, cities)
    n=value_new[j]
    o=value_old[j]
    plt.legend()
    plt.savefig('comparison between the average '+value_str[j] +' of november and december.png')
    plt.show()
   
    #pressure with log scale
    plt.subplots(1)
    rects1 = plt.bar(p-width/2, value_old[j], width, color='blue', label='from 07/11/21 to 13/11/21', edgecolor='white', log=True)
    rects2 = plt.bar(p+width/2, value_new[j], width, color='orange', label='from 13/12/21 to 19/12/21', edgecolor='white', log=True)
    plt.ylabel(value_str[j])
    plt.xlabel('cities')
    plt.title('comparison between the average '+value_str[j] +' of november and december in log scale')
    plt.xticks(p, cities)
    n=value_new[j]
    o=value_old[j]
    plt.legend()
    plt.savefig('comparison between the average '+value_str[j] +' of november and december in log scale.png')
    plt.show()

  #other average data    
  else:
    plt.subplots()
    rects1 = plt.bar(p-width/2, value_old[j], width, color='blue', label='from 07/11/21 to 13/11/21', edgecolor='white')
    rects2 = plt.bar(p+width/2, value_new[j], width, color='orange', label='from 13/12/21 to 19/12/21', edgecolor='white')

    plt.ylabel(value_str[j])
    plt.xlabel('cities')
    plt.title('comparison between the average'+ value_str[j]+' of november and december')
    plt.xticks(p, cities)
    n=value_new[j]
    o=value_old[j]
    plt.legend()
    plt.savefig('comparison between the average '+value_str[j] +' of november and december.png')
    plt.show()
