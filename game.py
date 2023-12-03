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

        # dessiner le calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=2)



        self.run()


       

    def run(self):
        clock = pygame.time.Clock()

        while True:
            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



            self.group.draw(self.screen)


            # Dessin sur la fenêtre
            pygame.display.flip()  # Mettre à jour l'affichage            
            clock.tick(60)  # Limiter le taux de rafraîchissement à 60 FPS
