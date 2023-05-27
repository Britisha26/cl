import pymongo

m = pymongo.MongoClient("mongodb://localhost:27017/")

dbs = m.list_database_names()
print("The available databases are: ",dbs)

if "Student" in dbs:
  print("\nThe database Student exists.")

mydb = m["Student"]
collist = mydb.list_collection_names()
print("\n\nThe available collections in Student database are: ",collist)

if "Books" in collist:
  print("\nThe collection Books exists.")

  
a={'Name':'Dhanush','age':20,1:"abhi"}
print(a[1])
