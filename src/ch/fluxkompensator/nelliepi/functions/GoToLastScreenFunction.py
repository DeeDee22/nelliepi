'''
Created on Oct 5, 2013

@author: geraldine
'''
from ch.fluxkompensator.nelliepi.ui.state import UiState
def function(*args):
    screen = UiState.getLastScreen()
    if(screen is None):
        raise ValueError("screen not found " + args[0])
    else:
        print("Going back to screen " + screen.getName());
        UiState.setScreen(screen)