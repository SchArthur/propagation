import pygame
import ini_reader
from playerClass import Player
from keyboard import Keyboard

pygame.init()

clock = pygame.time.Clock()

fps = 144 #à changer en fonction de la personne

dtGlobal = 0
colorFile = "color.ini" #votre fichier de couleurs
colors = ini_reader.readini(colorFile) #enregistrement des couleurs
bgColor = tuple([int(elt) for elt in colors["bgColor"].split(",")]) 
playerOneColor = tuple([int(elt) for elt in colors["playerOneColor"].split(",")])      #définition des couleurs manuellement car pygame
playerTwoColor = tuple([int(elt) for elt in colors["playerTwoColor"].split(",")])      #est embêtant avec ses formats RGB en tuple


tilesize = 32 #la tilesize
size = pygame.Vector2(700, 700) #taille de l'écran
screen = pygame.display.set_mode((size.x, size.y))

p1Axis = {'vertical':[0, [pygame.K_z, pygame.K_s]], 'horizontal':[0, [pygame.K_q, pygame.K_d]], 'quit':False} #on gère les déplacements par un système d'axe
p2Axis = {'vertical':[0, [pygame.K_UP, pygame.K_DOWN]], 'horizontal':[0, [pygame.K_LEFT, pygame.K_RIGHT]], 'quit':False}


p1StartPos = [round((size.x/tilesize)/8), round((size.y/tilesize)/8)]
p2StartPos = [round(size.x/tilesize)-round((size.x/tilesize)/8), round(size.y/tilesize)-round((size.y/tilesize)/8)]

playerOne = Player(p1StartPos, playerOneColor, screen, 5, p1Axis) #création d'instances de la classe player
playerTwo = Player(p2StartPos, playerTwoColor, screen, 5, p2Axis)

players = []
players.append(playerOne)
players.append(playerTwo)

running = True

while running:
    dtGlobal = clock.tick(fps)
    screen.fill(bgColor)

    quit = []
    for player in players:
        quit.append(player.k["quit"])
        player.draw(tilesize)
        player.dt += dtGlobal
    
    for i in range(len(quit)-1):
        if quit[i] != quit[i+1]:
            running = False
    if len(quit) == 1 and quit[0] == True:
        running = False

    for player in players:
        player.k = Keyboard(player.k).get()
        if player.dt >= 1000/player.sp and (player.k["vertical"][0] != 0 or player.k["horizontal"][0] != 0):
            player.dt = 0
            player.p.x += player.k["vertical"][0]
            player.p.y += player.k["horizontal"][0]

            if player.k['quit'] == True:
                running = False

    for event in pygame.event.get():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playerOne.k['quit'] = True

    pygame.display.flip()
pygame.quit()