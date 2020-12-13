from abc import ABC

class Building(ABC):

    def num_rooms(self):
        numRooms = 2
        print ("Колличесво комнат " + str(numRooms))
        return '\n'


    def people(self):
        people = 3
        print ("Колличество прживающих/работающих " + str(people))
        return '\n'



    def size_rooms(self):
        return '\n'







