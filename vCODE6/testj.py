import json
data = {
    "taches" : [ "Tache1", "Tache2", "Tache3" ]
}

with open("data.json", "w") as f:
    json.dump(data, f)


with open("data.json", "r") as f:
    data = json.load(f)

print(data)