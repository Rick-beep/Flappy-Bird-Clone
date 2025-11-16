import pygame
import player
import obstacle
import background
import setting
import hud
from random import randint
  
PIPE_SPAWN_EVENT = pygame.USEREVENT 
PIPE_SPAWN_INTERVAL = 2000

class FlappyBird():
    def __init__(self):
        pygame.init()
        self.window_size = setting.get_window_size()
        self.window = pygame.display.set_mode(self.window_size)
        
        self.point = 0
        self.start = False
        self.game_over = False
        self.set_music()
        self.set_sprite()
        self.set_settings()
        self.main_loop()  
    
    def set_settings(self):
        self.clock = pygame.time.Clock() 
        self.fps = 60
        pygame.time.set_timer(PIPE_SPAWN_EVENT, PIPE_SPAWN_INTERVAL)
        
    def set_music(self):
        try:
            # Try to load the sound file.
            # Make sure you have a folder named "sounds" with "flap.wav" in it.
            pygame.mixer.music.load("flappybird/sounds/main-theme.mp3")

        except pygame.error as e:
            # If the file is missing, print an error
            # The game will still run, just without sound.
            print(f"Error loading sound: {e}")
    
        # Set volume(0.0 - 1.0)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1, 0.0)
            
    def set_sprite(self):
        #set sprite
        self.my_player = player.Player()
        self.score_sprite = hud.Score()
        self.interface = hud.Interface()
        
        #set sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.obstacle_group = pygame.sprite.Group()
        self.point_detector = pygame.sprite.Group()
        
        for i in range(0,17):
            self.background = background.Background(i)
            self.all_sprites.add(self.background)
        
        for i in range(0, 3):
            self.background = background.Background(17)
            self.all_sprites.add(self.background)
            self.background = background.Background(18)
            self.all_sprites.add(self.background) 
    
    def hit(self):
        self.game_over = True
        self.my_player.crash_sound.play()
        self.my_player.game_over_sound.play()
        self.my_player.gameover()
        
    def add_point(self):
        self.point += 1
        self.my_player.score_sound.play()
        self.score_sprite.set_point(self.point)
    
    def reset(self):
        self.point = 0
        self.start = False
        self.game_over = False
        self.set_music()
        self.set_sprite()
        self.set_settings()        

    def main_loop(self):  
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if self.start and not self.game_over:
                        if event.key == pygame.K_SPACE:
                            self.my_player.jump()
                            self.my_player.flap_sound.play()
                            
                    if event.key == pygame.K_BACKSPACE:
                        self.reset()
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.game_over and self.start:                       
                        self.my_player.jump()
                        self.my_player.flap_sound.play()
                        
                    # CHECK POSISI CLICK DARI USER UNTUK KOLISI TOMBOL
                    pos = pygame.mouse.get_pos()
                    x_check = False
                    y_check = False
                    
                    if pos[0] >= 448 and pos[0] <= 575:
                        x_check = True
                    if pos[1] >= 256 and pos[1] <= 321:
                        y_check = True
                        
                    if x_check and y_check:
                        
                        if not self.start:
                            self.start = True
                            # Fadeout background musik
                            pygame.mixer.music.fadeout(1500)
                        if self.game_over:
                            self.reset()

                if event.type == PIPE_SPAWN_EVENT and self.start:
                    center_gap_y = randint(120,self.window_size[1]-225)
                    
                    for i in range(0,4):
                        if i == 3:
                            dectect_point = obstacle.Obstacle(i, center_gap_y)
                            self.point_detector.add(dectect_point)
                        else:
                            top_obstacle = obstacle.Obstacle(i, center_gap_y)
                            self.obstacle_group.add(top_obstacle) 
                            self.all_sprites.add(top_obstacle)
                    
                if event.type == pygame.QUIT: 
                    exit()
                    
            self.my_player.update()
            self.score_sprite.update()
            if not self.game_over:
                self.all_sprites.update()
                self.point_detector.update()
                
                #pos = pygame.mouse.get_pos()
                #elf.my_player.set_pos(pos)
                
                self.passed = pygame.sprite.spritecollide(self.my_player, self.point_detector, False)
                self.collision_check = pygame.sprite.spritecollide(self.my_player, self.obstacle_group, False)
                
                
                #check kolisi antara player dan pipa
                if self.collision_check:
                    self.hit()
                    self.score_sprite.set_point(self.point)
                    
                #check jika hitbox untuk dekteksi point sudah terpenuhi, maka point di tambah 1
                if self.passed:
                    self.add_point()
                    pygame.sprite.spritecollide(self.my_player, self.point_detector, True)
            
            self.window.fill((12, 95, 218))
            
            self.all_sprites.draw(self.window)
            self.my_player.draw_image(self.window)
            
            # check status game
            if self.start:
                self.score_sprite.draw(self.window)
            else:
                self.interface.draw(4, self.window)
                self.interface.draw(1, self.window)
                self.my_player.idle()
            
            if self.game_over:
                self.interface.draw(4, self.window)
                self.interface.draw(2, self.window)
            
            self.clock.tick(self.fps)            
            pygame.display.flip()
        
                    
if __name__ == "__main__":
    FlappyBird()

