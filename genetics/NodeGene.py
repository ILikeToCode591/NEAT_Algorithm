from data_structs.IndexedSet import IndexedSet
from genetics.Gene import Gene
from math import exp

import inspect
class NodeGene(Gene):

    def __init__(self, innovation_num):
        super().__init__(innovation_num)

        self.__x = 0
        self.__y = 0

        self.incoming_connections = IndexedSet()

        self.__output = 0

    @property
    def output(self):
        return self.__output

    @output.setter
    def output(self, value):
        self.__output = value

    def __eq__(self, other):
        if not isinstance(other, NodeGene): return False
        return self.innovation_num == other.innovation_num

    def __hash__(self):
        return self.innovation_num

    def setX(self, value):
        self.__x = value

    def setY(self, value):
        self.__y = value

    def addIncomingConnection(self, conn):
        print(inspect.stack()[1][3]) if conn in self.incoming_connections  else False
        self.incoming_connections.append(conn)

        # print([con.innovation_num for con in
        #                self.incoming_connections if self.incoming_connections.count(con) > 1], self.innovation_num)
    def calculate(self):

        total_input = 0

        for connector in self.incoming_connections:
            if connector.enabled:
                print(connector.weight)
                total_input += connector.input.output * connector.weight

        self.output = self.activation_funct(total_input)
        return self.output

    @staticmethod
    def activation_funct(x):
        return 1 / (1 + exp(-x))

    def __lt__(self, other):
        return self.x < other.x# or (self.innovation_num < other.innovation_num and self.x == other.x)

    def __le__(self, other):
        return self.x <= other.x# or (self.innovation_num <= other.innovation_num and self.x == other.x)

    def copy(self):
        copy = NodeGene(self.innovation_num)
        copy.setX(self.x)
        copy.setY(self.y)

        return copy

    @property
    def y(self):
        return self.__y

    @property
    def x(self):
        return self.__x

