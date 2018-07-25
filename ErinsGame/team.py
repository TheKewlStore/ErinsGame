from cocos.layer import Layer

import constants

from cocos.actions import MoveTo, CallFunc, CallFuncS


class Team(Layer):
    def __init__(self, *pokemon):
        Layer.__init__(self)
        self.pokemon = list(pokemon)
        self.orientation = constants.NO_ORIENTATION
        self.remove_sprite = CallFuncS(self._remove_sprite)
        self.add_sprite = CallFuncS(self._add_sprite)
        self.current_battle = None
        """ :type: battle.DoubleBattleLayer"""

    def add_to_battle(self, battle):
        """

        :param battle:
        :type battle: battle.DoubleBattleLayer
        :return:
        """
        self.current_battle = battle

    def set_orientation(self, orientation):
        self.orientation = orientation

        if orientation == constants.BACK_FACING:
            self.pokemon[0].get_sprite_for_orientation(orientation).position = constants.BACK_FACING_POSITION_LEFT
            self.pokemon[1].get_sprite_for_orientation(orientation).position = constants.BACK_FACING_POSITION_RIGHT
        else:
            self.pokemon[0].get_sprite_for_orientation(orientation).position = constants.FRONT_FACING_POSITION_LEFT
            self.pokemon[1].get_sprite_for_orientation(orientation).position = constants.FRONT_FACING_POSITION_RIGHT

        for sprite in self.get_active_sprites():
            self.add(sprite)

    def get_team_sprites(self):
        sprites = []

        for pokemon in self.pokemon:
            sprites.append(pokemon.get_front_sprite())

        return sprites

    def get_active_sprites(self):
        """

        :return:
        :rtype: list[cocos.sprite.Sprite]
        """
        return (self.pokemon[0].get_sprite_for_orientation(self.orientation),
                self.pokemon[1].get_sprite_for_orientation(self.orientation))

    def get_first_pokemon(self):
        """

        :return:
        :rtype: pokemon.Pokemon
        """
        return self.pokemon[0]

    def get_second_pokemon(self):
        """

        :return:
        :rtype: pokemon.Pokemon
        """
        return self.pokemon[1]

    def switch_pokemon(self, source_index, target_index):
        if not self.current_battle:
            raise RuntimeError("Trying to switch active pokemon when there is no battle active!")
        elif self.current_battle.animation_locked:
            return

        source_pokemon = self.pokemon[source_index]
        source_sprite = source_pokemon.get_sprite_for_orientation(self.orientation)
        destination_pokemon = self.pokemon[target_index]
        destination_sprite = destination_pokemon.get_sprite_for_orientation(self.orientation)
        original_position = source_sprite.position

        if self.orientation == constants.BACK_FACING:
            switch_out = MoveTo((0, 0), duration=0.25)
        else:
            destination_sprite.position = (640, 480)
            switch_out = MoveTo((640, 480), duration=0.25)

        def switch_in():
            destination_sprite.do(self.add_sprite +
                                  MoveTo(original_position, duration=0.25) +
                                  self.current_battle.toggle_animation_lock)

        switch_in = CallFunc(switch_in)

        source_sprite.do(switch_out + self.remove_sprite + switch_in)
        self.current_battle.enable_animation_lock()
        self.pokemon[target_index] = source_pokemon
        self.pokemon[source_index] = destination_pokemon
        self.current_battle.hud.update_health_bars()

    def switch_first(self, index):
        return self.switch_pokemon(0, index)

    def switch_second(self, index):
        return self.switch_pokemon(1, index)

    def attack(self, my_pokemon, opponent_pokemon):
        """

        :param my_pokemon:
        :type my_pokemon: pokemon.Pokemon
        :param opponent_pokemon:
        :type opponent_pokemon: pokemon.Pokemon
        :return:
        """
        if not self.current_battle:
            raise RuntimeError("Trying to attack pokemon when there is no battle active!")
        elif self.current_battle.animation_locked:
            return

        opponent_pokemon.decrement_current_health(my_pokemon.get_damage_to_target(opponent_pokemon))

        my_sprite = my_pokemon.get_sprite_for_orientation(self.orientation)
        opponent_sprite = opponent_pokemon.get_sprite_for_orientation(constants.opposite_orientation(self.orientation))

        original_position = my_sprite.position
        attack = MoveTo(opponent_sprite.position, duration=0.3)
        move_back = MoveTo(original_position, duration=0.25)
        my_sprite.do(attack +
                     move_back +
                     self.current_battle.toggle_animation_lock)

        self.current_battle.enable_animation_lock()

    def attack_with_first(self, target_pokemon):
        """

        :param target_pokemon:
        :type target_pokemon: pokemon.Pokemon
        :return:
        """
        self.attack(self.pokemon[0], target_pokemon)

    def attack_with_second(self, target_pokemon):
        self.attack(self.pokemon[1], target_pokemon)

    def _remove_sprite(self, sprite):
        self.remove(sprite)

    def _add_sprite(self, sprite):
        self.add(sprite)
