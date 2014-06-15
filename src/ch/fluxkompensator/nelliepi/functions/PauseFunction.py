'''
Created on Oct 5, 2013

@author: geraldine
'''
from ch.fluxkompensator.nelliepi.music import Player
def function(*args):
    #param 0 is the muteFunction, param 1 is the unmuteFunction
    print("Pausing")
    Player.pause()