from genetics.Gene import Gene


class IndexedSet(list):
    def __init__(self, seq = ()):
        super().__init__(seq)

    def add(self, element):
        if element not in self:
            self.append(element)

    def addSorted(self, element):
        if not issubclass(element, Gene): return
        for i in range(len(self)):
            if element.innovation_num < self[i].innovation_num:
                self.insert(i, element)

    def getRandomElement(self):
        pass

