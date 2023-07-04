import requests
import re
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self) -> None:
        url = "https://www.python.org/"
        req = requests.get(url)

        soup = BeautifulSoup(req.content, "html.parser")
        self.scraped = soup.get_text()

    def get_page(self):
        return self.scraped

    def get_greeting(self):
        if not hasattr(self, "greeting"):
            match = re.search("\s*(.*)", self.scraped)  # noqa: W605
            self.greeting = match.group(1)
        return self.greeting

    def get_latest_version(self):
        if not hasattr(self, "latest_version"):
            match = re.search("Latest: (Python [0-9.]*)", self.scraped)
            self.latest_version = match.group(1)
        return self.latest_version

    def get_success_story(self):
        if not hasattr(self, "success_story"):
            match = re.search(
                "Success Stories\sMore\s*(.*)", self.scraped  # noqa: W605
            )
            self.success_story = match.group(1)
        return self.success_story


scraper = Scraper()
print(scraper.get_page())
print(scraper.get_greeting())
print(scraper.get_latest_version())
print(scraper.get_success_story())
