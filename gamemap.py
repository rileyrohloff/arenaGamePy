from characters import Weapon, Hero
import characters
from random import randint
from sys import exit


def play():
     scene1 = WeponChoice()
     print(scene1)


class Scene(object):
     def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Death(Scene):
     
     quips = [
          "The Arena Master shoots you from his Box Stand...Dead",

     ] 
     def enter(self):
          print(Death.quips[1])




class WeponChoice(Scene):
     def enter(self):

          print("""
          You're a gladitor in an Post-apocoliptic arena...You are up next to fight another gladiator.
          The guards surronding you take you to a armoury where you have to choose your weapon to fight with. Your choices are:
          
          Rifile -DMG (12-17)
          Machete - DMG (8-20)
          """)

          print("What weapon do you want to select to fight with?")
          chooseWeapon = input('>> ')

          if chooseWeapon == 'Rifile':
               print(f"You choose {chooseWeapon}. You're more of a ranged combantant I see...")
               return AreanEntrance()
          elif chooseWeapon == 'Machete':
               print(f"You choose {chooseWeapon}. Up, close and personal...")
               return AreanEntrance()
          else:
               print("That is not a valid selection. Please choose either Machete or AR-15 as your wepon choice")
               return WeponChoice()
               


class AreanEntrance(Scene):
     def enter(self):
          print("""
          You are now being escorted to the arena! 
          You walk out into a massive, bloodsplattered sandpit. Surronded by hundreds of bloodthirsty scanvengers and bandits a like.
          They all want to see what you're made of!
          
          What looks like the Arena Master looks you up and down from the leaderbox. How do you want to respond? 
          
          Options:

          Stay silent and calm - 1
          
          Provoke - 2
          """)

          

          entranceChoice = input('>> ')

          if entranceChoice == 'Stay silent':
               print("The Arena Master know you're not the typical junk that gets fed through here. He decides to procede on with the event")

               return OpponentEncounter()
          elif entranceChoice == 'Provoke':
               return Death()




class OpponentEncounter(Scene):
     pass

class Combat(Scene):
     pass

class Victory(Scene):
     pass 


        


play()






