import pygame
pygame.init()
tela = pygame.display.set_mode((800, 600))
cor1 = (255, 0, 0)
cor2 = (0, 255, 0)
cor3 = (0, 0, 255)

titulo = True
jogo = False
gameOver = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                titulo = False
                jogo = True
                gameOver = False
            if event.key == pygame.K_s:
                titulo = False
                jogo = False
                gameOver = True
            if event.key == pygame.K_d:
                titulo = True
                jogo = False
                gameOver = False

    if (titulo):
        #Lógica da tela de título
        tela.fill(cor1)
    elif (jogo): 
        #Lógica da tela de jogo
        tela.fill(cor2)
    elif (gameOver):
        #Lógica da tela de Game Over
        tela.fill(cor3)      
            
    pygame.display.update()