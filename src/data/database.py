import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
librarydb = myclient["librarydatabase"]
usercol = librarydb["users"]
bookcol = librarydb["books"]
print(librarydb.list_collection_names())