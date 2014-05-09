'''
Created on Oct 4, 2013

@author: geraldine
'''
from ch.fluxkompensator.nelliepi.ui.screen.ScreenWithFooter import ScreenWithFooter
from ch.fluxkompensator.nelliepi.ui.widgets.TextButton import TextButton
from ch.fluxkompensator.nelliepi.Constants import RED
from ch.fluxkompensator.nelliepi.Constants import BLUE
from ch.fluxkompensator.nelliepi.functions import ListFunction
from ch.fluxkompensator.nelliepi.ui.state import UiState

class ListScreen(ScreenWithFooter):
    '''
    classdocs
    '''
    fileList = None
    PADDING = 5
    NUMBER_OF_POSSIBLE_ROWS = 8

    def __init__(self):
        '''
        Constructor
        '''
        ScreenWithFooter.__init__(self, "listScreen")
       
    def setDirectoryToList(self, pFileList, pStartIndex=0):
        print("start index is " + str(pStartIndex))
        
        self.fileList = pFileList
        fontSize=self.getFontSize(self.getMaxHeight(), len(self.fileList))
        self.addPrevButton(pStartIndex)
        i = 0
        maxIndex=self.getMaxIndex(pStartIndex, len(self.fileList))
        print("max index is " + str(maxIndex))
        for currentFile in self.fileList:
            if i >= pStartIndex and i <= maxIndex:
                if currentFile.has_key("directory"):
                    directoryName = currentFile["directory"]
                    #print("directory: " + directoryName)
                    button = TextButton(self.getMaxWidth() / 2, self.getHeightForButton(self.getMaxHeight(), len(self.fileList), i, pStartIndex), directoryName, pColor=RED, pFontSize=fontSize)
                    self.addButton(button)
                elif currentFile.has_key("file"):
                    fileName = self.extractFileName(currentFile["file"])
                    #print("file: " + fileName)
                    button = TextButton(self.getMaxWidth() / 2, self.getHeightForButton(self.getMaxHeight(), len(self.fileList), i, pStartIndex), fileName, pFontSize=fontSize)
                    self.addButton(button)
            i=i+1
        self.addNextButton(pStartIndex, maxIndex)

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
    
    def getMaxIndex(self, pStartIndex, pTotalNumber):
        maxIndex=pStartIndex + self.NUMBER_OF_POSSIBLE_ROWS -1
        if pTotalNumber > maxIndex + 1:
            #in this case we need a "next" element
            maxIndex = maxIndex -1
        if pStartIndex > 0:
            #in this case we need a "previous" element
            maxIndex = maxIndex -1
        return maxIndex
    
    def addPrevButton(self, pStartIndex):
            if pStartIndex > 0:
                nextStartIndex = pStartIndex - self.NUMBER_OF_POSSIBLE_ROWS
                
                #next screen definitly has a next button
                nextStartIndex = nextStartIndex  + 1
                    
                #does previous screen have a previous button?
                if nextStartIndex > 0:
                    nextStartIndex = nextStartIndex + 1
                
                if nextStartIndex < 0:
                    nextStartIndex = 0
                print("next start index for PrevButton: " + str(nextStartIndex))
                fontSize=self.getFontSize(self.getMaxHeight(), len(self.fileList))
                button = TextButton(self.getMaxWidth() / 2, self.getHeightForPrevElemetn(self.getMaxHeight(), len(self.fileList)), "<previous>", pColor=BLUE, pFontSize=fontSize, pMethod=ListFunction.function, pParams=[nextStartIndex ,])
                self.addButton(button)
                    
    def addNextButton(self, pStartIndex,pMaxIndex):
        if len(self.fileList) > pMaxIndex + 1:
            nextStartIndex=pMaxIndex + 1
            print("next start index forNextButton: " + str(nextStartIndex))
            fontSize=self.getFontSize(self.getMaxHeight(), len(self.fileList))
            button = TextButton(self.getMaxWidth() / 2, self.getHeightForButton(self.getMaxHeight(), len(self.fileList),pMaxIndex +1, pStartIndex), "<next>", pColor=BLUE, pFontSize=fontSize, pMethod=ListFunction.function, pParams=[nextStartIndex,])
            self.addButton(button)
                   