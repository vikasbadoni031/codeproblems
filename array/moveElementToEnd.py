'''
Ques: Move all instances of a given element to the end of the array.
1) The elemnets should be moved in place. Means you cant use another space.
2) We dont care about the order of other elements in the array.
eg: [2,1,2,2,2,3,4,2] 2
ans: [1,3,4,2,2,2,2,2]
'''



def moveElementToEnd(inputArray, targetNo):
    LP = 0
    RP = len(inputArray) - 1
    while LP < RP:
        while LP < RP and inputArray[LP] != targetNo:
            LP += 1
        while LP < RP and inputArray[RP] == targetNo:
            RP -= 1
        temp = inputArray[LP]
        inputArray[LP] = inputArray[RP]
        inputArray[RP] = temp
        print(inputArray)
    return inputArray



if __name__ == "__main__":
    #inputs
    inputArray = [2,1,2,2,2,3,4,2]
    targetNo = 2

    result = moveElementToEnd(inputArray, targetNo)
    #print(result)

