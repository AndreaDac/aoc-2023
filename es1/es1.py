import re

def partOne():
    sum = 0
    with open("input_simple.txt") as file:
        for line in file:
            singleLine = re.findall("[1-9]", line)
            number = int(singleLine[0] + singleLine[-1])
            sum = sum + number
    print(sum)       
            
def partTwo():
    sum = 0
    with open("input2_simple.txt") as file:
        for line in file:
            singleLine = re.findall ("(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))", line)
            number = int(numberValue(singleLine[0]) + numberValue(singleLine[-1]))
            sum = sum + number
    print(sum)        

def numberValue(numb):
    dic = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    return dic[numb] if (numb in dic.keys()) else numb

if  __name__ == "__main__":
    partOne()
    partTwo()