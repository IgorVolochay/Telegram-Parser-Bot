import telebot
import requests
import time

from bs4 import BeautifulSoup

token = "" # ыВаш токен
channel_id = "" # Ваш логин канала
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def commands(message):
    #bot.send_message(channel_id, message.text)
    if message.text == "Старт":
        #bot.send_message(channel_id, "Hello")
        back_post_id = None
        while True:
            post_text = parser(back_post_id)
            back_post_id = post_text[1]

            if post_text[0] != None:
                bot.send_message(channel_id, post_text[0])
                time.sleep(1800)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши Старт")

def parser(back_post_id):
    URL = "https://habr.com/ru/search/?target_type=posts&q=python&order_by=date"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    post = soup.find("li", class_="content-list__item content-list__item_post shortcuts_item", id=True)
    post_id = post["id"]
    
    if post_id != back_post_id:
        title = post.find("a", class_="post__title_link").text.strip()
        description = post.find("div", class_="post__text post__text-html post__text_v1").text.strip()
        url = post.find("a", class_="post__title_link", href=True)["href"].strip()
        
        return f"{title}\n\n{description}\n\n{url}", post_id
    else:
        return None, post_id

bot.polling()