import requests
from bs4 import BeautifulSoup

def fetch_seci_news():
    URL = 'https://www.seci.co.in/whats-new'
    
    # Send a GET request to the URL
    response = requests.get(URL)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the table with the news items
    table = soup.find('table', {'id': 'abc'})
    
    if not table:
        return "No news found."

    # Extract the news items
    news_items = []
    rows = table.find_all('tr')
    for row in rows[1:]: # Skip the header row
        columns = row.find_all('td')
        if len(columns) > 2:
            news_text = columns[1].text.strip()
            news_date = columns[2].text.strip()
            news_items.append(f"{news_text} (Date: {news_date})")

    return "\n".join(news_items)

# Test the function
if __name__ == "__main__":
    print(fetch_seci_news())
