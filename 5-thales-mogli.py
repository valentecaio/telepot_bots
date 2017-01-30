from pprint import pprint
import telepot
import time
import random

str_list = ['ola, eu sou um bot treinado para conversar com o mogli', 'ja sei o que pode te ajudar! da uma olhada nesse video: https://www.youtube.com/watch?v=S4J70C36RGU', 'thales mogliiii']
i = 0

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)

	pprint(msg)
	if content_type == 'text':
		if '/start' in msg['text']:
			txt = str_list[0]
		elif '?' in msg['text']:
			txt = str_list[1]
		else:
			txt = str_list[2]
		bot.sendMessage(chat_id, txt)

# instantiate bot
TOKEN = open('token_valentecaio2.txt', 'r').read()
bot = telepot.Bot(TOKEN)
pprint(bot.getMe())

# handling messages
bot.message_loop(handle)
pprint('Listening ...')

# hanging program execution
while True:
	time.sleep(10)