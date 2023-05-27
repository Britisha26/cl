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

mycol = mydb["Books"]
d = { "title": "Scarlett Letter",'author':'Nathaniel Hawthorne', "genre": "romance",'pages':130 }
print("Inserting the following record into the collection: ",d)
x = mycol.insert_one(d)


print("The ID of the one inserted record is generated automatically: ",x.inserted_id)

l = [{ "title": "13 Problems",'author':'Agatha Christie', "genre": "Mystery",'pages':264 },
          { "title": "They Came To Baghdad",'author':'Agatha Christie', "genre": "Suspense",'pages':345 },
          { "title": "Book Thief",'author':'Marcus Zusak', "genre": "war",'pages':768 }]
print("Inserting the following records into the collection: ",l)
x = mycol.insert_many(l)

print("The IDs of the many inserted records are generated automatically: ",x.inserted_ids)

print("Finding One record to display: ")
x = mycol.find_one()
print(x)

print("\nFinding All records to display: ")
for x in mycol.find():
  print(x)


s = mycol.find().sort("title")
print("Displaying the list sorted by title")
for x in s:
  print(x)



o = { "title": "13 Problems" }
n = { "$set": { "title": "Sparkling Cyanide" } }

mycol.update_one(o, n)
print("Updating the record...")
for x in mycol.find():
  print(x)

r = mycol.find().limit(5)
print("Using limit() to display 5 records: ")
for x in r:
  print(x)


mycol.delete_one(d)
x = mycol.delete_many(l)

print(x.deleted_count, "documents deleted")

