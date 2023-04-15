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

rectRocket = rectRocket.move(pygame.mouse.get_pos())

velocidadeRocket = 6
velocidadeLaser = 20
cooldown = 500

pygame.mouse.set_visible(False)

lista_lasers = []
last = pygame.time.get_ticks()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                exit()
                
    lmb, mmb, rmb = pygame.mouse.get_pressed()

    if lmb: #Clique no botão esquerdo do mouse
        now = pygame.time.get_ticks()
        if now - last >= cooldown:
            last = now
            rectLaser.x = rectRocket.x + 100
            rectLaser.y = rectRocket.y
            lista_lasers.append(rectLaser)
        
    tela.blit(background, (0,0))
    for tiro in lista_lasers:
        if tiro.left > tela.get_width():
            lista_lasers.remove(tiro)
        tiro.move_ip (velocidadeLaser, 0)
        tela.blit(imagemLaser, tiro)
        
    x, y = pygame.mouse.get_pos()
    rectRocket.x = x
    rectRocket.y = y
    tela.blit(imagemRocket, rectRocket)

    pygame.display.update()
    
    clock.tick(60) #30 FPS






