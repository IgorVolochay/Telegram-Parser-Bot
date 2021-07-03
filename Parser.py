import requests

from bs4 import BeautifulSoup

URL = "https://habr.com/ru/search/?target_type=posts&q=python&order_by=date"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

post = soup.find("li", class_="content-list__item content-list__item_post shortcuts_item", id=True)
post_id = post["id"]
print(post_id)

title = post.find("a", class_="post__title_link").text.strip()
description = post.find("div", class_="post__text post__text-html post__text_v1").text.strip()
url = post.find("a", class_="post__title_link", href=True)["href"].strip()

print(title, description, url)