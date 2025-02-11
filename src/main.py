import requests
import pandas as pd
import feedparser

def fetch_data(regio, poule, type):
    # url = rf"https://api.nevobo.nl/export/poule/{regio}/{poule}/stand.{type}"
    url = rf"https://api.nevobo.nl/export/poule/{regio}/competitie-seniorencompetitie-4/{regio}-{poule.lower()}/resultaten.{type}"

    # Parse the RSS feed
    feed = feedparser.parse(url)

    # Print feed title
    print(f"Feed Title: {feed.feed.title}")

    return feed

    # # Loop through entries
    # for entry in feed.entries:
    #     print("\nMatch Title:", entry.title)
    #     print("Published:", entry.published)
    #     print("Link:", entry.link)
    #     print("Summary:", entry.summary)


data = fetch_api(regio='nationale-competitie', poule='2FH', type='rss')
