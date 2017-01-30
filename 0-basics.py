from pprint import pprint
import telepot
import time

def handle(msg):
	pprint(msg)

# instantiate bot
TOKEN = open('token_valentecaio2.txt', 'r').read()
bot = telepot.Bot(TOKEN)
pprint(bot.getMe())

# get messages
response = bot.getUpdates()
pprint(response)

# handling messages
bot.message_loop(handle)
pprint('Listening ...')

# sending messages
bot.sendMessage(145083564, 'coe lekao bonito')

# hanging program execution

while True:
	time.sleep(2)

# message example	
'''
>>> from pprint import pprint
>>> response = bot.getUpdates()
>>> pprint(response)
[{'message': {'chat': {'first_name': 'Nick',
                       'id': 999999999,
                       'type': 'private'},
              'date': 1465283242,
              'from': {'first_name': 'Nick', 'id': 999999999},
              'message_id': 10772,
              'text': 'Hello'},
  'update_id': 100000000}]
'''