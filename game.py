import sys
import pygame
import pytmx
import pyscroll
from player import Player

class Game():
    
    def __init__(self):
        print("creation d'un game")
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 400))
        pygame.display.set_caption("Justice")

        # charger la carte
        tmx_data = pytmx.util_pygame.load_pygame('../tiled/test.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1

        # initialiser le player
        obj_player = tmx_data.get_object_by_name("player")
        self.player = Player(obj_player.x, obj_player.y)

        # dessiner le calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=2)
        self.group.add(self.player)



        self.run()

    def update(self):
        self.group.update()

        #self.player.fall()
        # verif collision avec env
        player_sprite = self.group.sprites()[0]
        print(player_sprite)
        if player_sprite.hitbox.collidelist(self.walls) > -1:
            print("collide")
       

    def run(self):
        clock = pygame.time.Clock()

        while True:
            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # contour
            pygame.draw.rect(self.player.image, (255, 0, 0), self.player.image.get_rect(), 2)
            pygame.draw.rect(self.screen, (125, 0, 0), self.player.player_hitbox, 2)

            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)


            # Dessin sur la fenêtre
            pygame.display.flip()  # Mettre à jour l'affichage            
            clock.tick(60)  # Limiter le taux de rafraîchissement à 60 FPS
