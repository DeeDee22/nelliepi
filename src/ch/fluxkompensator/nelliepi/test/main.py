'''
Created on Oct 3, 2013

@author: geraldine
'''
from ch.fluxkompensator.nelliepi.ui.widgets.TextButton import TextButton
import pygame, sys
from pygame.locals import *
from ch.fluxkompensator.nelliepi.Constants import RESOLUTION

pygame.init()


# set up the window
screen = pygame.display.set_mode(RESOLUTION, 0, 32)
pygame.display.set_caption('Drawing')

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(WHITE)


textButton = TextButton(background.get_width()/2, background.get_height()/2, "My button")

background.blit(textButton.getSurface(), textButton.getPosition())

screen.blit(background, (0, 0))
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
            if textButton.wasTouched(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()
                running = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
    pygame.display.update()