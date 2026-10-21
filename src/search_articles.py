
import random
from src.read_xml import load_articles


def search_articles(keyword="", topic="", start_year="", end_year="",
                    open_access="", sort_by=""):

    articles = load_articles()
    results = []

    keyword = keyword.strip().lower()

    for article in articles:
        # Read article information
        title = article.findtext("title", "").lower()
        topic_text = article.findtext("topic", "").lower()
        journal = article.findtext("journal", "").lower()

        # Read multiple keywords from XML
        keywords = [
            item.text.lower()
            for item in article.findall("keywords/keyword")
            if item.text
        ]

        year = int(article.findtext("year", "0"))
        access = article.findtext("open_access", "").lower()
        # citations = int(article.findtext("citation_count", "0"))
        citations = float(article.findtext("citations_per_year", "0"))

        # Search by keyword in title, topic, journal, or keywords
        if keyword:
            searchable_text = [title, topic_text, journal] + keywords

            if not any(keyword in text for text in searchable_text):
                continue

        # Filter 1: Topic
        if topic and topic_text != topic.lower():
            continue

        # Filter 2: Start year
        if start_year and year < int(start_year):
            continue

        # Filter 3: End year
        if end_year and year > int(end_year):
            continue

        # Filter 4: Open access
        if open_access == "true" and access != "true":
            continue

        # Add matching article and citation count
        results.append((article, citations))

    # Sort by citations or randomise results
    if sort_by == "citations":
        results.sort(key=lambda item: item[1], reverse=True)
    else:
        random.shuffle(results)

    return [article for article, citations in results]
