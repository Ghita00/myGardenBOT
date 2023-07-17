class Plant:
    name = ""
    quantity = 0

    def __init__(self, plantSTR):
        plantSTR = plantSTR.split()
        self.name = plantSTR[1]
        self.quantity = plantSTR[2]