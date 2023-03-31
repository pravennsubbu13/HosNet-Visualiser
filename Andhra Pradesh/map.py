import folium
import json

# read the JSON file
with open('Andhra.json') as f:
    data = json.load(f)

# create a map centered at the first location
map = folium.Map(location=[data['results'][0]['latitude'], data['results'][0]['longitude']], zoom_start=10)

# add markers for each location to the map
for location in data['results']:
    folium.Marker([location['latitude'], location['longitude']], popup=location['name']).add_to(map)

# save the map to an HTML file
map.save('Andhra.html')
