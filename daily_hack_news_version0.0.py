## --Getting only headings of news from www.thehackernews.com--
## Made by Kushal 18BCE0557
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as u_req
my_url = "https://thehackernews.com"
u_client = u_req(my_url)
page_html = u_client.read()
u_client.close()
page_soup = soup(page_html, "html.parser")
container = page_soup.findAll("div", {"class":"clear home-right"})
for getter in container:
    print(getter.h2.text)
    print()
