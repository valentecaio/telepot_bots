from pprint import pprint
import telepot
import time
from telepot import namedtuple

# to show inline keyboard
def on_chat_message_inline(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)

	button1 = namedtuple.InlineKeyboardButton(text='inline button', callback_data='press')
	button2 = namedtuple.InlineKeyboardButton(text='inline button 2', callback_data='press')
	keyboard1 = namedtuple.InlineKeyboardMarkup(inline_keyboard=[[button1], ])

	if content_type == 'text':
		answer = 'answer'
		bot.sendMessage(chat_id, answer, reply_markup=keyboard1)

# to show custom keyboard
def on_chat_message_custom(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)

	button2 = namedtuple.KeyboardButton(text='normal button')
	button3 = namedtuple.KeyboardButton(text='normal button 2')
	keyboard2 = namedtuple.ReplyKeyboardMarkup(keyboard=[[button2, button3], ])

	if content_type == 'text':
		answer = 'answer'
		bot.sendMessage(chat_id, answer, reply_markup=keyboard2)

# to answer inline buttons
def on_callback_query(msg):
	query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
	#content_type, chat_type, chat_id = telepot.glance(msg)
	print('Callback Query:', query_id, from_id, query_data)
	#bot.sendMessage(query_id, 'got it!')
	bot.answerCallbackQuery(query_id, text=query_id)

# instantiate bot
TOKEN = open('token_valentecaio2.txt', 'r').read()
bot = telepot.Bot(TOKEN)
pprint(bot.getMe())

# handling messages
bot.message_loop({'chat': on_chat_message_custom,'callback_query': on_callback_query})
pprint('Listening ...')

# hanging program execution
while True:
	time.sleep(10)
