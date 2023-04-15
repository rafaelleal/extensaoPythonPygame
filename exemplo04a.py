import pygame
pygame.init()
tela = pygame.display.set_mode((800, 600))

imagemRocket = pygame.image.load("Spacepack/Rocket.png")
imagemRocket = pygame.transform.scale(imagemRocket, (200,100))

rectRocket1 = imagemRocket.get_rect()
rectRocket2 = imagemRocket.get_rect()
rectRocket3 = imagemRocket.get_rect()


rectRocket1.move_ip(100, 200)
rectRocket2.move_ip(300, 400)


while True:
    #GameUpdate
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #DrawUpdate
    tela.fill((0, 0, 50))  
    tela.blit(imagemRocket, rectRocket1)
    tela.blit(imagemRocket, rectRocket2)
    tela.blit(imagemRocket, rectRocket3)
  
    pygame.display.update()
