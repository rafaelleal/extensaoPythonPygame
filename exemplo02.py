import pygame
pygame.init()
tela = pygame.display.set_mode((1024, 768))

cor = (100, 100, 100) #tupla de três valores inteiros representando uma cor no esquema RGB
tela.fill(cor)

while True: #Game Loop
    pygame.display.update()
