#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):

    k=n-1  #k=4
    for i in range(0,n): #range(0,3 ) 0 1 2
        for j in range(0,k): #range(0,4)0 1 2 3
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("#",end="")

        print("\r")
    

if __name__ == '__main__':
    n = int(input())

    staircase(n)
