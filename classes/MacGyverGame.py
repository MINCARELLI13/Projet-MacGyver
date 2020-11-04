import os
import time

import pygame
from pygame.locals import *

from Maze import Maze
from MacGyver import MacGyver
from config import STEP_MOV, FAST


class Game:

    def __init__(self):
        self.maze = Maze()
        self.game_result = 0    # win_game = 1 and lose_game = 2
        self.construct_maze()   # construction of the graphic maze
        self.play_game()        # game management

    def construct_maze(self):
        """ construction of the graphic maze """
        # path to graphics resources
        os.chdir("c:/Users/utilisateur/Desktop/Formation_OpenClassRoom/Projet_3/Projet/Ressources_graphiques")

        pygame.init()
        # creates a window to put in items of the maze
        self.fenetre = pygame.display.set_mode((600, 600))

        # loads the differents pics of the maze
        self.fond = pygame.image.load("fond_mcg.jpg").convert()
        self.mur = pygame.image.load("mur.png").convert()
        self.macgyver = pygame.image.load("macgyver.png").convert_alpha()
        self.guardian = pygame.image.load("gardien.png").convert_alpha()
        self.needle = pygame.image.load("seringue.png").convert_alpha()
        self.tube = pygame.image.load("tube_plastique.png").convert_alpha()
        self.ether = pygame.image.load("ether.png").convert_alpha()

        self.win = pygame.image.load("win.png").convert_alpha()
        self.game_over = pygame.image.load("game_over.png").convert_alpha()

        # calculates the coordinates of MacGyver which will change during the play
        self.macgyver_position = self.macgyver.get_rect()

        self.macgyver_position = self.macgyver_position.move(self.maze.macgyver.x*40, self.maze.macgyver.y*40)

        self.display_maze_game()

    def display_maze_game(self):
        """ displays the items of maze after each movement of MacGyver """
        self.fenetre.blit(self.fond, (0,0))                             # display the background in the window "fenetre"
        self.fenetre.blit(self.macgyver, self.macgyver_position)        # display MacGyver in the window "fenetre"

        # display differents items of the maze in the window "fenetre"
        for (coords, element) in self.maze.grid.items():
            if element == "w":                              # "w" is equivalent to a wall
                self.fenetre.blit(self.mur, (coords[0]*40, coords[1]*40))
            elif element == "G":                            # "G" is equivalent to the Guardian
                if not self.game_result:
                    self.fenetre.blit(self.guardian, (coords[0]*40, coords[1]*40))
            elif element == "needle":
                self.fenetre.blit(self.needle, (coords[0]*40, coords[1]*40))
            elif element == "tube":
                self.fenetre.blit(self.tube, (coords[0]*40, coords[1]*40))
            elif element == "ether":
                self.fenetre.blit(self.ether, (coords[0]*40, coords[1]*40))

        if self.game_result == 1:           # if the player win
            self.fenetre.blit(self.win, (40, 10))
        elif self.game_result == 2:         # if the player lose
            self.fenetre.blit(self.game_over, (0, 0))
        pygame.display.flip()   # Screen refresh

    def play_game(self):
        """ detects pressing the keyboard's arrows, calculates new coordinates of MacGyver and moves him """
        pygame.key.set_repeat(FAST[0], FAST[1])         # movement when an arrow is held down
        mouvements = {K_DOWN:(0,STEP_MOV), K_UP:(0,-STEP_MOV), K_RIGHT:(STEP_MOV,0), K_LEFT:(-STEP_MOV,0)}  # corresponding movement in the game
        mvt_in_maze = {K_DOWN:"bottom", K_UP:"top", K_RIGHT:"right", K_LEFT:"left"}     # corresponding movement in the Maze class

        # this loop continues until the game is closed
        continuer = 1
        while continuer:

            for event in pygame.event.get():        # we browse the list of all the events received

                if event.type == QUIT:              # if an event is "QUIT"
                    continuer = 0                   # we stop the loop

                if event.type == KEYDOWN:
                    try:
                        x_new, y_new = self.maze.macgyver.move_to(mvt_in_maze[event.key])    # calculate new coordinates of MacGyver in the Maze class

                        if self.maze.test_destination_is_valid(x_new, y_new):   # tests if destination is ok
                            self.maze.consequences_MacGyver_displacement(x_new, y_new)  # assigns news coordinates to MacGyver after displacement
                                                                                        # and collects an object if it is on the new cell

                            if self.maze.test_presence_of_guardian(x_new, y_new):                   # tests presence of "Guardian" for news coordinates
                                if sorted(self.maze.macgyver.bag) == ['ether', 'needle', 'tube']:   # tests if MacGyver has collet all objects to win
                                    self.game_result = 1        # it's wined
                                else:
                                    self.game_result = 2        # it's lost

                            self.macgyver_position = self.macgyver_position.move(mouvements[event.key]) # calculate new position of Angus after "event.key"
                    except KeyError:
                        print("PAS LA BONNE TOUCHE !!!")

            self.display_maze_game()


if __name__ == "__main__":
    game = Game()



