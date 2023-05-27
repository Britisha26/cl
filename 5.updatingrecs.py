import pymongo

m = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = m["Student"]
mycol = mydb["Books"]

o = { "title": "13 Problems" }
n = { "$set": { "title": "Sparkling Cyanide" } }

mycol.update_one(o, n)
print("Updating the record...")
for x in mycol.find():
  print(x)
