import pygame
from pygame.locals import *

def main():

    tamTela = (800, 600)
    corTela = (255,255,255)
    background = pygame.image.load('bckgrd.jpg')

    pygame.init()
    pygame.display.set_caption("Creepy Creepy")
    
##    coordRetangulo = (100, 250)
##    tamRetangulo = (30,80)
##    espessuraRetangulo = (0)
    corRetangulo = (128, 128, 128)
    corRetangulo2 = (0, 0, 0)
     
    ret = pygame.Rect (10, 10, 45, 45)
    ret2 = pygame.Rect(30,30, 50, 50)
            
    encerrar = False

    tela = pygame.display.set_mode((tamTela), 0, 32)
    tempo = pygame.time.Clock()

    while not encerrar:
        tela.fill(corTela)
        tela.blit(background, (0, 0))  
            
##        pygame.draw.rect(tela, corRetangulo, ret)
##        pygame.draw.rect(tela, corRetangulo2, ret2)
##
        for event in pygame.event.get():
            if event.type == QUIT:
                encerrar = True
     
##        
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_LEFT:
##                ret.move_ip(-10, 0)
##                
##            if event.key == pygame.K_RIGHT:
##                ret.move_ip(10, 0)
##                
##            if event.key == pygame.K_UP:
##                ret.move_ip(0, -10)
##                
##            if event.key == pygame.K_DOWN:
##                ret.move_ip(0, 10)
##
##            (ret.left, ret.top) = pygame.mouse.get_pos()
##            ret.left -= ret.width/2
##            ret.top -= ret.height/2

##            pygame.draw.rect(tela, cor_vermelha, ret)
            
        
                    
        pygame.display.update()
        
       
        tempo.tick(30)
          
    pygame.display.quit()


main()
