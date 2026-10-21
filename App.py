from flask import Flask, render_template, request
#from src.search_articles import search_articles

app = Flask(__name__, template_folder="docs")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/algorithm")
def algorithm():
    return render_template("algorithm.html")
@app.route("/people")
def people():
    return render_template("people.html")
@app.route("/dataset")
def dataset():
    return render_template("dataset.html")

if __name__ == "__main__":
    app.run(debug=True)
