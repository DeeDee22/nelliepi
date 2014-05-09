'''
Created on Oct 4, 2013

@author: geraldine
'''
from ch.fluxkompensator.nelliepi.ui.screen.ScreenWithFooter import ScreenWithFooter
from ch.fluxkompensator.nelliepi.ui.widgets.TextButton import TextButton
from ch.fluxkompensator.nelliepi.Constants import RED
from ch.fluxkompensator.nelliepi.Constants import BLUE
from ch.fluxkompensator.nelliepi.functions import ListFunction

class ListScreen(ScreenWithFooter):
    '''
    classdocs
    '''
    fileList = None
    PADDING = 5

    def __init__(self):
        '''
        Constructor
        '''
        ScreenWithFooter.__init__(self, "listScreen")
       
    def setDirectoryToList(self, pFileList, pStartIndex=0):
        #clear screen first
        self.clear()
        
        self.fileList = pFileList
        fontSize=self.getFontSize(self.getMaxHeight(), len(self.fileList))
        if pStartIndex > 0:
            button = TextButton(self.getMaxWidth() / 2, self.getHeightForPrevElemetn(self.getMaxHeight(), len(self.fileList)), "<previous>", pColor=BLUE, pFontSize=fontSize)
            self.addButton(button)
        i = 0
        maxIndex=self.getMaxIndex(pStartIndex, self.getMaxHeight(), len(self.fileList))
        for currentFile in self.fileList:
            if i >= pStartIndex and i <= maxIndex:
                if currentFile.has_key("directory"):
                    directoryName = currentFile["directory"]
                    print("directory: " + directoryName)
                    button = TextButton(self.getMaxWidth() / 2, self.getHeightForButton(self.getMaxHeight(), len(self.fileList), i, pStartIndex), directoryName, pColor=RED, pFontSize=fontSize)
                    self.addButton(button)
                elif currentFile.has_key("file"):
                    fileName = self.extractFileName(currentFile["file"])
                    print("file: " + fileName)
                    button = TextButton(self.getMaxWidth() / 2, self.getHeightForButton(self.getMaxHeight(), len(self.fileList), i, pStartIndex), fileName, pFontSize=fontSize)
                    self.addButton(button)
            i=i+1
        if len(self.fileList) > maxIndex + 1:
            button = TextButton(self.getMaxWidth() / 2, self.getHeightForButton(self.getMaxHeight(), len(self.fileList),maxIndex +1, pStartIndex), "<next>", pColor=BLUE, pFontSize=fontSize, pMethod=ListFunction.function, pParams=[maxIndex + 1,])
            self.addButton(button)
            

    def extractFileName(self, fileWithPath):
        index = fileWithPath.rfind("/")
        return fileWithPath[index+1:]
    
    def getHeightForPrevElemetn(self, pMaxHeight, pTotalNumber):
        fontSize = self.getFontSize(pMaxHeight, pTotalNumber)
        return fontSize / 2 + self.PADDING
    
    def getHeightForButton(self, pMaxHeight,  pTotalNumber, pIndex, pStartIndex):
        relativeIndex = pIndex - pStartIndex
        rowForPrevElement = 0
        if pStartIndex > 0:
            rowForPrevElement = 1
        fontSize = self.getFontSize(pMaxHeight, pTotalNumber)
        firstElement = fontSize / 2 + self.PADDING
        rowHeight = fontSize + self.PADDING
        return firstElement + relativeIndex * rowHeight + rowForPrevElement * rowHeight

    def getFontSize(self, pMaxHeight, pTotalNumber):
        return 20
    
    def getMaxIndex(self, pStartIndex, pMaxHeight, pTotalNumber):
        numberOfPossibleRows=8
        maxIndex=pStartIndex + numberOfPossibleRows -1
        if pTotalNumber > maxIndex + 1:
            #in this case we need a "next" element
            maxIndex = maxIndex -1
        if pStartIndex > 0:
            #in this case we need a "previous" elemetn
            maxIndex = maxIndex -1
        return maxIndex
        