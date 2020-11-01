import os
import time

import pygame
from pygame.locals import *

class Game:

    def __init__(self, dico):
        self.dico = dico
        self.construct_maze()
        self.play_game()

    def construct_maze(self):

        os.chdir("c:/Users/utilisateur/Desktop/Formation_OpenClassRoom/Projet_3/Ressources_graphiques")

        pygame.init()
        self.fenetre = pygame.display.set_mode((600, 600))

        self.fond = pygame.image.load("fond_mcg.jpg").convert()
        self.fenetre.blit(self.fond, (0,0))
        pygame.display.flip()

        self.mur = pygame.image.load("mur.png").convert()
        self.macgyver = pygame.image.load("macgyver.png").convert_alpha()
        self.guardian = pygame.image.load("gardien.png").convert_alpha()
        self.needle = pygame.image.load("seringue.png").convert_alpha()
        self.tube = pygame.image.load("tube_plastique.png").convert_alpha()
        self.ether = pygame.image.load("ether.png").convert_alpha()

        self.position_macgyver = self.macgyver.get_rect()


        for (coords, element) in self.dico.items():
            if element == "w":
                self.fenetre.blit(self.mur, (coords[0]*40, coords[1]*40))
            elif element == "M":
                self.fenetre.blit(self.macgyver, (coords[0]*40, coords[1]*40))
            elif element == "G":
                self.fenetre.blit(self.guardian, (coords[0]*40, coords[1]*40))
            elif element == "needle":
                self.fenetre.blit(self.needle, (coords[0]*40, coords[1]*40))
            elif element == "tube":
                self.fenetre.blit(self.tube, (coords[0]*40, coords[1]*40))
            elif element == "ether":
                self.fenetre.blit(self.ether, (coords[0]*40, coords[1]*40))
        
        pygame.display.flip()



        # time.sleep(4)

    def play_game(self):

        pygame.key.set_repeat(300, 30)
        mouvements = {K_DOWN:(0,3), K_UP:(0,-3), K_RIGHT:(3,0), K_LEFT:(-3,0)}

        continuer = 1
        while continuer:

            for event in pygame.event.get():        # on parcours la liste de tous les événements reçus

                if event.type == QUIT:              # si un de ces événements est QUIT
                    continuer = 0                   # on arrête la boucle

                if event.type == KEYDOWN:
                    self.position_macgyver = self.position_macgyver.move(mouvements[event.key])

            self.fenetre.blit(self.fond, (0,0))
            self.fenetre.blit(self.macgyver, self.position_macgyver)
            pygame.display.flip()

if __name__ == "__main__":
    game = Game()



