import pygame
#Inicialização
pygame.init()
tela = pygame.display.set_mode( (800,600) )
cor = (0, 0, 110)
tela.fill( cor )

#Carregar imagem do player (Rocket.png)
imagemRocket = pygame.image.load("Spacepack/Rocket.png")
imagemRocket = pygame.transform.scale(imagemRocket, (400,200))

#Vamos utilizar um Rectangle para representar a área ocupada pelo personagem na tela
rectRocket = imagemRocket.get_rect()


while True: #Game Loop
    #Update - modificar os dados dos componentes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    #Drawing - desenhar os componentes na tela
    tela.blit(imagemRocket, rectRocket)
    pygame.display.update()