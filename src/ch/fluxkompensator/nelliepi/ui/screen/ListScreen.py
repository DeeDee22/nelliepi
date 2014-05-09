'''
Created on Oct 4, 2013

@author: geraldine
'''
from ch.fluxkompensator.nelliepi.ui.screen.ScreenWithFooter import ScreenWithFooter
from ch.fluxkompensator.nelliepi.ui.widgets.TextButton import TextButton
from ch.fluxkompensator.nelliepi.Constants import RED
from ch.fluxkompensator.nelliepi.Constants import BLUE
from ch.fluxkompensator.nelliepi.functions import ListFunction
from ch.fluxkompensator.nelliepi.functions import PlayFunction
from ch.fluxkompensator.nelliepi.music import Player


class ListScreen(ScreenWithFooter):
    '''
    classdocs
    '''
    fileList = None
    directoryName = None
    level = 0
    parentDirectory = None
    PADDING = 5
    NUMBER_OF_POSSIBLE_ROWS = 8

    def __init__(self):
        '''
        Constructor
        '''
        ScreenWithFooter.__init__(self, "listScreen")
       
    def setDirectoryToList(self, pDirectoryToList, pStartIndex=0, pParentDirectory=None):
        print("start index is " + str(pStartIndex))
        
        self.parentDirectory = pParentDirectory
        self.directoryName = pDirectoryToList
        self.fileList = self.getFileList(pDirectoryToList)
        
        fontSize=self.getFontSize(self.getMaxHeight(), len(self.fileList))
        self.addPrevButton(pStartIndex)
        i = 0
        maxIndex=self.getMaxIndex(pStartIndex, len(self.fileList))
        print("max index is " + str(maxIndex))
        for currentFile in self.fileList:
            if i >= pStartIndex and i <= maxIndex:
                if currentFile.has_key("directory"):
                    directoryName = self.extractFileName(currentFile["directory"])
                    #print("directory: " + directoryName)
                    button = TextButton(self.getMaxWidth() / 2, self.getHeightForButton(self.getMaxHeight(), len(self.fileList), i, pStartIndex), directoryName, pColor=RED, pFontSize=fontSize, pMethod=ListFunction.function, pParams=[currentFile["directory"], 0, currentFile["directory"]])
                    self.addButton(button)
                elif currentFile.has_key("file"):
                    fileName = self.extractFileName(currentFile["file"])
                    #print("file: " + fileName)
                    button = TextButton(self.getMaxWidth() / 2, self.getHeightForButton(self.getMaxHeight(), len(self.fileList), i, pStartIndex), fileName, pFontSize=fontSize, pMethod=PlayFunction.function, pParams=[currentFile["file"]])
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
                button = TextButton(self.getMaxWidth() / 2, self.getHeightForPrevElemetn(self.getMaxHeight(), len(self.fileList)), "<previous>", pColor=BLUE, pFontSize=fontSize, pMethod=ListFunction.function, pParams=[self.directoryName, nextStartIndex, self.parentDirectory])
                self.addButton(button)
                    
    def addNextButton(self, pStartIndex,pMaxIndex):
        if len(self.fileList) > pMaxIndex + 1:
            nextStartIndex=pMaxIndex + 1
            print("next start index forNextButton: " + str(nextStartIndex))
            fontSize=self.getFontSize(self.getMaxHeight(), len(self.fileList))
            button = TextButton(self.getMaxWidth() / 2, self.getHeightForButton(self.getMaxHeight(), len(self.fileList),pMaxIndex +1, pStartIndex), "<next>", pColor=BLUE, pFontSize=fontSize, pMethod=ListFunction.function, pParams=[self.directoryName, nextStartIndex, self.parentDirectory])
            self.addButton(button)
                   
    def getFileList(self, pDirectoryName):
            wholeList = Player.listFiles(pDirectoryName)
            result = []
            for currentFile in wholeList:
                    fileName = None
                    if(currentFile.has_key("directory")):
                        fileName=currentFile["directory"]
                    else:
                        fileName=currentFile["file"]
                    if self.isDirectlyInDirectory(fileName):
                        result.append(currentFile);
            
            return result
        
    def isDirectlyInDirectory(self, fileName):
        level = 0
        if not self.parentDirectory is None:
            level=self.parentDirectory.count("/") + 1
        occurences = fileName.count("/")
        
        parentDirString = "None"
        if not self.parentDirectory is None:
            parentDirString = self.parentDirectory
        print("parent: " + parentDirString + " fileName:" + fileName + " occurences: " + str(occurences) + " level: " + str(level))
        return occurences == level
