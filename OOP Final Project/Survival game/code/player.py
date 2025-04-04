import pygame.sprite
from settings import *
from os.path import join

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collisionSprites):
        super().__init__(groups)
        self.image = pygame.image.load(join('C:\\Users\\User\\PycharmProjects\\5 games\\Survival game\\images\\player\\down\\0.png')).convert_alpha()
        self.rect = self.image.get_frect(center = pos)
        self.hitboxRect = self.rect.inflate(-40, 0)

        # movement
        self.direction = pygame.Vector2()
        self.speed = 500
        self.collisionSprites = collisionSprites

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')

    def collision(self, direction):
        for sprite in self.collisionSprites:
            if sprite.rect.colliderect(self.rect):
                if direction == 'horizontal':
                    if self.direction.x > 0: self.rect.right = sprite.rect.left
                    if self.direction.x < 0: self.rect.left = sprite.rect.right
                else:
                    if self.direction.y < 0: self.rect.top = sprite.rect.bottom
                    if self.direction.y > 0: self.rect.bottom = sprite.rect.top


    def update(self, dt):
        self.input()
        self.move(dt)