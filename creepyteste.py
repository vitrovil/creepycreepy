import pygame
from pygame.locals import *

tamTela = (800, 600)
corTela = (255,255,255)
background = pygame.image.load('bckgrd.jpg')

pygame.init()

tela = pygame.display.set_mode((tamTela), 0, 32)
pygame.display.set_caption("Creepy Creepy")

jogadorImgCostas = pygame.image.load('mainchback.png')
imgCostasXY = (400, 480)

def jogador():
    tela.blit(jogadorImgCostas, (imgCostasXY))

encerrar = False

while not encerrar:
    tela.fill(corTela)
    tela.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            encerrar = True
                
    
    jogador()
    
    pygame.display.update()
   
        
          
pygame.display.quit()
