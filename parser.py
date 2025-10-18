import requests
from bs4 import BeautifulSoup

def parse_data():
    url = "https://api.coingecko.com/api/v3/simple/price?"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    items = [item.text.strip() for item in soup.select(".item")]
    return items
