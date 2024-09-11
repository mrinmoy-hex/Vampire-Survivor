from settings import *
from player import Player
from sprites import *
from pytmx.util_pygame import load_pygame
from groups import AllSprites

class Game:
    def __init__(self) -> None:
        # basic setup
        pygame.init()
        self.game_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Vampire Survivor")
        self.running = True
        self.clock = pygame.time.Clock()
        
        # groups
        self.all_sprites = AllSprites ()
        self.collision_sprite = pygame.sprite.Group()
        
        self.setup()
                 
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
        
        for obj in map.get_layer_by_name('Entities'):
            if obj.name == 'Player':
                self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprite)
        
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
            self.all_sprites.draw(self.player.rect.center)
            
            pygame.display.update()
        
        pygame.quit()
        
if __name__ == '__main__':
    game = Game()
    game.run()