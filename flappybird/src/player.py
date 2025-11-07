import pygame
import random
import setting
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_path):
        super().__init__()
        self.window_size = setting.get_window_size()
        self.path = sprite_sheet_path
        
        self.set_sheet()
        self.player_sprite()
        self.animation_start = 0
        self.jumped = False
        self.at_land = False
        
        
        self.x_pos = self.window_size[0]/4
        self.y_pos = 0
        
        self.gravitasi = 0.13
        self.y_vektor = 0
        
        self.rect = self.image.get_rect()
        self.rect.x = int(self.x_pos)
        self.rect.y = int(self.y_pos) 
        
    def set_sheet(self):
        WHITE = (255, 255, 255)
        self.sheet = pygame.image.load(self.path).convert_alpha()
        self.sheet.set_colorkey(WHITE)
    
    def player_sprite(self):
        self.frames = {}
        crop_area_1 = pygame.Rect(35, 1, 10, 8)
        #crop_area_2 = pygame.Rect(47, 1, 10, 8)
        #crop_area_3 = pygame.Rect(59, 1, 10, 8)
        
        for i in range(1, 4):
            crop_area = pygame.Rect(23 + (i * 12), 1, 10, 8)
            image = self.sheet.subsurface(crop_area)
            self.frames[i-1] = pygame.transform.scale(image, (40, 34))
        
        self.image = self.frames[0] 

    def draw_image(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
    def jump(self):
        self.at_land = False
        self.animation_start = 4
        self.rect.y = 180
        self.y_vektor = -4

    def set_pos(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    
    def animation(self):
        if self.animation_start > 0:
            self.image = self.frames[0]
        elif self.y_vektor > 1:
            self.image = self.frames[2]
        else:
            self.image = self.frames[1]
        self.animation_start -= 1
        
    def update(self):
        self.rect.y = int(self.y_pos)
        if self.rect.y <= self.window_size[1] - 152 and not self.at_land:
            self.y_pos += self.y_vektor
            if self.y_vektor <= 7:
                self.y_vektor += self.gravitasi
                
        else:
            print("Game over")
            self.y_pos = self.window_size[1] - 152
            self.at_land = True
            
        self.animation()