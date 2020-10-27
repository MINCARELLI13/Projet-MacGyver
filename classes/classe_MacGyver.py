#!/usr/bin/env python
# coding: utf-8

from classes.classe_Position import Position

class MacGyver(Position):

    def __init__(self, x, y):
        Position.__init__(self, x, y)
        self.x = x
        self.y = y
    
    def move_to (self, destination):
        """ calculates the new coordinates after move to bottom, top, right or left of the screen """
        coordinates = {"bottom": (self.x, self.y + 1), "top": (self.x, self.y - 1), "right": (self.x + 1, self.y), "left": (self.x - 1, self.y)}
        return coordinates[destination]
    
if __name__ == "__main__":
    mcgyver = MacGyver(8, 8)
    print("Le personnage de MacGyver possède les coordonnées : ({}, {})".format(mcgyver.x, mcgyver.y))

    
