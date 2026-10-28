
from flask import Flask, render_template, request
from src.search_articles import search_articles
from src.read_xml import load_articles

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET", "POST"])
def index():
    all_articles = load_articles()

    # Get unique topics from the XML dataset
    topics = sorted(set(
        article.findtext("topic", "").strip()
        for article in all_articles
        if article.findtext("topic", "").strip()
    ))

    articles = []

    if request.method == "POST":
        keyword = request.form.get("keyword", "")
        topic = request.form.get("topic", "")
        start_year = request.form.get("start_year", "")
        end_year = request.form.get("end_year", "")
        open_access = request.form.get("open_access", "")
        sort_by = request.form.get("sort_by", "")

        articles = search_articles(
            keyword=keyword,
            topic=topic,
            start_year=start_year,
            end_year=end_year,
            open_access=open_access,
            sort_by=sort_by
        )

    return render_template(
        "index.html",
        articles=articles,
        topics=topics
    )


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
