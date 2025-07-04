import requests
from bs4 import BeautifulSoup

def scrape_google_news(query, num_results=10):
    url = f"https://news.google.com/search?q={query}&hl=en-US&gl=US&ceid=US:en"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    articles = []
    for item in soup.select("article")[:num_results]:
        title = item.text.strip()
        articles.append(title)
    return articles