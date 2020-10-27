#!/usr/bin/env python
# coding: utf-8
import os
from random import randint

from classes.classe_MacGyver import MacGyver
from classes.classe_Guardian import Guardian

print()

class Maze():

    OBJECTS = ["needle", "tube", "ether"]

    def __init__(self):
        self._initialisation()
        self.parse_txt_in_coord()   # creates grid and path of the maze
        self.create_objects()       # creates the objects to find and put them in the grid
    
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
                    x += 1
                y += 1              # at each new line "y" increases by 1
        finally:
            text.close()

    def create_objects(self):
        """ calculates the coordinates of each objects to find and put them in the grid """        
        for object in self.OBJECTS:                         # for each object to find
            coords =self.path[randint(0, len(self.path)-1)]    # takes coordinates among those of path
            while self.grid[coords] in self.OBJECTS:        # avoid to take coordinates already used by another object
                coords = self.path[randint(0, len(self.path)-1)]
            self.grid[coords] = object                      # if all is ok, positionnes the object in the grid

    def _initialisation(self):
        self.grid = {}      # contains all the coordinates of wall, path, MacGyver, guardian and objects to find
        self.path = []      # contains all the coordinates of path
        self.macgyver = MacGyver(5, 5)      # creates MacGyver's character
        self.guardian = Guardian(7, 7)      # creates Guardian's character
        self.objects_coord = {}

    def test_destination_is_valid(self, x_new, y_new):
        """ testes if the MacGyver's destination is a not wall or out of the maze
            in this case return "True"
        """
        if (0<= x_new <= 14) and (0<= y_new <= 14):     # if destination is in the maze = "True"
            return (self.grid[(x_new, y_new)] != "w")   # if destination is not a wall = "True"
        else:
            return False                                # else "False"


if __name__ == "__main__":
    maze = Maze()
    print(maze.grid)

 