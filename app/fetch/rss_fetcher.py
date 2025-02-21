import feedparser
from pydantic import HttpUrl, ValidationError

# load feed contents
def fetch_rss_feeds(url:HttpUrl) -> list[dict]:
    """fetches rss data comprising of title, link and published date"""
    try:
        feed = feedparser.parse(url)
        news = [
        {'title':entry.title, 'link':entry.link, 'published':entry.published}
        for entry in feed.entries
    ]
    except ValidationError as e:
        print(e)
    return news
