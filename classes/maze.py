""" This class manages the back office of the game :
    building of the maze, creation of characters
    and of objects to find
"""

# !/usr/bin/env python
# coding: utf-8
import os
from random import randint

from classes.macgyver import MacGyver
from classes.guardian import Guardian
from classes.config import OBJECTS

print()


class Maze():
    """ This class manages the back office of the game :
        building of the maze, creation of characters
        and of objects to find
    """

    def __init__(self):
        self._initialisation()
        # creates grid and path of the maze
        self.parse_txt_in_coord()
        # creates the objects to find and put them in the grid
        self.create_objects()

    def parse_txt_in_coord(self):
        """
            Creates the maze (grid and path) by translating
            the "maze.txt" file created previously case by case
        """
        os.chdir("c:/Users/utilisateur/Desktop/"
                 "Formation_OpenClassRoom/Projet_3/Projet")
        text = open("maze.txt")

        # number of line of the file "maze.txt"
        line_maze_txt = 0
        try:
            for ligne in text.readlines():
                # number of column of the file "maze.txt"
                # each time a new line is read, x is reset to zero
                column_maze_txt = 0
                # each coordinate corresponds to a "wall" ("w")
                # or to a "path" ("O") or the Guardian ("G") ...
                for lett in ligne:
                    # to verify that grid loads only items of the maze
                    if lett in ["w", "O", "M", "G"]:
                        self.grid[(column_maze_txt, line_maze_txt)] = lett
                    if lett == "O":
                        self.path.append((column_maze_txt, line_maze_txt))
                    elif lett == "M":
                        self.macgyver.x = column_maze_txt
                        self.macgyver.y = line_maze_txt
                    elif lett == "G":
                        self.guardian.x = column_maze_txt
                        self.guardian.y = line_maze_txt
                    column_maze_txt += 1
                # at each time a new line is complitly read,
                # "line_maze_txt" is increased of one
                line_maze_txt += 1
        finally:
            text.close()

    def create_objects(self):
        """ calculates the coordinates of each object
            and put them in the grid
        """
        # for each object to find
        for object_name in OBJECTS:
            # takes coordinates among those of path
            coords = self.path[randint(0, len(self.path) - 1)]
            # to avoid to take coordinates already used by another object
            while self.grid[coords] in OBJECTS:
                coords = self.path[randint(0, len(self.path) - 1)]
            # if all is ok, positionnes the object in the grid
            self.grid[coords] = object_name

    def test_destination_is_valid(self, x_new, y_new):
        """ testes if the MacGyver's destination is not a wall or out of the maze
            In reception : receive coordonates of new destination
            of MacGyver as "x_new" = 5 and "y_new" = 13
            In return    : return "True" or "False" as result
        """
        # if destination is in the maze = "True"
        if (0 <= x_new <= 14) and (0 <= y_new <= 14):
            # if destination is not a wall = "True"
            return self.grid[(x_new, y_new)] != "w"
        # else return "False"
        return False

    def test_presence_object(self, x_new, y_new):
        """ tests the presence of object on the
            destination coordinates (x_new, y_new)
            In reception : receive the news coordonates
            of MacGyver as "x_new" = 5 and "y_new" = 13
            In return    : return True or False
        """
        return self.grid[x_new, y_new] in OBJECTS

    def collect_of_object(self):
        """ picks up object on the destination cell and
            up date the grid with "O"
            In reception : receive any parameter
            In return    : add object founded in Angus's attribut
            "macgyver.bag" and modifies the grid "maze.grid" in replace
            the "name of object" ("needle", for example) by the path "O"
        """
        # puts the object finded in the bag
        self.macgyver.bag.append(
            self.grid[self.macgyver.x, self.macgyver.y])
        # and up date the grid with "O" like path :)
        self.grid[self.macgyver.x, self.macgyver.y] = "O"

    def test_presence_of_guardian(self, x_new, y_new):
        """ tests the presence of Guardian
            In reception : receive the news coordonates
            of MacGyver as "x_new" = 5 and "y_new" = 13
            In return    : return True or False
        """
        return (x_new == self.guardian.x) and (y_new == self.guardian.y)

    def consequences_macgyver_displacement(self, x_new, y_new):
        """ assigns news coordinates to MacGyver after displacement
            and collects an object if it is on the new cell
            In reception : receive the news coordonates of MacGyver
            as "x_new" = 5 and "y_new" = 13
            In return    : assigns the new coordinates to MacGyver
            and collects object in case of presence
        """
        # modification of MacGyver's abscissa in the Maze class
        self.macgyver.x = x_new
        # modification of MacGyver's ordonate in the Maze class
        self.macgyver.y = y_new

        # tests presence of object to find
        if self.test_presence_object(x_new, y_new):
            # collects object and remove him of maze's grid
            self.collect_of_object()

    def _initialisation(self):
        # contains all the coordinates of wall, path,
        # MacGyver, guardian and objects to find
        self.grid = {}
        # contains all the coordinates of path
        self.path = []
        # creates MacGyver's character
        self.macgyver = MacGyver(0, 0)
        # creates Guardian's character
        self.guardian = Guardian(0, 0)


if __name__ == "__main__":
    maze = Maze()
    print(maze.grid)
