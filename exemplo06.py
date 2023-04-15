import pygame
pygame.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((800, 600))

imagemRocket = pygame.image.load("Spacepack/Rocket.png")
imagemRocket = pygame.transform.scale(imagemRocket, (200,100))
rectRocket = imagemRocket.get_rect()

preto = (0, 0, 0) #RGB: preto == 0R, 0G, 0B

velocidadeRocketX = 8
velocidadeRocketY = 4

while True:
    #UPDATE
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if rectRocket.right > tela.get_width() or rectRocket.left < 0:
        velocidadeRocketX *= -1
        imagemRocket = pygame.transform.flip(imagemRocket, True, False)
    if rectRocket.bottom > tela.get_height() or rectRocket.top < 0:
        velocidadeRocketY *= -1
        #imagemRocket = pygame.transform.flip(imagemRocket, False, True)
    rectRocket.move_ip(velocidadeRocketX, velocidadeRocketY)

    #DRAW
    tela.fill(preto)
    tela.blit(imagemRocket, rectRocket)
    pygame.display.update()
    clock.tick(60) #60 FPS
