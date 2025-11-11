import pygame
import player
import obstacle
import background
import setting
from random import randint
  
PIPE_SPAWN_EVENT = pygame.USEREVENT + 1
PIPE_SPAWN_INTERVAL = 2000

class FlappyBird():
    def __init__(self):
        pygame.init()
        self.window_size = setting.get_window_size()
        self.window = pygame.display.set_mode(self.window_size)
        
        self.point = 0
        self.is_hit = False
        self.game_over = False
        self.set_sprite()
        self.set_settings()
        self.set_sound()
        self.main_loop()  
    
    def set_settings(self):
        self.clock = pygame.time.Clock() 
        self.fps = 60
        pygame.time.set_timer(PIPE_SPAWN_EVENT, PIPE_SPAWN_INTERVAL)
    
    def set_sound(self):
        self.score_sound = None
        self.game_over_sound = None
        self.flap_sound = None 
        
        try:
            # Try to load the sound file.
            # Make sure you have a folder named "sounds" with "flap.wav" in it.
            self.score_sound = pygame.mixer.Sound("flappybird/sounds/beep.wav")
            self.game_over_sound = pygame.mixer.Sound("flappybird/sounds/game-over.wav")
            self.flap_sound = pygame.mixer.Sound("flappybird/sounds/wing-flap.wav")
            
        except pygame.error as e:
            # If the file is missing, print an error
            # The game will still run, just without sound.
            print(f"Error loading sound: {e}")
        
    def set_sprite(self):
        self.my_player = player.Player("flappybird/assets/1.png")
        
        #set sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.obstacle_group = pygame.sprite.Group()
        self.point_detector = pygame.sprite.Group()
        
        for i in range(0,17):
            self.background = background.Background("flappybird/assets/1.png", i)
            self.all_sprites.add(self.background)
        
        for i in range(0, 3):
            self.background = background.Background("flappybird/assets/1.png", 17)
            self.all_sprites.add(self.background)
            self.background = background.Background("flappybird/assets/1.png", 18)
            self.all_sprites.add(self.background) 

          
        #add player sprite to "all_sprites" group for drawing 
    
    def hit(self):
        self.game_over_sound.play()
        self.game_over = True
        self.my_player.gameover()
        print("GAME OVER")
        
    def add_point(self):
        self.point += 1
        self.score_sound.play()

        
    def main_loop(self):  
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_SPACE and not self.game_over:
                        self.my_player.jump()
                        self.flap_sound.play()
                        
                
                if event.type == PIPE_SPAWN_EVENT:
                    center_gap_y = randint(120,self.window_size[1]-225)
                    
                    for i in range(0,4):
                        if i == 3:
                            dectect_point = obstacle.Obstacle("flappybird/assets/1.png", i, center_gap_y)
                            self.point_detector.add(dectect_point)
                        else:
                            top_obstacle = obstacle.Obstacle("flappybird/assets/1.png", i, center_gap_y)
                            self.obstacle_group.add(top_obstacle) 
                            self.all_sprites.add(top_obstacle)
                    

                if event.type == pygame.QUIT: 
                    exit()
                    
            #update all sprites 
            self.my_player.update()
            if not self.is_hit:
                self.all_sprites.update()
                self.point_detector.update()
            
                #pos = pygame.mouse.get_pos()
                #self.my_player.set_pos(pos)
                
                self.passed = pygame.sprite.spritecollide(self.my_player, self.point_detector, False)
                self.is_hit = pygame.sprite.spritecollide(self.my_player, self.obstacle_group, False)
                
                
                #check kolisi antara player dan pipa
                if self.is_hit:
                    self.hit()
                    
                #check jika hitbox untuk dekteksi point sudah terpenuhi, maka point di tambah 1
                if self.passed:
                    self.add_point()
                    pygame.sprite.spritecollide(self.my_player, self.point_detector, True)

 
             
            self.window.fill((12, 95, 218))
            self.all_sprites.draw(self.window)
            self.my_player.draw_image(self.window) 
            
            self.clock.tick(self.fps)            
            pygame.display.flip()
        
                    
if __name__ == "__main__":
    FlappyBird()

