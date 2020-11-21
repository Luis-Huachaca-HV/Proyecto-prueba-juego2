import pygame
import random


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/player_3.png").convert()
        self.image.set_colorkey(Black)
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0
        self.rect.y = 320
        self.rect.x = 51

    def changespeed(self, y, x):
        self.speed_y += y
        self.speed_x += x

    def update(self):
        print(self.rect.x, "x", self.rect.y, "y")
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
all_sprite_list.add(player)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
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

    all_sprite_list.update()

    screen.fill(White)
    screen.blit(fondo, [0, 0])
    all_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
