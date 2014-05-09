'''
Created on Oct 5, 2013

@author: geraldine
'''
from ch.fluxkompensator.nelliepi.music import Player
def function(*args):
    if(len(args)) > 0:
        print("starting to play " + args[0])
        Player.play(args[0])
    else :
        Player.play()