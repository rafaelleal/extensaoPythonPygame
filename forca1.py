import pygame
pygame.init()

tela = pygame.display.set_mode((800, 600), 0, 32)

palavra = "PROGRAMACAO"
quant_letras = len(palavra)
jogador = list("?" * quant_letras)
tentativas = 5
ja_adivinhou = []

fonte = pygame.font.SysFont("Arial", 32)
txtPrompt = fonte.render("Digite uma letra!", True, (0, 0, 255))

relogio = pygame.time.Clock()  # Adicione um relógio para controlar a velocidade do loop do jogo

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:  # Verifique se uma tecla foi pressionada
            letra = event.unicode.upper()  # Obtenha a tecla pressionada e converta para maiúscula

            if letra in ja_adivinhou:
                print("Letra já digitada!")
                tentativas -= 1
            else:
                errou = True
                for i in range(len(palavra)):
                    if letra == palavra[i]:
                        ja_adivinhou.append(letra)
                        print("Acertou a letra: " + letra)
                        jogador[i] = letra
                        quant_letras -= 1
                        errou = False
                if errou:
                    print("ERRRRRRROU!")
                    tentativas -= 1
            txtJogador = fonte.render("".join(jogador), True, (0, 255, 255))
            txtTentativas = fonte.render("Tentativas: " + str(tentativas), True, (0, 255, 255))

    if tentativas == 0:
        print("FIM DE JOGO!")
        pygame.quit()
        exit()
    if quant_letras == 0:
        print("Acertou Mizerávi!")
        pygame.quit()
        exit()

    tela.fill((255, 255, 255))
    tela.blit(txtJogador, (50, 20))
    tela.blit(txtTentativas, (50, 62))
    tela.blit(txtPrompt, (50, 104))
    pygame.display.update()
    relogio.tick(30)  # Controle a velocidade do loop do jogo, 30 FPS nesse caso
