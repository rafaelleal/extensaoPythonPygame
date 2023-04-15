import pygame
pygame.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((800, 600))

background = pygame.image.load("space.jpg")

imagemRocket = pygame.image.load("Spacepack/Rocket.png")
imagemRocket = pygame.transform.scale(imagemRocket, (200,100))
rectRocket = imagemRocket.get_rect()

velocidadeRocket = 6
while True: #Game Loop
    #UPDATE
    for event in pygame.event.get(): #Event Loop
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()       
        #if event.type == pygame.KEYDOWN:
        #    if event.key == pygame.K_d:
        #        rectRocket.move_ip(velocidadeRocket, 0)
        #    if event.key == pygame.K_a:
        #       rectRocket.move_ip(-velocidadeRocket, 0)
        #    if event.key == pygame.K_w:
        #        rectRocket.move_ip(0, -velocidadeRocket)
        #    if event.key == pygame.K_s:
        #        rectRocket.move_ip(0, velocidadeRocket)
    
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_d]:
        rectRocket.move_ip(velocidadeRocket, 0)
    if tecla[pygame.K_a]:
        rectRocket.move_ip(-velocidadeRocket, 0)
    if tecla[pygame.K_w]:
        rectRocket.move_ip(0, -velocidadeRocket)
    if tecla[pygame.K_s]:
        rectRocket.move_ip(0, velocidadeRocket)

    #DRAW
    tela.blit(background, (0,0))    
    tela.blit(imagemRocket, rectRocket)
    pygame.display.update()
    clock.tick(60) #60 FPS
