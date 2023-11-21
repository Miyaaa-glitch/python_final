import json
import os

# Get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load meals data
meals_file_path = os.path.join(script_dir, "data", "meals.json")
with open(meals_file_path) as file:
    meals = json.load(file)

# Load combos data
combos_file_path = os.path.join(script_dir, "data", "combos.json")
with open(combos_file_path) as file:
    combos = json.load(file)

# ... rest of your code ...
