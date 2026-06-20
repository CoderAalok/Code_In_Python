
# Pickle is in python Built-in-Module. It is used to serialize and deserialize python object.
# Serialization is the process of converting a python object into a byte system or binary format.
# Deserialization is the process of converting a byte system or binary format into a python object.

import pickle

user_data = [
    {
        "UserID":"Alpha",
        "Password": "alpha!23"
    },
    {
        "UserID": "Berry",
        "Password": "@berry23"
    }
]


filename = "safe.pkl"
with open(filename, "wb")as fw:
    pickle.dump(user_data, fw)

with  open(filename, "rb")as fr:
    print(pickle.load(fr))



