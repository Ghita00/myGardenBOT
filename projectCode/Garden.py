from Plant import *
class Garden:
    name = ""
    plants = []

    def __init__(self, gardenSTR):
        self.name = gardenSTR[0].split()[1]
        for i in range(1, len(gardenSTR)):
            self.plants.append(Plant(gardenSTR[i]))