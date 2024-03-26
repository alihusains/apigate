import csv
import json

# Read CSV file and convert to JSON
with open('temp_without_header.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    json_data = json.dumps(list(csv_reader), indent=4)

# Write JSON data to file
with open('processed_response.json', 'w') as json_file:
    json_file.write(json_data)
