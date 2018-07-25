from cocos import scene

from cocos.director import director
from cocos.menu import Menu, MenuItem, shake, shake_back, CENTER, RIGHT, LEFT, TOP, BOTTOM
from cocos.scenes import FadeTRTransition
from pyglet.event import EventDispatcher

import constants
from battle import DoubleBattleLayer
from pokemon import Pokemon
from team import Team


class MainMenu(Menu):
    is_event_handler = True

    def __init__(self):
        Menu.__init__(self, title="Main Menu")

        self.menu_valign = CENTER
        self.menu_halign = CENTER

        items = [MenuItem("Demo", self.start_demo),
                 ]

        self.player_team = Team(Pokemon.from_dex("Lycanroc-Dusk"),
                                Pokemon.from_dex("Aegislash-Shield"),
                                Pokemon.from_dex("Aegislash-Blade"))
        self.enemy_team = Team(Pokemon.from_dex("Charizard-Mega-Y"),
                               Pokemon.from_dex("Amoonguss"),
                               Pokemon.from_dex("Charizard-Mega-X"))

        self.player_team.set_orientation(constants.BACK_FACING)
        self.enemy_team.set_orientation(constants.FRONT_FACING)

        self.battle_layer = DoubleBattleLayer(self.player_team, self.enemy_team, "darkbeach")

        self.create_menu(items, shake(), shake_back())

    def start_demo(self):
        game_scene = scene.Scene(self.battle_layer)
        director.replace(FadeTRTransition(game_scene, duration=.5))


class EventManager(EventDispatcher):
    pass


if __name__ == "__main__":
    window = director.init()
    director.show_FPS = True
    my_scene = scene.Scene(MainMenu())
    director.run(my_scene)
