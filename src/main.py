from settings import *
from player import Player
from sprites import *
from random import randint
from pytmx.util_pygame import load_pygame

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
        
        self.setup()
        
        # sprites
        self.player = Player((500, 300), self.all_sprites, self.collision_sprite)
    
    
    def setup(self):
        map = load_pygame(join('data', 'maps', 'world.tmx'))
        # for ground
        for x, y, image in map.get_layer_by_name('Ground').tiles():
            StaticSprite((x * TILE_SIZE ,y * TILE_SIZE ), image, self.all_sprites)
        # for objects 
        for obj in map.get_layer_by_name('Objects'):
            CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprite))
        #for invisible collision objects
        for obj in  map.get_layer_by_name('Collisions'):
            CollisionSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprite)
        
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