import folium
import json
import os 
p=os.listdir()
otis=[]

for i in p:
    if i=='represent.py' or i=='map.py': continue
    else:
        with open(i,'r') as f:
            data=json.load(f)
            more=data['results']
            
            if len(more)>0:
                for j in range(len(more)):
                    name=more[j]['name']
                    latitude=more[j]['latitude']
                    longitude=more[j]['longitude']
                    if (latitude == 0 and longitude == 0) or (latitude == None and longitude == None):
                        continue
                    else:
                        latty={}
                        latty['name']=name
                        latty['latitude']=latitude
                        latty['longitude']=longitude
                        otis.append(latty)
            else:
                continue
k={
    'results':otis
}

with open(os.path.basename(os.getcwd())+'.json', 'w') as f:
    json.dump(k, f,indent=3)


# read the JSON file
with open(os.path.basename(os.getcwd())+'.json') as f:
    data = json.load(f)

# create a map centered at the first location
map = folium.Map(location=[data['results'][0]['latitude'], data['results'][0]['longitude']], zoom_start=10)

# add markers for each location to the map
for location in data['results']:
    folium.Marker([location['latitude'], location['longitude']], popup=location['name']).add_to(map)

# save the map to an HTML file
map.save(os.path.basename(os.getcwd())+'.html')