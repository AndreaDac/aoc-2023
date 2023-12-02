import re
import numpy

# part 1
def partOne():
    sum = 0
    with open("input1.txt") as file:
        for line in file:
            s1 = line.split(":")
            combo = re.findall("\d+ \w", s1[1])  
            game = int(re.findall("\d+",s1[0])[0])
            if (isValidCombo(combo)):
                sum = sum + game
    print(sum)            

def isValidCombo(combo):
    dictValidation = {"r": 12, "g":13, "b":14}
    for elem in combo:
        if (dictValidation[elem.split(" ")[1]] < int(elem.split(" ")[0])):
            return False
    return True

# part 2 
def partTwo():
    sum = 0
    with open("input1.txt") as file:
        for line in file:
            s1 = line.split(":")
            combo = re.findall("\d+ \w", s1[1])
            sum = sum + findValue(combo)      
    print(sum)         

def findValue(combo):
    resultDict = {color: [int(value) for value, itemColor in map(str.split, combo) if itemColor == color] for _, color in map(str.split, combo)}
    maxValues = [max(values) for values in resultDict.values()]
    return numpy.prod(maxValues)

if __name__=="__main__":
    partOne()
    partTwo()