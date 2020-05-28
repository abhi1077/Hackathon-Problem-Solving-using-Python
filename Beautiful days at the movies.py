#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    cnt=0
    for x in range(i,j+1):
        rev=0
        y=x
        while y>0:
            dig=y%10
            rev=rev*10+dig
            y=y//10
        if abs(x-rev)%k==0 or abs(x-rev)==0:
            cnt+=1
    return cnt        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
