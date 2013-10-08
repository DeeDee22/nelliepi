'''
Created on Oct 4, 2013

@author: geraldine
'''
from ch.fluxkompensator.nelliepi.ui.state import UiState

def getPressedButton(pPosition):
    currentButtons = UiState.getButtonsForScreen(UiState.getCurrentScreen())
    for button in currentButtons:
        if button.wasTouched(pPosition):
            return button