from characters import Weapon, Combantant
import characters
from random import randint
from sys import exit



#environment Variables:
gladiator = Combantant()
gladiator.health= 100

glad2 = Combantant()
glad2.health = 100

rifle = Weapon()
rifle.DMG = randint(15,17)

machete = Weapon()
machete.DMG = randint(8,20)


class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #be sure to print out the last scene
        current_scene.enter()


class Scene(object):
     def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Death(Scene):
     
     quips = [
          "Wrong move...You died...",
          "You die of blunt force trauma"

     ] 
     def enter(self):
          print(Death.quips[randint(0,1)])
          exit(1)




class WeponChoice(Scene):
     def enter(self):

          print("""
          You're a gladitor in an Post-apocoliptic arena...You are up next to fight another gladiator.
          The guards surronding you take you to a armoury where you have to choose your weapon to fight with. Your choices are:
          
          Rifle -DMG (12-17)
          Machete - DMG (8-20)
          """)

          print("What weapon do you want to select to fight with?")
          chooseWeapon = input('>> ')

          if chooseWeapon == 'Rifle':
               print(f"You choose {chooseWeapon}. You're more of a ranged combantant I see...")
               return 'entrance'
          elif chooseWeapon == 'Machete':
               print(f"You choose {chooseWeapon}. Up, close and personal...")
               return 'entrance'
          else:
               print("That is not a valid selection. Please choose either Machete or AR-15 as your wepon choice")
               return 'weponChoice'
               


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
               print("The Arena Master knows you're not the typical junk that gets fed through here. He decides to procede on with the event")
               return 'combat'


          elif entranceChoice == 'Provoke':
               return 'death'
          else:
               print("WRONG ENTRY..")
               return 'entrance'




class OpponentEncounter(Scene):
     def enter(self):
          print("""
          The other side of the arena's bay doors open, and a huge, hulking goliath of a man walks out.
          He clearly doesn't shower regularly...
          
          With your weapon, you'll now have a face off with him...This will be a battle till the death...""")
          while glad2.health > 0:
               if glad2.health <= 0:
                              return 'finished'

               elif glad2.health > 0:
                         print("You can either attack or pass.. 'a' is for attack and 'p' is for pass. Choose wisely..")

                         combat_choice = input('a/p >> ')

                         if combat_choice == 'a':
                              print(f"You attack for {machete.DMG} damage! Enempy's health is now: ")
                              glad2.health -= machete.DMG
                              print(glad2.health)
                              
                         elif combat_choice == 'p':
                              print(f"Enemy attacks for {machete.DMG} damage! Your health is now: ")
                              gladiator.health -= machete.DMG
                              print(gladiator.health)
                              
               elif gladiator.health <= 0:
                    return 'death'
          while glad2.health < 0:
               return 'finish'
          
                    
                    

                    
          


class Victory(Scene):

     def enter(self):
          print("You won!")
          exit(1)

class Map(object):

    scenes = {
        'weponChoice' : WeponChoice(),
        'entrance' : AreanEntrance(),
        'death' : Death(),
        'finish': Victory(),
        'combat' : OpponentEncounter()
    }
    def __init__(self,start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)




f = Map('weponChoice')
fMap = Engine(f)
fMap.play()










