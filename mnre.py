from bs4 import BeautifulSoup

def fetch_mnre_news():
    # HTML content (replace this with the actual HTML or use requests to fetch it)
    HTML_CONTENT = """
    <!DOCTYPE html>
    <!-- Rest of the HTML content -->
    <div class="card-header" id="headingOne">
        <h2 class="mb-0">
            <button class="btn btn-link english_title" type="button">
                <p class="_date">Submission Date: 22 Aug, 2023</p>
                "Supply, Pre-deployment Validation, Installation and Commissioning of Integrated Floating Buoy with offshore LiDAR together with Meteorological and Oceanographic Sensors (Wave, Current etc.,) on OUTRIGHT PROCUREMENT BASIS at Sub Zone-7 in Gulf of Mannar off, Tamil Nad Coast in India including Warranty & Comprehensive Operation and Maintenance 10-08-2023, 2.6 mb, PDF) "
            </button>
            <!-- Rest of the content -->
        </h2>
    </div>
    """

    # Parse the HTML content
    soup = BeautifulSoup(HTML_CONTENT, 'html.parser')

    # Find the button element with class "btn btn-link english_title"
    button = soup.find('button', class_='btn btn-link english_title')

    # Return the text content of the button
    return button.text.strip() if button else "Element not found"
