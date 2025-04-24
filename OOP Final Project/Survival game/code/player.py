import pygame.sprite
from settings import *
from os.path import join

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collisionSprites):
        super().__init__(groups)
        self.loadImages()
        self.state, self.frameIndex = 'down', 0
        self.image = pygame.image.load(join('Survival game', 'images', 'player', 'down', '0.png')).convert_alpha()
        self.rect = self.image.get_frect(center = pos)
        self.hitboxRect = self.rect.inflate(-60, -120)

        # movement
        self.direction = pygame.Vector2()
        self.speed = 500
        self.collisionSprites = collisionSprites

    def loadImages(self):
        self.frames = {'left': [], 'right': [], 'up': [], 'down': []}

        for state in self.frames.keys():
            for folderPath, subFolders, fileNames in walk(join('images', 'player', state)):
                if fileNames:
                    for fileName in sorted(fileNames, key = lambda name: int(name.split('.')[0])):
                        fullPath = join(folderPath, fileName)
                        surf = pygame.imgae.load(fullPath).convert_alpha()
                        self.frames[state].append(surf)

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self, dt):
        self.hitboxRect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.hitboxRect.y += self.direction.y * self.speed * dt
        self.collision('vertical')
        self.rect.center = self.hitboxRect.center

    def collision(self, direction):
        for sprite in self.collisionSprites:
            if sprite.rect.colliderect(self.hitboxRect):
                if direction == 'horizontal':
                    if self.direction.x > 0: self.hitboxRect.right = sprite.rect.left
                    if self.direction.x < 0: self.hitboxRect.left = sprite.rect.right
                else:
                    if self.direction.y < 0: self.hitboxRect.top = sprite.rect.bottom
                    if self.direction.y > 0: self.hitboxRect.bottom = sprite.rect.top

    def animate(self, dt):
        # get state

        # animate
        self.frameIndex += 5 * dt
        self.image = self.frames[self.state][int(self.frameIndex) % len(self.frames[self.state])]

    def update(self, dt):
        self.input()
        self.move(dt)