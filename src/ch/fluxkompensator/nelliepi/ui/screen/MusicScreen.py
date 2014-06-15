'''
Created on Oct 4, 2013

@author: geraldine
'''
from ch.fluxkompensator.nelliepi.ui.screen.ScreenWithFooter import ScreenWithFooter
from ch.fluxkompensator.nelliepi.ui.widgets.TextButton import TextButton
from ch.fluxkompensator.nelliepi.functions import StopFunction, PlayFunction,\
    ListFunction

class MusicScreen(ScreenWithFooter):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        ScreenWithFooter.__init__(self, "musicScreen")
        
        playButton = TextButton(self.getMaxWidth() / 2, self.getMaxHeight() / 4, "Play", pMethod=PlayFunction.function)
        self.addButton(playButton)

        listButton = TextButton(self.getMaxWidth() / 2, self.getMaxHeight() / 4 * 2, "List Files", pMethod=ListFunction.function, pParams=["_main_", 0, None])
        self.addButton(listButton)
        
        stopButton = TextButton(self.getMaxWidth() / 2, self.getMaxHeight() / 4 * 3, "Stop", pMethod=StopFunction.function)
        self.addButton(stopButton)
        