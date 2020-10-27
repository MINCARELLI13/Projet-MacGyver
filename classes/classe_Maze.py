#!/usr/bin/env python
# coding: utf-8

import os

print()


class Maze():

    def __init__(self):
        self.grid = {}      # contains all the coordinates of wall, path, MacGyver, guardian and objects to find
        self.path = []      # contains all the coordinates of path
        self.parse_txt_in_coord()
    
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


if __name__ == "__main__":
    maze = Maze()
    print(maze.grid)

 