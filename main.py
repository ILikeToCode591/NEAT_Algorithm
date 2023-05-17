from neat.NEAT import NEAT
import pygame as pg
from GenomeVisualizer import Visualizer

def drawWindow(winWidth, winHeight):
    pg.init()

    DIMS = winWidth, winHeight = winWidth, winHeight
    SCREEN = pg.display.set_mode(DIMS, pg.SRCALPHA)

    neat = NEAT(3, 5, 2)
    genome = neat.createGenome()

    visualizer = Visualizer(genome, 400, 250)

    gameEnd = False

    while not gameEnd:
        # event checking
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit(69)
            if event.type == pg.KEYUP:
                if event.key == pg.K_r:
                    genome.mutateWeightRandom()
                if event.key == pg.K_s:
                    genome.mutateWeightShift()
                if event.key == pg.K_c:
                    genome.mutateConnector()
                if event.key == pg.K_n:
                    genome.mutateNode()
                if event.key == pg.K_t:
                    genome.mutateConnectorToggle()
                if event.key == pg.K_m:
                    genome.mutate()

                visualizer.update()

        SCREEN.fill((255, 255, 200))

        SCREEN.blit(visualizer.surface, (winWidth//2 - visualizer.surfWidth//2, winHeight//2 - visualizer.surfHeight//2))

        pg.display.flip()


if __name__ == "__main__":
    drawWindow(700, 500)
