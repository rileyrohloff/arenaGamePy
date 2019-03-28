from random import randint






class BadGuy(object):


    health = 100
    HP = int(health)

class GoodGuy(object): 


    health = 100
    HP = int(health)


class Hero(GoodGuy):
    name = input(">> ")