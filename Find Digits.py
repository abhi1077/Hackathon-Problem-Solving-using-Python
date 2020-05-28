#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    m=n
    cnt=0
    ar=[0]*9
    for i in range(0,9):
        ar[i]=int(n%10)
        n=int(n/10)
        if n==0:
            break
    for i in range(0,9):
        if ar[i]!=0:

            if m%ar[i]==0:
                 cnt+=1
    return cnt       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
