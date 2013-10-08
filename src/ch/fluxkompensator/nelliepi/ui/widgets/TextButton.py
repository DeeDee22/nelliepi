'''
Created on Oct 3, 2013

@author: geraldine
'''
from Button import Button
import pygame
from ch.fluxkompensator.nelliepi.Constants import BLACK

class TextButton(Button):
    '''
    classdocs
    '''

    def __init__(self, pX, pY, pText, pMethod=None, pName=None, pParams=None):
        '''
        Constructor
        '''
        if pName == None:
            name = pText
        else:
            name = pName
        Button.__init__(self, pX, pY, pName=name, pMethod=pMethod, pParams=pParams)
        font = pygame.font.Font(None, 36)
        self.text = font.render(pText, 1, (BLACK))
        
     
    def getPosition(self):
        return self.text.get_rect(centerx=self.x,centery=self.y)

    def wasTouched(self, pPosition):
        result = self.getPosition().collidepoint(pPosition)
        if(result):
            print("button <" + self.getName() + "> was touched")
        return result
    
    def getSurface(self):
        return self.text