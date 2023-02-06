'''
Ques: Check if an array is monotonic. Which means its either increasing or decreasing. (Equals values are allowed.) 

edge cases:
when the starting nos are same. So from the starting nos u cant find the flow direction.
'''


#checks and sets direction
def setDirection(inputArray,p2,p1):
    if inputArray[p1] > inputArray[p2]:
        direction = "increasing"
    elif inputArray[p2] > inputArray[p1]:
        direction = "decreasing"
    return direction

def isMonotonic(inputArray):
    p1 = 0
    p2 = -1
    flag = "unset"
    for i in range(0,len(inputArray)-2):
        p1 = p1 + 1
        p2 = p1 + 1
        if inputArray[p1] == inputArray[p2]:
            continue

        #finding direction once
        if flag == "unset":
            direction = setDirection(inputArray,p2,p1)
            flag = "set"
        
        if direction == "increasing":
            if inputArray[p2] > inputArray[p1]:
                return "Non Monotonic"
        elif direction == "decreasing":
            if inputArray[p1] > inputArray[p2]:
                return "Non Monotonic"
    return "Monotonic"




if __name__ == "__main__":
    #inputs
    inputArray = [-1,-5,-10,-1100,-1101,-1102,-9001,-9001]

    result = isMonotonic(inputArray)
    print(result)












