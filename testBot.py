from bot.Bot import *
from slack import WebClient

TOKEN = 'xoxb-2292519191940-2310009770128-U2Zas1hmt1O70cObjiygQOP9'
CHANNEL = 'test'

slackClient = WebClient(TOKEN)

bot = Bot(channel=CHANNEL)
message = bot.getMessage()
print(message)

slackClient.chat_postMessage(**message)