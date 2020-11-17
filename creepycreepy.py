

from random import randint
import pygame                                       
from pygame.locals import *


LarX = 800
AltY = 600

X = 350
Y = 500

passoX = 1
passoY = 1

pygame.init()                                        
tela = pygame.display.set_mode((LarX, AltY), 0, 32)     
pygame.display.set_caption('Creepy Creepy')        

fundo = pygame.image.load('bckgrd.jpg')
personagem = pygame.image.load('mainchback.png')

XQ = 300
YQ = 300

XQ2 = 100
YQ2 = 100


enemy1 = pygame.image.load('enemy1.png')
corRetangulo = (0, 128, 0)
tamRetangulo= (20, 20)
espessuraRetangulo = (0)

fim = False
while not fim:
  tela.blit(fundo, (0, 0))
  tela.blit(personagem, (X, Y))
  pygame.draw.rect(tela, corRetangulo, ((XQ, YQ), tamRetangulo), espessuraRetangulo)
  tela.blit(enemy1, (XQ2, YQ2))
  pygame.display.update()
  
  XQ = XQ + passoX
  YQ2 = YQ2 + passoY
  
  
  pygame.time.delay(10)
                     
  Teclas = pygame.key.get_pressed()
  
  
  if Teclas[K_UP]:
    Y = Y - 1.25
    personagem = pygame.image.load('mainchback.png')
    tela.blit(personagem, (X, Y))
    
  if Teclas[K_DOWN]:
    Y = Y + 1.25
    personagem = pygame.image.load('mainchfront.png')
    tela.blit(personagem, (X, Y))
  if Teclas[K_LEFT]:
      
    X = X - 1.25
    personagem = pygame.image.load('mainchleft.png')
    tela.blit(personagem, (X, Y))
    
  if Teclas[K_RIGHT]:
    X = X + 1.25
    personagem = pygame.image.load('mainchright.png')
    tela.blit(personagem, (X, Y))


  for event in pygame.event.get():                   
    if event.type == QUIT:                           
      fim = True                                    

pygame.display.quit()  
print("Fim do programa")
