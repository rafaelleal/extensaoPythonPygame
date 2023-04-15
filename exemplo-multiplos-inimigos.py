import pygame, random

pygame.init()

clock = pygame.time.Clock()

tela = pygame.display.set_mode((800, 600))

background = pygame.image.load("space.jpg").convert()

imagemRocket = pygame.image.load("Spacepack/Rocket.png")
imagemRocket = pygame.transform.scale(imagemRocket, (200,100))
rectRocket = imagemRocket.get_rect()

pygame.mouse.set_visible(True)

lista_naves = []
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

    if lmb:
        rectRocket = imagemRocket.get_rect()
        xRand = random.randrange(0,600,200)
        yRand = random.randrange(0,700,100)
        rectRocket = rectRocket.move(xRand,yRand)
        lista_naves.append(rectRocket)
        
    tela.blit(background, (0,0))

    #Movimento aleatório das naves a cada 50 ms
    cooldown = 50
    now = pygame.time.get_ticks()
    if now - last > cooldown:
        for nave in lista_naves:
            last = now
            #Intervalo de movimento
            moveX=random.randint(-2,3)
            moveY=random.randint(-2,3)
            nave.move_ip (moveX, moveY)
            
    for nave in lista_naves:
       tela.blit(imagemRocket, nave)
   
    pygame.display.update()
    
    clock.tick(60) #30 FPS






