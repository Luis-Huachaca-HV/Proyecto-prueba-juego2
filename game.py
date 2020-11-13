import pygame
import menu
from menu import Menu,Creditos,Settings
WIDTH = 844
HEIGHT = 508
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    FPS = 10#Frames per second
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
                pygame.mixer.music.set_volume(0)
                #sound3.play()   
            elif f == 1:
                fase = 1
            elif f == 2:
                fase = 2
        elif fase == creditos:
            clock.tick(10)
            pygame.display.flip()
            f =  Creditos()#esta funcion imprime los nombres de los creadores
            if f == 0:
                fase = 0
        elif fase == settings:
            running = game.process_events()
            Settings()
            f = Settings()
            if f == 0:
                game.player.ELE_P = 0
                game.player2.ELE_P = 1
                print(game.player.ELE_P)
                fase = 0
            elif f == 1:
                game.player.ELE_P  = 1
                game.player2.ELE_P = 0
                print(game.player.ELE_P)
                fase = 0
            elif f == 2:
                fase = 0

        elif fase == PACBOMBS:
            running = game.process_events()
            game.run_logic()
            game.display_frame(screen)
            clock.tick(10)
    pygame.quit()
#if __name__ == "__main__":
#    main()
Menu()