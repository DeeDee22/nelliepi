'''
Created on Oct 5, 2013

@author: geraldine
'''

def function(*args):
    button=args[0]
    currentFunction= args[1]
    nextFunction= args[2]
    currentText= args[3]
    nextText= args[4]
    currentFunction()
   
    button.setText(nextText)
    button.setMethod(function, pParams=[button, nextFunction, currentFunction, nextText, currentText])