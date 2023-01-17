class Player:
    # Constructor
    def __init__(self, name, elo=1000):
        self.__name = name
        self.__elo = elo

    # Getters & Setters
    def get_elo(self):
        return self.__elo

    def set_elo(self, elo):
        self.__elo = elo

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

