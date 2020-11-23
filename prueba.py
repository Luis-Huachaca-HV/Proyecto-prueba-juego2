<<<<<<< HEAD
import pygame
import random
=======
import pygame,random
#----------------------cLASE eENENEMY-----------
#terminar esto
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
        print(self.rect.x,self.rect.y)
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
class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/pelota_1.png").convert()
        self.image.set_colorkey(Verde)
        self.rect = self.image.get_rect()
>>>>>>> 7c825ea594bee5d73f969d5bb32d2c48d80ab79f

    def update(self):
        self.rect.x += 5
#----------------------Clase PLAYER---------------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/player_3.png").convert()
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0
        self.rect.y = 320
<<<<<<< HEAD
        self.rect.x = 51

    def changespeed(self, y, x):
        self.speed_y += y
        self.speed_x += x

    def update(self):
        print(self.rect.x, "x", self.rect.y, "y")
        self.rect.y += self.speed_y
=======
        self.rect.x = 71
    
    def changespeed(self, y,x):
        self.speed_y += y  
        self.speed_x += x      
    
    def update(self):
        #print(self.rect.x,self.rect.y)
        if self.rect.y < 239:
            self.rect.y = 239
        if self.rect.y > 395:
            self.rect.y = 395
        if self.rect.x > 365:
            self.rect.x = 365
        if self.rect.x < 47:
            self.rect.x = 47
        #if self.rect.
        self.rect.y += self.speed_y 
>>>>>>> 7c825ea594bee5d73f969d5bb32d2c48d80ab79f
        self.rect.x += self.speed_x


class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/pelota_1.png").convert()
        self.image.set_colorkey(Verde)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += 5


Black = (0, 0, 0)
White = (255, 255, 255)
Verde = (0, 255, 0)
pygame.init()
screen = pygame.display.set_mode([844, 508])
fondo = pygame.image.load("img/fondo_final.png").convert()
clock = pygame.time.Clock()
done = False
score = 0

all_sprite_list = pygame.sprite.Group()
#meteor_list = pygame.sprite.Group()
pelota_list = pygame.sprite.Group()


player = Player()
enemy = Enemy_sin_IA()
all_sprite_list.add(player)
all_sprite_list.add(enemy)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
<<<<<<< HEAD
            if event.key == pygame.K_UP:
                if player.rect.y > 218:
                    player.changespeed(0, 0)
                else:
                    player.changespeed(0, 0)
            if event.key == pygame.K_LEFT:
                if player.rect.x > 40:
                    player.changespeed(0, 0)
                else:
                    player.changespeed(0, 0)
            if event.key == pygame.K_DOWN:
                if player.rect.y < 392:
                    player.changespeed(0, 0)
                else:
                    player.changespeed(0, 0)
            if event.key == pygame.K_RIGHT:
                if player.rect.x < 366:
                    player.changespeed(0, 0)
                else:
                    player.changespeed(0, 0)
=======
            if event.key == pygame.K_UP :
                player.changespeed(-3,0)
            if event.key == pygame.K_LEFT:
                player.changespeed(0,-3)
            if event.key == pygame.K_DOWN :
                player.changespeed(3,0)
            if event.key == pygame.K_RIGHT :
                player.changespeed(0,3)
            if event.key == pygame.K_w :
                enemy.changespeed(-3,0)
            if event.key == pygame.K_a:
                enemy.changespeed(0,-3)
            if event.key == pygame.K_s :
                enemy.changespeed(3,0)
            if event.key == pygame.K_d :
                enemy.changespeed(0,3)
>>>>>>> 7c825ea594bee5d73f969d5bb32d2c48d80ab79f
            if event.key == pygame.K_SPACE:
                pelota = Pelota()
                pelota.rect.x = player.rect.x + 10
                pelota.rect.y = player.rect.y - 20

                all_sprite_list.add(pelota)
                pelota_list.add(pelota)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                if player.rect.y > 218:
                    player.changespeed(0, 0)
                else:
                    player.changespeed(0, 0)
            if event.key == pygame.K_LEFT:
                if player.rect.x > 40:
                    player.changespeed(0, 0)
                else:
                    player.changespeed(0, 0)

            if event.key == pygame.K_DOWN:
<<<<<<< HEAD
                if player.rect.y < 392:
                    player.changespeed(0, 0)
                else:
                    player.changespeed(0, 0)
                # player.changespeed(-3,0)
            if event.key == pygame.K_RIGHT:
                if player.rect.x < 366:
                    player.changespeed(0, 0)
                else:
                    player.changespeed(0, 0)
                # player.changespeed(0,-3)

=======
                player.changespeed(-3,0)
            if event.key == pygame.K_RIGHT :
                player.changespeed(0,-3)
            if event.key == pygame.K_w:
                enemy.changespeed(3,0)
            if event.key == pygame.K_a:
                enemy.changespeed(0,3)
            if event.key == pygame.K_s:
                enemy.changespeed(-3,0)
            if event.key == pygame.K_d :
                enemy.changespeed(0,-3)
            
        
     
>>>>>>> 7c825ea594bee5d73f969d5bb32d2c48d80ab79f
    all_sprite_list.update()

    screen.fill(White)
    screen.blit(fondo, [0, 0])
    all_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
