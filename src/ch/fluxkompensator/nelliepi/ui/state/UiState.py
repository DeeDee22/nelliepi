'''
Created on Oct 4, 2013

@author: geraldine
'''
import pygame
screens = None
buttons = None

currentScreen = None
lastScreen = None

pygameScreen = None

def getCurrentScreen():
    return currentScreen

def getLastScreen():
    return lastScreen

def setScreen(pScreen):
    global lastScreen
    global currentScreen
    
    if lastScreen is None:
        lastScreen = pScreen
    else:
        lastScreen = currentScreen
        
    currentScreen = pScreen
    
    pygameScreen.blit(currentScreen.getSurface(), (0, 0))
    pygame.display.flip()
        

def addButton(pButton, pScreen): 
    global buttons
    global buttons
    if screens is None or not pScreen in screens:
        raise ValueError("The screen you are trying to add the button to does not exist.")
    if buttons is None:
        buttons = [(pButton, pScreen),]
    else:
        buttons.append((pButton, pScreen))
            
def addScreen(pScreen):
    global screens
    if screens is None:
        screens = [pScreen,]
    else:
        screens.append(pScreen)
        
def getButtonsForScreen(pScreen):
    result = []
    for button in buttons:
        if button[1] == pScreen:
            result.append(button[0])
    return result

def getScreen(pName):
    if screens is None:
        return None
    for screen in screens:
        if screen.getName() == pName:
            return screen
    return None
        
def toString():
    if not screens is None:
        result = "screens are: "
        for screen in screens:
            result += " <"
            result += screen.getName()
            result += "> "
    else:
        result = "no screens"
        
    if not buttons is None:
        result += " :: buttons are: "
        for button in buttons:
            result += " [<"
            result += button[0].getName()
            result += "> of <"
            result += button[1].getName()
            result += ">]"
    else:
        result += " :: no buttons"
        
    result += " :: current state is <"
    if currentScreen is None:
        result += "NONE"
    else:
        result += currentScreen.getName()
    result += "> , last state is <"
    if lastScreen is None:
        result += "NONE"
    else:
        result += lastScreen.getName()
    result += ">"
    return result 