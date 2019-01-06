import pygame

class Background(pygame.sprite.Sprite):

    image = None

    def __init__(self, x, y, image):
        super().__init__()
#        self.image = pygame.image.load("images/atlantic.png").convert_alpha()
        self.image = pygame.image.load(image)
        self.rect = pygame.Rect(x, y, 1274, 965)
