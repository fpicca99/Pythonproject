import requests
cities=['Berlin', 'Paris', 'London', 'Madrid', 'Athens', 'Rome']
latitude=['52.5235', '48.8567', '51.5002', '40.4167', '37.9792', '41.8955']
longitude=['13.4115', '2.3510', '-0.1262', '-3.7033', '23.7166', '12.4823']
for i in range(0,len(cities)):
    url = 'https://api.open-meteo.com/v1/forecast?latitude='+latitude[i]+'&longitude='+longitude[i]+'&hourly=temperature_2m,relativehumidity_2m,apparent_temperature,pressure_msl,precipitation'
    response = requests.get(url)
    file = open("./file-"+cities[i]+".json", "w+")
    print(file.name)
    file.writelines(response.text)
    file.close()


import json
import pandas

berlin=[] 
paris=[]
london=[]
madrid=[]
athene=[]
rome=[] 
lists=[berlin, paris, london, madrid, athene, rome]
for x in range(0,len(lists)):
    dati_json = json.load(open("./file-"+cities[x]+".json"))
    a=dati_json['hourly']['temperature_2m']
    b=dati_json['hourly']['relativehumidity_2m']
    c=dati_json['hourly']['time']
    d=dati_json['hourly']['apparent_temperature']
    e=dati_json['hourly']['pressure_msl']
    f=dati_json['hourly']['precipitation']
    for h in range(0,len(c)):
        n=[cities[x] ,c[h], a[h], b[h], d[h], e[h], f[h]]
        lists[x].append(n)
l=[]
for y in lists:
    l=l+y

csv_file_path = 'wheaterforecast_eu_capitals.csv'
df = pandas.DataFrame(l)
df.columns = [' city', ' time', ' temperature', ' relative humidity', ' apparent temperature', ' pressure', ' precipitation']
df.to_csv(csv_file_path, index=False)

