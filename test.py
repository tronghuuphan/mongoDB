import pymongo
from pymongo import MongoClient
from datetime import datetime

cluster = MongoClient('mongodb+srv://huu:abc123abc@cluster0.ft8ih.mongodb.net/<dbname>?retryWrites=true&w=majority')
db = cluster['room']
collection = db['log']

def get_time():
    now = datetime.now()
    return {"date": now.strftime("%d/%m/%Y"), "time":now.strftime("%H:%M:%S")}



#post = {}
#post.update(get_time())
#print(post)
#while True:
A = "Phan Trong Huu"
B = "Phan Ben"
C = "Pham Van Nhat"
D = "Tran Chi Thanh"
E = "Nguyen Dac Quy"
F = "Nguyen Van Thuan"
import random
list=[A,B,C,D,E,F]
import time

for a in range(163, 180):
    post = {"_id":a, "ID":random.choice(list)}
    post.update(get_time())
    collection.insert_one(post)
    time.sleep(random.choice([1,5,7,2,3,9]))
     


#    post = get_time()
#    collection.insert_one(post)

"""import time
while 1:
    collection.update_one({"_id":0},{"$set":{"d1":0, "d2":0, "d3":5}})
    time.sleep(5)
    collection.update_one({"_id":0},{"$set":{"d1":2, "d2":4, "d3":5}})
    time.sleep(5)
    collection.update_one({"_id":0},{"$set":{"d1":2, "d2":0, "d3":0, "d4":5}})
    time.sleep(5)"""
#post1 = {"_id":5, "name":"Ben"}
#post2 = {"_id":6, "name":"Hue"}

#collection.insert_many([post1, post2])

#array=list(collection.find())
#print(type(array[0]))

#for i in result:
#    print(i)

#collection.update_one({"_id":0}, {"$set":{"name":"tronghuuphan"}})

def stat():
    result = collection.find()
    
#    sort_orders = sorted(dict_result[0].items(), key=lambda x: x[1], reverse=True)
    a = list(result)
    b = sorted(a, key=lambda k: k['_id'], reverse=True)
    s = [b[i] for i in range(10)]
    print(s)
#stat()
