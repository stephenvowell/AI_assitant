import json

# Read the JSON data from the file
with open('data.json', 'r') as file:
    data = json.load(file)

# Filter out entries with URLs containing "https://consent.yahoo.com"
filtered_data = [entry for entry in data if "https://consent.yahoo.com" not in entry['url']]

# Write the cleaned data back to the file
with open('data.json', 'w') as file:
    json.dump(filtered_data, file, indent=4)

print("Filtered data has been written to data.json")