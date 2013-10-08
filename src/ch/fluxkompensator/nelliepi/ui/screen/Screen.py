'''
Created on Oct 3, 2013

@author: geraldine
'''
from ch.fluxkompensator.nelliepi.Constants import WHITE, RESOLUTION
import pygame
from ch.fluxkompensator.nelliepi.ui.state import UiState

class Screen(object):
    '''
    classdocs
    '''
    def getSurface(self):
        return self.background

    def __init__(self, pName):
        '''
        Constructor
        '''        
        self.name = pName
        self.background = pygame.Surface(RESOLUTION)
        self.background = self.background.convert()
        self.background.fill(WHITE)
        
        UiState.addScreen(self);
        
    def addElement(self, pElement, pPosition):
        self.background.blit(pElement, pPosition)
        
    def addButton(self, pButton):
        self.addElement(pButton.getSurface(), pButton.getPosition())
        UiState.addButton(pButton, self)
        
    def getMaxHeight(self):
        return self.background.get_size()[1]
    
    def getMaxWidth(self):
        return self.background.get_size()[0]
    
    def getName(self):
        return self.name