import requests
import schedule
import time
from seci import fetch_seci_news
from mnre import fetch_mnre_news

def post_to_teams(message):
    WEBHOOK_URL = 'https://hygencoin.webhook.office.com/webhookb2/f2ec3478-9d11-4553-8c65-6708e56da9e6@7ae7c16b-7491-45c1-b6a7-c4dc469742af/IncomingWebhook/b7deab2cc69047eeb362ec0dba559631/07aa046b-a66f-434c-9239-3a22dfe3e09c'
    headers = {'Content-Type': 'application/json'}
    data = {'text': message}
    response = requests.post(WEBHOOK_URL, json=data, headers=headers)
    return response.status_code

def fetch_and_post_news():
    # Read previous day's headlines
    with open('previous_headlines.txt', 'r') as file:
        previous_seci_news, previous_mnre_news = file.read().strip().split('\n')

    # Fetch current headlines
    seci_news = fetch_seci_news()
    mnre_news = fetch_mnre_news()

    # Check if the headlines are different from the previous day
    if seci_news != previous_seci_news:
        post_to_teams(f"SECI News: {seci_news}")

    if mnre_news != previous_mnre_news:
        post_to_teams(f"MNRE News: {mnre_news}")

    # Write the current headlines to the file
    with open('previous_headlines.txt', 'w') as file:
        file.write(f"{seci_news}\n{mnre_news}")

# Schedule the job to run every day at 6 AM
schedule.every().day.at("06:00").do(fetch_and_post_news)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
