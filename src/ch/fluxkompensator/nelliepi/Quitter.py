'''
Created on Oct 4, 2013

@author: geraldine
'''
import pygame, sys
from ch.fluxkompensator.nelliepi.music import Player

def quit_nelliepi():
    Player.dispose()
    pygame.quit()
    sys.exit()
