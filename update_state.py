import json
import sys

component = sys.argv[1]
new_version = sys.argv[2]

# Load the golden state file
with open("golden-state.json", "r") as file:
    state = json.load(file)

# Update only the relevant component
state[component] = new_version

# Save the updated state
with open("golden-state.json", "w") as file:
    json.dump(state, file, indent=4)

print(f"Updated {component} to {new_version} in golden-state.json")

