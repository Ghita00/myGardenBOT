# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

##### IMPORT PYTHON #####
import telebot
import datetime

##### IMPORT MY FILE #####
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

######## GLOBAL VARIABLES #######
global myGarden
global weekWater
myGarden = None
weekWater = []

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
        bot.reply_to(message, "Bene, scrivi pure un messaggio GIARDINO <nome> seguito da un elenco puntato seguendo questa struttura:\n- <quantità> <pianta>\nUn esempio è il seguente:\nGIARDINO balcone\n- 1 salvia\n- 1 rosmarino")

@bot.message_handler(commands=['giardino'])
def welcomeCommand(message):
    if (checkMyGarden()):
        str = "Giardino " + myGarden.name + '\n'
        for plant in myGarden.plants:
            str = str + "- " + plant.name + " " + plant.quantity + "\n"
        bot.reply_to(message, str)
    else:
        bot.reply_to(message,"Nel mio sistema non è presente nessun giardino registrato")

@bot.message_handler(commands=['acquaIeri'])
def lastDayWatherCommand(message):

    yesterday = weekWater[(len(weekWater)-1)]
    yesterday = yesterday.split('\n ')
    text = "Annaffiate ieri:\n"
    for i in range(1, len(yesterday)):
        text += "- " + yesterday[i] + "\n"
    bot.reply_to(message, text)

@bot.message_handler(commands=['annaffiaOggi'])
def todayWatherCommand(message):
    if checkMyGarden() :
        bot.reply_to(message, "Bene, scrivi pure un messaggio OGGI seguito da un elenco puntato seguendo questa struttura:\n- <pianta>\nUn esempio è il seguente:\nOGGI\n- salvia\n- rosmarino")
    else:
        bot.reply_to(message, "Nel mio sistema non è presente nessun giarino registrato. Creane uno subito con il comando \creaGiardino")
@bot.message_handler(commands=['reportIdrico'])
def reportWatherCommand(message):
    print(weekWater)
    bot.reply_to(message, "wip")


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

@bot.message_handler(func=lambda message: checkWater(message.text))
def storangeWater(message):
    if (checkMyGarden()):
        bot.reply_to(message, "Registrazione...")
        now = datetime.datetime.now()

        water = "" + now.strftime("%m/%d/%Y, %H:%M:%S") + "\n"
        text = message.text.split('-')
        for i in range(1, len(text)):
            water += text[i]

        print(water)

        if(len(weekWater) == 6):
            weekWater.pop()
        weekWater.append(water)

        bot.reply_to(message, "Registrazione completata")
    else:
        bot.reply_to(message, "el mio sistema non è presente nessun giarino registrato. Creane uno subito con il comando \creaGiardino")


bot.infinity_polling()
