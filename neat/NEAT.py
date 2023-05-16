from data_structs.IndexedSet import IndexedSet
from genetics.Gene import Gene, NodeGene, ConnectorGene
from genetics.Genome import Genome


class NEAT:

    def __init__(self, input_size: int, output_size: int, clients: int ):
        self.__all_connections = dict()
        self.__all_nodes = IndexedSet()
        self.__clients = IndexedSet()

        self.reset(input_size, output_size, clients)

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

        for i in range(input_size):
            inp = self.getNode()
            inp.setX(0.1)
            inp.setY((i+1)/(input_size+1))
        for o in range(output_size):
            inp = self.getNode()
            inp.setX(0.9)
            inp.setY((o+1)/(input_size+1))

    def createGenome(self):

        g = Genome(self)
        g.nodes.extend(self.all_nodes)

        return g

    def getNode(self, id:int = None):
        if id is None or id > len(self.all_nodes):
            newNode = NodeGene(len(self.all_nodes)+1)
            self.all_nodes.add(newNode)

            return newNode
        else:
            return self.all_nodes[id-1]