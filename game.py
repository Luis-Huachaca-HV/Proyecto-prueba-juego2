import pygame,random
import menu
from menu import Menu, Creditos, Settings
WIDTH = 844
HEIGHT = 508
Black = (0,0,0)
White = (255,255,255)
Verde = (0,255,0)
clock = pygame.time.Clock()

class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/pelota_1.png").convert()
        self.image.set_colorkey(Verde)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += 5

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/enemy_1.png").convert()
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0
    def update(self):
        self.rect.y += self.speed_y 
        self.rect.x += self.speed_x
    def changespeed(self, y,x):
        self.speed_y += y  
        self.speed_x += x 

class Game(object):
    def __init__(self):
        self.player = Player()
        #self.pelota = Pelota()
        self.pelota_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.player)
    def process_events(self):
        pygame.init()
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

                    self.all_sprites_list.add(self.pelota)
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
        return False    
    def run_logic(self):
        self.all_sprites_list.update()
    def display_frame(self,screen):
        screen.fill(White)
        fondo = pygame.image.load("img/fondo_final.png").convert()
        screen.blit(fondo,[0,0])
        self.all_sprites_list.draw(screen)
        pygame.display.flip()


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
    game = Game()
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
            running = game.process_events()
            game.run_logic()
            game.display_frame(screen)
            clock.tick(60)
            #pseudo_clasejuego()
            # aca ejecutara el juego
            #running = game.process_events()
            #game.run_logic()
            #game.display_frame(screen)
            #clock.tick(10)
            
    pygame.quit()
            

if __name__ == "__main__":
    main()

a = 2
B = "este es un cambio de prueba"
