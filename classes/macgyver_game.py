"""
    This class manages the animation
    and the graphics part of the program
"""

import os

from pygame import display, key, event, image, QUIT
from pygame import K_DOWN, K_UP, K_RIGHT, K_LEFT, KEYDOWN

from classes.maze import Maze
from classes.config import STEP_MOV, FAST


class Game:
    """
        This class manages the animation
        and the graphics part of the program
    """

    def __init__(self):
        self.maze = Maze()
        self.game_result = 0    # win_game = 1 and lose_game = 2
        self._initialisation()
        self.construct_maze()   # construction of the graphic maze
        self.play_game()        # game management

    def construct_maze(self):
        """ construction of the graphic maze """
        self.display_maze_game()

    def display_maze_game(self):
        """ displays the items of maze after each movement of MacGyver """
        # display the background in the window "fenetre"
        self.fenetre.blit(self.fond_pic, (0, 0))
        # display MacGyver in the window "fenetre"
        self.fenetre.blit(self.macgyver_pic, self.macgyver_pic_position)

        # display differents items of the maze in the window "fenetre"
        for (coords, element) in self.maze.grid.items():
            if element == "w":  # "w" is equivalent to a wall
                self.fenetre.blit(self.mur_pic, (coords[0]*40, coords[1]*40))
            elif element == "G":  # "G" is equivalent to the Guardian
                # game_result != 0 => "end of game" => no more Guardian
                if not self.game_result:
                    self.fenetre.blit(self.guardian_pic,
                                      (coords[0]*40, coords[1]*40))
            elif element == "needle":
                self.fenetre.blit(self.needle_pic, (coords[0]*40, coords[1]*40))
            elif element == "tube":
                self.fenetre.blit(self.tube_pic, (coords[0]*40, coords[1]*40))
            elif element == "ether":
                self.fenetre.blit(self.ether_pic, (coords[0]*40, coords[1]*40))

        if self.game_result == 1:           # if the player win
            self.fenetre.blit(self.win_pic, (40, 10))
            # to block MacGyver at end
            self.maze.grid[13, 13] = "w"
        elif self.game_result == 2:         # if the player lose
            self.fenetre.blit(self.game_over_pic, (0, 0))
            # to block MacGyver at end
            self.maze.grid[13, 13] = "w"
        display.flip()   # Screen refresh

    def play_game(self):
        """ detects pressing the keyboard's arrows,
            calculates new coordinates of MacGyver and moves him
        """
        # movement when an arrow is held down
        key.set_repeat(FAST[0], FAST[1])

        # this loop continues until the game is closed
        continuer = 1
        while continuer:
            # we browse the list of all the events received
            for evt in event.get():

                if evt.type == QUIT:  # if an event is "QUIT"
                    continuer = 0   # we stop the loop

                if evt.type == KEYDOWN:
                    self.test_destination_after_keydown(evt.key)

            self.display_maze_game()

    def test_destination_after_keydown(self, eventkey):
        """ tests the destination after "KEYDOWN" """
        # corresponding movement in the game
        mouvements = {K_DOWN: (0, STEP_MOV), K_UP: (0, -STEP_MOV),
                      K_RIGHT: (STEP_MOV, 0), K_LEFT: (-STEP_MOV, 0)}
        # corresponding movement in the Maze class
        mvt_in_maze = {K_DOWN: "bottom", K_UP: "top",
                       K_RIGHT: "right", K_LEFT: "left"}
        try:
            # calculate new coordinates
            # of MacGyver in the Maze class
            x_new, y_new = self.maze.macgyver.move_to(
                            mvt_in_maze[eventkey])
            # tests if destination is ok
            if self.maze.test_destination_is_valid(
                    x_new, y_new):
                # assigns news coordinates to MacGyver
                # after displacement and collects
                # if an object is on the new cell
                self.maze.consequences_macgyver_displacement(
                    x_new, y_new)

                # tests presence of "Guardian" for news coordinates
                if self.maze.test_presence_of_guardian(
                        x_new, y_new):
                    # tests if MacGyver has collect
                    # all objects to win
                    if sorted(self.maze.macgyver.bag) == \
                            ['ether', 'needle', 'tube']:
                        self.game_result = 1  # it's wined
                    else:
                        self.game_result = 2  # it's lost
                # calculate new position of Angus
                # after "event.key"
                self.macgyver_pic_position = \
                    self.macgyver_pic_position.move(
                        mouvements[eventkey])
        except KeyError:
            print("PAS LA BONNE TOUCHE !!!")

    def _initialisation(self):

        # path to graphics resources
        os.chdir("c:/Users/utilisateur/Desktop/Formation_OpenClassRoom/"
                 "Projet_3/Projet/Ressources_graphiques")

        # creates a window to put in items of the maze
        self.fenetre = display.set_mode((600, 600))

        # loads the differents pics of the maze
        self.fond_pic = image.load("fond_mcg.jpg").convert()
        self.mur_pic = image.load("mur.png").convert()
        self.macgyver_pic = image.load("macgyver.png").convert_alpha()
        self.guardian_pic = image.load("gardien.png").convert_alpha()
        self.needle_pic = image.load("seringue.png").convert_alpha()
        self.tube_pic = image.load("tube_plastique.png").convert_alpha()
        self.ether_pic = image.load("ether.png").convert_alpha()

        self.win_pic = image.load("win.png").convert_alpha()
        self.game_over_pic = image.load("game_over.png").convert_alpha()

        # calculates the coordinates of MacGyver \
        #  which will change during the play
        self.macgyver_pic_position = self.macgyver_pic.get_rect()
        self.macgyver_pic_position = self.macgyver_pic_position.move(
                                    self.maze.macgyver.x*40,
                                    self.maze.macgyver.y*40)


if __name__ == "__main__":
    game = Game()
