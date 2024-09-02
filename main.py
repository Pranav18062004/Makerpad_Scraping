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
        tutorial_tag = post.find("div", class_="tag-type tutorial")
        if tutorial_tag and tutorial_tag.text == "Tutorial":
            links_for_tut.append(post.find("a")["href"])
    return links_for_tut


def tut_link_file(html, main_url):
    link_list = tut_links(html)
    with open(file="Makerpad_Scraping\\posts\\tut_links.txt", mode="w") as f:
        for index, link in enumerate(link_list):
            f.write(f"{index + 1}: {main_url}{link}\n")


url = "https://makerpad.zapier.com/?tags=tutorials"
main_url = "https://makerpad.zapier.com"
html = get_html(url)
tut_link_file(html, main_url)
