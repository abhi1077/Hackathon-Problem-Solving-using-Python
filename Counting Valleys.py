#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    height=0
    cnt=0
    prevheight=0
    for i in range(0,n):
        if s[i]=='U':
            height+=1
        elif s[i]=='D':
            height-=1
        if height==0 and prevheight==-1:
            cnt=cnt+1
        prevheight=height
    return(cnt)               
 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = list(input())

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
