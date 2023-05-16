import pygame as pg
from neat.NEAT import NEAT

if __name__ == "__main__":
   neat = NEAT(3, 3, 2)
   neat.reset(3, 3, 2)

   genome = neat.createGenome()

   print(len(genome.nodes))