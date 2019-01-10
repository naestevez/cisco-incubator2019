from pymongo import MongoClient
import re

#  creates new database (incubator) and collection (ADDRESSBOOK)
def get_mongo():
    client = MongoClient("localhost", 27017)
    db = client["incubator"]
    col = db.ADDRESSBOOK
    return col

#  creates new document based on data parameter (newdoc is a dictionary)
def insert_new_entry(newdoc):
    collection = get_mongo()
    doc = collection.insert_one(newdoc)

#  updates a document matching first and last names with new data (newinfo is a dictionary)
def update_entry(fname, lname, newinfo):
    collection = get_mongo()
    collection.update_one({"$and":[ {"firstname": fname}, {"lastname": lname} ]}, {"$set": newinfo})

#  displays documents matching both first and last names
#  if None, displays all documents sorted alphabetically by last names

def display_entries(fname=None, lname=None):
    collection = get_mongo()
    if fname == None and lname == None:
        docs = collection.find().sort("lastname")
        for d in docs:
            print(d)
    else:
        fname = "(?=" + fname + ")\w+"
        lname = "(?=" + lname + ")\w+"
        docs = collection.find({"$and": [{"firstname": {"$regex": fname}},
                                         {"lastname": {"$regex": lname}} ]
                              })
