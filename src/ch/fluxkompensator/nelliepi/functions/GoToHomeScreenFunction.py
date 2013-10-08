'''
Created on Oct 5, 2013

@author: geraldine
'''
from ch.fluxkompensator.nelliepi.ui.state import UiState
def function(*args):
    print("seting screen to home screen");
    screen = UiState.getScreen("startScreen")
    if(screen is None):
        raise ValueError("screen not found " + args[0])
    else:
        UiState.setScreen(screen)