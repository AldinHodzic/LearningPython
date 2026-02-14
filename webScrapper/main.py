import requests
from bs4 import BeautifulSoup

def scrapeHeadlines(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("h3")

    for index, title in enumerate(headlines, 1):

        linkTag = title.find("a")

        if linkTag:
            link = linkTag["href"]
            text = title.text.strip()

            print(f"{index}. {text}")
            print(f"     Link: {link}")

target_url = "http://books.toscrape.com/" 
scrapeHeadlines(target_url)