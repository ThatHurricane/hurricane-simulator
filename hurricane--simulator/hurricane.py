import pygame

class Hurricane(pygame.sprite.Sprite):

    image = None

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("images/hurric.gif").convert_alpha()
        self.rect = pygame.Rect(x, y, 50, 50)
