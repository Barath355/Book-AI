from .scraper import scrape_book_description
from .ai_utils import generate_summary


def get_book_summary_from_url(url):
    content = scrape_book_description(url)
    summary = generate_summary(content)

    return {
        "content": content,
        "summary": summary
    }