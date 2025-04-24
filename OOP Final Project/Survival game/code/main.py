import pygame.sprite
from settings import *
from player import Player
from sprites import *
from random import randint
from pytmx.util_pygame import load_pygame
from groups import AllSprites

class Game():
    def __init__(self):
        pygame.init()
        self.dispSurf = pygame.display.set_mode((WINwid, WINhei))
        pygame.display.set_caption('OOP Survival game')
        self.clock = pygame.time.Clock()
        self.running = True

        # groups
        self.allSprites = AllSprites()
        self.collisionSprites = pygame.sprite.Group()

        self.setup()

        # sprites

    def setup(self):
        map = load_pygame(join('C:\\Users\\User\\PycharmProjects\\5 games\\Survival game\\data\\maps\\world.tmx'))
        for x,y, image in map.get_layer_by_name('Ground').tiles():
            Sprite((x * TILEsize,y * TILEsize), image, self.allSprites)

        for coll in map.get_layer_by_name('Collisions'):
            CollisionSprite((coll.x, coll.y), pygame.Surface((coll.width, coll.height)), self.collisionSprites)

        for obj in map.get_layer_by_name('Objects'):
            CollisionSprite((obj.x, obj.y), obj.image, (self.allSprites, self.collisionSprites))
            print(obj.x)
            print(obj.y)
            print(obj.image)

        for mark in map.get_layer_by_name('Entities'):
            if mark.name == 'Player':
                self.player = Player((mark.x, mark.y), self.allSprites, self.collisionSprites)

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
            self.allSprites.draw(self.player.rect.center)

            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
