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
        self.set_sprite()
        self.set_background()
        self.set_settings()
        self.main_loop()  
    
    def set_settings(self):
        self.clock = pygame.time.Clock() 
        self.fps = 60
        pygame.time.set_timer(PIPE_SPAWN_EVENT, PIPE_SPAWN_INTERVAL)
        
    def set_sprite(self):
        self.my_player = player.Player("assets/1.png")
        
        #set sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.obstacle_group = pygame.sprite.Group()
        
        for i in range(0,10):
            self.background = background.Background("assets/1.png", i)
            self.all_sprites.add(self.background)
          
        #add player sprite to "all_sprites" group for drawing 
    
    def set_background(self):
        pass
        
    def main_loop(self):  
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.my_player.jump()
                
                if event.type == PIPE_SPAWN_EVENT:
                    center_gap_y = randint(120,self.window_size[1]-225)
                    
                    for i in range(0,3):
                        top_obstacle = obstacle.Obstacle("assets/1.png", i, center_gap_y)
                        self.obstacle_group.add(top_obstacle) 
                        self.all_sprites.add(top_obstacle)
                    
                if event.type == pygame.QUIT: 
                    exit()
                    
            #pos = pygame.mouse.get_pos()
            #self.my_player.set_pos(pos)
        
            #update all sprites  
            self.all_sprites.update()
            self.my_player.update()
            
            pygame.sprite.spritecollide(self.my_player, self.obstacle_group, True)
             
            self.window.fill((12, 95, 218))
            self.all_sprites.draw(self.window)
            self.my_player.draw_image(self.window) 
            
            self.clock.tick(self.fps)            
            pygame.display.flip()
        
                    
if __name__ == "__main__":
    FlappyBird()

