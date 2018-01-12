import sys
import json


a = '[ \
    {"id": 1, "name": "San Francisco Bay Area", "parent_id": "null"}, \
    {"id": 2, "name": "San Jose", "parent_id": 3}, \
    {"id": 3, "name": "South Bay", "parent_id": 1}, \
    {"id": 4, "name": "San Francisco", "parent_id": 1}, \
    {"id": 5, "name": "Manhattan", "parent_id": 6}, \
    {"id": 6, "name": "New York", "parent_id": "null"}]'

# Read from stdin
locations = json.loads(a)

output = []
parents = {}
names = {}
for loc in locations:
    if loc["parent_id"] == 'null':
        if loc["id"] not in parents:
            parents[loc["id"]] = []
        names[loc["id"]] = loc["name"]
    else:
        if loc["parent_id"] not in parents:
            print loc["name"]
            parents[loc["parent_id"]] = [loc["id"]]
        else:
            parents[loc["parent_id"]].append(loc["id"])
        names[loc["id"]] = loc["name"]



print [names[k] for k in parents.keys()]
for k in parents.keys():
    output.append((names[k],[names[i] for i in parents[k]]))

print parents
print sorted(output)

for k in sorted(parents.keys()):
    print names[k]
    d = '-'
    for v in parents[k]:
        if v in parents:
            d += '-'
            continue
        print d + names[v]