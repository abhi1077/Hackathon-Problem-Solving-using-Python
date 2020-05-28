#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    a=0
    for i in range(-1,n):
        if i==0:
            a=a+1
        elif i%2!=0:
            a=a+1
        elif i%2==0:
            a=a*2    
    
    return (a)        


      


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
