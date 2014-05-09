'''
Created on Oct 3, 2013

@author: geraldine
'''
from Screen import Screen
from ch.fluxkompensator.nelliepi.ui.widgets.TextButton import TextButton
import pygame
from ch.fluxkompensator.nelliepi.Constants import BLACK
from ch.fluxkompensator.nelliepi.Constants import WHITE
from ch.fluxkompensator.nelliepi.functions import GoToHomeScreenFunction,\
    GoToLastScreenFunction, QuitFunction, MuteFunction, UnmuteFunction,\
    MuteUnmuteFunction

class ScreenWithFooter(Screen):
    '''
    classdocs
    '''
    FOOTER_SIZE = 40

    def __init__(self, pName):
        '''
        Constructor
        '''
        Screen.__init__(self, pName)
        
        homeButton = TextButton(50, 220, "Home", pMethod=GoToHomeScreenFunction.function)
        self.addButton(homeButton)

        backButton = TextButton(130, 220, "Back", pMethod=GoToLastScreenFunction.function)
        self.addButton(backButton)
        
        muteButton = TextButton(200, 220, "Mute")
        muteButton.setMethod(MuteUnmuteFunction.function, pParams=[muteButton, MuteFunction.function, UnmuteFunction.function, "Mute", "Unmute"])
        self.addButton(muteButton)

        quitButton = TextButton(270, 220, "Quit", pMethod=QuitFunction.function)
        self.addButton(quitButton)
        
        pygame.draw.line(self.background, BLACK, (0, self.getMaxHeight()), (self.getMaxWidth(), self.getMaxHeight()))
    
    def clear(self):
        self.background.fill(WHITE) 
        homeButton = TextButton(50, 220, "Home", pMethod=GoToHomeScreenFunction.function)
        self.addButton(homeButton)

        backButton = TextButton(130, 220, "Back", pMethod=GoToLastScreenFunction.function)
        self.addButton(backButton)
        
        muteButton = TextButton(200, 220, "Mute")
        muteButton.setMethod(MuteUnmuteFunction.function, pParams=[muteButton, MuteFunction.function, UnmuteFunction.function, "Mute", "Unmute"])
        self.addButton(muteButton)

        quitButton = TextButton(270, 220, "Quit", pMethod=QuitFunction.function)
        self.addButton(quitButton)
        
        pygame.draw.line(self.background, BLACK, (0, self.getMaxHeight()), (self.getMaxWidth(), self.getMaxHeight()))   
        
    def addElement(self, pElement, pPosition):
        #TODO check if it fits
        Screen.addElement(self, pElement, pPosition)
        
    def getMaxHeight(self):
        return Screen.getMaxHeight(self) - self.FOOTER_SIZE
    
        