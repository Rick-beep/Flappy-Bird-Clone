import pygame
import setting
class Background(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_path, id):
        super().__init__()
        self.id = id
        self.path = sprite_sheet_path
        self.move_counter = 0
        self.set_sheet()
        self.draw_image()
    
    def set_sheet(self):
        WHITE = (255, 255, 255)
        self.sheet = pygame.image.load(self.path).convert_alpha()
        self.sheet.set_colorkey(WHITE)
        
    #BACKGROUND 0-6 adalah Gunung        
    def background_0(self):
        crop_area_background_0 = pygame.Rect(1, 28, 40, 31)
        background_0 = self.sheet.subsurface(crop_area_background_0) 
        self.background = pygame.transform.scale(background_0, (320, 248))
        self.x_pos_offset = 0
        self.y_pos_offset = 50
        self.speed = -1
        
    def background_1(self):
        crop_area_background_1 = pygame.Rect(42, 28, 40, 31)
        background_1 = self.sheet.subsurface(crop_area_background_1)
        self.background = pygame.transform.scale(background_1, (320, 248))
        self.x_pos_offset = 0
        self.y_pos_offset = 50
        self.speed = -1
        
    def background_2(self):
        crop_area_background_2 = pygame.Rect(83, 28, 40, 31)
        background_2 = self.sheet.subsurface(crop_area_background_2)
        self.background = pygame.transform.scale(background_2, (320, 248))
        self.x_pos_offset = 0
        self.y_pos_offset = 50
        self.speed = -1
        
    def background_3(self):
        crop_area_background_3 = pygame.Rect(124, 43, 40, 31)
        background_3 = self.sheet.subsurface(crop_area_background_3)
        self.background = pygame.transform.scale(background_3, (320, 248))
        self.x_pos_offset = 0
        self.y_pos_offset = 50
        self.speed = -1
    
    def background_4(self):
        crop_area_background_4 = pygame.Rect(1, 60, 40, 14)
        background_4 = self.sheet.subsurface(crop_area_background_4)
        self.background = pygame.transform.scale(background_4, (320, 112))
        self.x_pos_offset = 0
        self.y_pos_offset = 50
        self.speed = -1

    def background_5(self):
        crop_area_background_5 = pygame.Rect(42, 60, 40, 14)
        background_5 = self.sheet.subsurface(crop_area_background_5)
        self.background = pygame.transform.scale(background_5, (320, 112))
        self.x_pos_offset = 0
        self.y_pos_offset = 50
        self.speed = -1

    def background_6(self):
        crop_area_background_6 = pygame.Rect(83, 60, 40, 14)
        background_6 = self.sheet.subsurface(crop_area_background_6)
        self.background = pygame.transform.scale(background_6, (320, 112))
        self.x_pos_offset = 0
        self.y_pos_offset = 50
        self.speed = -1
        
    # Lantai
    def background_7(self):
        crop_area_background_7 = pygame.Rect(1, 20, 36, 7)
        background_7 = self.sheet.subsurface(crop_area_background_7)
        self.background = pygame.transform.scale(background_7, (144, 28))
        self.x_pos_offset = 0
        self.y_pos_offset = 60
        self.speed = -2
        

    # Refleksi lantai
    def background_8(self):
        crop_area_background_8 = pygame.Rect(42, 24, 36, 3)
        background_8 = self.sheet.subsurface(crop_area_background_8)
        self.background = pygame.transform.scale(background_8, (144, 12))
        self.x_pos_offset = 0
        self.y_pos_offset = 50
        self.speed = -2

    # Air
    def background_9(self):
        crop_area_background_9 = pygame.Rect(42, 18, 40, 4)
        background_9 = self.sheet.subsurface(crop_area_background_9)
        self.background = pygame.transform.scale(background_9, (160, 16))
        self.x_pos_offset = 0
        self.y_pos_offset = self.background.get_height()/2 + 55 
        self.speed = -2
        
    def inisialisasi(self):
        if self.id == 0:
            self.background_0()
        elif self.id == 1:
            self.background_1()
        elif self.id == 2:
            self.background_2()
        elif self.id == 3:
            self.background_3()
        elif self.id == 4:
            self.background_4()
        elif self.id == 5:
            self.background_5()
        elif self.id == 6:
            self.background_6()
        elif self.id == 7:
            self.background_7()
        elif self.id == 8:
            self.background_8()
        elif self.id == 9:
            self.background_9()
            
    def draw_image(self):
        self.inisialisasi()
        
        background_width = self.background.get_width()
        self.background_blu = pygame.Surface((background_width*8, 640), pygame.SRCALPHA)
        self.background_blu.blit(self.background, (0, 0))
        
        for i in range(1, 9):
            self.background_blu.blit(self.background, (background_width*i, 0))
    
        self.image = self.background_blu
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 320 - self.background.get_height() - self.y_pos_offset
    
    def reset(self):
        self.rect.x = 0
    
    def update(self):
        if self.rect.x <= -self.background.get_width()*2:
            self.reset()
            
        self.move_counter += 1
        
        if self.move_counter >= 7 - self.id:
            self.move_counter = 0
            self.rect.x += self.speed
            
            
# BUAT physics bird dengan cara mengunakan 2 variable 
# contoh
#   self.x = 2.9
#   self.rect.x = int(self.x)