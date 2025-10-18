import requests
from bs4 import BeautifulSoup

def parse_data():
    url = "https://example.com/data"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    items = [item.text.strip() for item in soup.select(".item")]
    return items
