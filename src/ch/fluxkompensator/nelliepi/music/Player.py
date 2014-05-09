'''
Created on Oct 4, 2013

@author: geraldine
'''
from mpd import MPDClient

client = MPDClient()
oldVolume = None

def init():
    # logging.basicConfig(level=logging.DEBUG)
    client.timeout = 10                # network timeout in seconds (floats allowed), default: None
    client.idletimeout = None          # timeout for fetching the result of the idle command is handled seperately, default: None
    client.connect("localhost", 6600)  # connect to localhost:6600
    
def listFiles(pDirectoryName=None):
    if pDirectoryName is None :
        return client.listall()
    else:
        return client.listall(pDirectoryName)

def play(pSong=None):
    if pSong is None:
        client.play()
    else :
        client.clear()
        client.add(pSong)
        client.play()

def stop():
    client.stop()    
    
def pause():
    client.pause()
    
def mute():
    global oldVolume
    
    oldVolume = 80
    print("muting once i found out how")
#     client.setvol(0);
    
def unmute():
    print("unmuting once i found out how")
  #  client.setvol(oldVolume)
    
def dispose():        
    client.close()                     # send the close command
    client.disconnect()