import csv
import json

def csv_to_geojson(csv_file, json_file):
    data = {}
    data['type'] = 'FeatureCollection'
    data['features'] = []
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            feature = {}
            feature['type'] = 'Feature'
            feature['geometry'] = {}
            feature['geometry']['type'] = 'Point'
            feature['geometry']['coordinates'] = [float(row['lng']), float(row['lat'])]
            feature['properties'] = row
            data['features'].append(feature)

    with open(json_file, 'w') as f:
        json.dump(data, f)

csv_to_geojson("C:\\Temp\\data.csv", "C:\\Temp\\data2.json")