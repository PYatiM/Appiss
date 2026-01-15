# app.py
from flask import Flask, render_template, request
from checker import bulk_check

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    results = None

    if request.method == "POST":
        urls = request.form.get("urls", "")
        url_list = urls.splitlines()
        results = bulk_check(url_list)

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
