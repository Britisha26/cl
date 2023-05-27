import pymongo

m = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = m["Student"]
mycol = mydb["Books"]

print("Finding One record to display: ")
x = mycol.find_one()
print(x)

print("\nFinding All records to display: ")
for x in mycol.find():
    print(x)
