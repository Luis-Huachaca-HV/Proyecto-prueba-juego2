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
            Settings()
            f = Settings()
            if f == 0:
                fase = 0
            elif f == 1:
                fase = 0
            elif f == 2:
                fase = 0
        elif fase == PACBOMBS:
            #aca ejecutara el juego
            running = game.process_events()
            game.run_logic()
            game.display_frame(screen)
            clock.tick(10)
    pygame.quit()
if __name__ == "__main__":
    main()

