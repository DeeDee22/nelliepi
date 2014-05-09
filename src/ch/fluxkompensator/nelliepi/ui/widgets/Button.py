'''
Created on Oct 3, 2013

@author: geraldine
'''

class Button(object):
    '''
    classdocs
    '''


    def __init__(self, pX, pY, pName, pMethod=None, pParams=None):
        '''
        Constructor
        '''
        self.x = pX
        self.y = pY
        self.name = pName
        self.method = pMethod
        self.params = pParams
        
    def execute(self):
        if not self.method is None:
            if not self.params is None:
                self.method(*self.params)
            else:
                self.method()
        
    def wasTouched(self, pPosition): 
        return False
    
    def getSurface(self):
        return None
    def getPosition(self):
        return None
    
    def getName(self):
        return self.name
    
    def setMethod(self, pMethod, pParams=None):
        self.method = pMethod
        self.params = pParams