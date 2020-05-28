#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    cnt1,cnt2,cnt3,cnt4,fcnt=0,0,0,0,0
    
    for a in password:
        if a.isupper()==True:
            cnt1+=1
        elif a.islower()==True:
            cnt2+=1
        elif a.isdigit()==True:
            cnt3+=1
        elif a=="!" or a=="@" or a=="#" or a=="$" or a=="%" or a=="^" or a=="&" or a=="*" or a=="(" or a==")" or a=="-" or a=="+":

            cnt4+=1   
    if cnt1>0:
        fcnt+=1
    if cnt2>0:
        fcnt+=1
    if cnt3>0:
        fcnt+=1
    if cnt4>0:
        fcnt+=1  
    if n<6:
        b=6-n
        c=4-fcnt
        if c>b: 
            return (c)
        else:
            return (b)

        return(6-n)
    else:
        return(4-fcnt)    

                          


    

    # Return the minimum number of characters to make the password strong

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
