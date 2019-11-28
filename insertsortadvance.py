#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort(arr):
    shifts=0
    arrindex=[0]*(max(arr)+1)
    count=0
    currmin=arr[0]
    currmax=arr[0]
    for x,y in enumerate(arr):
        if y<currmin:
            currmin=y
            shifts+=count
            count+=1
            arrindex[y]+=1
            print('1here',shifts)
            continue
        if y>currmax:
            currmax=y
            count+=1
            arrindex[y]+=1
            continue
        
        if (y-currmin)<(currmax-y):
            smallercount=0
            print('currmin',currmin, y)
            for x in arrindex[currmin:y]:
                smallercount+=x
            shifts+=(count-smallercount)
            print('here c' ,shifts)
        else:
            for x in arrindex[y+1:currmax+1]:
                print('here test',x)
                shifts+=x
        print(shifts)
        arrindex[y]+=1
        count+=1
                
    return shifts

print(insertionSort([2,1,3,1,2]))
