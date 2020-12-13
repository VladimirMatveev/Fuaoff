import random
import numpy as np
from rage.Building import Building



class Rezidential (Building):
    def info_rezidential_(self):
        print ("Данные по квартире: ")
        return '\n'

    def size_residential(self):
        werehouse_1 = 1
        length = np.empty(werehouse_1)
        width = np.empty(werehouse_1)
        for i in range(werehouse_1):
            length[i] = random.randint(1, 10)
            width[i] = random.randint(1, 10)
            print("Длинна кухни: ", length[i], " ширина кухни: ", width[i])
            print('Периметр:', length[i] * length[i])

        werehouse_2 = 1
        length = np.empty(werehouse_2)
        width = np.empty(werehouse_2)
        for i in range(werehouse_2):
            length[i] = random.randint(1, 10)
            width[i] = random.randint(1, 10)
            print("длинна гостинной: ", length[i], " ширина гостинной: ", width[i])
            print('Периметр:', length[i] * length[i])

        print('Общая площадь квартры: ' + str(np.dot(length, width)))

        return '\n'
