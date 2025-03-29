import pygame.sprite
from settings import *
from player import Player

class Game():
    def __init__(self):
        pygame.init()
        self.dispSurf = pygame.display.set_mode((WINwid, WINhei))
        pygame.display.set_caption('OOP Survival game')
        self.clock = pygame.time.Clock()
        self.running = True
        self.allSprites = pygame.sprite.Group()

        self.player = Player((400, 300), self.allSprites)

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000  # convert to seconds

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update
            self.allSprites.update(dt)

            # draw
            self.dispSurf.fill('black')
            self.allSprites.draw(self.dispSurf)

            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
