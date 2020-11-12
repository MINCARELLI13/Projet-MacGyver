# "MacGyver in the maze" (E. MINCARELLI - 07/11/2020)

# What is the goal in this game ?
The goal is to help MacGyver to get out of a maze in which he's locked.
For that, you will have to guide the character of MacGyver in this labyritnh, with the arrow keys, in order to retrieve 3 objects scattered around the maze and which will be necessary to put to sleep the guard who forbids the exit

# How to install the game ?
To install the game, you just have to download all the files and folders contained in the following Github repository : https://github.com/MINCARELLI13/Projet-MacGyver.git

# How to start the game ?
To start playing, all you have to do is run the "main.py" file.

# What are the necessary resources for the game to function ?
This game requires the use of the Python.exe application as well as the following libraries and modules : Pygame, os and random.

# How to create virtual environnement ?
1) In your command prompt, you must first install the "virtualenv" application by typing the following command : " pip install virtualenv " (installes "virtualenv" with "pip" application).
2) In the folder of the project, create the virtual environnement in typing the command line : " "virtualenv -p python3 project_venv " (where "project_venv" is the name of the created virtual environment and "python3" is the version of python used in this new virtual environment).
3) To activate the virtual environment, type the command : " source project_venv/Scripts/activate " because the "activate" file is located in the "project_venv/Scripts /" folder.
4) You must too specify the external packages necessary for the project. To do this, put a file named "requirements.txt" in the source folder of your project and add in this file the name of the following module : pygame==1.9.6
5) Now you just have to install the dependencies useful for the project in typing the following command : " pip install -r requirements.txt "
6) Finally, to launch the game in the virtual environment "projet_venv", you must type the following command : "python main.py"
7) At the end, to quit the virtual environment "projet_venv", you just have to type : " deactivate "
