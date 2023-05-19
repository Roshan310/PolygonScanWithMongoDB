from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['bitcoin']
collection = db['dummy']

collection.insert_one({})
print("Created sucessfully")

print(client.list_database_names())