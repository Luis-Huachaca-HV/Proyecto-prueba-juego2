import pygame,random
import menu
from menu import Menu, Creditos, Settings
WIDTH = 844
HEIGHT = 508
Black = (0,0,0)
White = (255,255,255)
Verde = (0,255,0)
clock = pygame.time.Clock()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/player_3.png").convert()
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0
    
    def changespeed(self, y,x):
        self.speed_y += y  
        self.speed_x += x      
    
    def update(self):
        self.rect.y += self.speed_y 
        self.rect.x += self.speed_x
class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/pelota_1.png").convert()
        self.image.set_colorkey(Verde)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += 5

class Game(object):
    def __init__(self):
        self.all_sprite_list = pygame.sprite.Group()
        self.meteor_list = pygame.sprite.Group()
        self.pelota_list = pygame.sprite.Group()
        self.player = Player()
        self.all_sprite_list.add(self.player)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.changespeed(-3,0)
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(0,-3)
                if event.key == pygame.K_DOWN:
                    self.player.changespeed(3,0)
                if event.key == pygame.K_RIGHT:
                    self.player.changespeed(0,3)
                if event.key == pygame.K_SPACE:
                    self.pelota = Pelota()
                    self.pelota.rect.x = self.player.rect.x + 10
                    self.pelota.rect.y = self.player.rect.y -20 

                    self.all_sprite_list.add(self.pelota)
                    self.pelota_list.add(self.pelota)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.player.changespeed(3,0)
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(0,3)
                if event.key == pygame.K_DOWN:
                    self.player.changespeed(-3,0)
                if event.key == pygame.K_RIGHT:
                    self.player.changespeed(0,-3)
  

    def run_logic(self):
        self.all_sprite_list.update()
    def display_frame(self,screen):
        screen.fill(White)
        fondo = pygame.image.load("img/fondo_final.png").convert()
        screen.blit(fondo,[0,0])
        self.all_sprite_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        
#-------------Esta función tiene un error : AttributeError: 'Player' object has no attribute '_Sprite__g'
#---------- se habla sobre el init en la clase pelota, el error puede estar ahi, igual recomiendo poner nombres sin separación en las imagenes 5:41pm 15/11


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
            pygame.init()
            screen = pygame.display.set_mode([WIDTH,HEIGHT])
            clock = pygame.time.Clock()
            game = Game()
            running = game.process_events()
            game.run_logic()
            game.display_frame(screen)
            # pygame.display.flip()
            clock.tick(60)
    pygame.quit()
            

if __name__ == "__main__":
    main()

a = 2
B = "este es un cambio de prueba"
