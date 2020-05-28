#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    min1=0
    max1=0
    for i in range(0,4):
        min1=min1+arr[i]
    for i in range(1,5):
        max1=max1+arr[i]

    print(min1,max1)
   

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
