#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
     a =0.000000
     b =0.000000
     c =0.000000
     for i in range(0,n):

        if arr[i]>0:
            a=a+1
        elif arr[i]<0:
            b=b+1
        else:
            c=c+1    
     print(a/n)
     print(b/n)
     print(c/n)
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
