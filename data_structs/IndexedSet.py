from genetics.Gene import Gene
from random import choice

class IndexedSet(list):
    def __init__(self, seq = ()):
        super().__init__(seq)

    def add(self, *elements):
        for element in elements:
            if element not in self:
                self.append(element)

    def addSorted(self, element):
        if not issubclass(element, Gene): return
        for i in range(len(self)):
            if element.innovation_num < self[i].innovation_num:
                self.insert(i, element)

    def getRandomElement(self, n = 1):
        if len(self): return tuple(choice(self) for i in range(n)) if n>1 else choice(self)
        else: return (None,) * n if n>1 else None