import re

# part One
def partOne():
    sum = 0
    with open("input1.txt") as file:
        for line in file:
            winningNumber = line.split(":")[1].split("|")[0]
            myNumber = line.split(":")[1].split("|")[1]
            sum += matchNumber(re.findall("\d+",winningNumber), re.findall("\d+",myNumber))
    print(sum)        

def matchNumber(winningNumber, myNumber):
    return int(pow(2, len(list(set(winningNumber) & set(myNumber)))-1))

#part Two
def partTwo():
    dictCard={}
    with open("input1.txt") as file:
        for line in file:
            gameNumber = int(re.findall("\d+",line.split(":")[0])[0])
            match = len(list(set(re.findall("\d+", line.split(":")[1].split("|")[0])) & set(re.findall("\d+", line.split(":")[1].split("|")[1]))))
            constructDict(gameNumber, dictCard, match)
    print(sum(dictCard.values()))        

def constructDict(gameNumber, dictCard, match):
    addElementsToDict(gameNumber, dictCard, 1)
    for elem in range(gameNumber+1, gameNumber+match+1):
        addElementsToDict(elem, dictCard, dictCard[gameNumber])

def addElementsToDict(number, dict, value):
    if number in dict:
        dict[number] += value
    else:
        dict[number] = value

if __name__ == "__main__":
    partOne()
    partTwo()