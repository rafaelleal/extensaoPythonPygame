import pygame
pygame.init()
tela = pygame.display.set_mode((800, 600))
cor = (255, 0, 0)
tela.fill(cor)
while True:
    #GameUpdate
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #DrawUpdate
    pygame.display.update()