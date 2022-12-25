import app
import time
import telebot
import config
import random

from elasticsearch import helpers
import csv

connected = False

with open('posts.csv') as f:
    reader = csv.DictReader(f)
    for i in range(100):
        if not app.es.ping():
            time.sleep(1)
        else:
            time.sleep(2)
            break
    if app.es.ping() and app.es.count()['count'] < 1500:
        helpers.bulk(app.es, reader, index='my-index')
        connected = True
    else:
        print("cannot")

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, " Қайырлы күн, {0.first_name}!\nЯ - <b>{1.first_name}</b>.".format(message.from_user, bot.get_me()),
        parse_mode='html')


@bot.message_handler(commands=['da'])
def balda(message):
    bot.send_message(message.chat.id, "Balda")


@bot.message_handler(commands=['Чики'])
def balda(message):
    bot.send_message(message.chat.id, "Брики")


@bot.message_handler(commands=['kak'])
def balda(message):
    bot.send_message(message.chat.id, "Beshbarmak")


@bot.message_handler(commands=['balda'])
def balda(message):
    if (connected):
        result = app.es.search(body={'query': {'match': {'text': random.randint(0, 9)}}})
        result = result['hits']['hits']
        if len(result) > 1:
            result = result[:1]
        bot.send_message(message.chat.id, str(result))
    else:
        with open('posts.csv') as f:
            reader = csv.DictReader(f)
            for i in range(random.randint(1, 30)):
                row1 = next(reader)
            row1 = next(reader)
            bot.send_message(message.chat.id, str(row1))




@bot.message_handler(content_types=['text'])
def speak(message):
    if (connected):
        result = app.es.search(body={'query': {'match': {'text': message}}})
        result = result['hits']['hits']
        if len(result) > 20:
            result = result[:20]
        bot.send_message(message.chat.id, str(result))
    else:
        bot.send_message(message.chat.id, "...")

bot.polling(non_stop=True)
