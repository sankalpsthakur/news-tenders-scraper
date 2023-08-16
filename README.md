# news-tenders-scraper
 MNRE, SECI, Twitter Feeds scraped and delivered to teams/email


# Overview

The News & Tenders Scraper project is designed to scrape news and tenders from various sources including MNRE, SECI, Twitter, and other news websites. The scraped information is then delivered through multiple channels like Teams, WhatsApp, and Email. The system is built with scalability in mind, allowing for easy addition of new sources and delivery methods.

# Table of Contents

Installation
Configuration
Usage
Project Structure
Extending the System
Contributing
License

# Installation

Clone the repository: git clone https://github.com/your-repo/news-tenders-scraper.git
Navigate to the project directory: cd news-tenders-scraper
Install dependencies: pip install -r requirements.txt

# Configuration

Copy the config/settings.env.example file to config/settings.env.
Update the .env file with the appropriate configurations for sources, delivery channels, and other settings.
Ensure that the necessary API keys, URLs, and credentials are set.

# Usage

Run the main script to start scraping and delivering news:

bash
Copy code
python src/main.py

# Structure

src/scrapers/: Contains individual scraper modules for different sources.
src/delivery/: Contains modules for different delivery channels.
src/main.py: Main script for orchestrating the scraping and delivery.
config/: Configuration files and environment settings.

# Extending the System

Adding New Sources
Create a new scraper module in src/scrapers/.
Implement the scraper class, possibly extending a base scraper class.
Update the main script to include the new source.
Adding New Delivery Channels
Create a new delivery module in src/delivery/.
Implement the delivery class, possibly extending a base delivery class.
Update the main script to include the new delivery channel.

# Contributing

Contributions are welcome! Please follow the standard Git workflow and submit pull requests for review.

# License

This project is licensed under the MIT License. See the LICENSE file for details
