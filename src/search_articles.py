import random
from src.read_xml import load_articles


def search_articles(keyword="", topic="", start_year="", end_year="",
                    open_access="", sort_by=""):

    articles = load_articles()
    results = []

    keyword = keyword.strip().lower()

    for article in articles:
        title = article.findtext("title", "").lower()
        topic_text = article.findtext("topic", "").lower()
        journal = article.findtext("journal", "").lower()

        year = int(article.findtext("year", "0"))
        access = article.findtext("open_access", "").lower()
        citations = int(article.findtext("citation_count", "0"))

        # Keyword search
        if keyword and keyword not in title and keyword not in topic_text and keyword not in journal:
            continue

        # Filter 1: Topic
        if topic and topic_text != topic.lower():
            continue

        # Filter 2: Year range
        if start_year and year < int(start_year):
            continue

        if end_year and year > int(end_year):
            continue

        # Filter 3: Open access
        if open_access == "true" and access != "true":
            continue

        results.append((article, citations))

    # Filter 4: Sort by citations or randomise
    if sort_by == "citations":
        results.sort(key=lambda item: item[1], reverse=True)
    else:
        random.shuffle(results)

    return [article for article, citations in results]