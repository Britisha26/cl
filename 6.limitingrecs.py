import pymongo

m = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = m["Student"]
mycol = mydb["Books"]

r = mycol.find().limit(5)
print("Using limit() to display 5 records: ")
for x in r:
  print(x)