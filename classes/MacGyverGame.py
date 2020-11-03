import os
import time

import pygame
from pygame.locals import *

from Maze import Maze
from MacGyver import MacGyver
from config import STEP_MOV


class Game:

    def __init__(self):
        self.maze = Maze()
        # self.grid = grid
        self.construct_maze()
        self.play_game()

    def construct_maze(self):
        """ construction of the graphic maze """
        # path to graphics resources
        os.chdir("c:/Users/utilisateur/Desktop/Formation_OpenClassRoom/Projet_3/Ressources_graphiques")

        # creates a window to put in items of the maze
        pygame.init()
        self.fenetre = pygame.display.set_mode((600, 600))

        # loads the differents items of the maze
        self.fond = pygame.image.load("fond_mcg.jpg").convert()
        self.mur = pygame.image.load("mur.png").convert()
        self.macgyver = pygame.image.load("macgyver.png").convert_alpha()
        self.guardian = pygame.image.load("gardien.png").convert_alpha()
        self.needle = pygame.image.load("seringue.png").convert_alpha()
        self.tube = pygame.image.load("tube_plastique.png").convert_alpha()
        self.ether = pygame.image.load("ether.png").convert_alpha()

        # calculates the coordinates of MacGyver which will change during the play
        self.position_macgyver = self.macgyver.get_rect()
        self.position_macgyver = self.position_macgyver.move(40, 0)
        print("coord de Angus :", self.maze.macgyver.x, self.maze.macgyver.y)
        self.display_maze_game()


    def display_maze_game(self):
        """ displays the items of maze after each movement of MacGyver """
        self.fenetre.blit(self.fond, (0,0))                             # display the background in the window "fenetre"
        self.fenetre.blit(self.macgyver, self.position_macgyver)        # display MacGyver in the window "fenetre"

        # display differents items of the maze in the window "fenetre"
        for (coords, element) in self.maze.grid.items():
            if element == "w":
                self.fenetre.blit(self.mur, (coords[0]*40, coords[1]*40))
            # elif element == "M":
            #     self.fenetre.blit(self.macgyver, (coords[0]*40, coords[1]*40))        # MACGYVER
            elif element == "G":
                self.fenetre.blit(self.guardian, (coords[0]*40, coords[1]*40))
            elif element == "needle":
                self.fenetre.blit(self.needle, (coords[0]*40, coords[1]*40))
            elif element == "tube":
                self.fenetre.blit(self.tube, (coords[0]*40, coords[1]*40))
            elif element == "ether":
                self.fenetre.blit(self.ether, (coords[0]*40, coords[1]*40))
        pygame.display.flip()   # Screen refresh

    def play_game(self):
        """ detects pressing the keyboard's arrows, calculates new coordinates of MacGyver and moves him """
        # pygame.key.set_repeat(300, 30)
        mouvements = {K_DOWN:(0,STEP_MOV), K_UP:(0,-STEP_MOV), K_RIGHT:(STEP_MOV,0), K_LEFT:(-STEP_MOV,0)}

        # this loop continues until the game is closed
        continuer = 1
        while continuer:

            for event in pygame.event.get():        # we browse the list of all the events received

                if event.type == QUIT:              # if an event is "QUIT"
                    continuer = 0                   # we stop the loop

                if event.type == KEYDOWN:
                    # if "test_destination_is_valid":
                    #       if "test_presence_object":
                    #           collect_of_object ET remove_object_of_game
                    #       if "test_presence_of_guardian":
                    #           teste si tous les objects ont été collectés ET arrête le jeu
                    #       Déplace MacGyver sur la nouvelle case du game et enregistre ses nouvelles coordonnées dans grid
                    #           et remet un "O" sur l'ancienne case de MacGyver
                    #
                    self.position_macgyver = self.position_macgyver.move(mouvements[event.key]) # calculate new position of Angus after "event.key"

            self.display_maze_game()


if __name__ == "__main__":
    game = Game()



