'''
Question: Given two arrays, find pair of numbers, one from each array, so that the difference between them is smallest.
Eg: [-1,5,10,20,28,3] and [26,134,135,15,17]
ans: [28,26]
'''

#O(n+m) + O(nlogn + mlogm), O(1) space
def smallestDifference(inputarray1, inputarray2):
    leftPointer = 0
    rightPointer = 0

    smallestDifference = float("inf")

    while leftPointer < len(inputarray1)-1 and rightPointer < len(inputarray2)-1:

        # When both numbers are equal
        if inputarray2[rightPointer] == inputarray1[leftPointer]:
            return 0, inputarray2[rightPointer], inputarray1[leftPointer]

        if inputarray2[rightPointer] > inputarray1[leftPointer]:
            leftPointer = leftPointer + 1
        else:
            rightPointer = rightPointer + 1
        tempDifference = inputarray2[rightPointer] - inputarray1[leftPointer]
        if abs(tempDifference) <= smallestDifference:
            smallestDifference = abs(tempDifference)
            numberOne = inputarray2[rightPointer]
            numberTwo = inputarray1[leftPointer]
    return smallestDifference, numberOne, numberTwo

if __name__ == "__main__":
    #inputs
    inputarray1 = [-1,5,10,20,28,3]
    inputarray2 = [26,34,10,15,17]

    #sort inputs
    inputarray1.sort()  #adds nlogn + mlogm complexity
    inputarray2.sort() 

    difference, numberOne, numberTwo =  smallestDifference(inputarray1, inputarray2)
    print("Difference = ",difference)
    print("numberOne = ", numberOne)
    print("numberTwo = ", numberTwo)



