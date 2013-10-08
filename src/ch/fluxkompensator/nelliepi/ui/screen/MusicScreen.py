'''
Created on Oct 4, 2013

@author: geraldine
'''
from ch.fluxkompensator.nelliepi.ui.screen.ScreenWithFooter import ScreenWithFooter
from ch.fluxkompensator.nelliepi.ui.widgets.TextButton import TextButton
from ch.fluxkompensator.nelliepi.functions import ChangeScreenFunction

class MusicScreen(ScreenWithFooter):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        ScreenWithFooter.__init__(self, "musicScreen")
        
        playButton = TextButton(self.getMaxWidth() / 2, self.getMaxHeight() / 4, "Play", pMethod=ChangeScreenFunction.function,  pParams=["startScreen",])
        self.addButton(playButton)
        
        stopButton = TextButton(self.getMaxWidth() / 2, self.getMaxHeight() / 4 * 3, "Stop")
        self.addButton(stopButton)
        