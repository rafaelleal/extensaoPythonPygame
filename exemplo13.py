import pygame
import random
pygame.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((800, 600))
fonte = pygame.font.SysFont("arial", 40)
imagemRocket = pygame.image.load("Spacepack/Rocket.png")
imagemRocket = pygame.transform.scale(imagemRocket, (200,100))
rectRocket = imagemRocket.get_rect()
imagemLaser = pygame.image.load("Spacepack/LaserBeam.png")
imagemLaser = pygame.transform.scale(imagemLaser, (100,100))
rectLaser = imagemLaser.get_rect()
imagemUFO = pygame.image.load("Spacepack/UFOBoss.png")
imagemUFO = pygame.transform.scale(imagemUFO, (200, 200))
rectUFO = imagemUFO.get_rect()

preto = (0, 0, 0) #RGB: preto == 0R, 0G, 0B
pygame.mixer.music.load("Spacepack/reBoyShadowRunnerTheme.mp3")
pygame.mixer.music.play(loops = -1)
sfxLaser = pygame.mixer.Sound("Spacepack/space_laser_shot.wav")
#Variáveis de controle do jogo
velocidadeRocket = 7
velocidadeLaser = 15
velocidadeInimigo = 3
pontos = 0
disparos = [] #lista de disparos
inimigos = [] #lista de inimigos

#Carregar a pool de Inimigos
quantidadeInimigos = 10
for i in range(quantidadeInimigos):
    rectUFO = imagemUFO.get_rect()
    
    #Loop para posicionar randomicamente os inimigos de forma que eles não fiquem sobrepostos
    while True: 
        novoX = random.randint(500, 2000)
        novoY = random.randint(100, 400)
        rectUFO.x = novoX
        rectUFO.y = novoY
        if rectUFO.collidelist(inimigos) == -1: #Se a posição sorteada não colidir com as posições já existentes na lista ...
            break
    #...pode inserir na lista e ir para o próximo inimigo
    inimigos.append(rectUFO)

while True:
    #UPDATE
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sfxLaser.play(loops=0, maxtime=0) #Reproduz o SFX do disparo
                rectLaser.x = rectRocket.x + 100 #Posicionando o disparo com relação à nave do Player
                rectLaser.y = rectRocket.y
                disparos.append(rectLaser) #Incluir o disparo na lista de disparos
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_d]:
        rectRocket.move_ip(velocidadeRocket, 0)
    if tecla[pygame.K_a]:
        rectRocket.move_ip(-velocidadeRocket, 0)
    if tecla[pygame.K_w]:
        rectRocket.move_ip(0, -velocidadeRocket)
    if tecla[pygame.K_s]:
        rectRocket.move_ip(0, velocidadeRocket)

    #Movimentação dos disparos na tela 
    for cada_disparo in disparos:
        cada_disparo.move_ip (velocidadeLaser, 0)
        if cada_disparo.left > tela.get_width(): #Remover os disparos que saem da tela
            disparos.remove(cada_disparo)
    
    #Movimentação dos inimigos em direção do jogador
    for cada_inimigo in inimigos:
        cada_inimigo.move_ip(-velocidadeInimigo, 0) #inimigo se move da direita para a esquerda na tela (-x) somente no eixo x (y=0)
        if cada_inimigo.right < 0: #Se o inimigo sair da tela...
            inimigos.remove(cada_inimigo) #...remova-o da lista...
            pontos -= 200 #...e o player perde pontos
            if pontos < 0:
                pontos = 0
    
    #Controle de colisão dos disparos com os inimigos
    for cada_inimigo in inimigos:
        i = cada_inimigo.collidelist(disparos) #O método collidelist retorna o índice do primeiro objeto da lista de disparos que colidiu com o objeto 'cada_inimigo'
        if i != -1: #Se não houver colisão o método collidelist retorna -1
            disparos.pop(i) #o comando pop remove o objeto da posição i da lista (disparos)
            inimigos.remove(cada_inimigo) #O comando remove remove diretamente um objeto da lista (remover o inimigo 'morto' da lista de inimigos)
            pontos += 100
    
    #DRAW
    tela.fill(preto)
    tela.blit(imagemRocket, rectRocket)
    for cada_disparo in disparos:
        tela.blit(imagemLaser, cada_disparo)
    for cada_inimigo in inimigos:
        tela.blit(imagemUFO, cada_inimigo)
    score = fonte.render ("Score: " + str(pontos), True, (255, 255, 255))
    tela.blit(score, (10,5))

    pygame.display.update()
    clock.tick(30)