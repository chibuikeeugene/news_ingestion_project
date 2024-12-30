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
    print(news)
    return news



# testing the function
# url =  "https://feeds.skynews.com/feeds/rss/technology.xml"
# fetch_rss_feeds(url=url)