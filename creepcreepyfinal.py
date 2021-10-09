import pygame                                       
from pygame.locals import *
from random import randint

pygame.init()

Lar = 800
Alt = 600

titulo = pygame.image.load('title.png')
titulofundo = pygame.image.load('bg.gif')
fundo = pygame.image.load('bg.gif')
ambiente = pygame.mixer.music.load('creeper.mp3')

personagem = pygame.image.load('mainchback.png')
disparo = pygame.image.load('disparo.png')
mainchfront = pygame.image.load('mainchfront.png')
mainchleft = pygame.image.load('mainchleft.png')
mainchright = pygame.image.load('mainchright.png')

vida = pygame.image.load('life1.png')
morte = pygame.image.load('life2.png')

enemy1 = pygame.image.load('enemy1.png')
enemy2 = pygame.image.load('enemy6.png')


tela = pygame.display.set_mode((Lar, Alt), 0, 32)
pygame.display.set_caption("Creepy Creepy")

#Coord Personagem
x = 350
y = 460
#Coord Disparo
a = x
b = y
#Coord Inimigos
w = 350
z = 0
#Lar//Alt
wp = 80
hp = 140


velocidade = 0.5

inicio = True

while inicio:
    tela.blit(titulofundo, (0,0))
    tela.blit(titulo, (220, 180)) 
    pygame.display.update()

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_SPACE]:
       inicio = False

    for event in pygame.event.get():
        if event.type == pygame.K_SPACE:
            inicio = False

rodando = True

while rodando:
    
    tela.blit(fundo, (0,0))
    tela.blit(vida, (10, 10))
    tela.blit(disparo, (a, b))
    tela.blit(enemy1, (w, z))
    tela.blit(personagem, (x, y))

#    pygame.time.delay(1000)
    pygame.mixer.music.play(-1, 0.0, 1)
    pygame.display.update()

    z += velocidade
    if z == (Alt + hp) - hp - velocidade:
        z = z - velocidade
        z = 0
        w = (randint (80, 740))
    elif (w + wp, z + hp) == (x + wp, y + hp):
         vida = pygame.image.load('life2.png')
         tela.blit(morte, (10, 10))
            
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT] and x > velocidade:
        x -= velocidade
        personagem = pygame.image.load('mainchleft.png')
        tela.blit(personagem, (x, y))

    if teclas[pygame.K_RIGHT] and x < Lar - wp - velocidade:
        x += velocidade
        personagem = pygame.image.load('mainchright.png')
        tela.blit(personagem, (x, y))
        
    if teclas[pygame.K_UP] and y > velocidade:
        y -= velocidade
        personagem = pygame.image.load('mainchback.png')
        tela.blit(personagem, (x, y))
       
    if teclas[pygame.K_DOWN] and y < Alt - hp - velocidade:
        y += velocidade
        personagem = pygame.image.load('mainchfront.png')
        tela.blit(personagem, (x, y))

    if teclas[pygame.K_SPACE] and b > velocidade:
        b = b - (velocidade + 1)
        disparo = pygame.image.load('disparo.png')
        tela.blit(disparo, (a, b))
    elif b == b > velocidade and a == a > velocidade:
          b = velocidade == 0
          a = velocidade == 0
          b = y
          a = x
    else:
         a = x
         b = y
       

pygame.quit()
        
