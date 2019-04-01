from characters import Rifile


class Scene(object):
     pass

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
     pass


class OpponentEncounter(Scene):
     pass

class Combat(Scene):
     pass

class Death(Scene):
     pass

class Victory(Scene):
     pass 


        

     


# f = WeponChoice()
# f.enter()

# gun = Rifile()
# print(gun.DMG)