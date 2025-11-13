import pygame
import setting
import game
from random import randint
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, pipe_id, center_gap_y):
        super().__init__()
        self.center_gap_y = center_gap_y
        self.path = setting.get_sprite_path()
        self.pipe_id = pipe_id
        self.point = 0
        self.window_size = setting.get_window_size()
        
        self.set_sheet()
        self.set_sprite()
        self.set_obstacle()
    
    def set_sheet(self):
        #set colour key to make it trasparent    
        WHITE = (255, 255, 255)
        self.sheet = pygame.image.load(self.path).convert_alpha()
        self.sheet.set_colorkey(WHITE)
    
    def set_sprite(self):
        crop_area_body = pygame.Rect(1, 9, 16, 10)
        crop_area_body_reflection = pygame.Rect(18, 9, 16, 5)
        
        
        pipe_body = self.sheet.subsurface(crop_area_body)
        pipe_body_re = self.sheet.subsurface(crop_area_body_reflection)
        
        
        self.scaled_body = pygame.transform.scale(pipe_body, (64, 40))
        self.scaled_body_re = pygame.transform.scale(pipe_body_re, (64, 20))
        
    
    def set_obstacle(self):
        #Modifikasi inni untuk atur buffer jarak pixel
        self.y_top_pipe_end = self.center_gap_y - 90
        self.y_bottom_pipe_start = self.center_gap_y + 90
        if self.pipe_id == 0:
            self.obstacle_0()
        elif self.pipe_id == 1:
            self.obstacle_1()
        elif self.pipe_id == 2:
            self.obstacle_2()
        elif self.pipe_id == 3:
            self.obstacle_3()
        elif self.pipe_id == 4:
            self.obstacle_4()
        elif self.pipe_id == 5:
            self.obstacle_5()
        elif self.pipe_id == 6:
            self.obstacle_6()
        elif self.pipe_id == 7:
            self.obstacle_7()
        elif self.pipe_id == 8:
            self.obstacle_8()
        elif self.pipe_id == 9:
            self.obstacle_9()
        
    def obstacle_0(self):
        crop_area_cap_bottom = pygame.Rect(1, 1, 16, 7)
        pipe_cap_bottom = self.sheet.subsurface(crop_area_cap_bottom)
        self.scaled_cap_bottom = pygame.transform.scale(pipe_cap_bottom, (64, 28))
        
        self.pipe_height = self.window_size[1] - self.y_bottom_pipe_start - 88
        self.pipe_surface = pygame.Surface((64, self.pipe_height), pygame.SRCALPHA)
        
        self.pipe_surface.blit(self.scaled_cap_bottom, (0, 0))
        
        current_y = self.scaled_cap_bottom.get_height()
                
        while current_y < self.pipe_height:
            self.pipe_surface.blit(self.scaled_body, (0, current_y))
            current_y += self.scaled_body.get_height()

        self.image = self.pipe_surface
            
        self.rect = self.image.get_rect()
        self.rect.x = self.window_size[0]
        self.rect.y = self.y_bottom_pipe_start - 30
    
    def obstacle_1(self): 
        crop_area_cap_top = pygame.Rect(18, 1, 16, 7)
        pipe_cap_top = self.sheet.subsurface(crop_area_cap_top)
        self.scaled_cap_top = pygame.transform.scale(pipe_cap_top, (64, 28))
        
        self.pipe_height = self.y_top_pipe_end
        self.pipe_surface = pygame.Surface((64, self.pipe_height), pygame.SRCALPHA)
        
        self.pipe_surface.blit(self.scaled_cap_top, (0, self.pipe_height - self.scaled_cap_top.get_height()))
        
        current_y = self.pipe_height - self.scaled_cap_top.get_height()
        while current_y > 0:
            current_y -= self.scaled_body.get_height()
            self.pipe_surface.blit(self.scaled_body, (0, current_y))
        
        self.image = self.pipe_surface
            
        self.rect = self.image.get_rect()
        self.rect.x = self.window_size[0]
        self.rect.y = 0
    
    def obstacle_2(self):
        crop_area_cap_re = pygame.Rect(18, 15, 16, 4)
        pipe_cap_re = self.sheet.subsurface(crop_area_cap_re)
        self.scaled_cap_re = pygame.transform.scale(pipe_cap_re, (64, 16))
        
        self.pipe_height = ((self.window_size[1] - self.y_bottom_pipe_start) - 92)/2
        self.pipe_surface = pygame.Surface((64, self.pipe_height), pygame.SRCALPHA)
        
        self.pipe_surface.blit(self.scaled_cap_re, (0, self.pipe_height - self.scaled_cap_re.get_height()))
        
        current_y = self.pipe_height - self.scaled_cap_re.get_height()
        while current_y > 0:
            current_y -= self.scaled_body_re.get_height()
            self.pipe_surface.blit(self.scaled_body_re, (0, current_y))
        
        self.image = self.pipe_surface
            
        self.rect = self.image.get_rect()
        self.rect.x = self.window_size[0]
        self.rect.y = self.window_size[1] - 80


    # HITBOX FOR GETTING POINT
    def obstacle_3(self):

        self.pipe_height = self.window_size[1]
        self.pipe_surface = pygame.Surface((64, self.pipe_height), pygame.SRCALPHA)
                
        self.image = self.pipe_surface
            
        self.rect = self.image.get_rect()
        self.rect.x = self.window_size[0] + 60
        self.rect.y = 0
                
    def update(self):
        if self.rect.x < -self.pipe_surface.get_width():
            self.kill()
        self.rect.x += -2
        