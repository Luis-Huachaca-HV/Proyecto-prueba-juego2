import pygame
import random
import menu
#from Dodgeball_introIMG import *

from menu import Menu, Creditos, Settings
WIDTH = 844
HEIGHT = 508
Black = (0, 0, 0)
White = (255, 255, 255)
Verde = (0, 255, 0)
clock = pygame.time.Clock()
pygame.display.set_mode()

#------------------ANIMACIÓN INTRO-----------------------#
def intro1_anim():
    for i in intro_list:
        screen.blit(i, [0,0])
        time.sleep(0.08)
        pygame.display.update() 
def intro2_anim():
    for i in intro_list2:
        screen.blit(i, [0,0])
        time.sleep(0.1)
        pygame.display.update() 
def music_intro():
    pygame.mixer.music.load("Music/intro2.mp3")
    pygame.mixer.music.play(0)
def unload_music():
    pygame.mixer.music.stop()
def fadeout_screen(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        #redrawWindow()
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(10)


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




class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = l_pel[0]
        self.image.set_colorkey(Verde)
        
        self.index = 0

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
        
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x


class enemy(pygame.sprite.Sprite):
    def __init__(self,lvl,vida=0):
        super().__init__()
        self.lvl = lvl
        self.vida = vida      
        self.images = []
        self.image = imageN[1][0]
        self.image.set_colorkey(Black)
        self.images.append(self.image)
        
        self.rect = self.image.get_rect()
        self.index = 0
        self.lanzo = False
        self.imagen = self.images[self.index]
        self.rect.x = 363 + (215)
        self.rect.y = 198 + (100)
        self.x_objetivo = 578                             
        self.y_objetivo = 298

        Level_names =[["BOT Harry","BOT Ron","BOT Hermione"],["BOT Luke","BOT Leia","BOT Solo"],["BOT Ayrton","BOT Cesar","BOT Luis","BOT Rafael"]]
        
        if self.lvl == 1:
            self.name = Level_names[0][random.randint(0,2)]
            self.lvl_alias = "Fácil"
            self.vida = 5
            self.pct_throw = 15
            self.pct_move = 300
        elif self.lvl == 2:
            self.name = Level_names[1][random.randint(0,2)]
            self.lvl_alias = "Normal"
            self.vida = 10
            self.pct_throw = 55
            self.pct_move = 500
        elif self.lvl == 3:
            self.name = Level_names[2][random.randint(0,3)]
            self.lvl_alias = "Difícil"
            self.vida = 15
            self.pct_throw = 105
            self.pct_move = 800

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
                self.image = imageN[1][0]
                self.images = imageN[1]
                self.image.set_colorkey(Black)
                sound3.play()
                # X aderecha
            if (self.x_objetivo > self.rect.x):
                self.rect.x += 6
                self.image = imageN[1][0]
                self.images = imageN[1]
                self.image.set_colorkey(Black)
                sound3.play() 
                # Y arriba 
            if (self.y_objetivo > self.rect.y):
                self.rect.y += 6
                self.image = imageN[1][0]
                self.images = imageN[1]
                self.image.set_colorkey(Black)
                sound3.play()
                # Y abajo 
            if (self.y_objetivo < self.rect.y):
                self.rect.y -= 6
                self.image = imageN[1][0]
                self.images = imageN[1]
                self.image.set_colorkey(Black)
                sound3.play() 

        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.image.set_colorkey(Black)
        self.index += 1


    def atak(self):
        self.image = imageN[1][0]
        self.images = imageL[1]
        self.image.set_colorkey(Black)
        pelota_enemigo = Pelota()
        pelota_enemigo.lanzador = "enemy"
        pelota_enemigo.rect.x = self.rect.x - 10
        pelota_enemigo.rect.y = self.rect.y + 20
        game.pelota_enemy_list.add(pelota_enemigo)
        game.all_sprites_list.add(pelota_enemigo)
        
    def damage(self):
        self.vida -= 1
        
        
    def porcentaje(self):
        self.pct = random.randint(14,1000)
        if self.pct <= self.pct_throw:
            self.lanzo  = True
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
        self.enemigo1 = enemy(1)   
        self.game_over = False
        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.player)
        self.my_players = pygame.sprite.Group(self.enemy)
        self.pelota_player_list = pygame.sprite.Group()
        self.pelota_enemy_list = pygame.sprite.Group() 
        self.nivel1 = True
        self.nivel2 = False
        self.nivel3 = False
        
        
    def process_events(self):
        pygame.init()
        if self.proceso == "pvia":
            self.all_sprites_list.add(self.enemigo1)
        if self.proceso == "pvp":
            self.all_sprites_list.add(self.enemy)
        
        #--------CHOQUES CON COLLIDE---------------#
        pygame.sprite.groupcollide(self.pelota_enemy_list,self.pelota_player_list,True,True)

        for pelota in self.pelota_player_list:                             
            if pelota.rect.x >= 844:
                self.pelota_player_list.remove(pelota)

        for pelota in self.pelota_enemy_list:                         
            if pelota.rect.x <= -80: #COLLISION 
                self.pelota_enemy_list.remove(pelota)

        if pygame.sprite.spritecollide(self.player, self.pelota_enemy_list, True, collided = None):
            
            self.player.vida -= 1
            if self.player.vida == 0:
                self.game_over = True
                #main()

                sound6.play()
            sound5.play()

        if pygame.sprite.spritecollide(self.enemy, self.pelota_player_list, True, collided = None):
            
            self.enemy.vida -= 1
            if self.enemy.vida == 0:
                self.game_over = True
                
                
                sound6.play()

            sound5.play()
            
        
        tecla1 = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if tecla1[pygame.K_SPACE]:
                if self.game_over:
                    self.__init__()
                    pygame.display.flip()
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
                       

                if event.key == pygame.K_m:
                    if(len(self.pelota_enemy_list) <= 3):
                        pelo_enemy = Pelota()
                        pelo_enemy.lanzador = "enemy"
                        pelo_enemy.rect.x = self.enemy.rect.x + 10
                        pelo_enemy.rect.y = self.enemy.rect.y - 20
                        self.all_sprites_list.add(pelo_enemy)
                        self.pelota_enemy_list.add(pelo_enemy)
                        
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
        
    def process_events2(self):
        pygame.init()
        if self.proceso == "pvia":
            self.all_sprites_list.add(self.enemigo1)
        if self.proceso == "pvp":
            self.all_sprites_list.add(self.enemy)
        #--------CHOQUES CON COLLIDE---------------#
        #choque entre pelota1 y pelota2
        pygame.sprite.groupcollide(self.pelota_enemy_list,self.pelota_player_list,True,True)

        for pelota in self.pelota_player_list:                             
            if pelota.rect.x >= 844:
                self.pelota_player_list.remove(pelota)

        for pelota in self.pelota_enemy_list:                         
            if pelota.rect.x <= -80: #COLLISION 
                self.pelota_enemy_list.remove(pelota)

        if pygame.sprite.spritecollide(self.player, self.pelota_enemy_list, True, collided = None):
            
            self.player.vida -= 1
            if self.player.vida == 0:
                # función GAME OVER
                self.nivel1 = False
                self.game_over = True
                
                sound6.play()
            sound5.play()

       
        if pygame.sprite.spritecollide(self.enemigo1, self.pelota_player_list, True, collided = None):
            
            self.enemigo1.vida -= 1
            if self.enemigo1.vida == 0:
                self.enemigo1.image = pygame.image.load("img/enemy_5.png")
                if self.nivel1 == True:
                    self.all_sprites_list.remove(self.enemigo1)
                    del self.enemigo1
                    self.nivel1 = False
                    self.nivel2 = True
                    self.enemigo1 = enemy(2)
                    self.all_sprites_list.add(self.enemigo1)
                    sound6.play()
                    
                elif self.nivel2 == True:
                    self.all_sprites_list.remove(self.enemigo1)
                    del self.enemigo1
                    self.nivel2 = False
                    self.nivel3 = True
                    self.enemigo1 = enemy(3)
                    self.all_sprites_list.add(self.enemigo1)
                    sound6.play()
                elif self.nivel3 == True:
                    self.nivel3 = False
                    self.game_over = True  #corregir la eliminación de enemigo
                    sound6.play()
            sound5.play()           
                    
        tecla1 = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if tecla1[pygame.K_SPACE]:
                if self.game_over:
                    self.__init__()
                    pygame.display.flip()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player.changespeed(-6, 0)
                if event.key == pygame.K_a:
                    self.player.changespeed(0, -6)
                if event.key == pygame.K_s:
                    self.player.changespeed(6, 0)
                if event.key == pygame.K_d:
                    self.player.changespeed(0, 6)
                if event.key == pygame.K_c:
                    if(len(self.pelota_player_list) <= 3):
                        pelota = Pelota()
                        pelota.lanzador = "player"
                        pelota.rect.x = self.player.rect.x + 10
                        pelota.rect.y = self.player.rect.y - 20
                        self.all_sprites_list.add(pelota)
                        self.pelota_player_list.add(pelota)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.player.changespeed(6, 0)
                if event.key == pygame.K_a:
                    self.player.changespeed(0, 6)
                if event.key == pygame.K_s:
                    self.player.changespeed(-6, 0)
                if event.key == pygame.K_d:
                    self.player.changespeed(0, -6)
                              
        self.enemigo1.porcentaje()         
        
        return False    

    
    def run_logic(self):
        self.all_sprites_list.update()
        

    def display_frame(self, screen):
        screen.fill(White)
        fondo = pygame.image.load("img/fondo_final.png").convert()
        screen.blit(fondo, [0, 0])
        self.all_sprites_list.draw(screen)
        if self.game_over:
            font = pygame.font.SysFont("serif", 35)
            text = font.render("Game Over, pulse la tecla espacio para continuar", False, Black)
            center_x = (WIDTH//2)-(text.get_width()//2)
            center_y = (HEIGHT//2)-(text.get_height()//2)
            screen.blit(text, [center_x, center_y])
        if not self.game_over:
            self.all_sprites_list.draw(screen)
            pygame.display.flip()
        pygame.display.flip()

#proceso = "pvia"
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

    game.proceso = "pvp"
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
                game.proceso = "pvp"
                fase = 0
            elif f == 1:
                game.proceso = "pvia"
                fase = 0
            elif f == 2:
                fase = 0
        elif fase == DODGE:
            
            if game.proceso == "pvp":
                
                running = game.process_events()
                game.run_logic()
                game.display_frame(screen)
                clock.tick(9)
        
            elif game.proceso == "pvia":
                
                running = game.process_events2()
                game.run_logic()
                game.display_frame(screen)
                clock.tick(9)
                

    pygame.quit()
game = Game()

if __name__ == "__main__":
    main()
