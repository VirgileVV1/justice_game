import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.tile_size = 128

        self.images = {
            'left': pygame.image.load("../img/Shinobi/Run_green.png"),
            'right': pygame.image.load("../img/Shinobi/Run_green.png"),
            'idle': pygame.image.load("../img/Shinobi/Idle_green.png"),
            'left': pygame.image.load("../img/Shinobi/Run_green.png"),
            'jump': pygame.image.load('../img/Shinobi/Jump_green.png')            
        }

        self.sprite_sheet = self.images['idle']
        self.image = self.get_image(0, 0)           #Surface 128x128
        self.image.set_colorkey([0, 255 ,0])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        print("self.rect" , self.rect)

        self.player_hitbox = pygame.Rect(0, 0, self.rect.width * 0.5, 100)
        print("self.player_hitbox", self.player_hitbox)

        #self.rect.topleft = self.position
        print("self.player_hitbox.midbottom", self.player_hitbox.midbottom)
        print("self.rect.midbottom", self.rect.midbottom)
        self.player_hitbox.midbottom = self.rect.midbottom


        

        


    def update(self):
        # Logique de mise à jour du joueur (si nécessaire)
        pass

    def get_image(self, x, y):
        image = pygame.Surface([self.tile_size, self.tile_size])
        image.blit(self.sprite_sheet, (0, 0), (x, y, self.tile_size, self.tile_size))
        return image