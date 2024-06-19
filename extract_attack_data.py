import json
import random


with open('enterprise-attack-10.1.json', 'r') as file:
    data = json.load(file)

attacks = data.get('objects', [])


selected_attacks = random.sample(attacks, 2000)

with open('enterprise-attack-subset.json', 'w') as subset_file:
    json.dump(selected_attacks, subset_file, indent=4)

print(f"Extracted {len(selected_attacks)} attacks into 'enterprise-attack-subset.json'")
