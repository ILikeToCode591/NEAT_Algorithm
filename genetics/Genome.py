from random import random, choice, sample

from data_structs.IndexedSet import IndexedSet
from genetics.Gene import ConnectorGene, NodeGene


class Genome:

    def __init__(self, parent_neat):
        self.__neat = parent_neat
        self.__connectors = IndexedSet()
        self.__nodes = IndexedSet()

    def getConnector_Inums(self):
        return [conn.innovation_num for conn in self.connectors]

    @property
    def neat(self):
        return self.__neat

    @property
    def connectors(self):
        return self.__connectors

    @property
    def nodes(self):
        return self.__nodes

    def mutate(self):
        if random() > self.neat.PROBABILITY_MUTATE_NODE:
            self.mutateNode()
        if random() > self.neat.PROBABILITY_MUTATE_CONNECTION:
            self.mutateConnector()
        if random() > self.neat.PROBABILITY_MUTATE_RANDOMWEIGHT:
            self.mutateWeightRandom()
        if random() > self.neat.PROBABILITY_MUTATE_SHIFTWEIGHT:
            self.mutateWeightShift()
        if random() > self.neat.PROBABILITY_MUTATE_TOGGLE:
            self.mutateConnectorToggle()

    def mutateConnector(self):

        for i in range(50):
            n1, n2 = self.nodes.getRandomElement(2)
            if n1 is None: return

            if n1.x == n2.x: continue
            if n1.x < n2.x:
                conn = ConnectorGene(n1, n2)
            else:
                conn = ConnectorGene(n2, n1)

            if conn in self.connectors: continue

            conn = self.neat.getConnector(conn.input, conn.output, (random() * 2 - 1) * self.neat.WEIGHT_RANDOM_STRENGTH, True)

            self.connectors.add(conn)
            break

    def mutateNode(self):

        conn = self.connectors.getRandomElement()
        if conn is None: return

        left = conn.input
        middle = self.neat.getNode()
        right = conn.output

        con1 = self.neat.getConnector(left, middle, 1, conn.enabled)
        con2 = self.neat.getConnector(middle, right, conn.weight, conn.enabled)

        self.connectors.remove(conn)
        self.connectors.add(con1, con2)

        middle.setX((left.x + right.x)/2)
        middle.setY((left.y + right.y)/2 + random() * 0.1 - 0.05)
        self.nodes.add(middle)

    def mutateWeightRandom(self):
        conn = self.connectors.getRandomElement()
        if conn is None: return
        conn.setWeight((random() * 2 - 1) * self.neat.WEIGHT_RANDOM_STRENGTH)

    def mutateWeightShift(self):
        conn = self.connectors.getRandomElement()
        if conn is None: return
        conn.setWeight((random()* 2 - 1)*self.neat.WEIGHT_SHIFT_STRENGTH + conn.weight)

    def mutateConnectorToggle(self):
        conn = self.connectors.getRandomElement()
        if conn is None: return
        conn.setEnabled(not conn.enabled)

    def __sub__(self, other):

        if not isinstance(other, Genome): raise ValueError('Invalid Subtrahend')

        con_Inums1 = self.getConnector_Inums()
        con_Inums2 = other.getConnector_Inums()

        smallerSet, largerSet = (
            (con_Inums1, con_Inums2) if len(con_Inums1) < len(con_Inums2) else (con_Inums2, con_Inums1))

        similarInums = list(set(con_Inums1).intersection(con_Inums2))

        similar = len(similarInums)
        excess = len(largerSet) - largerSet.index(max(smallerSet)) + 1
        disjoint = len(con_Inums1) + len(con_Inums2) - 2 * similar - excess

        weightDiff = 0

        for i in similarInums:
            breaker = False
            for sGene in self.connectors:
                if sGene.innovation_num != i: continue
                for oGene in other.connectors:
                    if oGene.innovation_num != i: continue
                    if oGene.innovation_num == sGene.innovation_num:
                        weightDiff += abs(oGene.weight - sGene.weight) / similar
                        breaker = True
                        break
                if breaker: break

        N = len(largerSet)
        if N < 20:
            N = 1

        return (self.neat.C1 * disjoint / N) + (self.neat.C2 * excess / N) + weightDiff

    def __mul__(self, other):

        if not isinstance(other, Genome): raise ValueError('Invalid Subtrahend')

        newGenome = self.neat.createGenome()

        con_Inums1 = self.getConnector_Inums()
        con_Inums2 = other.getConnector_Inums()

        smallerSet, largerSet = (
            (con_Inums1, con_Inums2) if len(con_Inums1) < len(con_Inums2) else (con_Inums2, con_Inums1))

        similarInums = set(con_Inums1).intersection(con_Inums2)
        excessInums = set(largerSet[largerSet.index(max(smallerSet)) + 1:])
        disjointInums = set(con_Inums1).union(set(con_Inums2)).difference(similarInums, excessInums)

        similarPairs = dict()

        for conn in self.connectors + other.connectors:
            if conn.innovation_num in similarPairs:
                if conn.innovation_num not in similarPairs:
                    similarPairs[conn.innovation_num] = [conn]
                else:
                    similarPairs[conn.innovation_num] += [conn]
                    newGenome.connections.add(choice(similarPairs[conn.innovation_num]).copy())

                continue
            if conn.innovation_num in disjointInums or conn.innovation_num in excessInums:
                newGenome.connections.add(conn.copy())

        for conn in newGenome.connections:
            newGenome.nodes.add(conn.input())
            newGenome.nodes.add(conn.output())


