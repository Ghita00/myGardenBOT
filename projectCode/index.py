# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from credential import *

bot = telebot.TeleBot(API_TOKEN)



'''
Command to implement
- Create Garden -> /creaGiardino 
- Update water -> /annaffiaOggi
- Last day water -> /acquaIeri
- Report water last week -> /reportIdrico
'''

# Handle '/help'
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, """I comandi offerti sono:\n/creaGiardino -> crea un tuo giardino.\n/annaffiaOggi -> aggiorna la fornitura d'acqua concessa oggi.\n/acquaIeri -> fornisce un prospetto di quali piante hanno ricevuto l'acqua ieri.\n/reportIdrico -> fornisce un prospetto rispetto alla fornitura d'acqua nell'ultima settimana.
    """)

# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """Ciao, sono MyGardenBOT e mi occupo di aiutarti con il tuo giardino :).\nCrea il tuo giardino con il comando /creaGiardino.\nPer tutti visualizzare tutti i comandi utilizza il comando /help""")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "test della risposta")

bot.infinity_polling()
