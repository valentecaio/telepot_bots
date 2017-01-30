from pprint import pprint
import telepot
import time

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)

	if content_type == 'text':
		snake = u'\U0001F40D'
		heart = u'\U00002764'
		dog = u'\U0001F436'
		answer = snake + heart + dog
		bot.sendMessage(chat_id, answer)

# instantiate bot
TOKEN = open('token_jamilinda.txt', 'r').read()
bot = telepot.Bot(TOKEN)
pprint(bot.getMe())

# handling messages
bot.message_loop(handle)
pprint('Listening ...')

# hanging program execution
while True:
	time.sleep(10)