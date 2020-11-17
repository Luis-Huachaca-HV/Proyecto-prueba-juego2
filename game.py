import pygame
import menu
from menu import Menu, Creditos, Settings
WIDTH = 844
HEIGHT = 508
Black = (0,0,0)
White = (255,255,255)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("personaje_prueba.PNG").convert()
        self.image.set_colorkey(White)
        self.rect =self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0

    def changespeed(self, y):
        self.speed_y += y        
    
    def update(self):
        self.rect.y += self.speed_y 
        player.rect.x = 210

class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        #super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pelota 1.png").convert()
        self.image.set_colorkey(White)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x -= 5



#-------------Esta función tiene un error : AttributeError: 'Player' object has no attribute '_Sprite__g'
#---------- se habla sobre el init en la clase pelota, el error puede estar ahi, igual recomiendo poner nombres sin separación en las imagenes 5:41pm 15/11
def pseudo_clasejuego():
    pygame.init()
    screen=pygame.display.set_mode([WIDTH,HEIGHT])
    clock=pygame.time.Clock()

    done= False

    fondo = pygame.image.load("fondo final.png").convert()
    all_sprite_list = pygame.sprite.Group()
    meteor_list = pygame.sprite.Group()
    laser_list = pygame.sprite.Group()
    player = Player()
    all_sprite_list.add(player)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player.changespeed(-3)
                if event.key == pygame.K_UP:
                    player.changespeed(3)
                if event.key == pygame.K_SPACE:
                    pelota = Pelota()
                    pelota.rect.x = player.rect.x + 10
                    pelota.rect.y = player.rect.y -20 

                    all_sprite_list.add(pelota)
                    laser_list.add(pelota)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.changespeed(3)
                if event.key == pygame.K_DOWN:
                    player.changespeed(-3)
     
    screen.blit(fondo,[0,0])
    all_sprite_list.update()
    all_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    '''

    #pygame.quit()

'''
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    FPS = 10  # Frames per second
    clock = pygame.time.Clock()
    fase = 0
    menu = 0
    creditos = 1
    settings = 2
    PACBOMBS = 3
    running = False
    while not running:
        pygame.display.flip()
        if fase == menu:
            f = Menu()
            if f == 0:
                fase = 3
            elif f == 1:
                fase = 1
            elif f == 2:
                fase = 2
        elif fase == creditos:
            clock.tick(10)
            pygame.display.flip()
            f = Creditos()  # esta funcion imprime los nombres de los creadores
            if f == 0:
                fase = 0
        elif fase == settings:
            Settings()
            f = Settings()
            if f == 0:
                fase = 0
            elif f == 1:
                fase = 0
            elif f == 2:
                fase = 0
        elif fase == PACBOMBS:
            #pseudo_clasejuego()
            # aca ejecutara el juego
            #running = game.process_events()
            #game.run_logic()
            #game.display_frame(screen)
            #clock.tick(10)
            Black = (0,0,0)
            White = (255,255,255)
            pygame.init()
            screen = pygame.display.set_mode([WIDTH,HEIGHT])
            clock = pygame.time.Clock()
            done = False
            score = 0

            all_sprite_list = pygame.sprite.Group()
            meteor_list = pygame.sprite.Group()
            laser_list = pygame.sprite.Group()

            
            player = Player()
            all_sprite_list.add(player)

            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done =True
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            player.changespeed(-3)
                        if event.key == pygame.K_UP:
                            player.changespeed(3)
                        if event.key == pygame.K_SPACE:
                            pelota = Pelota()
                            pelota.rect.x = player.rect.x + 10
                            pelota.rect.y = player.rect.y -20 

                            all_sprite_list.add(pelota)
                            laser_list.add(pelota)
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP:
                            player.changespeed(3)
                        if event.key == pygame.K_DOWN:
                            player.changespeed(-3)
                
                all_sprite_list.update()

                screen.fill(White)
                all_sprite_list.draw(screen)
                pygame.display.flip()
                clock.tick(60)
                pygame.quit()
'''

if __name__ == "__main__":
    main()

a = 2
B = "este es un cambio de prueba"
'''