from random import randint






class BadGuy(object):


    health = 100
    HP = int(health)

class GoodGuy(object): 


    health = 100
    HP = int(health)


class Hero(GoodGuy):
    pass

class Weapon(object):
    pass


class Machete(Weapon):
    DMG = randint(8,20)


class Rifile(Weapon):
    DMG = randint(12,15)


        