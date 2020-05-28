#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    ar=[0]*5
    for i in range(0,n):
        if arr[i]==1:
            ar[0]=ar[0]+1
        elif arr[i]==2:
            ar[1]=ar[1]+1
        elif arr[i]==3:
            ar[2]=ar[2]+1
        elif arr[i]==4:
            ar[3]=ar[3]+1
        elif arr[i]==5:
            ar[4]=ar[4]+1
    a=max(ar)
    b=ar.index(a)
    b+=1
    return (b)                    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
