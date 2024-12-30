import requests
from requests import HTTPError

def fetch_news_via_api(url, header) -> list[dict]:
    """fetches news data comprising of the title, url and the source"""
    try:
        response = requests.get(url=url, headers=header)
        data = response.json()
    except HTTPError as e:
        print('check that you have entered a valid url')
        
    print(data)
    return data

# Testing the function
# url = "https://f1-latest-news.p.rapidapi.com/news/f1"

# headers = {
# 	"x-rapidapi-key": "0f1d602546msh31dca6e76b6c48ap107ba0jsn95028d78e8ff",
# 	"x-rapidapi-host": "f1-latest-news.p.rapidapi.com"
# }

# fetch_news_via_api(url=url, header=headers)