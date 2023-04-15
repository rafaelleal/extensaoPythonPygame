import pygame
pygame.init()
clock = pygame.time.Clock()

tela = pygame.display.set_mode((800, 600))

imagemRocket = pygame.image.load("Spacepack/Rocket.png")
imagemRocket = pygame.transform.scale(imagemRocket, (200,100))
rectRocket = imagemRocket.get_rect()

imagemUFO = pygame.image.load("Spacepack/UFOBoss.png")
imagemUFO = pygame.transform.scale(imagemUFO, (200, 200))
rectUFO = imagemUFO.get_rect()
rectUFO = rectUFO.move(600, 400)

velocidade = 2
velocidadeRocket = 5

while True:
    clock.tick(60) #60 fps

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

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

    #Movimentação do inimigo
    if rectUFO.x > rectRocket.x:
        rectUFO.x -= velocidade
    else:
        rectUFO.x += velocidade

    if rectUFO.y > rectRocket.y:
        rectUFO.y -= velocidade
    else:
        rectUFO.y += velocidade

    #Desenho dos sprites  
    tela.fill((0,0,0))
    tela.blit(imagemRocket, rectRocket)
    tela.blit(imagemUFO, rectUFO)

    pygame.display.update()
