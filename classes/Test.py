from MacGyver import MacGyver
from Maze import Maze
from MacGyverGame import Game

print()

if __name__ == "__main__":
    maze = Maze()
    # print(maze.grid)
    print("MacGyver : ", maze.macgyver.x, maze.macgyver.y)
    print("Guardian : ", maze.guardian.x, maze.guardian.y)
    print("test_presence_of_guardian : ", maze.test_presence_of_guardian(13, 14))
    print()
    
