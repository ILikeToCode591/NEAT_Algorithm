class Gene:

    def __init__(self, *args : int):
        self.__innovation_num = args[0] if len(args) else None

    def setInnovation_num(self, value):
        self.__innovation_num = value

    @property
    def innovation_num(self):
        return self.__innovation_num
