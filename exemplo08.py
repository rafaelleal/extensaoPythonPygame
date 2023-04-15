import pygame
pygame.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((800, 600))

background = pygame.image.load("space.jpg")

imagemRocket = pygame.image.load("Spacepack/Rocket.png")
imagemRocket = pygame.transform.scale(imagemRocket, (200,100))
rectRocket = imagemRocket.get_rect()

imagemLaser = pygame.image.load("Spacepack/LaserBeam.png")
imagemLaser = pygame.transform.scale(imagemLaser, (100,100))
rectLaser = imagemLaser.get_rect()

velocidadeRocket = 5
velocidadeLaser = 10

atirou = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #Disparo de Laser
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and atirou == False:
                atirou = True
                rectLaser.x = rectRocket.x + 100
                rectLaser.y = rectRocket.y
        
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_d]:
        rectRocket.move_ip(velocidadeRocket, 0)
    if tecla[pygame.K_a]:
        rectRocket.move_ip(-velocidadeRocket, 0)
    if tecla[pygame.K_w]:
        rectRocket.move_ip(0, -velocidadeRocket)
    if tecla[pygame.K_s]:
        rectRocket.move_ip(0, velocidadeRocket)

    if atirou == True:
        rectLaser.move_ip (velocidadeLaser, 0)
        if rectLaser.left > tela.get_width():
            atirou = False
    #rectLaser.move_ip (velocidadeLaser, 0)
    #Drawing Loop
    tela.blit(background, (0,0))
    if atirou == True:
        tela.blit(imagemLaser, rectLaser)  
    #tela.blit(imagemLaser, rectLaser)
    tela.blit(imagemRocket, rectRocket)


    pygame.display.update()
    clock.tick(60)
