from settings import *
 
class AllSprites(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.Vector2()  # offset is used for moving camera
        
    def draw(self, target_pos):
        self.offset.x = -(target_pos[0] - WINDOW_WIDTH/2)   # for moving camera to x axis
        self.offset.y = -(target_pos[1] - WINDOW_HEIGHT/2)  # for moving camera to y axis
        
        ground_sprites =  [sprite for sprite in self if hasattr(sprite, 'ground')]
        object_sprites =  [sprite for sprite in self if not hasattr(sprite, 'ground')]
        
        for layer in [ground_sprites, object_sprites]:
            for sprite in sorted(layer, key = lambda sprite: sprite.rect.centery):   # this ensures that the obj having more center pos will be drawn later
                # to make camera the drawing method should be customized 
                self.display_surface.blit(sprite.image, sprite.rect.topleft +  self.offset) 