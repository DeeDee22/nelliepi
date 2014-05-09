'''
Created on Oct 5, 2013

@author: geraldine
'''
from ch.fluxkompensator.nelliepi import Quitter
from ch.fluxkompensator.nelliepi.music import Player

def function(*args):
    Player.stop()
    Quitter.quit_nelliepi()