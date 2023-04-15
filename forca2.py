import pygame
pygame.init()
largura = 800
altura = 600
tela = pygame.display.set_mode( (largura, altura), 0, 32 )

palavra = "ARARAQUARA"
quant_letras = len(palavra)
jogador = list("?" * quant_letras)
tentativas = 5
ja_adivinhou = []

preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)
estranho = (0, 255, 255)

fonte = pygame.font.SysFont("Arial", 32)



txtPrompt = fonte.render("Digite uma letra!", True, azul)
txtLetraDigitada = fonte.render("Letra já digitada!", True, vermelho)
txtErrou = fonte.render("ERRRRROU!", True, vermelho)
txtAcertoupalavra = fonte.render("Acertou MIZERÁVI! ", True, azul)
txtGameOver = fonte.render("GAME OVER!", True, vermelho)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            letra = chr(event.key).upper()
            if letra in ja_adivinhou:
                tentativas -= 1
                tela.fill(preto)
                tela.blit(txtLetraDigitada, (400, 300))
                pygame.display.update()
                pygame.time.delay(500)
            else:
                errou = True
                for i in range(len(palavra)):
                    if letra == palavra[i]:
                        ja_adivinhou.append(letra)
                        jogador[i] = letra
                        quant_letras -= 1
                        errou = False
                        txtAcertouLetra = fonte.render("Acertou a letra: " + letra, True, azul)
                        tela.fill(branco)
                        tela.blit(txtAcertouLetra, (400, 300))
                        pygame.display.update()
                        pygame.time.delay(500)
                if errou:
                    tela.fill(preto)
                    tela.blit(txtErrou, (400, 300))
                    pygame.display.update()
                    pygame.time.delay(500)
                    tentativas -= 1
    if tentativas == 0:
        tela.fill(preto)
        tela.blit(txtGameOver, (400, 300))
        pygame.display.update()
        pygame.time.delay(1000)
        exit()
    if quant_letras == 0:
        tela.fill(verde)
        tela.blit(txtAcertoupalavra, (400, 300))
        pygame.display.update()
        pygame.time.delay(1000)
        exit()

    tela.fill(branco)
    txtJogador = fonte.render(str(jogador), True, preto)
    tela.blit(txtJogador, (50, 20))
    txtTentativas = fonte.render("Tentativas: " + str(tentativas), True, preto)
    tela.blit(txtTentativas, (50, 62))
    tela.blit(txtPrompt, (50, 104))
    pygame.display.update()

