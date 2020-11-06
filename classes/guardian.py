""" this class allows to create the guardian """

from classes.position import Position


class Guardian(Position):
    """ this class allows to create the guardian """
    def __init__(self, x, y):
        Position.__init__(self, x, y)


if __name__ == "__main__":
    pass
