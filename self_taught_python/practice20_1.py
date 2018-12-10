import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self,site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read().decode('utf-8')
        parser = "html.parser"
        sp = BeautifulSoup(html,parser)
        print(sp.title)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            # if url is None:
            #     continue
            # if "html" in url:
            print("\n" + url)


if __name__ == '__main__':

    news = "https://news.google.com"
    Scraper(news).scrape()





