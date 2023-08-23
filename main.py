import requests
import schedule
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from Updater import CheckRepoUpdates
MNRE_URL = 'https://www.mnre.gov.in/tenders/recent' 
SECI_URL = "https://seci.co.in/whats-new"
WEBHOOK_URL = 'https://hygencoin.webhook.office.com/webhookb2/f2ec3478-9d11-4553-8c65-6708e56da9e6@7ae7c16b-7491-45c1-b6a7-c4dc469742af/IncomingWebhook/b7deab2cc69047eeb362ec0dba559631/07aa046b-a66f-434c-9239-3a22dfe3e09c'


def fetch_mnre_news(url):
    # Fetch the HTML content from the given URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the accordion container
    accordion_container = soup.find('div', class_='accordion', id='accordionExample')

    # Initialize a list to hold the news items
    news_items = []

    # Iterate through the buttons within the accordion container
    if accordion_container:
        for button in accordion_container.find_all('button', class_='btn btn-link english_title'):
            date_tag = button.find('p', class_='date')
            date = date_tag.text.strip() if date_tag else ''
            title = button.text.replace(date, '').strip() if date_tag else button.text.strip()
            news_items.append((date, title))
    
    return news_items


def fetch_seci_news(url):
    def fetch_heading(link_url):
        response = requests.get(link_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        heading = soup.find('h3', class_='inner-page-heading')
        return heading.text.strip() if heading else "Element not found"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all table cells with class 'td_grid'
    td_grids = soup.find_all('td', class_='td_grid')
    print(td_grids)
    
    results = []
    for td_grid in td_grids:
        # Find the anchor tags within each table cell
        anchors = td_grid.find_all('a')
        for anchor in anchors:
            relative_link = anchor['href']
            # Combine the base URL with the relative link
            full_link = urljoin(url, relative_link)
            heading = fetch_heading(full_link)
            results.append((full_link, heading))
    print(results)
    
    return results

def post_to_teams(message):
    WEBHOOK_URL = 'https://hygencoin.webhook.office.com/webhookb2/f2ec3478-9d11-4553-8c65-6708e56da9e6@7ae7c16b-7491-45c1-b6a7-c4dc469742af/IncomingWebhook/b7deab2cc69047eeb362ec0dba559631/07aa046b-a66f-434c-9239-3a22dfe3e09c'
    headers = {'Content-Type': 'application/json'}
    data = {'text': message}
    response = requests.post(WEBHOOK_URL, json=data, headers=headers)
    return response.status_code


def fetch_and_post_news():
    # Read previous day's headlines
    CheckRepoUpdates()
    
    with open('previous_headlines.txt', 'r') as file:
        previous_headlines = file.read().strip().split('\n')
        previous_seci_news = previous_headlines[0] if len(previous_headlines) > 0 else ""
        previous_mnre_news = previous_headlines[1] if len(previous_headlines) > 1 else ""

    # Fetch current headlines
    seci_news = fetch_seci_news(SECI_URL)

    mnre_news = fetch_mnre_news(MNRE_URL)

    # Check if the headlines are different from the previous day
    if seci_news != previous_seci_news:
        post_to_teams(f"SECI News: {seci_news}")
        print("Posted SECI news to Teams.")

    if mnre_news != previous_mnre_news:
        post_to_teams(f"MNRE News: {mnre_news}")
        print("Posted MNRE news to Teams.")

    # Write the current headlines to the file
    with open('previous_headlines.txt', 'w') as file:
        seci_news_str = '\n'.join([f"{link}: {heading}" for link, heading in seci_news])
        mnre_news_str = '\n'.join([f"{date}: {title}" for date, title in mnre_news])
        file.write(f"{seci_news_str}\n{mnre_news_str}")

# Schedule the job to run every day at 6 AM
schedule.every().day.at("06:00").do(fetch_and_post_news)


# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
