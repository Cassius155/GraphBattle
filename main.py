import matplotlib.pyplot as plt
import numpy as np
import re

OPERATORS = ['+', '-', '*', '/', '^']

def functionParser():
    while(True):
        print("Input function:")
        userInput = input()
        valid = validFunction(userInput)
        if(valid):
            print("Function is valid")
            break
        else:
            print("Invalid function")
        break

def validFunction(func):
    funcChars = list(func)
    funcTerms = []
    lastChar = 0
    for currIdx in range(len(funcChars)):
        if(funcChars[currIdx] in OPERATORS):
            if(currIdx == lastChar):
                return False
            else:
                funcTerms.append(funcChars[lastChar:currIdx])
                lastChar = currIdx + 1
    


    #regEx = re.compile(r"^([-+/*]\d+(\.\d+)?)*")
    #return regEx.match(func)

functionParser()