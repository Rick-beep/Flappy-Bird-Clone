import pygame
import setting

class Hud(pygame.sprite.Sprite):
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
        for id, sprite in self.current_sprites.items():
            off_set = i * 20
            window.blit(sprite, (-20 + off_set + x_pos, y_pos ))
            i += 1
            
    def update(self):
        self.set_curret_sprite()
        
        