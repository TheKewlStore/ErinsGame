from cocos.layer import Layer

import constants
from graphics.health_bar import HealthBar


class BattleHUD(Layer):
    def __init__(self, battle):
        """

        :param battle:
        :type battle: battle.DoubleBattleLayer
        """
        Layer.__init__(self)

        self.battle = battle
        self.back_left_health = None
        self.back_right_health = None
        self.front_left_health = None
        self.front_right_health = None

        self.update_health_bars()

    def update_health_bars(self):
        if self.back_left_health:
            self.remove(self.back_left_health)
        if self.back_right_health:
            self.remove(self.back_right_health)
        if self.front_right_health:
            self.remove(self.front_right_health)
        if self.front_left_health:
            self.remove(self.front_left_health)

        back_left_pokemon = self.battle.back_team.get_first_pokemon()
        back_right_pokemon = self.battle.back_team.get_second_pokemon()
        front_left_pokemon = self.battle.front_team.get_first_pokemon()
        front_right_pokemon = self.battle.front_team.get_second_pokemon()

        self.back_left_health = HealthBar(constants.BACK_LEFT_HEALTH_BAR, back_left_pokemon)
        self.back_right_health = HealthBar(constants.BACK_RIGHT_HEALTH_BAR, back_right_pokemon)
        self.front_left_health = HealthBar(constants.FRONT_LEFT_HEALTH_BAR, front_left_pokemon)
        self.front_right_health = HealthBar(constants.FRONT_RIGHT_HEALTH_BAR, front_right_pokemon)

        self.add(self.back_left_health)
        self.add(self.back_right_health)
        self.add(self.front_left_health)
        self.add(self.front_right_health)
