import random
import libraries.yomomma as ym
import libraries.quote as quote
import libraries.helper as helper
import libraries.roast as roast
import libraries.pickuplines as pick
import json


def empty_response(author):
    empty_choices = [' what\'s up.', ' what can i help you with.', ' what can i do for you.']
    return 'Hey ' + author + empty_choices[random.randint(0, len(empty_choices))]


def unpredicted_respose(author, response):
    with open('D:\Django\DiscordBot\data\greetings.json', encoding="utf8") as file:
        greetings = json.load(file)

    if response in greetings:
        return greetings[response][0] + ' ' + author + ' ' + greetings[response][1]
    return author + 'i am still learning what ' + response + ' is'


def message_responder(author, response):
    if response.startswith('yomomma'):
        return ym.yomomma()
    if response.startswith('help'):
        return helper.helper()
    if response.startswith('roast'):
        return roast.roaster()
    if response.startswith('pickup'):
        return pick.pickup()
    if response.startswith('quote'):
        return quote.get_quote()
    else:
        return unpredicted_respose(author, response)


def message_reader(author, message):
    try:
        response = message.split(' ', 1)[1]
    except IndexError:
        response = 'null'

    if response == 'null':
        return empty_response(author)
    else:
        return message_responder(author, response)
