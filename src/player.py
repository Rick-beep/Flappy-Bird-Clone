import pygame
import random
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_path):
        super().__init__()
        
        crop_area = pygame.Rect(35, 1, 10, 8)
        
        sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        
        WHITE = (255, 255, 255)
        
        sheet.set_colorkey(WHITE)
        
        self.image = sheet.subsurface(crop_area)
        self.image = pygame.transform.scale(self.image, (40, 32))
        self.image.set_colorkey((WHITE))
        
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50
        
    def jump(self):
        self.rect.y += -60

    def set_pos(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        
    def update(self):
        self.rect.y += 2 # Example: always falling
    
