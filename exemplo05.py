import pygame
pygame.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((1024, 768))
cor = (0, 0, 50) #RGB: azul == 0R, 0G, 50B


imagemRocket = pygame.image.load("Spacepack/Rocket.png")
imagemRocket = pygame.transform.scale(imagemRocket, (200,100))
rectRocket = imagemRocket.get_rect()

velocidadeRocket = 10

while True:
    #UPDATE
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    rectRocket.move_ip(velocidadeRocket, 0)

    #DRAW
    tela.fill(cor)
    tela.blit(imagemRocket, rectRocket)
    pygame.display.update()
    clock.tick(60) #60 FPS