import pygame
pygame.init()
tela = pygame.display.set_mode((640,480), 0, 32)
pygame.display.set_caption("Jogo da Forca")
fonte = pygame.font.SysFont("arial", 24)

palavra = "Araraquara"
palavra = palavra.upper()
quantidadeLetras = len(palavra)
jogador = list("?" * quantidadeLetras)
tentativas = 5
while True:
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			pygame.quit()
			exit()
		elif evento.type == pygame.KEYDOWN:
			letra = chr(evento.key).upper()
			posicaoLetra = 0
			errou = True
			while posicaoLetra < len(palavra): 
				if letra == palavra[posicaoLetra]:
					jogador[posicaoLetra] = letra
					quantidadeLetras -= 1
					errou = False
				posicaoLetra += 1
			if errou:
				print("ERRRRRRROU!")
				tentativas -= 1
			if tentativas == 0:
				print ("Morreu, mas passa bem...")
				exit()
			if quantidadeLetras == 0:
				print ("Acertou Mizerávi!")
				exit()
			
	txtPalavra = fonte.render (palavra, True, (0, 0, 255), (255, 255, 255))
	
	txtJogador = fonte.render (str(jogador), True, (0, 255, 0), (255, 255, 255))
	
	txtLetras = fonte.render ("Quantidade de Letras: " + str(quantidadeLetras), True, (0, 0, 0), (255, 255, 255))
	
	txtTentativas = fonte.render ("Tentativas: " + str(tentativas), True, (255, 0, 0), (255, 255, 255))
	
	
	tela.fill((255,255,255))
	tela.blit(txtPalavra, (10, 10))
	tela.blit(txtJogador, (10, 42))
	tela.blit(txtLetras, (10, 74))
	tela.blit(txtTentativas, (10, 106))
	pygame.display.update()
	
	
