import pymongo
m=pymongo.MongoClient("mongodb://localhost:27017/")

mydb = m["Student"]
mycol = mydb["Music"]

collist = mydb.list_collection_names()
print("\n\nThe available collections in Student database are: ",collist)


mycol.drop()

collist = mydb.list_collection_names()
print("\n\nThe available collections in Student database are: ",collist)


