# import pygame
# from pygame.locals import *

from classes.classe_MacGyver import MacGyver
from classes.classe_Maze import Maze

print()

if __name__ == "__main__":
    maze = Maze()
    print(maze.grid)
    print("MacGyver : ", maze.macgyver.x, maze.macgyver.y)
    print("Guardian : ", maze.guardian.x, maze.guardian.y)
    print("test_presence_of_guardian : ", maze.test_presence_of_guardian(13, 14))
    print()
    # coords = str(input("coordonnées : "))
    # coords = (coords.strip()).split()
    # print()
    # print(len(maze.grid))
    # print()
    # print(maze.path)
    # print(len(maze.path))


    # print("Le personnage de MacGyver possède les coordonnées : ({}, {})".format(maze.macgyver.x, maze.macgyver.y))
    # print("MacGyver se dirige vers le bas : ", maze.macgyver.move_to("bottom"))
    # print("MacGyver se dirige vers la droite : ", maze.macgyver.move_to("right"))
    # print("MacGyver se dirige vers le haut : ", maze.macgyver.move_to("top"))
    # print("MacGyver se dirige vers la gauche : ", maze.macgyver.move_to("left"))
    # print()
    







