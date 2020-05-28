#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(string):
    cnt=0
    for a in string:
        if a.isupper()==True:
            cnt+=1
    return (cnt+1)        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    string = input()

    result = camelcase(string)

    fptr.write(str(result) + '\n')

    fptr.close()
