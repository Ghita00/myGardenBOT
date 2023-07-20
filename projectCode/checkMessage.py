def checkCreateGarden(message):
    message = message.split()
    return message[0] == "GIARDINO"

def checkWater(message):
    message = message.split()
    return message[0] == "OGGI"