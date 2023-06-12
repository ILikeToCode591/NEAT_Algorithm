from data_structs.IndexedSet import IndexedSet
from genetics.Genome import Genome
from genetics.NodeGene import NodeGene
from genetics.ConnectorGene import ConnectorGene

class NEAT:

    def __init__(self, input_size: int, output_size: int, clients: int):
        self.__all_connections = dict()
        self.__all_nodes = IndexedSet()
        self.__clients = IndexedSet()

        self.__input_size = None
        self.__ouput_size = None

        self.__C1, self.__C2, self.__C3 = 1, 1, 1
        self.__WEIGHT_RANDOM_STRENGTH = 0.5
        self.__WEIGHT_SHIFT_STRENGTH = 0.5

        self.__PROBABILITY_MUTATE_NODE = 0.11
        self.__PROBABILITY_MUTATE_CONNECTION = 0.16
        self.__PROBABILITY_MUTATE_TOGGLE = 0.11
        self.__PROBABILITY_MUTATE_RANDOMWEIGHT = 0.19
        self.__PROBABILITY_MUTATE_SHIFTWEIGHT = 0.2

        self.reset(input_size, output_size, clients)

    @property
    def PROBABILITY_MUTATE_CONNECTION(self):
        return self.__PROBABILITY_MUTATE_CONNECTION

    @property
    def PROBABILITY_MUTATE_RANDOMWEIGHT(self):
        return self.__PROBABILITY_MUTATE_RANDOMWEIGHT

    @property
    def PROBABILITY_MUTATE_SHIFTWEIGHT(self):
        return self.__PROBABILITY_MUTATE_SHIFTWEIGHT

    @property
    def PROBABILITY_MUTATE_TOGGLE(self):
        return self.__PROBABILITY_MUTATE_TOGGLE

    @property
    def PROBABILITY_MUTATE_NODE(self):
        return self.__PROBABILITY_MUTATE_NODE

    @property
    def WEIGHT_RANDOM_STRENGTH(self):
        return self.__WEIGHT_RANDOM_STRENGTH

    @property
    def WEIGHT_SHIFT_STRENGTH(self):
        return self.__WEIGHT_SHIFT_STRENGTH

    @property
    def C1(self):
        return self.__C1

    @property
    def C2(self):
        return self.__C2

    @property
    def C3(self):
        return self.__C3

    @property
    def all_connections(self):
        return self.__all_connections

    @property
    def all_nodes(self):
        return self.__all_nodes

    @property
    def clients(self):
        return self.__clients

    def reset(self, input_size, output_size, clients):
        self.all_connections.clear()
        self.all_nodes.clear()
        self.clients.clear()

        self.__input_size = input_size
        self.__ouput_size = output_size

        for i in range(input_size):
            inp = self.getNode()
            inp.setX(0.1)
            inp.setY((i + 1) / (input_size + 1))
        for o in range(output_size):
            inp = self.getNode()
            inp.setX(0.9)
            inp.setY((o + 1) / (output_size + 1))

    def createGenome(self):

        g = Genome(self)
        g.set_input_nodes(self.__input_size)
        g.set_output_nodes(self.__ouput_size)

        for node in self.all_nodes:
            g.nodes.add(node.copy())

        return g

    def getConnector(self, inputNode=None, outputNode=None):

        if isinstance(inputNode, NodeGene) and isinstance(outputNode, NodeGene):

            key = str(hash(inputNode)) + ' -> ' + str(hash(outputNode))

            if key in self.all_connections:
                # print('already in connections')
                return self.all_connections[key]
            else:
                newCon = ConnectorGene(inputNode, outputNode)
                newCon.setInnovation_num(len(self.all_connections.items()) + 1)
                self.all_connections[key] = newCon
                return self.all_connections[key]

    def getNode(self, id: int = None):
        if id is None or id > len(self.all_nodes):
            newNode = NodeGene(len(self.all_nodes) + 1)
            self.all_nodes.add(newNode)

            return newNode
        else:
            return self.all_nodes[id - 1]
