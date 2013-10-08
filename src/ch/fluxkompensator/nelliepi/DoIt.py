'''
Created on Oct 4, 2013

@author: geraldine
'''
import pygame, sys
from pygame.locals import *
from ch.fluxkompensator.nelliepi.Constants import RESOLUTION
from ch.fluxkompensator.nelliepi.ui.screen.StartScreen import StartScreen
from ch.fluxkompensator.nelliepi.ui.state import UiState
from ch.fluxkompensator.nelliepi.ui.controller import ButtonCollisionDetector
from ch.fluxkompensator.nelliepi.ui.screen.MusicScreen import MusicScreen

if __name__ == '__main__':
    pygame.init()

    # set up the window
    pygameScreen = pygame.display.set_mode(RESOLUTION, 0, 32)
    UiState.pygameScreen = pygameScreen

    startScreen = StartScreen()
    musicScreen = MusicScreen()
   
    UiState.setScreen(startScreen)

    running = True
    
    print(UiState.toString())
    
    # run the game loop
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                running = False 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    #print("Pos: %sx%s\n" % pygame.mouse.get_pos())
                    pressedButton = ButtonCollisionDetector.getPressedButton(pygame.mouse.get_pos())
                    if(not pressedButton is None):
                        pressedButton.execute()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
        pygame.display.update()