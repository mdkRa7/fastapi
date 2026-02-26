

from time import sleep
from datetime import datetime
class Player:

    @classmethod
    def change_for_holidey(cls):
        cls.__LVL = 10

    __LVL, __HEALTH = 1, 100
    __slots__ = ['__lvl', '__health', '__born']

    def __init__(self):
        self.__lvl = Player.__LVL
        self.__health = Player.__HEALTH
        self.__born = datetime.now()

    @property
    def lvl(self):
        return self.__lvl, f'{datetime.now()-self.__born}'

    @lvl.setter
    def lvl(self, param):
        self.__lvl += param

Player.change_for_holidey()
x = Player()
print(x.lvl)

Player.change_for_holidey()
y = Player()
print(y.lvl)
