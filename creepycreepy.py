
from random import randint
import pygame                                       
from pygame.locals import *


LarX = 800
AltY = 600

X = 350
Y = 500

passoXe1 = 3.5
passoYe1 = 3.5

pygame.init()                                        
tela = pygame.display.set_mode((LarX, AltY), 0, 32)     
pygame.display.set_caption('Creepy Creepy')        

fundo = pygame.image.load('bckgrd.jpg')
personagem = pygame.image.load('mainchback.png')


enemy1XQ = 350
enemy1YQ = 100

d = (X - enemy1XQ) ** 2 + (Y - enemy1YQ) ** 0.5


enemy1 = pygame.image.load('enemy1.png')
corRetangulo = (0, 128, 0)
tamRetangulo= (20, 20)
espessuraRetangulo = (0)

fim = False
while not fim:
  tela.blit(fundo, (0, 0))
  tela.blit(personagem, (X, Y))
  
  tela.blit(enemy1, (enemy1XQ, enemy1YQ))
    
  pygame.display.update()
  
  enemy1YQ = enemy1YQ + passoYe1
  
  
  pygame.time.delay(10)
                     
  Teclas = pygame.key.get_pressed()

  if X == enemy1XQ and Y == enemy1YQ: 
    print("aaa")
    
  if Teclas[K_UP]:
    Y = Y - 1.25
    personagem = pygame.image.load('mainchback.png')
    tela.blit(personagem, (X, Y))
##  elif Y > 550:
##    Y = Y - 30
    
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

  coordRetangulo = (100,100)
  tamRetangulo = (90,90)
  
  if Teclas[K_SPACE]:
     pygame.draw.rect(tela, corRetangulo, (coordRetangulo, tamRetangulo), espessuraRetangulo)

  

  for event in pygame.event.get():                   
    if event.type == QUIT:                           
      fim = True                                    

pygame.display.quit()  
print("Fim do programa")
