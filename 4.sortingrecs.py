import pymongo

m = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = m["Student"]
mycol = mydb["Books"]

s = mycol.find().sort("title")
print("Displaying the list sorted by title")
for x in s:
  print(x)
