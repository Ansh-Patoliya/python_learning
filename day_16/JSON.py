"""
Goal: Learn basic JSON operations in Python using the built-in json module.
What you'll practice:
- JSON string vs Python dict
- json.dumps (dict -> JSON string) vs json.dump (dict -> JSON file)
- json.loads (JSON string -> dict) vs json.load (JSON file -> dict)
- Pretty printing with indent
"""

import json

# -----------------------------
# Part 1 — JSON as a plain string
# -----------------------------
# Example: A JSON value represented as a plain Python string.
# Note: This is NOT a Python dict yet; it's just text formatted as JSON.
first_json = '{"name" : "ansh" , "age":20}'
print(first_json)  # Shows the raw JSON string

# -----------------------------
# Part 2 — A Python dict (native structure)
# -----------------------------
# We'll convert this dict to a JSON string and also write it to a JSON file.
for_json_dict = {
    "name": "ansh",
    "age": 19,
    "address": {
        "area": "nikol",
        "city": "ahmedabad",
        "pincode": 382350,
    },
}
print(for_json_dict)               # Human-readable Python dict output
print(type(for_json_dict))         # <class 'dict'>

# -----------------------------
# Part 3 — Convert between dict and JSON string (dumps/loads)
# -----------------------------
# dict -> JSON string (in-memory). Use dumps ("s" for string).
# Tip: Use indent=4 in dumps if you want a pretty JSON string; here we keep it compact.
dict_to_json = json.dumps(for_json_dict)
print(dict_to_json)
print(type(dict_to_json))          # <class 'str'> (JSON is text)

# JSON string -> dict (back to Python). Use loads ("s" for string).
json_to_dict = json.loads(dict_to_json)
print(json_to_dict)
print(type(json_to_dict))          # <class 'dict'>

# -----------------------------
# Part 4 — Write/Read JSON files (dump/load)
# -----------------------------
# Write dict to a JSON file. Use dump (no "s"), passing a file object.
# indent=4 makes the file pretty and easier to read.
# Mode "w" overwrites the file if it already exists.
with open("first.json", "w", encoding="utf-8") as f:
    json.dump(for_json_dict, f, indent=4)

# Read JSON back from the file. Use load (no "s").
with open("first.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print(loaded_data)
print(type(loaded_data))           # <class 'dict'>
