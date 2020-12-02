import pygame
import random
import menu
import math
from menu import Menu, Creditos, Settings
WIDTH = 844
HEIGHT = 508
Black = (0, 0, 0)
White = (255, 255, 255)
Verde = (0, 255, 0)
clock = pygame.time.Clock()
pygame.display.set_mode()

pygame.mixer.init()
sound = pygame.mixer.Sound("audio_trote.ogg")
sound2 = pygame.mixer.Sound("audio_trote.ogg")
sound3 = pygame.mixer.Sound("audio_trote.ogg")
sound4 = pygame.mixer.Sound("audio_estadio.ogg")
sound5 = pygame.mixer.Sound("grito_golpe.ogg")
sound6 = pygame.mixer.Sound("grito_muerte.wav")

#----------ARREGLO DE IMÁGENES-DERECHA------------------#
image_EN1 = pygame.image.load("img/enemy_1.png").convert()
image_EN2 = pygame.image.load("img/enemy_6.png").convert()
image_EN3 = pygame.image.load("img/enemy_7.png").convert()

imageEN = [image_EN1, image_EN2, image_EN3]
# ---------------sprites derecha----------------------
image_PN1 = pygame.image.load("img/player_1.png").convert()
image_PN3 = pygame.image.load("img/player_6.png").convert()
image_PN2 = pygame.image.load("img/player_7.png").convert()

imagePN = [image_PN1, image_PN2, image_PN3]


imageN = [imagePN, imageEN]  # encima de esta lina pon los sprites del enemy
'''
# ---------------sprites izquierda----------------------
image_PI1 = pygame.image.load("img/player_7.png").convert()
image_PI2 = pygame.image.load("img/player_6.png").convert()
image_PI3 = pygame.image.load("img/player_1.png").convert()
imagePI = [image_PI1,image_PI2,image_PI3]

imageI = [image_PI, image_EI] #encima de esta lina pon los sprites del enemy
'''
# ---------------sprites lanzar player----------------------
image_PL1 = pygame.image.load("img/player_3.png").convert()
image_PL2 = pygame.image.load("img/player_4.png").convert()
imagePL = [image_PL1, image_PL2]
# sprites lanzar enemy
image_EL1 = pygame.image.load("img/enemy_3.png").convert()
image_EL2 = pygame.image.load("img/enemy_4.png").convert()
imageEL = [image_EL1, image_EL2]

imageL = [imagePL, imageEL]  # encima de esta lina pon los sprites del enemy

# images = [imageN,imageL]
# image = imageN[personaje][animación]
# balon(lanzamiento) = imageL[personaje][animacion]
# ----------------SPRITES PELOTA----------------
pel_1 = pygame.image.load("img/pelota_1.png").convert()
pel_2 = pygame.image.load("img/pelota_2.png").convert()
pel_3 = pygame.image.load("img/pelota_3.png").convert()
pel_4 = pygame.image.load("img/pelota_4.png").convert()
pel_5 = pygame.image.load("img/pelota_5.png").convert()
pel_6 = pygame.image.load("img/pelota_6.png").convert()

l_pel = [pel_1, pel_2, pel_3]


def colision(px, py, ex, ey,):
    '''px = self.player.rect.x
    py = self.player.rect.y
    ex = self.enemy.rect.x
    ey = self.enemy.rect.y'''
    b = math.sqrt(((ex-px)**2)+((ey-py)**2))
    if b < 27:
        return True
    else:
        return False


class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.images = []
        self.image = l_pel[0]
        self.image.set_colorkey(Verde)
        # self.image.append()
        self.index = 0
       # self.pelo_clock = pygame.time.Clock()
        # se
        self.rect = self.image.get_rect()
        self.lanzador = ""

    def update(self):
        self.image = l_pel[self.index]
        self.image.set_colorkey(Verde)
        self.index += 1
        if self.index >= len(l_pel)-1:
            self.index = 0
        if self.lanzador == "enemy":  # se activa enemy cuando lo lanza el enemigo
            self.rect.x -= 25
        elif self.lanzador == "player":  # se activa player cuando lo lanza el jugador
            self.rect.x += 25


class Enemy_sin_IA(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []
        self.image = imageN[1][0]
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.images.append(self.image)
        self.index = 0
        self.imagen = self.images[self.index]
        self.vida = 30
        self.speed_x = 0
        self.speed_y = 0
        self.rect.y = 320
        self.rect.x = 640
        self.vida = 10
        '''self.estado ='''

    def changespeed(self, y, x):
        self.speed_y += y
        self.speed_x += x

    def update(self):
        # print(self.rect.x,self.rect.y)
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_RIGHT]:
            self.image = imageN[1][0]
            self.images = imageN[1]
            self.image.set_colorkey(Black)
            sound.play()

        elif tecla[pygame.K_LEFT]:
            self.image = imageN[1][0]
            self.images = imageN[1]
            self.image.set_colorkey(Black)
            sound.play()

        elif tecla[pygame.K_UP]:
            self.image = imageN[1][0]
            self.images = imageN[1]
            self.image.set_colorkey(Black)
            sound.play()

        elif tecla[pygame.K_DOWN]:
            self.image = imageN[1][0]
            self.images = imageN[1]
            self.image.set_colorkey(Black)
            sound.play()

        elif tecla[pygame.K_m]:
            self.image = imageN[1][0]
            self.images = imageL[1]
            self.image.set_colorkey(Black)

        elif self.vida == 0:
            self.images = [pygame.image.load("img/enemy_5.png")]
            
        else:
            self.image = imageN[1][0]
            self.images = [self.image]

        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.image.set_colorkey(Black)
        self.index += 1

        if self.rect.y < 239:
            self.rect.y = 239
        if self.rect.y > 395:
            self.rect.y = 395
        if self.rect.x > 745:
            self.rect.x = 745
        if self.rect.x < 424:
            self.rect.x = 424
        # if self.rect.
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x


class enemy(pygame.sprite.Sprite):
    def __init__(self,lvl,lives=0):
        super().__init__()
        self.lvl = lvl
        self.lives = lives
        self.image = pygame.image.load("enemigo_1.png").convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = 363 + (215)
        self.rect.y = 198 + (100)
        self.x_objetivo = 578                             
        self.y_objetivo = 298

        Level_names =[["BOT Harry","BOT Ron","BOT Hermione"],["BOT Luke","BOT Leia","BOT Solo"],["BOT Ayrton","BOT Cesar","BOT Luis","BOT Rafael"]]

        if self.lvl == 1:
            self.name = Level_names[0][random.randint(0,2)]
            self.lvl_alias = "Fácil"
            self.lives = 5
            self.pct_throw = 15
            self.pct_move = 300
            self.pct_none = 100
        elif self.lvl == 2:
            self.name = Level_names[1][random.randint(0,2)]
            self.lvl_alias = "Normal"
            self.lives = 10
            self.pct_throw = 25
            self.pct_move = 500
            self.pct_none = 100
        elif self.lvl == 3:
            self.name = Level_names[2][random.randint(0,3)]
            self.lvl_alias = "Difícil"
            self.lives = 15
            self.pct_throw = 45
            self.pct_move = 800
            self.pct_none = 100

    def __del__(self):
        del self.image
        del self.rect
        

    def move1(self):                                                                                        #       <----------------     Función MOVERSE
        validacion_x = self.rect.x >= self.x_objetivo - 8 and self.rect.x  <= self.x_objetivo + 8
        validacion_y = self.rect.y >= self.y_objetivo - 8 and self.rect.y  <= self.y_objetivo + 8
        if(validacion_x and validacion_y):
            self.x_objetivo = random.randint(440,615)
            self.y_objetivo = random.randint(210,390)
        else:
            # X izquierda
            if (self.x_objetivo < self.rect.x):
                self.rect.x -= 6 
                # X aderecha
            if (self.x_objetivo > self.rect.x):
                self.rect.x += 6 
                # Y arriba 
            if (self.y_objetivo > self.rect.y):
                self.rect.y += 6 
                # Y abajo 
            if (self.y_objetivo < self.rect.y):
                self.rect.y -= 6 


    def atak(self):
        pelota_enemigo = Pelota2()
        pelota_enemigo.rect.x = self.rect.x - 10
        pelota_enemigo.rect.y = self.rect.y + 20
        pelota_enemy_list.add(pelota_enemigo)
        all_sprite_list.add(pelota_enemigo)
        
    def damage(self):
        self.lives -= 1
        

    def porcentaje(self):
        self.pct = random.randint(14,1000)
        if self.pct <= self.pct_throw:
            self.atak()
        
        else:
            self.move1()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []
        self.image = imageN[0][0]
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.images.append(self.image)
        self.index = 0
        self.imagen = self.images[self.index]
        self.vida = 10
        self.speed_x = 0
        self.speed_y = 0
        self.rect.y = 320
        self.rect.x = 71

    def update(self):
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_d]:
            self.image = imageN[0][0]
            self.images = imageN[0]
            self.image.set_colorkey(Black)
            sound2.play()

        elif tecla[pygame.K_a]:
            self.image = imageN[0][0]
            self.images = imageN[0]
            self.image.set_colorkey(Black)
            sound2.play()

        elif tecla[pygame.K_w]:
            self.image = imageN[0][0]
            self.images = imageN[0]
            self.image.set_colorkey(Black)
            sound2.play()

        elif tecla[pygame.K_s]:
            self.image = imageN[0][0]
            self.images = imageN[0]
            self.image.set_colorkey(Black)
            sound2.play()

        elif tecla[pygame.K_c]:
            self.image = imageN[0][0]
            self.images = imageL[0]
            self.image.set_colorkey(Black)

        elif self.vida == 0:
            self.images = [pygame.image.load("img/player_5.png")]
            
        else:
            self.image = imageN[0][0]
            self.images = [self.image]

        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.image.set_colorkey(Black)
        self.index += 1

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

    def changespeed(self, y, x):
        self.speed_y += y
        self.speed_x += x


class Game(object):
    def __init__(self):
        
        self.player = Player()
        
        self.enemy = Enemy_sin_IA()
        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.player)
        self.all_sprites_list.add(self.enemy)
        self.my_players = pygame.sprite.Group(self.enemy)
        self.pelota_player_list = pygame.sprite.Group()
        self.pelota_enemy_list = pygame.sprite.Group()   

    def process_events(self):
        pygame.init()
        #--------CHOQUES CON COLLIDE---------------#
        pygame.sprite.groupcollide(self.pelota_enemy_list,self.pelota_player_list,True,True)
        for pelota in self.pelota_player_list:                             
            if pelota.rect.x >= 844:
                self.pelota_player_list.remove(pelota)

        for pelota in self.pelota_enemy_list:                         
            if pelota.rect.x <= -80: #COLLISION 
                self.pelota_enemy_list.remove(pelota)

        if pygame.sprite.spritecollide(self.player, self.pelota_enemy_list, True, collided = None):
            #player.damage()
            self.player.vida -= 1
            if self.player.vida == 0:
                pass
                #sound6.play()
                #print("He muerto:C")
                #self.enemy.image = pygame.image.load("img/enemy_5.png")
            #print(self.player.vida)
            #sound5.play()

        if pygame.sprite.spritecollide(self.enemy, self.pelota_player_list, True, collided = None):
            #enemigo1.damage()
            self.enemy.vida -= 1
            if self.enemy.vida == 0:
                pass
                #sound6.play()
                #print("He muerto:C")
                #self.enemy.image = pygame.image.load("img/enemy_5.png")
            #print(self.enemy.vida)
            #sound5.play()
            


        '''
        if colision(self.pelota.rect.x, self.pelota.rect.y, self.enemy.rect.x, self.enemy.rect.y) == True:
            self.pelota.rect.x = -1000
            self.pelota.rect.y = -100
            self.enemy.vida -= 5
            if self.enemy.vida == 0:
                sound6.play()
                print("He muerto:C")
               #self.enemy.image = pygame.image.load("img/enemy_5.png")
            print(self.enemy.vida)
            sound5.play()
        if colision(self.pelo_enemy.rect.x, self.pelo_enemy.rect.y, self.player.rect.x, self.player.rect.y) == True:
            self.pelo_enemy.rect.x = -1000
            self.pelo_enemy.rect.y = -100
            self.player.vida -= 5
            if self.player.vida == 0:
                sound6.play()
                print("He muerto:C")
               #self.enemy.image = pygame.image.load("img/enemy_5.png")
            print(self.player.vida)
            sound5.play()'''
            
        '''hits = pygame.sprite.spritecollide(Player, Pelota, True)'''

        '''if hits:
            print("choco")'''
        # acerte1 = pygame.sprite.groupcollide(self.pelota_list,self.my_players, True, True)
        # acerte2 = pygame.sprite.groupcollide(self.pelo_enemy,self.player, True, True)
        # if acerte1:
        # print("enemy recibio un golpe")
        # if acerte2:
        #    print("player recibio un golpe")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player.changespeed(-6, 0)
                if event.key == pygame.K_a:
                    self.player.changespeed(0, -6)
                if event.key == pygame.K_s:
                    self.player.changespeed(6, 0)
                if event.key == pygame.K_d:
                    self.player.changespeed(0, 6)
                if event.key == pygame.K_UP:
                    self.enemy.changespeed(-6, 0)
                if event.key == pygame.K_LEFT:
                    self.enemy.changespeed(0, -6)
                if event.key == pygame.K_DOWN:
                    self.enemy.changespeed(6, 0)
                if event.key == pygame.K_RIGHT:
                    self.enemy.changespeed(0, 6)
                if event.key == pygame.K_c:
                    if(len(self.pelota_player_list) <= 3):
                        pelota = Pelota()
                        pelota.lanzador = "player"
                        pelota.rect.x = self.player.rect.x + 10
                        pelota.rect.y = self.player.rect.y - 20
                        self.all_sprites_list.add(pelota)
                        self.pelota_player_list.add(pelota)
                        # clock = pygame.time.Clock()

                        #self.pelota_list.add(self.pelota)
                        # self.pelota.pelo_clock.tick(13)

                if event.key == pygame.K_m:
                    if(len(self.pelota_enemy_list) <= 3):
                        pelo_enemy = Pelota()
                        pelo_enemy.lanzador = "enemy"
                        pelo_enemy.rect.x = self.enemy.rect.x + 10
                        pelo_enemy.rect.y = self.enemy.rect.y - 20
                        self.all_sprites_list.add(pelo_enemy)
                        self.pelota_enemy_list.add(pelo_enemy)
                        #self.pelota_list.add(self.pelo_enemy)
                        # self.pelo_enemy.pelo_clock.tick(13)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.player.changespeed(6, 0)
                if event.key == pygame.K_a:
                    self.player.changespeed(0, 6)
                if event.key == pygame.K_s:
                    self.player.changespeed(-6, 0)
                if event.key == pygame.K_d:
                    self.player.changespeed(0, -6)
                if event.key == pygame.K_UP:
                    self.enemy.changespeed(6, 0)
                if event.key == pygame.K_LEFT:
                    self.enemy.changespeed(0, 6)
                if event.key == pygame.K_DOWN:
                    self.enemy.changespeed(-6, 0)
                if event.key == pygame.K_RIGHT:
                    self.enemy.changespeed(0, -6)
        return False

    def run_logic(self):

        self.all_sprites_list.update()

    def display_frame(self, screen):
        screen.fill(White)
        fondo = pygame.image.load("img/fondo_final.png").convert()
        screen.blit(fondo, [0, 0])
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
                pygame.mixer.music.set_volume(0)
                sound4.play(3)
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
            if f == 0:
                running = game.process_events()
                game.run_logic()
                game.display_frame(screen)
                clock.tick(9)
            elif f == 1:
                #acá ejecutara la clase juego de el p vs IA
                pass


            # pseudo_clasejuego()
            # aca ejecutara el juego
            # running = game.process_events()
            # game.run_logic()
            # game.display_frame(screen)
            # clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()
