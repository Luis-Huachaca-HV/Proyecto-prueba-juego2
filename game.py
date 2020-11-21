import pygame,random
import menu
from menu import Menu, Creditos, Settings
WIDTH = 844
HEIGHT = 508
Black = (0,0,0)
White = (255,255,255)
Verde = (0,255,0)
clock = pygame.time.Clock()

#---------------sprites derecha----------------------
image_PN1 = pygame.image.load("img/player_1.png").convert()
image_PN2 = pygame.image.load("img/player_6.png").convert()
image_PN3 = pygame.image.load("img/player_7.png").convert()
imagePN = [image_PN1,image_PN2,image_PN3]

imageN = [image_PN, image_EN] #encima de esta lina pon los sprites del enemy
'''
#---------------sprites izquierda----------------------
image_PI1 = pygame.image.load("img/player_7.png").convert()
image_PI2 = pygame.image.load("img/player_6.png").convert()
image_PI3 = pygame.image.load("img/player_1.png").convert()
imagePI = [image_PI1,image_PI2,image_PI3]

imageI = [image_PI, image_EI] #encima de esta lina pon los sprites del enemy
'''
#---------------sprites lanzar----------------------
image_PL1 = pygame.image.load("img/player_3.png").convert()
image_PL2 = pygame.image.load("img/player_4.png").convert()
imagePL = [image_PL1, image_PL2]

imageL = [imagePL, imageEL] #encima de esta lina pon los sprites del enemy


class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/pelota_1.png").convert()
        self.image.set_colorkey(Verde)
        self.rect = self.image.get_rect()
        self.lanzador = ""
    def update(self):
        if self.lanzador == "enemy":#se activa enemy cuando lo lanza el enemigo
            self.rect.x -= 5
        elif self.lanzador == "player":#se activa player cuando lo lanza el jugador
            self.rect.x += 5
class Enemy_sin_IA(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/enemy_1.png").convert()
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0
        self.rect.y = 320
        self.rect.x = 640
    
    def changespeed(self, y,x):
        self.speed_y += y  
        self.speed_x += x      
    
    def update(self):
        #print(self.rect.x,self.rect.y)
        if self.rect.y < 239:
            self.rect.y = 239
        if self.rect.y > 395:
            self.rect.y = 395
        if self.rect.x > 745:
            self.rect.x = 745
        if self.rect.x < 424:
            self.rect.x = 424
        #if self.rect.
        self.rect.y += self.speed_y 
        self.rect.x += self.speed_x
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/player_1.png").convert()
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0
        self.rect.y = 320
        self.rect.x = 71
    def update(self):
        self.tecla = pygame.key.get_pressed()
        if self.tecla[pygame.K_RIGHT]:

        if self.rect.y < 239:
            self.rect.y = 239
        if self.rect.y > 395:
            self.rect.y = 395
        if self.rect.x > 365:
            self.rect.x = 365
        if self.rect.x < 47:
            self.rect.x = 47
        self.rect.y += self.speed_y 
        self.rect.x += self.speed_x
    def changespeed(self, y,x):
        self.speed_y += y  
        self.speed_x += x 

class Game(object):
    def __init__(self):
        self.player = Player()
        self.enemy = Enemy_sin_IA()
        #self.pelota = Pelota()
        self.pelota_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.player)
        self.all_sprites_list.add(self.enemy)
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
                if event.key == pygame.K_w :
                    self.enemy.changespeed(-3,0)
                if event.key == pygame.K_a:
                    self.enemy.changespeed(0,-3)
                if event.key == pygame.K_s :
                    self.enemy.changespeed(3,0)
                if event.key == pygame.K_d :
                    self.enemy.changespeed(0,3)
                if event.key == pygame.K_SPACE:
                    self.pelota = Pelota()
                    self.pelota.lanzador = "player"
                    self.pelota.rect.x = self.player.rect.x + 10
                    self.pelota.rect.y = self.player.rect.y -20 

                    self.all_sprites_list.add(self.pelota)
                    self.pelota_list.add(self.pelota)
                if event.key == pygame.K_m:
                    self.pelo_enemy = Pelota()
                    self.pelo_enemy.lanzador = "enemy"
                    self.pelo_enemy.rect.x = self.enemy.rect.x + 10
                    self.pelo_enemy.rect.y = self.enemy.rect.y -20 
                    self.all_sprites_list.add(self.pelo_enemy)
                    self.pelota_list.add(self.pelo_enemy)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.player.changespeed(3,0)
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(0,3)
                if event.key == pygame.K_DOWN:
                    self.player.changespeed(-3,0)
                if event.key == pygame.K_RIGHT:
                    self.player.changespeed(0,-3)
                if event.key == pygame.K_w:
                    self.enemy.changespeed(3,0)
                if event.key == pygame.K_a:
                    self.enemy.changespeed(0,3)
                if event.key == pygame.K_s:
                    self.enemy.changespeed(-3,0)
                if event.key == pygame.K_d :
                    self.enemy.changespeed(0,-3)
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
    DODGE = 3
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
        elif fase == DODGE:
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

