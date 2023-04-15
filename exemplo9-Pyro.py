import pygame
import random
import Pyro4

nome = input("Nome: ")

pygame.init()
clock = pygame.time.Clock()

tela = pygame.display.set_mode((800, 600))
#Um objeto font é necessário para escrever valores na HUD do jogo
fonte = pygame.font.SysFont("arial", 40)

imagemRocket = pygame.image.load("Spacepack/Rocket.png")
imagemRocket = pygame.transform.scale(imagemRocket, (200,100))
rectRocket = imagemRocket.get_rect()

imagemLaser = pygame.image.load("Spacepack/LaserBeam.png")
imagemLaser = pygame.transform.scale(imagemLaser, (100,100))
rectLaser = imagemLaser.get_rect()

imagemUFO = pygame.image.load("Spacepack/UFOBoss.png")
imagemUFO = pygame.transform.scale(imagemUFO, (200, 200))
rectUFO = imagemUFO.get_rect()
rectUFO = rectUFO.move(400, 300)

preto = (0, 0, 0) #RGB: preto == 0R, 0G, 0B
velocidadeRocket = 5
velocidadeLaser = 18
atirou = False
pontos = 0

#Obtendo referência remota do inimigo
inimigoRemoto = Pyro4.Proxy("PYRONAME:capirotauro")

lista_lasers = []
dano = None
#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #Controle de disparos
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rectLaser = imagemLaser.get_rect()
                rectLaser.x = rectRocket.x + 100
                rectLaser.y = rectRocket.y
                lista_lasers.append(rectLaser)
                
    #Movimentação do personagem
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_d]:
        rectRocket.move_ip(velocidadeRocket, 0)
    if tecla[pygame.K_a]:
        rectRocket.move_ip(-velocidadeRocket, 0)
    if tecla[pygame.K_w]:
        rectRocket.move_ip(0, -velocidadeRocket)
    if tecla[pygame.K_s]:
        rectRocket.move_ip(0, velocidadeRocket)

    #Desenho do background
    tela.fill(preto)

        
    #Desenhar os sprites do player e do inimigo (sempre)
    tela.blit(imagemRocket, rectRocket)
    tela.blit(imagemUFO, rectUFO)
    

    #Lógica para tratar a exibição dos disparos na tela
    for tiro in lista_lasers:
        #Movimentar o disparo na tela
        tiro.move_ip (velocidadeLaser, 0)
        #Teste para determinar se o disparo deve ser eliminado 
        if tiro.left > tela.get_width():
            lista_lasers.remove(tiro)
        #Desenho do disparo (apenas realizado quando houver disparo
        tela.blit(imagemLaser, tiro)
        #Tratamento de colisão do disparo com um inimigo

        if rectLaser.colliderect(rectUFO):
            lista_lasers.remove(tiro)
            #Computar os pontos para o player
            pontos += 100

            #Acessando o método remoto
            status = inimigoRemoto.levar_dano(nome, 10)

            #Criando o objeto de exibição de texto na HUD
            dano = fonte.render(str(status), True, (0,255,0))

    
    #Desenhar a HUD
    score = fonte.render ("Score: " + str(pontos), True, (255, 255, 255))
    tela.blit(score, (10,5))
    if dano:
        tela.blit(dano, rectUFO)
    
    pygame.display.update()
    clock.tick(30)









    
