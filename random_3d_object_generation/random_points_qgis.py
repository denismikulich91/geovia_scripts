import processing, qgis.core
import os
import random
import geojson

input_file = 'temp_polygon_layer'
output_file = 'temp_random_points.shp'

# Create random points inside polygon
processing.run("qgis:randompointsinsidepolygons", {'INPUT':input_file, 'STRATEGY':0,'VALUE':250, 'MIN_DISTANCE':1,'OUTPUT':output_file})

# Load generated points to the Canvas
layer = iface.addVectorLayer(output_file, "temp_random_points", "ogr")

if not layer:
  print("Layer failed to load!")

# accessing point layer by name
layer = QgsProject.instance().mapLayersByName('temp_random_points')[0]

if not layer.isValid():
    print("Layer failed to load!")

layer_provider = layer.dataProvider()

# adding coordinate fields

for attr in ["X", "Y"]:
  layer_provider.addAttributes([QgsField(attr, QVariant.Double)])

layer.updateFields()

# starting layer editing
layer.startEditing()

# Calculate X and Y attributes
for feature in layer.getFeatures():

    fields = layer.fields() # accessing layer fields

    attrs = {
            fields.indexFromName("X"): feature.geometry().asPoint()[0],
            fields.indexFromName("Y"): feature.geometry().asPoint()[1]
            }
    layer_provider.changeAttributeValues({feature.id(): attrs})
    
layer.commitChanges()

# Create a list of 3D objects from the directory
trees = os.listdir(r"E:\MDA\Beta Testing\City\Sunderland data sets\scripting\tree_models")
tree_color_list = ["#27ae60", "#2ecc71", "#1abc9c", "#A3CB38", "#F79F1F", "#009432"]

# Load the GeoJSON file
with open(r"E:\MDA\Beta Testing\City\Sunderland data sets\scripting\temp.geojson", "r") as f:
    data = geojson.load(f)

# Save Shp file as a CSV
QgsVectorFileWriter.writeAsVectorFormat(layer, "qgis_coords.csv", "utf-8",driverName = "CSV" , layerOptions = ['GEOMETRY=AS_XYZ'])

# Read CSV and populate GeoJSON file
with open("qgis_coords.csv", 'r') as coords:

    for line in coords.readlines()[1:]:
      line = line[:-1].split(",")
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
              "COLOR": random.choice(tree_color_list)
          }
      }
      data["features"].append(new_feature)

# Save the modified GeoJSON file
with open(r"E:\MDA\Beta Testing\City\Sunderland data sets\scripting\output_temp.geojson", 'w') as f:
    geojson.dump(data, f)
