'''
Created on Oct 4, 2013

@author: geraldine
'''
from ch.fluxkompensator.nelliepi import IPAddressFinder
from ch.fluxkompensator.nelliepi.functions import ChangeScreenFunction
from ch.fluxkompensator.nelliepi.ui.screen.ScreenWithFooter import \
    ScreenWithFooter
from ch.fluxkompensator.nelliepi.ui.widgets.TextButton import TextButton
from ch.fluxkompensator.nelliepi.Constants import RED


class StartScreen(ScreenWithFooter):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        ScreenWithFooter.__init__(self, "startScreen")
        
        musicButton = TextButton(self.getMaxWidth() / 2, self.getMaxHeight() / 4, "Music", pMethod=ChangeScreenFunction.function, pParams=["musicScreen",])
        self.addButton(musicButton)
        
        diagnosticsButton = TextButton(self.getMaxWidth() / 2, self.getMaxHeight() / 4 * 2, "Nellies Data")
        self.addButton(diagnosticsButton)
        
            
        ipAddress=IPAddressFinder.get_ip_address("wlan0")
        ipButton = TextButton(self.getMaxWidth() / 2, self.getMaxHeight() / 4 * 3, "Hi, you can reach me at " + ipAddress, pColor=RED, pFontSize=25)
        self.addButton(ipButton)
        