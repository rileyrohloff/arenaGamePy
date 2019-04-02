from characters import Weapon, Hero
import characters
from random import randint
from sys import exit

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
        print("This is the parent class")
 


class WeponChoice(Scene):
    def enter(self):
        print("test")
        return 'entrance'


class AreanEntrance(Scene):
     def enter(self):
         print(self)

class Map(object):

    scenes = {
        'weponChoice' : WeponChoice(),
        'entrance' : AreanEntrance()
    
    }
    def __init__(self,start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)
    

a_map = Map('weponChoice')
a_game = Engine(a_map)
a_game.play()