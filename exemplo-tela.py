import pygame
pygame.init()
tela = pygame.display.set_mode((800,600))

#Tela de menu
def menu():
    tela.fill((0,0,0))
    pygame.draw.rect(tela, (255, 0, 0), pygame.Rect(0, 0, 40, 30))
    pygame.draw.rect(tela, (0, 255, 0), pygame.Rect(40, 0, 40, 30))
    pygame.draw.rect(tela, (0, 0, 255), pygame.Rect(80, 0, 40, 30))

#Tela do jogo
def game():
    tela.fill((255,255,255))

opcao = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                opcao = 1
            elif event.key == pygame.K_2:
                opcao = 2
                
    if opcao == 1:
        menu()
    elif opcao == 2:
        game()
        
    pygame.display.update()
