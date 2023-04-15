import pygame
import random
pygame.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((800, 600))
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
velocidadeLaser = 20
atirou = False
pontos = 0
pygame.mixer.music.load("Spacepack/reBoyShadowRunnerTheme.mp3")
pygame.mixer.music.play(loops = -1)
sfxLaser = pygame.mixer.Sound("Spacepack/space_laser_shot.wav")
while True:
    #UPDATE
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and atirou == False:
                sfxLaser.play(loops=0, maxtime=0)
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
    tela.fill(preto)
    if atirou == True:
        rectLaser.move_ip (velocidadeLaser, 0)
        if rectLaser.left > tela.get_width():
            atirou = False
    if rectLaser.colliderect(rectUFO):
        novoX = random.randint(100, 600)
        novoY = random.randint(100, 400)
        rectLaser = rectLaser.move (1000, 1000) #retirar da tela
        rectUFO.x = novoX
        rectUFO.y = novoY
        pontos += 100

    #DRAW
    tela.blit(imagemRocket, rectRocket)
    if atirou == True:
        tela.blit(imagemLaser, rectLaser)
    tela.blit(imagemUFO, rectUFO)
    score = fonte.render ("Score: " + str(pontos), True, (255, 255, 255))
    tela.blit(score, (10,5))
    pygame.display.update()
    clock.tick(30)