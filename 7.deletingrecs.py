import pymongo

m = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = m["Student"]
mycol = mydb["Books"]

d = { "title": "Scarlett Letter" }
l = {'author':'Agatha Christie'}


mycol.delete_one(d)
x = mycol.delete_many(l)

print(x.deleted_count, "documents deleted")