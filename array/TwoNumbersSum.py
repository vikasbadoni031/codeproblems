'''
Question: 
1) find two numbers in the array that sums up to a target sum.
2) No number is repeated
eg: [-1,5,9,8,11,3,1,6]
target sum = 10
ans: [-1,11]
'''


def convertToDict(inputArray):
    tempDict = {}
    index = 0
    for item in inputArray:
        tempDict[item] = index
        index = index + 1
    return tempDict


def findSum(inputDict, targetSum):
    for item in inputDict.keys():
        otherNumber = targetSum - item
        if otherNumber == item:
            continue
        if otherNumber in inputDict:
            return [item, otherNumber]
    return "No pair found"


if __name__ == "__main__":
    # inputs
    inputArray = [-1,5,9,8,11,3,1,6]
    targetSum = -5

    inputDict = convertToDict(inputArray)
    solutionPair = findSum(inputDict, targetSum)
    print(solutionPair)


'''
test edge cases:
1) What if the number compares to itself.
2) What if the target sum expectation is negative.
'''