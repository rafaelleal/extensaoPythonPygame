import pygame
pygame.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((800, 600))

background = pygame.image.load("space.jpg")

imagemRocket = pygame.image.load("Spacepack/Rocket.png")
imagemRocket = pygame.transform.scale(imagemRocket, (200,100))
rectRocket = imagemRocket.get_rect()

rectRocket = rectRocket.move(pygame.mouse.get_pos())

pygame.mouse.set_visible(False)

while True:
    #Update
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    x, y = pygame.mouse.get_pos()    
    
    #Draw
    tela.blit(background, (0, 0))
    #tela.blit(imagemRocket, (x, y))
    tela.blit(imagemRocket, (x - 100, y - 50))

    pygame.display.update()
    clock.tick(30) #30 FPS






