import pygame
from random import randint

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_path, pipe_segment, center_gap_y):
        super().__init__()
        self.center_gap_y = center_gap_y
        self.path = sprite_sheet_path
        self.segment_type = pipe_segment
        
        self.set_sheet()
        self.set_sprite()
        self.set_obstacle()
    
    def set_sheet(self):
        #set colour key to make it trasparent    
        WHITE = (255, 255, 255)
        self.sheet = pygame.image.load(self.path).convert_alpha()
        self.sheet.set_colorkey(WHITE)
    
    def set_sprite(self):
        crop_area_cap_top = pygame.Rect(18, 1, 16, 7)
        crop_area_cap_bottom = pygame.Rect(1, 1, 16, 7)
        crop_area_body = pygame.Rect(1, 9, 16, 10)
        
        pipe_cap_bottom = self.sheet.subsurface(crop_area_cap_bottom)
        pipe_cap_top = self.sheet.subsurface(crop_area_cap_top)
        pipe_body = self.sheet.subsurface(crop_area_body)
        
        self.scaled_cap_bottom = pygame.transform.scale(pipe_cap_bottom, (64, 28))
        self.scaled_cap_top = pygame.transform.scale(pipe_cap_top, (64, 28))
        self.scaled_body = pygame.transform.scale(pipe_body, (64, 40))
    
    def set_obstacle(self):
        #Modifikasi inni untuk atur buffer jarak pixel
        self.y_top_pipe_end = self.center_gap_y - 60
        self.y_bottom_pipe_start = self.center_gap_y + 60
        
        if self.segment_type == 'BOTTOM':
            self.bottom_obstacle()
        elif self.segment_type == 'TOP':
            self.top_obstacle()
        
    def bottom_obstacle(self):
        self.pipe_height = 320 - self.y_bottom_pipe_start
        self.pipe_surface = pygame.Surface((64, self.pipe_height), pygame.SRCALPHA)
        
        self.pipe_surface.blit(self.scaled_cap_bottom, (0, 0))
        
        current_y = self.scaled_cap_bottom.get_height()
                
        while current_y < self.pipe_height:
            self.pipe_surface.blit(self.scaled_body, (0, current_y))
            current_y += self.scaled_body.get_height()

        self.image = self.pipe_surface
            
        self.rect = self.image.get_rect()
        self.rect.x = 640
        self.rect.y = self.y_bottom_pipe_start
        
        
    def top_obstacle(self): #TODO polish bagian ini 
        self.pipe_height = self.y_top_pipe_end
        self.pipe_surface = pygame.Surface((64, self.pipe_height), pygame.SRCALPHA)
        
        self.pipe_surface.blit(self.scaled_cap_top, (0, self.pipe_height - self.scaled_cap_top.get_height()))
        
        current_y = self.pipe_height - self.scaled_cap_top.get_height()
        while current_y > 0:
            current_y -= self.scaled_body.get_height()
            self.pipe_surface.blit(self.scaled_body, (0, current_y))
        
    
        self.image = self.pipe_surface
            
        self.rect = self.image.get_rect()
        self.rect.x = 640
        self.rect.y = 0
    
        
    def update(self):
        if self.rect.x < -50:
            self.kill()
        self.rect.x += -1
        