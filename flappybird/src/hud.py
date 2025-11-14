import pygame
import setting

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.path = setting.get_sprite_path()
        self.window_size = setting.get_window_size()

        self.point = 0
        
        self.current_sprites = {}
        self.set_sheet()
        self.set_sprite()
    
    def set_point(self, point):
        self.point = point
        
    def set_sheet(self):
        WHITE = (255, 255, 255)
        self.sheet = pygame.image.load(self.path).convert_alpha()
        self.sheet.set_colorkey(WHITE)
    
    def set_sprite(self):
        self.sprites = {}
        for i in range(0, 10):
            if i == 0:
                off_set = 6
                crop_area_background = pygame.Rect(166 + off_set, 1, 5, 7)
            elif i <= 4:
                off_set = 6 * i + 6
                crop_area_background = pygame.Rect(166 + off_set, 1, 5, 7)
            
            elif i == 5:
                off_set = 6
                crop_area_background = pygame.Rect(166 + off_set, 9, 5, 7)
                
            else:
                off_set = 6 * (i-5) + 6
                crop_area_background = pygame.Rect(166 + off_set, 9, 5, 7)
                
            sprite = self.sheet.subsurface(crop_area_background) 
            self.sprites[i] = pygame.transform.scale(sprite, (20, 28))
    
    def set_curret_sprite(self):
        point_str = str(self.point)
        for i in range(0, len(point_str)):
            self.current_sprites[i-1] =  self.sprites[int(point_str[i])]
    
    def draw(self, window):
        i = 1
        x_pos = self.window_size[0]/2 - len(self.current_sprites)*20
        y_pos = self.window_size[1]/4 - 100
        
        for sprite in self.current_sprites.values():
            off_set = i * 20
            window.blit(sprite, (-20 + off_set + x_pos, y_pos ))
            i += 1
            
    def update(self):
        self.set_curret_sprite()
        
class Interface(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.path = setting.get_sprite_path()
        self.window_size = setting.get_window_size()
                
        self.current_sprites = {}
        self.set_sheet()
        self.set_sprite()
        
    def set_sheet(self):
        WHITE = (255, 255, 255)
        self.sheet = pygame.image.load(self.path).convert_alpha()
        self.sheet.set_colorkey(WHITE)
    
    def set_sprite(self):
        self.sprites = {}
        for i in range(1,5):
            if i == 1: # "Start" sprite
                cord = (134, 1, 29, 7)
                upscale = (116, 28)
            elif i == 2: # "Game over" sprite
                cord = (135, 10, 26, 15)
                upscale = (104, 60)
            elif i == 3: # "New best" sprite
                cord = (135, 24, 27, 16)
                upscale = (108, 64)
            elif i == 4: # backdrop
                cord = (169, 19, 34, 19)
                upscale = (136, 76)
                
            crop_area_background = pygame.Rect(cord)
            sprite = self.sheet.subsurface(crop_area_background) 
            self.sprites[i] = pygame.transform.scale(sprite, (upscale))
    
    def set_curret_sprite(self):
        point_str = str(self.point)
        for i in range(0, len(point_str)):
            self.current_sprites[i-1] =  self.sprites[int(point_str[i])]
    
    def draw(self, id,  window):
        sprite = self.sprites[id]
        
        x_pos = self.window_size[0]/2 - sprite.get_width()/2
        y_pos = self.window_size[1]/2 - sprite.get_height()/2
        
        window.blit(sprite, (x_pos, y_pos ))