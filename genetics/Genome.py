from data_structs.IndexedSet import IndexedSet


class Genome:

    def __init__(self, parent_neat):
        self.__neat = parent_neat
        self.__connectors = IndexedSet()
        self.__nodes = IndexedSet()

    @property
    def neat(self):
        return self.__neat

    @property
    def connectors(self):
        return self.__connectors

    @property
    def nodes(self):
        return self.__nodes

    def __sub__(self, other):
        pass

    def __add__(self, other):
        pass