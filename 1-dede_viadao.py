from pprint import pprint
import telepot
import time

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	pprint(msg)

	if content_type == 'text':
		answer = ''
		if 'que?' in msg['text']:
			answer = 'DEDE BICHA'
		elif 'maylan' in msg['text'] or 'Maylan' in msg['text']:
			answer = 'vai se fuder'
		elif 'max' in msg['text'] or 'Max' in msg['text']:
			answer = 'bem-vindo mlk, eu sou viadao'
		elif 'majeur' in msg['text']:
			answer = 'majeur maromba PUSHUP CHALLENGE'
		elif 'bomberman' in msg['text']:
			answer = 'eu sou o unico que nao evolui'
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
