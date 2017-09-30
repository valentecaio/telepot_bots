from pprint import pprint
import telepot
import time

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	pprint(msg)

	stickers = ['CAADAQAD-AIAAqzMpQiWbR28mG-ITwI', 'CAADAQAD3gIAAqzMpQj6CNyXfz9EEAI']

	send_sticker = False
	answer = ''

	if content_type == 'text':
		if 'que?' in msg['text']:
			answer = ['DEDE BICHA']
		elif 'maylan' in msg['text'] or 'Maylan' in msg['text']:
			answer = ['vai se fuder']
		elif 'max' in msg['text'] or 'Max' in msg['text']:
			answer = ['bem-vindo mlk, eu sou viadao']
		elif 'majeur' in msg['text']:
			answer = ['majeur maromba PUSHUP CHALLENGE']
		elif 'bomberman' in msg['text']:
			answer = ['eu sou o unico que nao evolui']
		elif 'portugal' in msg['text'] or 'Portugal' in msg['text']:
			answer = ['melhor país do mundo dps do BR']
		elif 'bicicleta' in msg['text'] or 'velo' in msg['text'] or 'bike' in msg['text']:
			answer = ['voce nao pode namo', 'ficar*', 'com o caio sem saber andar de bicicleta']
		elif 'alto' in msg['text']:
			answer = ['DEDE BICHA']
		elif 'esh' in msg['text'] or 'ESH' in msg['text']:
			answer = ['tirei 13 pq sou otario']
		elif 'yan' in msg['text'] or 'Yan' in msg['text']:
			answer = ['yan anda mais de bike que eu', 'mas nos compramos panelas juntos']
		elif 'vitoria' in msg['text'] or 'Vitoria' in msg['text'] or 'ES' in msg['text'] or 'espirito santo' in msg['text']:
			answer = ['prefiro o RJ, mas sou capixa']
		elif 'quanto?' in msg['text']:
			answer = ['o quanto o caio quiser']
		elif 'bot' in msg['text']:
			answer = ['sou gay mas nao sou bot']
		elif 'aniversario' in msg['text']:
			answer = ['valeu cara', 'me visitem em vitoria qndo voltarem', 'soiree chez moi', 'casa de dedé']
		elif 'chegou o dede' in msg['text'] or 'dede chegou' in msg['text']:
			answer = ['namoral vcs falam mt nesse grupo', 'resume ai pfvr']
		elif 'zangief' in msg['text'] or 'street fighter' in msg['text']:
			send_sticker = True
			answer = stickers[1]
		else:
			send_sticker = True
			answer = stickers[0]

		if not send_sticker:
			for a in answer:
				bot.sendMessage(chat_id, a, reply_to_message_id=msg['message_id'])

	else:
		send_sticker = True
		answer = stickers[1]

	if send_sticker:
		# sending sticker from existing sticker id
		bot.sendSticker(chat_id, answer, reply_to_message_id=msg['message_id'])

		# sending sticker from file
		# bot.sendSticker(chat_id, open("dede1.webp", 'rb'), reply_to_message_id=msg['message_id'])


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
