import random

def getRandomList(start, end):
    startingList = []
    for _ in range(0, 3):
        startingList.append(random.randint(start, end))
    return startingList

def getRandomTimes(start, end):
    return random.randint(start, end)

def tribonacci(signature, n):
    if n == 2:
        signature.pop(2)
    elif n == 1:
        signature.pop(1)
        signature.pop(0)
    elif n == 0:
        signature = []
    else:
        for _ in range(n-3):
            num1, num2, num3 = signature[-3], signature[-2], signature[-1]
            newNum = num1+num2+num3
            signature.append(newNum)
    return signature


if __name__ == "__main__":
    listStartValue = int(input("What's the starting range to the list: "))
    listEndingValue = int(input("What's the ending range to the list: "))
    amountStartingValue = int(input("What's the starting range of the amount of times: "))
    amountEndingValue = int(input("What's the starting range of the amount of times: "))

    try:
        if listStartValue > listEndingValue and amountStartingValue > amountEndingValue:
            print("The starting value cannot be higher than the ending value.")
        elif listStartValue < 0 and listEndingValue < 0 and amountStartingValue < 0 and amountEndingValue < 0:
            print("Range cannot exceed into the negatives.")
        else:
            print(tribonacci(getRandomList(listStartValue, listEndingValue), getRandomTimes(amountStartingValue, amountEndingValue)))
    except ValueError:
        print("Values have to be integer numbers. (No floats, no non-numbers)")