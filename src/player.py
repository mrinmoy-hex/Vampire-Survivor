from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprite) -> None:
        super().__init__(groups)
        self.load_images()
        self.state, self.frame_index = 'down', 0
        self.image = pygame.image.load(join("img","player", "down", "0.png")).convert_alpha()
        self.rect = self.image.get_frect(center = pos)
        self.hitbox_rect = self.rect.inflate(-60, -80)
        
        # movement
        self.player_dir = pygame.math.Vector2()
        self.player_speed = 500
        self.collision_sprites = collision_sprite
   
    def load_images(self):
        '''
        For importing player animation images
        '''
        self.frames = {'left': [],
                       'right': [],
                       'up': [],
                       'down': []
                       }
        
        for state in self.frames.keys():
            # walk function in os is used for walking into directories
            for folder_path, sub_folders, file_names in  walk(join("img", "player", state)):
                if file_names:
                    for file in sorted(file_names, key= lambda name: int(name.split('.')[0])):
                        full_path = join(folder_path, file)
                        # print(full_path)
                        surf = pygame.image.load(full_path).convert_alpha()
                        self.frames[state].append(surf)
        
        #print(self.frames)
        
        
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
        
    def animate(self, dt):
         # get state
        if self.player_dir.x != 0:
            self.state = 'right' if self.player_dir.x > 0 else  'left'
        if self.player_dir.y != 0:
            self.state = 'up' if self.player_dir.y < 0 else  'down'
         
         
         # actual animation
        self.frame_index = self.frame_index + 5 * dt if self.player_dir else 0
        # need to review the logic of animation 
        self.image = self.frames[self.state][int(self.frame_index) % len(self.frames[self.state ])]
    
    def update(self, dt) -> None:
        self.input()
        self.move(dt)
        self.animate(dt)
        



