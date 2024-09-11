from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprite) -> None:
        super().__init__(groups)
        self.image = pygame.image.load(join("img","player", "down", "0.png")).convert_alpha()
        self.rect = self.image.get_frect(center = pos)
        self.hitbox_rect = self.rect.inflate(-60, 0)
        
        # movement
        self.player_dir = pygame.math.Vector2()
        self.player_speed = 500
        self.collision_sprites = collision_sprite
        
    def input(self):
        keys = pygame.key.get_pressed()
        self.player_dir.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.player_dir.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.player_dir = self.player_dir.normalize() if self.player_dir else self.player_dir
        
    def move(self, dt):
        self.hitbox_rect.x += self.player_dir.x * self.player_speed * dt
        self.collision('horizontal')
        self.hitbox_rect.y += self.player_dir.y * self.player_speed * dt
        self.collision('vertical')
        self.rect.center = self.hitbox_rect.center
    
    def collision(self, dir):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox_rect):
                if dir == 'horizontal':
                    if self.player_dir.x > 0: 
                        self.hitbox_rect.right = sprite.rect.left
                    if self.player_dir.x < 0:
                        self.hitbox_rect.left = sprite.rect.right
                else:
                    if self.player_dir.y > 0:
                        self.hitbox_rect.bottom = sprite.rect.top
                    if self.player_dir.y < 0:
                        self.hitbox_rect.top = sprite.rect.bottom
    
    def update(self, dt) -> None:
        self.input()
        self.move(dt)
        



