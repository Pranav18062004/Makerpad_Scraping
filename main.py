import requests
from bs4 import BeautifulSoup


def get_html(site_url):
    html_text = requests.get(url=site_url).text
    soup = BeautifulSoup(html_text, "lxml")
    return soup


def tut_links(soup):
    posts = soup.find_all("div", class_="posts-item w-dyn-item")
    links_for_tut = []
    for post in posts:
        links_for_tut.append(post.find("a")["href"])
    return links_for_tut


url = "https://makerpad.zapier.com/?tags=tutorials"
html = get_html(url)
tutorial_link_list = tut_links(html)
print(tutorial_link_list)
