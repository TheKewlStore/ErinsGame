import pyglet
from cocos.actions import CallFunc
from cocos.layer import Layer
from cocos.sprite import Sprite

import constants
import resource
from hud import BattleHUD


class DoubleBattleLayer(Layer):
    is_event_handler = True

    def __init__(self, back_team, front_team, location):
        """

        :param back_team:
        :type back_team: team.Team
        :param front_team:
        :type front_team: team.Team
        :param location:
        :type location: str
        """
        Layer.__init__(self)

        self.background_image = Sprite(pyglet.image.load(
            resource.load_resource("bg-" + location + ".jpg", "BattleBackgrounds")),
            position=(640/2, 480/2), scale=0.8)
        self.add(self.background_image)

        self.back_team = back_team
        self.front_team = front_team

        self.back_team.set_orientation(constants.BACK_FACING)
        self.front_team.set_orientation(constants.FRONT_FACING)

        self.back_team.add_to_battle(self)
        self.front_team.add_to_battle(self)

        self.add(self.front_team)
        self.add(self.back_team)

        self.animation_locked = False
        self.toggle_animation_lock = CallFunc(self._toggle_animation_lock)
        self.hud = BattleHUD(self)
        self.add(self.hud)

    def enable_animation_lock(self):
        self.animation_locked = True

    def _toggle_animation_lock(self):
        self.animation_locked = not self.animation_locked

    def on_key_press(self, key, modifiers):
        if self.animation_locked:
            return

        if key == pyglet.window.key.Q:
            self.back_team.switch_first(2)
        elif key == pyglet.window.key.W:
            self.back_team.switch_second(2)
        elif key == pyglet.window.key.E:
            self.front_team.switch_first(2)
        elif key == pyglet.window.key.R:
            self.front_team.switch_second(2)
        elif key == pyglet.window.key.T:
            self.back_team.attack_with_first(self.front_team.get_first_pokemon())
        elif key == pyglet.window.key.Y:
            self.back_team.attack_with_first(self.front_team.get_second_pokemon())
        elif key == pyglet.window.key.U:
            self.back_team.attack_with_second(self.front_team.get_first_pokemon())
        elif key == pyglet.window.key.I:
            self.back_team.attack_with_second(self.front_team.get_second_pokemon())
        elif key == pyglet.window.key.O:
            self.front_team.attack_with_first(self.back_team.get_first_pokemon())
        elif key == pyglet.window.key.P:
            self.front_team.attack_with_first(self.back_team.get_second_pokemon())
        elif key == pyglet.window.key.BRACKETLEFT:
            self.front_team.attack_with_second(self.back_team.get_first_pokemon())
        elif key == pyglet.window.key.BRACKETRIGHT:
            self.front_team.attack_with_second(self.back_team.get_second_pokemon())
        else:
            self.animation_locked = False

    def on_key_release(self, key, modifiers):
        pass
