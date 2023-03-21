import os
import random
import geojson
trees = os.listdir("tree_models")
# Load the GeoJSON file
with open('temp.geojson', 'r') as f:
    data = geojson.load(f)

with open("qgis_coords.csv", 'r') as coords:
    for line in coords.readlines()[1:]:
      line = line[:-1].split(",")
      print(line)
      id = line[0].strip('"')
      height_ratio = round(1 * (3 / random.randint(1, 6)), 1)
      new_feature = {
          "type": "Feature",
          "geometry": {
              "type": "Point",
              "coordinates": [float(line[1]), float(line[2])],
          },
          "properties": {
              "name": f"tree-{id}",
              "ALTITUDE": 0,
              "SCALE": f"1.0 1.0 {height_ratio}",
              "STRID": id,
              "FILENAME": random.choice(trees),
              "ORIENT": f"{random.randint(0, 270)} 0 0",
              "WEIGHT": 100,
              "COLOR": "#27ae60"
          }
      }
      data["features"].append(new_feature)

# Save the modified GeoJSON file
with open('output_temp.geojson', 'w') as f:
    geojson.dump(data, f)
# print(data)