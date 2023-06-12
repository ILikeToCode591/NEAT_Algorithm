class Calculator:

    def __init__(self, genome):
        self.genome = genome
    
    def calculate(self, inputs : list[int]):
        if len(inputs) != self.genome.input_nodes: raise ValueError('Input size does not match available slots')
        self.genome.nodes.sort()
        inputs = inputs.copy()

        outputs = []

        for n in range(len(self.genome.nodes)):
            if n < self.genome.input_nodes:
                self.genome.nodes[n].output = inputs.pop(0)
            elif n >= len(self.genome.nodes) - self.genome.output_nodes:
                outputs.append(self.genome.nodes[n].calculate())
            else:
                self.genome.nodes[n].calculate()

        return outputs
