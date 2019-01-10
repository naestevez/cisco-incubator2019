from pymongo import MongoClient
import re

#  create new database and collection
def get_mongo():
    client = MongoClient("localhost", 27017)
    db = client["incubator"]
    col = db.ADDRESSBOOK
    return col
