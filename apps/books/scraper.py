import requests
from bs4 import BeautifulSoup


def scrape_book_description(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        # Try common tags (safe fallback logic)
        paragraphs = soup.find_all("p")

        text = ""
        for p in paragraphs[:5]:
            text += p.get_text() + " "

        return text.strip()

    except Exception as e:
        return "Failed to scrape content"