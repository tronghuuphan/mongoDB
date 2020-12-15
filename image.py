import pymongo
from pymongo import MongoClient
import base64

# establish a connection to the database
cluster = MongoClient('mongodb+srv://huu:abc123abc@cluster0.ft8ih.mongodb.net/<dbname>?retryWrites=true&w=majority')
db = cluster['room']
collection = db['log']

dic = collection.find({})

a = list(dic)
b = sorted(a, key=lambda k: k['_id'], reverse=True)
print(b)
print(b[0]["_id"])
