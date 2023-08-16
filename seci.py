import requests
from bs4 import BeautifulSoup

def fetch_seci_news():
    # Code to scrape SECI news
    # Replace URL with the actual URL
    URL = 'https://www.seci.co.in/whats-new-detail/2490'
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    heading = soup.find('h3', class_='inner-page-heading')
    return heading.text.strip() if heading else "Element not found"
