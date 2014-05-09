'''
Created on Oct 5, 2013

@author: geraldine
'''
from ch.fluxkompensator.nelliepi.music import Player
from ch.fluxkompensator.nelliepi.ui.state import UiState
def function(*args):
    print("setting screen to ListScreen")
    screen = UiState.getScreen("listScreen")
    if(screen is None):
        raise ValueError("screen not found listScreen")
    else:
        startIndex=0
        if(len(args) > 0):
            startIndex=args[0]
        screen.setDirectoryToList(Player.listFiles(), pStartIndex=startIndex)
        UiState.setScreen(screen)