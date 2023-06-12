from Globals import MAX_NODES
from genetics.Gene import Gene
from genetics.NodeGene import NodeGene

class ConnectorGene(Gene):

    def __init__(self, inp = None, out = None):
        super().__init__()

        self.__input = None
        self.__output = None

        self.setIn(inp)
        self.setOut(out)

        self.__weight = None
        self.__enabled = True

    def setOut(self, obj):
        if not isinstance(obj, NodeGene): return
        self.__output = obj

    def setIn(self, obj):
        if not isinstance(obj, NodeGene): return
        self.__input = obj

    def setWeight(self, weight: float):
        self.__weight = weight

    def setEnabled(self, value: bool):
        self.__enabled = value

    def __eq__(self, other):
        if not isinstance(other, ConnectorGene): return False

        return self.input == other.input and self.output == other.output

    def __hash__(self):
        return hash(self.input) * MAX_NODES + hash(self.output)

    def copy(self):
        copy = ConnectorGene(self.input, self.output)
        copy.setEnabled(self.enabled)
        copy.setWeight(self.weight)
        copy.setInnovation_num(self.innovation_num)

        return copy

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
