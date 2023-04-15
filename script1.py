palavra = "Araraquara"
palavra = palavra.upper()
quantidadeLetras = len(palavra)
jogador = list("?" * quantidadeLetras)
tentativas = 5
while True:
	print (palavra)
	print (jogador)
	print ("Quantidade de Letras: " + str(quantidadeLetras))
	print ("Tentativas: " + str(tentativas))
	letra = input("Digite uma letra: ").upper()
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
		
	
