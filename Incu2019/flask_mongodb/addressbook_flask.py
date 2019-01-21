from flask import Flask, request, render_template
import uuid
# from flask_pymongo import PyMongo
# from mongo import *

app = Flask(__name__)
# app.config["MONGO_DBNAME"] = get_mongo()
# app.config["MONGO_URI"] = "mongodb://localhost:27017/incubator"
# mongo = PyMongo(app)

entry={}
all_entries={}

@app.route("/", methods=["GET", "POST"])
def new_entry():
    if request.method == "GET":
        return render_template("add_new.html")
    else:
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        phone = request.form.get("phone")
        email = request.form.get("email")
        user_id = uuid.uuid4().hex
        entry.clear()
        entry["fname"] = fname
        entry["lname"] = lname
        entry["phone"] = phone
        entry["email"] = email
        all_entries[user_id] = entry
        return render_template("view_entry.html", fname=fname, lname=lname, phone=phone, email=email)

@app.route("/view_all")
def viewall():
    return render_template("view_all.html", all_entries = all_entries)

app.run(host="0.0.0.0", port=7676)
