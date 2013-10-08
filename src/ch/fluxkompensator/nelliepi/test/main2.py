'''
Created on Oct 3, 2013

@author: geraldine
'''
import pygame, sys
from pygame.locals import *
from ch.fluxkompensator.nelliepi.Constants import RESOLUTION
from ch.fluxkompensator.nelliepi.ui.screen.StartScreen import StartScreen

pygame.init()


# set up the window
screen = pygame.display.set_mode(RESOLUTION, 0, 32)

nellieScreen = StartScreen("startScreen")

#textButton = TextButton(0, 0, "My button")
#nellieScreen.addElement(textButton.getSurface(), textButton.getPosition())

screen.blit(nellieScreen.getSurface(), (0, 0))
pygame.display.flip()

running = True
# run the game loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            running = False 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Pos: %sx%s\n" % pygame.mouse.get_pos())
#            if textButton.wasTouched(pygame.mouse.get_pos()):
 #               pygame.quit()
  #              sys.exit()
   #             running = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
    pygame.display.update()