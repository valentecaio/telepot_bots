from pprint import pprint
import telepot
import time

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)

	if content_type == 'text':
		answer = ''
		if 'que?' in msg['text']:
			answer = 'DEDE BICHA'
		elif 'alto' in msg['text']:
			answer = 'DEDE BICHA'
		elif 'quanto?' in msg['text']:
			answer = 'o quanto o caio quiser'
		else:
			answer = 'dede viadao'
		bot.sendMessage(chat_id, answer)

# instantiate bot
TOKEN = open('token_valentecaio1.txt', 'r').read()
bot = telepot.Bot(TOKEN)
pprint(bot.getMe())

# handling messages
bot.message_loop(handle)
pprint('Listening ...')

# hanging program execution
while True:
	time.sleep(10)