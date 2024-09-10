from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups) -> None:
        super().__init__(groups)
        self.image = pygame.image.load(join("img","player", "down", "0.png")).convert_alpha()
        self.rect = self.image.get_frect(center = pos)
        
        # movement
        self.player_dir = pygame.math.Vector2()
        self.player_speed = 500
        
    def input(self):
        keys = pygame.key.get_pressed()
        self.player_dir.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.player_dir.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.player_dir = self.player_dir.normalize() if self.player_dir else self.player_dir
        
    def move(self, dt):
        self.rect.center += self.player_dir * self.player_speed * dt
    
    def update(self, dt) -> None:
        self.input()
        self.move(dt)
        



