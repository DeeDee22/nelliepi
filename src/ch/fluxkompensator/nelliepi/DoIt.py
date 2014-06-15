'''
Created on Oct 4, 2013

@author: geraldine
'''
import pygame, os, sys
from pygame.locals import *
from ch.fluxkompensator.nelliepi.Constants import RESOLUTION
from ch.fluxkompensator.nelliepi.ui.screen.StartScreen import StartScreen
from ch.fluxkompensator.nelliepi.ui.state import UiState
from ch.fluxkompensator.nelliepi.ui.controller import ButtonCollisionDetector
from ch.fluxkompensator.nelliepi.ui.screen.MusicScreen import MusicScreen
from ch.fluxkompensator.nelliepi.ui.screen.ListScreen import ListScreen
from ch.fluxkompensator.nelliepi.music import Player
from ch.fluxkompensator.nelliepi import Quitter
from evdev import InputDevice, list_devices
from signal import alarm, signal, SIGALRM, SIGKILL
    
if __name__ == '__main__':
    
    if(len(sys.argv) > 1 and sys.argv[1] == "ON_PI"):
        devices = map(InputDevice, list_devices())
        eventX=""
        for dev in devices:
            if dev.name == "ADS7846 Touchscreen":
                eventX = dev.fn
        print eventX

        os.environ["SDL_FBDEV"] = "/dev/fb1"
        os.environ["SDL_MOUSEDRV"] = "TSLIB"
        os.environ["SDL_MOUSEDEV"] = eventX


       # this section is an unbelievable nasty hack - for some reason Pygame
    # needs a keyboardinterrupt to initialise in some limited circs (second time running)
    class Alarm(Exception):
        pass
    def alarm_handler(signum, frame):
        raise Alarm
    signal(SIGALRM, alarm_handler)
    alarm(3)
    try:
        pygame.init()
        pygameScreen = pygame.display.set_mode(RESOLUTION, 0, 32)
        alarm(0)
    except Alarm:
        raise KeyboardInterrupt

  #  pygame.display.init()
   # pygame.mixer.init()
   # pygame.joystick.init()
    #pygame.cdrom.init()
    #pygame.font.init()

    # set up the window
    UiState.pygameScreen = pygameScreen
    
    #set up the music player
    Player.init()
    
    #set up the screens

    startScreen = StartScreen()
    musicScreen = MusicScreen()
    listScreen = ListScreen()
   
    UiState.setScreen(startScreen)
    
    running = True
    
    print(UiState.toString())
    
    # run the game loop
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                Quitter.quit_nelliepi()
                running = False 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    #print("Pos: %sx%s\n" % pygame.mouse.get_pos())
                    pressedButton = ButtonCollisionDetector.getPressedButton(pygame.mouse.get_pos())
                    if(not pressedButton is None):
                        pressedButton.execute()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
        pygame.display.update()
        