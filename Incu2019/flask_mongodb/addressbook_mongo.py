from pymongo import MongoClient
import re

#  creates new database (incubator) and collection (ADDRESSBOOK)
def get_mongo():
    client = MongoClient("localhost", 27017)
    db = client["incubator"]
    col = db.ADDRESSBOOK
    return (db, col)

#  creates new document based on data parameter (newdoc is a dictionary)
def insert_new_entry(newdoc):
    db, collection = get_mongo()
    doc = collection.insert(newdoc)
    return "Success! - New Entry Added"

# def view_new_entry():
#     collection = get_mongo()
#     view_entry = db.collection.find().limit(1).sort({$natural: -1}).pretty()
#     return view_entry

#  updates a document matching first and last names with new data (newinfo is a dictionary)
def update_entry(fname, lname, newinfo):
    db, collection = get_mongo()
    collection.update_one({"$and":[ {"firstname": fname}, {"lastname": lname} ]}, {"$set": newinfo})

#  displays documents matching both first and last names (or variations of them)
#  if None, displays all documents sorted alphabetically by last names
def display_entries(fname=None, lname=None):
    db, collection = get_mongo()
    if fname == None and lname == None:
        docs = collection.find().sort("lastname")
        return docs
    else:
        fname = "(?=" + fname + ")\w+"
        lname = "(?=" + lname + ")\w+"
        docs = collection.find({"$and": [{"firstname": {"$regex": fname}},
                                         {"lastname": {"$regex": lname}} ]
                              })
        return docs
#  deletes documents matching both first and last names (or variations of them)
def delete_entries(fname=None, lname=None):
    db, collection = get_mongo()
    fname = "(?=" + fname + ")\w+"
    lname = "(?=" + lname + ")\w+"
    collection.delete_many({"$and": [{"firstname": {"$regex": fname}},
                                {"lastname": {"$regex": lname}}]
                     })
    docs = collection.find()
    for d in docs:
        print(d)

def delete_all_entries():
    db, collection = get_mongo()
    collection.delete_many({})
