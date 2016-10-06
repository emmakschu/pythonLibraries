# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 13:01:27 2016

@author: michael
"""


def mean(myArray):
    mean = sum(myArray) / len(myArray)
    return mean

def sortedArray(myArray):
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
    if len(myArray) % 2 == 0:
        myArray = sortedArray(myArray)
        index = len(myArray) / 2 - 1
        index2 = len(myArray) - 1 / 2 - 2
        midIndices = [myArray[index], myArray[index2]]
        print midIndices
        
        median = mean(midIndices)
    else:
        index = (len(myArray) + 1) / 2
        median = myArray[index]       

    return median


testArray = [21, 12, 15, 7, 31, 9, 5, 16]

newArray2 = sortedArray(testArray)
firstMean = mean(testArray)

yetAnother = [-5, 14.9, 12, 17, 9, 22.1, 15]

newArray3 = sortedArray(yetAnother)
secondMean = mean(newArray3)

print "Did it work??? {0}".format(newArray2)

print "And the mean: {0}".format(firstMean)
print

print "Please... {0}".format(newArray3)
print "And the mean: {0}".format(secondMean)


print 

print median(testArray)
