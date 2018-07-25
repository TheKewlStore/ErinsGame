from cocos.batch import BatchableNode
from pyglet import graphics, gl

import constants


class HealthBar(BatchableNode):
    def __init__(self, top_left, pokemon, height=15):
        """

        :param top_left:
        :type top_left: tuple[int, int]
        :param pokemon:
        :type pokemon: pokemon.Pokemon
        :param height:
        :type height: int
        """
        BatchableNode.__init__(self)
        self.x, self.y = top_left
        self.pokemon = pokemon
        self.max_width = 150
        self.height = height
        self.pokemon.push_handlers(self)

    def health_changed(self, pokemon):
        if self.pokemon == pokemon:
            print "{0} health changed to {1}!".format(pokemon.name, pokemon.get_current_health())
            self.draw()

    def pokemon_died(self, pokemon):
        if self.pokemon == pokemon:
            print "{0} died!".format(self.pokemon.name)
            self.draw()

    def draw(self):
        width = int(self.max_width * (self.pokemon.get_current_health() / float(self.pokemon.get_max_health())))
        vertex_list = graphics.vertex_list(4, 'v2f', 'c3b')
        full_bar = graphics.vertex_list(4, 'v2f', 'c3b')
        full_bar.vertices = [self.x, self.y,
                             self.x + self.max_width, self.y,
                             self.x + self.max_width, self.y + self.height,
                             self.x, self.y + self.height]
        full_bar.colors = [0, 0, 0,
                           0, 0, 0,
                           0, 0, 0,
                           0, 0, 0]
        vertex_list.vertices = [self.x, self.y,
                                self.x + width, self.y,
                                self.x + width, self.y + self.height,
                                self.x, self.y + self.height]
        vertex_list.colors = (constants.HEALTH_BAR_COLOR +
                              constants.HEALTH_BAR_COLOR +
                              constants.HEALTH_BAR_COLOR +
                              constants.HEALTH_BAR_COLOR)
        full_bar.draw(gl.GL_QUADS)
        vertex_list.draw(gl.GL_QUADS)
