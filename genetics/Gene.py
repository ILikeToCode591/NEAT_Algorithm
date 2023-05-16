from Globals import MAX_NODES

class Gene:

    def __init__(self, *args : int):
        self.__innovation_num = args[0] if len(args) else None

    def set_innovation_num(self, value):
        self.__innovation_num = value

    @property
    def innovation_num(self):
        return self.__innovation_num


class NodeGene(Gene):

    def __init__(self, innovation_num):
        super().__init__(innovation_num)

        self.__x = 0
        self.__y = 0

    def __eq__(self, other):
        if not isinstance(other, NodeGene): return False
        return self.innovation_num == other.innovation_num

    def __hash__(self):
        return self.innovation_num

    def setX(self, value):
        self.__x = value

    def setY(self, value):
        self.__y = value

    @property
    def y(self):
        return self.__y

    @property
    def x(self):
        return self.__x


class ConnectorGene(Gene):

    def __init__(self, *args):
        super().__init__()

        self.__input = args[0] if len(args) == 2 else None
        self.__output = args[1] if len(args) == 2 else None
        self.__weight = None
        self.__enabled = True

    def setOut(self, obj):
        self.__output = obj

    def setIn(self, obj):
        self.__input = obj

    def setWeight(self, weight: float):
        self.__weight = weight

    def setEnabled(self, value: bool):
        self.__enabled = value

    def __eq__(self, other):
        if not isinstance(other, ConnectorGene): return False

        return self.input == other.input and self.output == other.output

    def __hash__(self):
        return self.input * MAX_NODES + self.output

    @property
    def output(self):
        return self.__output

    @property
    def enabled(self):
        return self.__enabled

    @property
    def weight(self):
        return self.__weight

    @property
    def input(self):
        return self.__input
