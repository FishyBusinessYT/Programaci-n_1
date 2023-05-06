from classes.imports import project_directory
import json

optionNumber = 0
options = {}

while True:
    optionName = input(f"Enter option #{optionNumber}:\n")
    if optionName == "":
        break
    options[optionName.upper()] = optionNumber
    optionNumber += 1

with open(f"{project_directory}\\RENAME.json", "w") as file:
    file.write(json.dumps(options))

print("Json file generated.")