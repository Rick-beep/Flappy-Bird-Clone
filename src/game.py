import pygame
import player
import obstacle
import random
import setting

class FlappyBird():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((640, 320))
        self.set_sprite()
        self.set_settings()
        self.main_loop()     
    
    def set_settings(self):
        self.clock = pygame.time.Clock()
        self.fps = 60
        
    def set_sprite(self):
        self.my_player = player.Player("assets/1.png")
        self.all_sprites = pygame.sprite.Group()
        self.obstacle_group = pygame.sprite.Group()
        
        for _ in range(0,10):
            new_obstacle = obstacle.Obstacle("assets/1.png")
            
            self.obstacle_group.add(new_obstacle) 
            self.all_sprites.add(new_obstacle)         
            
        self.all_sprites.add(self.my_player)
        
        
    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.my_player.jump()
                if event.type == pygame.QUIT:
                    exit()
                    
            pos = pygame.mouse.get_pos()
            self.my_player.set_pos(pos)
            
            self.my_player.update()
            
            pygame.sprite.spritecollide(self.my_player, self.obstacle_group, True)
            
            self.window.fill((135, 206, 235))
            self.all_sprites.draw(self.window)
            
            self.clock.tick(self.fps)            
            pygame.display.flip()
        
                    
                    
if __name__ == "__main__":
    FlappyBird()
    import pygame

