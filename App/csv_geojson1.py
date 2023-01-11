import csv
import geojson

def csv_to_geojson(csv_file):
    features = []
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            feature = geojson.Feature(geometry=geojson.Point((float(row['lng']), float(row['lat']))), properties=row)
            features.append(feature)
    return geojson.FeatureCollection(features)

geojson_data = csv_to_geojson("C:\\Temp\\data.csv")
with open("data.json", "w") as f:
    geojson.dump(geojson_data, f)