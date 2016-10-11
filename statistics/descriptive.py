# -*- coding: utf-8 -*-
"""
statistics/descriptive.py

Author: Michael K Schumacher
Github: mkschu
Web:    mkschumacher.com

Created:  10/05/2016
Modified: 10/06/2016

A custom Python3 module to perform basic descriptive statistical
calculations without importing other modules (e.g. NumPy, SciPy).
Will be mirrored by equivalent libraries for C++ and Java.

"""

def length(myArray):
    i = 0
    for item in myArray:
        i += 1
    return i

def arraySum(myArray):
    total = 0
    for item in myArray:
        total += item
    return total

def mean(myArray):
    mean = float(arraySum(myArray)) / length(myArray)
    return mean 
    
def sortArray(myArray):
    for i in range(0, len(myArray) - 1):
        for j in range(0, len(myArray) - 1):
            if myArray[j] > myArray[j+1]:
                temp = myArray[j+1]
                myArray[j+1] = myArray[j]
                myArray[j] = temp  
        if myArray[i] > myArray[i+1]:
            temp = myArray[i+1]
            myArray[i+1] = myArray[i]
            myArray[i] = temp
    return myArray

def median(myArray):
    myArray = sortArray(myArray)
    i = length(myArray)
    
    if i % 2 == 0:
        index1 = int(i / 2)
        index2 = int(i / 2 - 1)
        
        midIndices = [myArray[index1], myArray[index2]]
        
        median = mean(midIndices)
    
    else:
        index = int(i / 2)
        median = myArray[index]
    
    return median
  

"""
Testing section:
"""  
array1 = [1,12,7,13,2,5,3]

print(length(array1))
print(arraySum(array1))
print(mean(array1))
print()

print(sortArray(array1))
print()
print(median(array1))
