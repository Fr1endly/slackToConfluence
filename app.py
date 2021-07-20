import os
import logging
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from bot.Bot import *

TOKEN = 'xoxb-2292519191940-2310009770128-BvZMNJrGv2a6JjNYsjVgS48a'
EVENT_TOKEN = '408c3fa28fda01f9eec533d6976d78a9'
CHANNEL = 'test'

app = Flask(__name__)
slackEventsAdapter = SlackEventAdapter(
    EVENT_TOKEN,
    '/slack/events/',
    app
)
slackClient = WebClient(TOKEN)

@slackEventsAdapter.on('message')
def listen(payload):
    event = payload.get('event', {})

    text = event.get('text')
    if '!read' in text.lower():
        bot = Bot(channel=CHANNEL)
        message = bot.getMessage()
        slackClient.chat_postMessage(**message)


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    app.run(host='46.101.20.226', port=3000)