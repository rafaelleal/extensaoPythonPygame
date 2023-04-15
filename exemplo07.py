import pygame
import random

pygame.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((800, 600))

background = pygame.image.load("space.jpg")
imagemRocket = pygame.image.load("Spacepack/Rocket.png")
imagemRocket = pygame.transform.scale(imagemRocket, (300,150))
rectRocket = imagemRocket.get_rect()

preto = (0, 0, 0) #RGB: preto == 0R, 0G, 0B

#Criar uma lista (vazia) para armazenar as várias naves
naves = []
while True:
    #GameUpdate
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_SPACE]:
        #Criar uma nova nave
        nova_nave = imagemRocket.get_rect()
        #Posicionar aleatoriamente na tela
        aleatorio_x = random.randrange(0, tela.get_width()+1)
        aleatorio_y = random.randrange(0, tela.get_height()+1)
        nova_nave = nova_nave.move(aleatorio_x, aleatorio_y)
        #Inserir a nova nave na lista
        naves.append(nova_nave)
    #GameDraw
    tela.blit(background, (0,0))
    for cada_nave in naves:
        tela.blit(imagemRocket, cada_nave)

    pygame.display.update()
    clock.tick(30) #30 FPS
