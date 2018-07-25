import pyglet
import constants
import resource

from cocos.sprite import Sprite
from pokedex import pokedex


class Pokemon(pyglet.event.EventDispatcher):
    def __init__(self):
        pyglet.event.EventDispatcher.__init__(self)

        self.name = None
        self.stats = None
        self.current_health = None

    @classmethod
    def create(cls, name, stats):
        self = cls()

        self.name = name
        self.stats = stats
        self.current_health = self.stats["hp"]

        animation = pyglet.image.load_animation(
            resource.load_resource(name.lower() + ".gif", "PokemonSprites/Front/Regular"))

        for frame in animation.frames:
            frame.duration = 0.03  # (1/60)

        self.front_sprite = Sprite(animation)

        animation = pyglet.image.load_animation(
            resource.load_resource(name.lower() + ".gif", "PokemonSprites/Back/Regular"))

        for frame in animation.frames:
            frame.duration = 0.03  # (1/60)

        self.back_sprite = Sprite(animation)

        return self

    @classmethod
    def from_dex(cls, name):
        stats = pokedex[name.lower()]["base_stats"]
        return cls.create(name, stats)

    def get_current_health(self):
        return self.current_health

    def get_max_health(self):
        return self.stats["hp"]

    def get_damage_to_target(self, target):
        return 15

    def decrement_current_health(self, amount):
        self.current_health -= amount

        if self.current_health <= 0:
            self.current_health = 0
            self.dispatch_event("pokemon_died", self)
        else:
            self.dispatch_event("health_changed", self)

    def set_current_health(self, new_health):
        self.current_health = new_health
        self.dispatch_event("health_changed", self)

        if new_health == 0:
            self.dispatch_event("pokemon_died", self)

    def get_sprite_for_orientation(self, orientation):
        if orientation == constants.FRONT_FACING:
            return self.get_front_sprite()
        elif orientation == constants.BACK_FACING:
            return self.get_back_sprite()
        else:
            return RuntimeError("Invalid orientation for get_sprite_for_orientation()")

    def get_front_sprite(self):
        return self.front_sprite

    def get_back_sprite(self):
        return self.back_sprite


Pokemon.register_event_type("health_changed")
Pokemon.register_event_type("pokemon_died")
