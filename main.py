from neat.NEAT import NEAT
import pygame as pg
from GenomeVisualizer import Visualizer
from Calculator import Calculator


def drawWindow(winWidth, winHeight):
    pg.init()

    DIMS = winWidth, winHeight = winWidth, winHeight
    SCREEN = pg.display.set_mode(DIMS, pg.SRCALPHA)

    neat = NEAT(3, 5, 2)
    genome = neat.createGenome()
    genome2 = neat.createGenome()

    calc2 = Calculator(genome2)
    calc = Calculator(genome)

    visualizer = Visualizer(genome, 200, 125)
    visualizer2 = Visualizer(genome2, 200, 125)

    gameEnd = False

    clock = pg.time.Clock()

    while not gameEnd:
        # event checking
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit(69)
            if event.type == pg.KEYUP:
                if event.key == pg.K_u:
                    visualizer.update()
                    visualizer2.update()
                if event.key == pg.K_o:
                    print(calc.calculate([1, 1, 1]))
                    print(calc2.calculate([1, 1, 1]))
                if event.key == pg.K_m:
                    for i in genome2.nodes:
                        if genome.input_nodes < hash(i) <= genome.input_nodes + genome.output_nodes:
                            pass
                            # print([con.innovation_num for con in
                            #        i.incoming_connections if i.incoming_connections.count(con) > 1])
                    print()
                    for i in genome.nodes:
                        if genome.input_nodes < hash(i) <= genome.input_nodes + genome.output_nodes:
                            pass
                            # print([con.innovation_num for con in
                            #        i.incoming_connections if i.incoming_connections.count(con) > 1])

        genome2.mutate()
        genome.mutate()

        SCREEN.fill((255, 255, 200))

        SCREEN.blit(visualizer.surface, (winWidth//2 - visualizer.surfWidth//2, winHeight//2 - visualizer.surfHeight//2 - 70))
        SCREEN.blit(visualizer2.surface, (winWidth//2 - visualizer2.surfWidth//2, winHeight//2 - visualizer2.surfHeight//2 + 70))

        clock.tick()
        pg.display.flip()




if __name__ == "__main__":
    drawWindow(700, 500)
