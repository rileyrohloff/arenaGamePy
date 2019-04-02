from random import randint

class Combantant(object):
    def __init__(self):

        health = int(100)




class Hero(Combantant):
    def __init__(self):
        pass

class Opponent(Combantant):
    def __init__(self):
        health = 100
        


class Weapon(object):
    pass



    DMG = randint(8,20)

Rifle = Weapon()
Rifle.DMG = randint(12,17)

Machete = Weapon()
Machete.DMG = randint(8,20)



        