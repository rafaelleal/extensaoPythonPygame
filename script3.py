import pygame
pygame.init()
tela = pygame.display.set_mode((800, 600))
imgNave =  pygame.image.load("Spacepack/Rocket.png")
imgNave = pygame.transform.scale(imgNave, (200,100))
imgUFO = pygame.image.load("Spacepack/UFOBoss.png")
imgUFO = pygame.transform.scale(imgUFO, (200,200))
rect_nave = imgNave.get_rect()
rect_ufo = imgUFO.get_rect()
posicao = (400, 300)
rect_ufo = rect_ufo.move(posicao)
clock = pygame.time.Clock()
velocidadeNave = 7
velocidadeUFO = 5
while True:
	rect_ufo.move_ip(velocidadeUFO, 0)
	if rect_ufo.right > 800 or rect_ufo.left < 0:
		velocidadeUFO *= -1
		imgUFO = pygame.transform.flip(imgUFO, True, False)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	tecla = pygame.key.get_pressed()
	if tecla[pygame.K_d]:
		rect_nave.move_ip(velocidadeNave, 0)
	if tecla[pygame.K_a]:
		rect_nave.move_ip(-velocidadeNave, 0)
	if tecla[pygame.K_w]:
		rect_nave.move_ip(0, -velocidadeNave)
	if tecla[pygame.K_s]:
		rect_nave.move_ip(0, velocidadeNave)
	if rect_nave.colliderect(rect_ufo):
		tela.fill((255,0,0))
		fonte = pygame.font.SysFont("arial", 48)
		txtGameOver = fonte.render("GAME OVER!", True, (255,255,255))
		tela.blit(txtGameOver,(400, 300))
		pygame.display.update()
		pygame.time.delay(2000)
		pygame.quit()
		exit()
	tela.fill((0,0,0))
	tela.blit(imgNave, rect_nave)
	tela.blit(imgUFO, rect_ufo)
	pygame.display.update()
	clock.tick(60)