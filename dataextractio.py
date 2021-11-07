#the first part of the program requests the data from the API using the request library 
# and puts them in json files.
import requests
cities=['Berlin', 'Paris', 'London', 'Madrid', 'Athens', 'Rome']#Cities names
latitude=['52.5235', '48.8567', '51.5002', '40.4167', '37.9792', '41.8955']#Latitude of each city respectively
longitude=['13.4115', '2.3510', '-0.1262', '-3.7033', '23.7166', '12.4823']#lLongitude of each city respectively
for i in range(0,len(cities)): # In this for cycle the data are taken from the API and written on a json file. At each cycle we create a json file for each city for a total of 6 cycles.
    url = 'https://api.open-meteo.com/v1/forecast?latitude='+latitude[i]+'&longitude='+longitude[i]+'&hourly=temperature_2m,relativehumidity_2m,apparent_temperature,pressure_msl,precipitation'
    response = requests.get(url)
    file = open("./file-"+cities[i]+".json", "w+")
    print(file.name)
    file.writelines(response.text)
    file.close()

#The second part of the program takes the json files and orders
#them in a dataframe and creates a .csv file with all the data sorted.
#For this part we had to install the json and pandas libraries. 
import json
import pandas
#Firstly we had created an empty list for each city.
berlin=[] 
paris=[]
london=[]
madrid=[]
athene=[]
rome=[]
#We then put these lists in another list.
lists=[berlin, paris, london, madrid, athene, rome]
#In this for loop, at each cycle, the program opens a different json file,
# one for each city.
for x in range(0,len(lists)):
    dati_json = json.load(open("./file-"+cities[x]+".json"))
#Then it takes only the requested data from each individul file.
    a=dati_json['hourly']['temperature_2m']
    b=dati_json['hourly']['relativehumidity_2m']
    c=dati_json['hourly']['time']
    d=dati_json['hourly']['apparent_temperature']
    e=dati_json['hourly']['pressure_msl']
    f=dati_json['hourly']['precipitation']
#The program take each different data that occur at the same time and
# put them togheter in a list.    
    for h in range(0,len(c)):
        n=[cities[x] ,c[h], a[h], b[h], d[h], e[h], f[h]]
#Each list composed of 'city name', 'time', 'temperature',
# 'relative humidity','apparent temperature', 'pressure',
# 'precipitations' is then put inside the corresponding city list,
# in order of time.        
        lists[x].append(n)
        
#This for loop take lists (the list composed of lists with name of cities)
# and merge each list inside of it creating a unique continuos list
# composed of the lists with the weather data.    
l=[]
for y in lists:
    l=l+y

#in this final part we created the csv file, the data frame with all the 
#data from the cities and then we converted the dataframe in the csv file
# we created.
csv_file_path = 'wheaterforecast_eu_capitals.csv'
df = pandas.DataFrame(l)
df.columns = [' city', ' time', ' temperature', ' relative humidity', ' apparent temperature', ' pressure', ' precipitation']
df.to_csv(csv_file_path, index=False)

