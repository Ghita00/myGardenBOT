# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from credential import *
from Garden import *
from checkMessage import *
bot = telebot.TeleBot(API_TOKEN)

'''
Command to implement
- Create Garden -> /creaGiardino ok
- Update water -> /annaffiaOggi
- Last day water -> /acquaIeri
- Report water last week -> /reportIdrico
ADD TO LIST
- Check Garden -> /giardino ok
'''

global myGarden
myGarden = None

######## UTILS ########
#TODO remove these method with call at DB
def checkMyGarden():
    return myGarden != None

def updateGarden(newGarden):
    global myGarden
    myGarden = newGarden

######### COMMAND BY / #########

# Handle '/help'
@bot.message_handler(commands=['help'])
def helpCommand(message):
    bot.reply_to(message, """I comandi offerti sono:\n/creaGiardino -> crea un tuo giardino.\n/annaffiaOggi -> aggiorna la fornitura d'acqua concessa oggi.\n/acquaIeri -> fornisce un prospetto di quali piante hanno ricevuto l'acqua ieri.\n/reportIdrico -> fornisce un prospetto rispetto alla fornitura d'acqua nell'ultima settimana.
    """)

# Handle '/start'
@bot.message_handler(commands=['start'])
def welcomeCommand(message):
    bot.reply_to(message, """Ciao, sono MyGardenBOT e mi occupo di aiutarti con il tuo giardino :).\nCrea il tuo giardino con il comando /creaGiardino.\nPer tutti visualizzare tutti i comandi utilizza il comando /help""")

# Handle '/creaGiardino'
@bot.message_handler(commands=['creaGiardino'])
def createGardenCommand(message):
    if(checkMyGarden()):
        bot.reply_to(message, "Nel mio sistema è già presente un giardino registrato")
    else:
        bot.reply_to(message, "Bene, scrivi pure un messaggio GIARDINO <nome> seguito da un elenco puntato seguendo questa struttura:\n- <quantità> <pianta>\nUn esempio è il seguente:\nGIARDINO balcone:\n- 1 salvia\n- 1 rosmarino")

@bot.message_handler(commands=['giardino'])
def welcomeCommand(message):
    print(myGarden)
    if (checkMyGarden()):
        str = "Giardino " + myGarden.name + '\n'
        for plant in myGarden.plants:
            str = str + "- " + plant.name + " " + plant.quantity + "\n"
        bot.reply_to(message, str)
    else:
        bot.reply_to(message,"Nel mio sistema non è presente nessun giarino registrato")

@bot.message_handler(commands=['acquaIeri'])
def welcomeCommand(message):
    print(myGarden)
    if (checkMyGarden()):
        str = "Giardino " + myGarden.name + '\n'
        for plant in myGarden.plants:
            str = str + "- " + plant.name + " " + plant.quantity + "\n"
        bot.reply_to(message, str)
    else:
        bot.reply_to(message,"Nel mio sistema non è presente nessun giarino registrato")

######### COMMAND BY MESSAGE #########

# Creating Garden...
@bot.message_handler(func=lambda message: checkCreateGarden(message.text))
def storangeGarden(message):
    if (checkMyGarden()):
        bot.reply_to(message, "Nel mio sistema è già presente un giardino registrato")
    else:
        bot.reply_to(message,"Registrazione...")
        editMessage = message.text
        editMessage = editMessage.split('\n')

        updateGarden(Garden(editMessage))
        bot.reply_to(message, "Registrazione completata")

bot.infinity_polling()
