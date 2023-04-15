import pygame
pygame.init()
tela = pygame.display.set_mode((400, 300))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    for vermelho in range(0,255,10):
        for verde in range(0,255,10):
            for azul in range(0,255,10):
                cor = (vermelho, verde, azul)
                print (cor)
                tela.fill(cor)
                pygame.display.update()
        
