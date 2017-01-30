from pprint import pprint
import telepot
import time
import random

str_list = ['dsafads', 'hfaids', 'ihjfds', 'dsaufhdsa', 'dsafgdsi', 'fhdka', 'fhkd', 'hksfds', 'uifidafjd']

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)

	if content_type == 'text':
		txt = 'schn' + str_list[random.randint(0,len(str_list))] + 'ider viadao'
		bot.sendMessage(chat_id, 'byron boiola 8===3')

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