""" this class allows to create the MacGyver character
    and of calculate the new coordinates of her destination """

# !/usr/bin/env python
# coding: utf-8

from classes.position import Position


class MacGyver(Position):
    """ this class allows to create the MacGyver character
    and of calculate the new coordinates of her destination """

    def __init__(self, x, y):
        Position.__init__(self, x, y)
        self.bag = []

    def move_to(self, destination):
        """ calculates the new coordinates after move to the "destination" :
                bottom, top, right or left of the screen
            In reception : receives a parameter "destination" as a direction :
                "bottom", "top", "right" or "left"
            In return    : return coordonates as a tuple  "(5, 8)" for example
        """
        coordinates = {"bottom": (self.x, self.y + 1),
                       "top": (self.x, self.y - 1),
                       "right": (self.x + 1, self.y),
                       "left": (self.x - 1, self.y)}
        return coordinates[destination]


if __name__ == "__main__":
    mcgyver = MacGyver(8, 8)
    print(mcgyver.move_to("bottom"))
    print("Le personnage de MacGyver possède les coordonnées : \
          ({}, {})".format(mcgyver.x, mcgyver.y))
