import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()

fenetre = pygame.display.set_mode((1880,1010 ))

perso = pygame.image.load("frites.png").convert_alpha()

position_perso = perso.get_rect()

while True :
    fenetre.fill([10,186,181])
    position_perso.topleft = (randint(0,540),randint(0,380))
    fenetre.blit(perso, position_perso)
    pygame.display.flip()
    pygame.time.delay(200)