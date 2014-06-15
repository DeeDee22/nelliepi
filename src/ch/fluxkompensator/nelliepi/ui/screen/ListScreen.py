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
    parentDirectories = None
    PADDING = 5
    NUMBER_OF_POSSIBLE_ROWS = 8

    def __init__(self):
        '''
        Constructor
        '''
        ScreenWithFooter.__init__(self, "listScreen")
       
    def setDirectoryToList(self, pDirectoryToList, pStartIndex=0, pParentDirectories=[]):
        if pParentDirectories is None :
            pParentDirectories = []
        print("start index is " + str(pStartIndex))
        dirString = "None"
        if not pDirectoryToList is None:
            dirString = pDirectoryToList
        print("pDirectoryToList is " + dirString)
        parentDirString = "None"
        if not len(pParentDirectories) == 0 :
            parentDirString = pParentDirectories[len(pParentDirectories) - 1]
        print("parent: " + parentDirString)
        
        
        self.parentDirectories = pParentDirectories
        self.directoryName = pDirectoryToList
        self.fileList = self.getFileList(pDirectoryToList)
        
        fontSize=self.getFontSize()
        self.addUpButton()
        self.addPrevButton(pStartIndex)
        i = 0
        maxIndex=self.getMaxIndex(pStartIndex, len(self.fileList))
        print("max index is " + str(maxIndex))
        for currentFile in self.fileList:
            if i >= pStartIndex and i <= maxIndex:
                if currentFile.has_key("directory"):
                    directoryName = self.extractFileName(currentFile["directory"])
                    #print("directory: " + directoryName)
                    height=self.getHeightForButton(self.getMaxHeight(), len(self.fileList), i, pStartIndex)
                    button = TextButton(10, height, ">", pColor=RED, pFontSize=fontSize, pMethod=PlayFunction.function, pParams=[currentFile["directory"]])
                    self.addButton(button)
                    button = TextButton(self.getMaxWidth() / 2, height, directoryName, pColor=RED, pFontSize=fontSize, pMethod=ListFunction.function, pParams=[currentFile["directory"], 0, self.getParentsOfChild(directoryName)])
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
        
    def getHeightForPrevElement(self, pMaxHeight, pTotalNumber):
        fontSize = self.getFontSize()
        return fontSize / 2 + self.PADDING
    
    def getHeightForButton(self, pMaxHeight,  pTotalNumber, pIndex, pStartIndex):
        relativeIndex = pIndex - pStartIndex
        rowForPrevElement = 0
        if pStartIndex > 0:
            rowForPrevElement = 1
        fontSize = self.getFontSize()
        firstElement = fontSize / 2 + self.PADDING
        rowHeight = fontSize + self.PADDING
        return firstElement + relativeIndex * rowHeight + rowForPrevElement * rowHeight

    def getFontSize(self):
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
    
    def addUpButton(self):
        if not len(self.parentDirectories) < 1:
                button = TextButton(self.getMaxWidth() -10, self.getHeightForPrevElement(self.getMaxHeight(), len(self.fileList)), "^", pColor=BLUE, pFontSize=self.getFontSize(), pMethod=ListFunction.function, pParams=[self.getDirectParent(), 0, self.getParentsOfParents()])
                self.addButton(button)
            
    def getDirectParent(self):
        if len(self.parentDirectories) < 1:
            return None
        return self.parentDirectories[len(self.parentDirectories) -1]
    
    def getParentsOfChild(self, dirNameOfThisScreen):
        if self.parentDirectories is None:
            return [self.directoryName]
        else :
            result = []
            for currentDir in self.parentDirectories:
                result.append(currentDir)
            result.append(self.directoryName)
            return result
    
    def getParentsOfParents(self):
        result = []
        i=0
        for parent in self.parentDirectories:
            if i<len(self.parentDirectories) -1:
                result.append(parent)
            i=i+1
        return result
    
    def addPrevButton(self, pStartIndex):
            if pStartIndex > 0:
                nextStartIndex = pStartIndex - self.NUMBER_OF_POSSIBLE_ROWS
                
                #next screen definitely has a next button
                nextStartIndex = nextStartIndex  + 1
                    
                #does previous screen have a previous button?
                if nextStartIndex > 0:
                    nextStartIndex = nextStartIndex + 1
                
                if nextStartIndex < 0:
                    nextStartIndex = 0
                print("next start index for PrevButton: " + str(nextStartIndex))
                button = TextButton(self.getMaxWidth() / 2, self.getHeightForPrevElement(self.getMaxHeight(), len(self.fileList)), "<previous>", pColor=BLUE, pFontSize=self.getFontSize(), pMethod=ListFunction.function, pParams=[self.directoryName, nextStartIndex, self.parentDirectories])
                self.addButton(button)
                    
    def addNextButton(self, pStartIndex,pMaxIndex):
        if len(self.fileList) > pMaxIndex + 1:
            nextStartIndex=pMaxIndex + 1
            print("next start index forNextButton: " + str(nextStartIndex))
            fontSize=self.getFontSize()
            button = TextButton(self.getMaxWidth() / 2, self.getHeightForButton(self.getMaxHeight(), len(self.fileList),pMaxIndex +1, pStartIndex), "<next>", pColor=BLUE, pFontSize=fontSize, pMethod=ListFunction.function, pParams=[self.directoryName, nextStartIndex, self.parentDirectories])
            self.addButton(button)
                   
    def getFileList(self, pDirectoryName):
            wholeList = None
            if pDirectoryName == "_main_":
                wholeList = Player.listFiles()
            else :
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
        if not len(self.parentDirectories) < 1:
            level=self.getDirectParent().count("/") + 2
            
        if self.getDirectParent() == "_main_":
            level = 1
            
        occurences = fileName.count("/")
        
        print("=====")
        parentDirString = "None"
        if not self.parentDirectories is None:
            for currentParent in self.parentDirectories:
                parentDirString = parentDirString + currentParent + ","
        print("parent: " + parentDirString + " fileName:" + fileName + " occurences: " + str(occurences) + " level: " + str(level))
        print("=====")
        return occurences == level
