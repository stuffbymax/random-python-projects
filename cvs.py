import csv
import json

csv_file = "data.csv"  # Replace with your file name
json_file = "data.json"

with open(csv_file, mode="r", encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)
    data = [row for row in csv_reader]

with open(json_file, mode="w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print(f"CSV successfully converted to {json_file}")
