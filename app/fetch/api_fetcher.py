import requests
from requests import HTTPError

def fetch_news_via_api(url, api_key) -> list[dict]:
    """fetches news data comprising of the title, url and the source"""
    try:
        response = requests.get(url=url, headers={"Authorization": f"Bearer {api_key}"})
        data = response.json()
        final_data = [
            {'title': article['title'], 'link': article['url'], 'published': article['publishedAt'] }
            for article in (data['articles'])]
    except HTTPError as e:
        print('check that you have entered a valid url')
    return final_data
