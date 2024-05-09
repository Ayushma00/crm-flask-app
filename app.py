from flask import Flask, render_template, url_for, request, redirect

# call post request methodS
import config
import requests

# requests library for making differenyt api calls
import json


def page_not_found(e):
    return render_template("404.html"), 404


app = Flask(__name__)
app.config.from_object(config.config["development"])

app.register_error_handler(404, page_not_found)

headers = {
    "authorization": "Bearer {}".format(app.config["AIRTABLE_KEY"]),
    "content-type": "application/json",
}


@app.route("/")
def index():
    return render_template("index.html", **locals())


@app.route("/delete/<string:rowId>", methods=["DELETE"])
def delete(rowId):
    print("https://api.airtable.com/v0/appZ8wloM4omloj0T/Team/{}".format(rowId)),
    requests.delete(
        "https://api.airtable.com/v0/appZ8wloM4omloj0T/Team/{}".format(rowId),
        headers=headers,
    )
    return redirect(url_for("users"))


@app.route("/users_edit", methods=["POST"])
def users_edit():

    payload = {
        "records": [
            {
                "id": request.form["rowid"],
                "fields": {
                    "teamid": request.form["teamId"],
                    "FirstName": request.form["FirstName"],
                    "LastName": request.form["LastName"],
                    "JobTitle": request.form["JobTitle"],
                    "Email": request.form["Email"],
                    "PhoneNumber": request.form["PhoneNumber"],
                },
            }
        ]
    }
    requests.put(
        " https://api.airtable.com/v0/appZ8wloM4omloj0T/Team",
        json=payload,
        headers=headers,
    )
    return redirect(url_for("users"))


@app.route("/users", methods=["GET", "POST"])
def users():
    url = "https://api.airtable.com/v0/appZ8wloM4omloj0T/Team?maxRecords=10&view=Grid%20view"
    r = requests.get(url, headers=headers)
    result = json.loads(r.text)
    if request.method == "POST":
        payload = {
            "records": [
                {
                    "fields": {
                        "teamid": request.form["teamId"],
                        "FirstName": request.form["FirstName"],
                        "LastName": request.form["LastName"],
                        "JobTitle": request.form["JobTitle"],
                        "Email": request.form["Email"],
                        "PhoneNumber": request.form["PhoneNumber"],
                    }
                }
            ]
        }
        requests.post(
            "https://api.airtable.com/v0/appZ8wloM4omloj0T/Team",
            json=payload,
            headers=headers,
        )
        return redirect(url_for("users"))
    return render_template("user.html", **locals())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8888", debug=True)
