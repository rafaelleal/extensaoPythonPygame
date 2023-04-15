import pygame
from pygame.locals import *
from sys import exit
pygame.init()
clock = pygame.time.Clock()
background_image_filename = 'Grassbg.png'
resolucao = (800, 600) #tupla que armazena a largura e altura da tela
screen = pygame.display.set_mode(resolucao, 0, 32)
background = pygame.image.load(background_image_filename).convert()
Fullscreen = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_f:
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode(resolucao, FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode(resolucao, 0, 32)
    screen.blit(background, (0,0))
    pygame.display.update()
    clock.tick(60)







