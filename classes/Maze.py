#!/usr/bin/env python
# coding: utf-8
import os
from random import randint

from MacGyver import MacGyver
from Guardian import Guardian
from MacGyverGame import Game
from config import OBJECTS

print()

class Maze():

    def __init__(self):
        self._initialisation()
        self.parse_txt_in_coord()   # creates grid and path of the maze
        self.create_objects()       # creates the objects to find and put them in the grid
        self.game = Game(self.grid) # construction of the maze with pygame
    
    def parse_txt_in_coord(self):
        """
            Creates the maze (grid and path) by translating the "maze.txt" file created previously case by case.
        """
        os.chdir("c:/Users/utilisateur/Desktop/Formation_OpenClassRoom/Projet_3/Projet")
        text = open("maze.txt")

        y = 0
        try:
            for ligne in text.readlines():
                x = 0               # each time a new line is read, x is reset to zero
                for lett in ligne:              # each coordinate corresponds to a "wall" ("w") or to a "path" ("O") ...
                    if lett in ["w", "O", "M", "G"]:    # to verify that grid loads only items of the maze
                        self.grid[(x, y)] = lett
                    if lett == "O":
                        self.path.append((x, y))
                    elif lett == "M":
                        self.macgyver.x = x
                        self.macgyver.y = y
                    elif lett == "G":
                        self.guardian.x = x
                        self.guardian.y = y
                    x += 1
                y += 1              # at each new line "y" increases by 1
        finally:
            text.close()

    def create_objects(self):
        """ calculates the coordinates of each object and put them in the grid """        
        for object in OBJECTS:                         # for each object to find
            coords =self.path[randint(0, len(self.path)-1)]    # takes coordinates among those of path
            while self.grid[coords] in OBJECTS:        # avoid to take coordinates already used by another object
                coords = self.path[randint(0, len(self.path)-1)]
            self.grid[coords] = object                 # if all is ok, positionnes the object in the grid

    def test_destination_is_valid(self, x_new, y_new):
        """ testes if the MacGyver's destination is a not wall or out of the maze
            in this case return "True"
        """
        if (0<= x_new <= 14) and (0<= y_new <= 14):     # if destination is in the maze = "True"
            return (self.grid[(x_new, y_new)] != "w")   # if destination is not a wall = "True"
        else:
            return False                                # else "False"

    def test_presence_object(self, x_new, y_new):
        """ tests the presence of object on the destination coordinates (x_new, y_new) """
        return self.grid[x_new, y_new] in OBJECTS

    def collect_of_object(self):
        """ picks up object on the destination cell and up date the grid with "O" """
        self.macgyver.bag.append(self.grid[self.macgyver.x, self.macgyver.y])   # puts the object finded in the bag
        self.grid[self.macgyver.x, self.macgyver.y] = "O"                       # and up date the grid with "O" like path :)

    def test_presence_of_guardian(self, x_new, y_new):
        return (x_new == self.guardian.x) and (y_new == self.guardian.y)

    def _initialisation(self):
        self.grid = {}      # contains all the coordinates of wall, path, MacGyver, guardian and objects to find
        self.path = []      # contains all the coordinates of path
        self.macgyver = MacGyver(0, 0)      # creates MacGyver's character
        self.guardian = Guardian(0, 0)      # creates Guardian's character


if __name__ == "__main__":
    maze = Maze()
    print(maze.grid)

 