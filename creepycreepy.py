##import pygame
##from pygame.locals import *
##
##tamTela = (800, 600)
##corTela = (255,255,255)
##background = pygame.image.load('bckgrd.jpg')
##
##pygame.init()
##
##tela = pygame.display.set_mode((tamTela), 0, 32)
##pygame.display.set_caption("Creepy Creepy")
##
##
##playerImg = pygame.image.load('mainchback.png')
##playerX = 370
##playerY = 480
##
##
##def player(x, y):
##    tela.blit(playerImg, (x, y))
##    playerX += 5
##
##running = True
##while running:
##
##    tela.fill(corTela)
##
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            running = False
##            
##    player(playerX, playerY)
##    pygame.display.update()
##    

from random import randint
import pygame                                       
from pygame.locals import *

# Inicialização de dados
LarX = 800
AltY = 600
X = 350
Y = 500

pygame.init()                                        
tela = pygame.display.set_mode((LarX, AltY), 0, 32)     
pygame.display.set_caption('Trabalhando com Imagens')        

fundo = pygame.image.load('bckgrd.jpg')
personagem = pygame.image.load('mainchback.png')



fim = False
while not fim:
    
  tela.blit(fundo, (0, 0))
  tela.blit(personagem, (X, Y))
  pygame.display.update()                            
  Teclas = pygame.key.get_pressed()
  
  
  if Teclas[K_UP]:
    Y = Y - 0.25
    personagem = pygame.image.load('mainchback.png')
    tela.blit(personagem, (X, Y))
    
  if Teclas[K_DOWN]:
    Y = Y + 0.25
    personagem = pygame.image.load('mainchfront.png')
    tela.blit(personagem, (X, Y))
  if Teclas[K_LEFT]:
      
    X = X - 0.25
    personagem = pygame.image.load('mainchleft.png')
    tela.blit(personagem, (X, Y))
    
  if Teclas[K_RIGHT]:
    X = X + 0.25
    personagem = pygame.image.load('mainchright.png')
    tela.blit(personagem, (X, Y))


  for event in pygame.event.get():                   
    if event.type == QUIT:                           
      fim = True                                    

pygame.display.quit()  
print("Fim do programa")
