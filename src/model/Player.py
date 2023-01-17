class Player:
    # Class attributes
    __elo = 1000

    # Constructor
    def __init__(self, name):
        self.__name = name

    # Getters & Setters
    def get_elo(self):
        return self.__elo

    def set_elo(self, elo):
        self.__elo = elo

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

