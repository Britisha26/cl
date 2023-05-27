import pymongo

m = pymongo.MongoClient("mongodb://localhost:27017/")

 mydb = m["College"]

 mycol = mydb["sist"]
  d = { "title": "Scarlett Letter",'author':'Nathaniel Hawthorne', "genre": "romance",'pages':130 }
  print("Inserting the following record into the collection: \n",d)
  x = mycol.insert_one(d)


 print("\nThe ID of the one inserted record is generated automatically: \n",x.inserted_id)

 l = [{ "title": "13 Problems",'author':'Agatha Christie', "genre": "Mystery",'pages':264 },
            { "title": "They Came To Baghdad",'author':'Agatha Christie', "genre": "Suspense",'pages':345 },
            { "title": "Book Thief",'author':'Marcus Zusak', "genre": "war",'pages':768 }]
  print("Inserting the following records into the collection: ",l)
  x = mycol.insert_many(l)

 print("\nThe IDs of the many inserted records are generated automatically: \n",x.inserted_ids)