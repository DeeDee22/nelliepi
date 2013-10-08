'''
Created on Oct 5, 2013

@author: geraldine
'''
from ch.fluxkompensator.nelliepi.ui.state import UiState
def function(*args):
    print("seting screen to " + args[0]);
    screen = UiState.getScreen(args[0])
    if(screen is None):
        raise ValueError("screen not found " + args[0])
    else:
        UiState.setScreen(screen)