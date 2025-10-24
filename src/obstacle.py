import pygame
from random import randint

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_path):
        super().__init__()
        
        crop_area = pygame.Rect(3, 9, 12, 10)

        sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        WHITE = (255, 255, 255)
    
        self.image = sheet.subsurface(crop_area)
        self.image = pygame.transform.scale(self.image, (40, 32))
        self.image.set_colorkey((WHITE))
        
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 640)
        self.rect.y = randint(0, 320)
        
        sheet.set_colorkey(WHITE)