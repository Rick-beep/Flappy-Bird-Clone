import pygame
import setting
class Background(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_path, id):
        super().__init__()
        self.id = id
        self.path = sprite_sheet_path
        self.move_counter = 0
        self.set_sheet()
        self.drawimage()
    
    def set_sheet(self):
        WHITE = (255, 255, 255)
        self.sheet = pygame.image.load(self.path).convert_alpha()
        self.sheet.set_colorkey(WHITE)
        
    def background_0(self):
        crop_area_background_0 = pygame.Rect(1, 28, 40, 31)
        background_0 = self.sheet.subsurface(crop_area_background_0) 
        self.background = pygame.transform.scale(background_0, (320, 246))
        
    def background_1(self):
        crop_area_background_1 = pygame.Rect(42, 28, 40, 31)
        background_1 = self.sheet.subsurface(crop_area_background_1)
        self.background = pygame.transform.scale(background_1, (320, 246))
        
    def background_2(self):
        crop_area_background_2 = pygame.Rect(83, 28, 40, 31)
        background_2 = self.sheet.subsurface(crop_area_background_2)
        self.background = pygame.transform.scale(background_2, (320, 246))
        
    def background_3(self):
        crop_area_background_3 = pygame.Rect(124, 43, 40, 31)
        background_3 = self.sheet.subsurface(crop_area_background_3)
        self.background = pygame.transform.scale(background_3, (320, 246))
    
    def background_4(self):
        crop_area_background_4 = pygame.Rect(1, 60, 40, 14)
        background_4 = self.sheet.subsurface(crop_area_background_4)
        self.background = pygame.transform.scale(background_4, (320, 112))

    def background_5(self):
        crop_area_background_5 = pygame.Rect(42, 60, 40, 14)
        background_5 = self.sheet.subsurface(crop_area_background_5)
        self.background = pygame.transform.scale(background_5, (320, 112))

    def background_6(self):
        crop_area_background_6 = pygame.Rect(83, 60, 40, 14)
        background_6 = self.sheet.subsurface(crop_area_background_6)
        self.background = pygame.transform.scale(background_6, (320, 112))

    def background_7(self):
        crop_area_background_7 = pygame.Rect(1, 20, 40, 7)
        background_7 = self.sheet.subsurface(crop_area_background_7)
        self.background = pygame.transform.scale(background_7, (320, 56))
        
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
            
    def drawimage(self):
        self.inisialisasi()
        
        self.background_blu = pygame.Surface((320*6, 246), pygame.SRCALPHA)
        self.background_blu.blit(self.background, (0, 0))
        
        for i in range(1, 7):
            self.background_blu.blit(self.background, (320*i, 0))
    
        self.image = self.background_blu
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 320 - self.background.get_height()
    
    def reset(self):
        self.rect.x = 0
    
    def update(self):
        if self.rect.x < -self.background.get_width() * 2:
            self.reset()
            
        self.move_counter += 1
        if self.move_counter >= 7 - self.id:
            self.move_counter = 0
            self.rect.x += -1