import pymongo
#client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb+srv://akash1994:Test1234@akashkumar1994.vtufi.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "Name":"Akash",
    "email":"test",
    "Surname":"Kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )