import telebot
from trans import to_cyrillic, to_latin 
TOKEN = "8625172188:AAH_cHuKFci8lh7jESo_o0bKxrATBfcAusA"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	text = message.text
	if text.isascii():
		bot.reply_to(message, to_cyrillic(text))
	else:
		bot.reply_to(message, to_latin(text))

bot.infinity_polling()