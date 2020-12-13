import random
import numpy as np
from rage.Building import Building



class Werehouse (Building):
    def info_werehouse(self):
        print ("Данные по складу: ")
        return '\n'

    def size_werehouse(self):
        werehouse_1 = 1
        length = np.empty(werehouse_1)
        width = np.empty(werehouse_1)
        for i in range(werehouse_1):
            length[i] = random.randint(1, 25)
            width[i] = random.randint(1, 25)
            print("Длинна помещения №1: ", length[i], " ширина помещения №1: ", width[i])
            print('Периметр:', length[i] * length[i])

        werehouse_2 = 1
        length = np.empty(werehouse_2)
        width = np.empty(werehouse_2)
        for i in range(werehouse_2):
            length[i] = random.randint(1, 25)
            width[i] = random.randint(1, 25)
            print("длинна помещения №2: ", length[i], " ширина помещения №2: ", width[i])
            print('Периметр:', length[i] * length[i])

        print('Общая площадь склада: ' + str(np.dot(length, width)))

        name = {1: 'Есин Максим Генрихович', 2: 'Ешков Жмых Алексеевич', 3: 'Жмышенко Валерий Альбертович'}
        print('Рабочие склада: ')
        for i in name:
            print(name[i])

        return '\n'
