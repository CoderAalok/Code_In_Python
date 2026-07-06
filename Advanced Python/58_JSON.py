import json

# convert JSON into python dictionary(Deserialization)
# data = '{"files":["music","photos"],"fruits":["banana","apple","coconut"]}'
# print(data) # by this way can't access value using key
# data = '{"files":["music","photos"],"fruits":["banana","apple","coconut"]}'
# # print(data) # by this way can't access value using key
# result = json.loads(data)
# print(result)
# print(result, type(result))
# re = json.dumps(result)
# print(type(re), re)
# print(result['files'])
# print(type(result))

data = {
    "Computer":"vision",
    "Compitative":"Programming",
    "Data Analytics":"Data Sciencetist",
    "Artificial Intellegence": "Machine Learning",
    "Loop Engineering": "casche memory"
}
# ======================================================================
from pathlib import Path
BASE = Path(__file__).parent
file = BASE/"data.json"

# Create and write json file
# with open(file,"w")as f:
#     json.dump([data], f, indent=4)



# Read JSON from file
with open(file,"r")as f:
    add_data = json.load(f)


add_data.append(data)
with open(file,"w")as f:
    json.dump(add_data, f, indent=4)

# add_data.append(data)
# with open("data.json","w+")as f:
#     print(json.dump(add_data, f, indent=4))

# print(int(list(add_data[1].keys())[-1])+123)