import pygame
import random
import setting
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.window_size = setting.get_window_size()
        self.path = setting.get_sprite_path()
        
        self.set_sheet()
        self.player_sprite()
        
        self.is_gameover = False
        self.animation_frames = 0
        self.jumped = False
        self.at_land = False
        
        self.angle = 0
        
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
        self.master_frames = {}
        self.master_frames_refleklsi = {}
        
        for i in range(1, 4):
            crop_area = pygame.Rect(23 + (i * 12), 1, 10, 8)
            image = self.sheet.subsurface(crop_area)
            self.master_frames[i-1] = pygame.transform.scale(image, (40, 32))
            
            
            #(35, 10, 10, 4)
            crop_area = pygame.Rect(23 + (i * 12), 10, 10, 4)
            image = self.sheet.subsurface(crop_area)
            self.master_frames_refleklsi[i-1] = pygame.transform.scale(image, (40, 16))
            

        self.image = self.master_frames[0] 
        self.image_refleksi = self.master_frames_refleklsi[0] 
        

    def draw_image(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))
        window.blit(self.image_refleksi, (self.rect.x,(-self.rect.y + self.window_size[1])/2 + 420))
        
        
    def jump(self):
        self.at_land = False
        self.angle = 40
        self.animation_frames = 4
        self.y_vektor = -4

    def set_pos(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    
    def animation(self):
        if self.animation_frames > 0:
            self.image = self.master_frames[0]
            self.image_refleksi = self.master_frames_refleklsi[0]
            
        elif self.y_vektor > 1:
            self.image = self.master_frames[2]
            self.image_refleksi = self.master_frames_refleklsi[2]

        else:
            self.image = self.master_frames[1]
            self.image_refleksi = self.master_frames_refleklsi[1]

        self.animation_frames -= 1
    
    def gameover(self):
        self.is_gameover = True
        self.jump()
        
    def rotate_image(self): # TODO menambah Rooatasi Gambar
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.image_refleksi = pygame.transform.rotate(self.image_refleksi, -self.angle)
        
        self.rect = self.image.get_rect()
        self.rect.x = int(self.x_pos)
        self.rect.y = int(self.y_pos)
            
    def update(self):
        self.rect.y = int(self.y_pos)
        
        if self.rect.y <= self.window_size[1] - 152 and not self.at_land:
            self.y_pos += self.y_vektor
            if self.y_vektor <= 7:
                self.y_vektor += self.gravitasi
                
        elif not self.is_gameover:
            self.y_pos = self.window_size[1] - 152
            self.at_land = True
        
        if self.at_land:
            self.angle = 0

        elif self.angle >= -60 and not self.at_land:
            if self.is_gameover:
                self.angle -= 2
            self.angle -= 1.3
            
            
        self.animation()
        self.rotate_image()