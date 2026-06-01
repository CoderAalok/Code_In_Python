import json

# convert JSON into python dictionary(Deserialization)
# data = '{"files":["music","photos"],"fruits":["banana","apple","coconut"]}'
# print(data) # by this way can't access value using key
data = '{"files":["music","photos"],"fruits":["banana","apple","coconut"]}'
# # print(data) # by this way can't access value using key
# result = json.loads(data)
# print(result)
# print(result, type(result))
# re = json.dumps(result)
# print(type(re), re)
# print(result['files'])
# print(type(result))

# ======================================================================

# Read JSON from file
with open("data.json","r")as f:
    add_data = (json.load(f))
# with open("data.json","r")as f:
#     add_data = (json.load(f))

# ======================================================================
    
# with open("data.json","r")as f:

# with open("data.json","r")as f:
# data = {
#     "Computer":"vision",
#     "Compitative":"Programming",
#     "Data Analytics":"Data Sciencetist"
#     "Data Analytics":"Data Sciencetist",
#     1: False
# }
# add_data.append(data)
# with open("data.json","w+")as f:
#     print(json.dump(add_data, f, indent=4))
# # add_data.append(data)
# # with open("data.json","w")as f:
# #     json.dump(add_data, f, indent=4)

# print(int(list(add_data[1].keys())[-1])+123)