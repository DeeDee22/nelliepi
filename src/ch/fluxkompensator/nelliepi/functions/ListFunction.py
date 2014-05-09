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
        fileList = None
        parentDirectory = None
        
        if len(args) > 0:
            fileList=args[0]
        if len(args) > 1:
            startIndex = args[1]
        if (len(args) > 2):
            parentDirectory = args[2]

        #clear screen first
        screen.clear()
        UiState.removeScreen(screen)
        screen.__init__()
        screen.setDirectoryToList(fileList, pStartIndex=startIndex, pParentDirectory=parentDirectory)
        UiState.setScreen(screen)