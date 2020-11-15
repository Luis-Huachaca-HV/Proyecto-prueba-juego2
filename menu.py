import pygame
#Definimos el estilo , color y pintamos la pantalla
def Palabrasf(Estilo,Tamano,Palabra,color,Pos,pantalla,anti=True):
        for e in range(len(Palabra)):
            PalabraFinal=pygame.font.Font(Estilo,Tamano)
            a=PalabraFinal.render(Palabra[e],anti,color)
            pantalla.blit(a,Pos[e])
#definimos la creacion del boton en el lugar indicado
def Boton(imagen,Pos,pantalla):
    mouse = pygame.mouse.get_pos()
    Rect=imagen.get_rect()
    if mouse[0]>Pos[0] and mouse[0]< Pos[0]+Rect[2]:
        if mouse[1]>Pos[1] and mouse[1]< Pos[1]+Rect[3]:
            pantalla.blit(imagen,Pos)
            return True
#definimos la funcion menu
def Menu():
##Variables:
        BLACK =(0,0,0)
        WHITE = (255,255,255)
        fase = None
        Color = (234,123,111)
        TamanoFuente = 30
        Fuente = "Texto/Assassin$.ttf"
        #,'Texto/LifeCraft_Font.ttf',"Texto/pricedown bl.ttf"]
        a=0
        Tamano_display = (844,508)
        imagenboton=pygame.image.load("2.png").convert()
        imagenboton.set_colorkey(WHITE)
        screen_fondo = pygame.image.load("SuperDodgeBall.jpg")
        pantalla = pygame.display.set_mode(Tamano_display)
        pantalla.fill(BLACK)
        pantalla.blit(screen_fondo,screen_fondo.get_rect())
##Titulo
        Palabra=['New Super World of Grand','Dodgeball Evil Creed','Offensive 64 Ultimate']
        PosicionInicial=[(50,30),(50,70),(50,110)]
        for i in Palabra:
    
            Palabrasf(Fuente,TamanoFuente,Palabra,Color,PosicionInicial,pantalla)
##Boton
        Palabra=["Play","Credits","Settings"]
        PosicionInicial=[(120,200),(120,260),(120,320)]
        for e in range(3):
            a = Boton(imagenboton,(PosicionInicial[e][0]/1.5,PosicionInicial[e][1]-(TamanoFuente/2.8)),pantalla)
            Palabrasf(Fuente,TamanoFuente,Palabra,Color,PosicionInicial,pantalla)
            if a:
                fase = e
##Eventos
    #fase son las pantallas que se mostraran en el menu
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()
            if event.type==pygame.MOUSEBUTTONDOWN or key[pygame.K_RETURN]:
                if fase == 0:
                    return 0
                elif fase == 1:
                    return 1
                elif fase == 2:
                    return 2
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    quit()

#esta fase define los valores que estaran en creditos
def Creditos():
        WHITE = (255,255,255) 
        ANY_COLOR = (0,0,0)
        Morado = (128,0,128)
        TamanoFuente = 20
        screen_fondo = pygame.image.load("SuperDodgeBall.jpg")
        Fuente = "Texto/04B_30__.TTF"
        Tamano_display = (844,508)
        #imagenfondo = 
        pantalla = pygame.display.set_mode(Tamano_display)
        pantalla.blit(screen_fondo,screen_fondo.get_rect())
##Titulo
        Palabra=["Créditos"]
        PosicionInicial=[(60,100)]
        Palabrasf(Fuente,TamanoFuente,Palabra,Morado,PosicionInicial,pantalla)
##Palabras
        Palabra=["Desarrolladores:","Luis Huachaca","Cesar Lengua","Ayrton Chávez","Rafael Ramirez"]
        PosicionInicial=[(80,180),(100,230),(100,260),(100,290),(100,320)]
        for e in range(3):
            Palabrasf(Fuente,TamanoFuente,Palabra,Morado,PosicionInicial,pantalla)

##Keys
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    return 0

def Settings():
##Variables:
        BLACK =(0,0,0)
        WHITE = (255,255,255)
        fase = None
        Color = (234,123,111)
        TamanoFuente = 30
        Fuente = "Texto/04B_30__.TTF"
        Tamano_display = (844,508)
        imagenboton=pygame.image.load("2.png").convert()
        imagenboton.set_colorkey(WHITE)
        imagenfondo=pygame.image.load("fondo menu.jpg").convert()
        pantalla = pygame.display.set_mode(Tamano_display)
        pantalla.fill(BLACK)
##Titulo
        Palabra=['Settings:']
        PosicionInicial=[(80,40)]
        Palabrasf(Fuente,TamanoFuente,Palabra,Color,PosicionInicial,pantalla)
##Boton 
        pac_choose = pygame.image.load("choose_pacman.png").convert()
        blin_choose = pygame.image.load('choose_blinky.png').convert()
        pac_choose.set_colorkey(WHITE)
        blin_choose.set_colorkey(WHITE)
        pantalla.blit(pac_choose,[250,150])
        pantalla.blit(blin_choose,[600,150])
        Palabra=["PACMAN","BLIBKY"]
        PosicionInicial=[(250,400),(600,400)];#/1.5,-(TamanoFuente/2.8)        
        for e in range(2):
            a = Boton(imagenboton,(PosicionInicial[e][0]-(TamanoFuente),PosicionInicial[e][1]-(TamanoFuente/2.6)),pantalla)
            Palabrasf(Fuente,TamanoFuente,Palabra,Color,PosicionInicial,pantalla)
            if a:
                fase = e
##Eventos #fase son las pantallas que se mostraran en el menu
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()
            if event.type==pygame.MOUSEBUTTONDOWN or key[pygame.K_RETURN]:
                if fase == 0:
                    return 0
                elif fase == 1:
                    return 1
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    return 2