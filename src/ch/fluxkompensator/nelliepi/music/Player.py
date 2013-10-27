'''
Created on Oct 4, 2013

@author: geraldine
'''
from mpd import MPDClient

client = None

def play():
    global client
    client = MPDClient()               # create client object
    client.timeout = 10                # network timeout in seconds (floats allowed), default: None
    client.idletimeout = None          # timeout for fetching the result of the idle command is handled seperately, default: None
    client.connect("localhost", 6600)  # connect to localhost:6600
    print(client.listall())           
            
    print(client.playlistinfo())
#    client.setvol(80)
    print(client.status())
    client.play()
    print(client.status())

    
def dispose():        
    client.close()                     # send the close command
    client.disconnect()