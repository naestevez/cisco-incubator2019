from addressbook_mongo import get_mongo, insert_new_entry, update_entry, display_entries, delete_entries, delete_all_entries
from flask import Flask, request, render_template, json, jsonify
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config["MONGO_DBNAME"], collection = get_mongo()
app.config["MONGO_URI"] = "mongodb://localhost:27017/incubator"
mongo = PyMongo(app)


@app.route("/", methods=["GET", "POST"])
def new_entry():
    if request.method == "GET":
        return render_template("add_new.html")
    else:
        # entry_list = []
        entry_dict = {
        "fname" : request.form.get("fname"),
        "lname" : request.form.get("lname"),
        "phone" : request.form.get("phone"),
        "email" : request.form.get("email")
        }

        # for key,value in entry_dict.items():
        #     entry_list.append({key:value})
        # entry = jsonify(json.dumps(entry_list))

        message = insert_new_entry(entry_dict)

        return render_template("view_entry.html", message = message)

# @app.route("/view_all")
# def viewall():
#     all_entries = display_entries()
#     return render_template("view_all.html", all_entries = all_entries)
#
# @app.route("/delete_all", methods = ["DELETE"])
# def delete_all():
#     addressbook_mongo.delete_all_entries()

app.run(host="0.0.0.0", port=7676)
