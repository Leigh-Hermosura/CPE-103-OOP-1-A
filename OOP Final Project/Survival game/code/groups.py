from settings import *

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.displaySurface = pygame.display.get_surface()
        self.offset = pygame.Vector2()

    # camera
    def draw(self, target_pos):
        self.offset.x = -(target_pos[0] - WINwid / 2)
        self.offset.y = -(target_pos[1] - WINhei / 2)

        groundSprites = [sprite for sprite in self if hasattr(sprite, 'ground')]
        objectSprites = [sprite for sprite in self if not hasattr(sprite, 'ground')]

        for layer in [groundSprites, objectSprites]:
            for sprite in sorted(layer, key = lambda sprite: sprite.rect.centery):
                self.displaySurface.blit(sprite.image, sprite.rect.topleft + self.offset)