from settings import *
from player import Player
from sprites import *
from random import randint

class Game:
    def __init__(self) -> None:
        # basic setup
        pygame.init()
        self.game_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Vampire Survivor")
        self.running = True
        self.clock = pygame.time.Clock()
        
        # groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprite = pygame.sprite.Group()
        
        # sprites
        self.player = Player((400, 300), self.all_sprites, self.collision_sprite)
        for i in range(6):
            x,y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
            w,h = randint(60, 100), randint(50, 100)
            CollisionSprite((x,y), (w,h), (self.all_sprites, self.collision_sprite))
    
    def run(self):
        while self.running:
            # delta time
            dt = self.clock.tick() / 1000   
            
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
   
            # update
            self.all_sprites.update(dt)
            
            # draw
            self.game_screen.fill('black')
            self.all_sprites.draw(self.game_screen)
            
            pygame.display.update()
        
        pygame.quit()
        
if __name__ == '__main__':
    game = Game()
    game.run()