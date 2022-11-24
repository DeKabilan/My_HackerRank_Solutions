#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    ne=0
    p=0
    z=0
    n=len(arr)
    for i in range(0,n):
        if arr[i]==0:
            z=1+z
        elif arr[i]<0:
            ne=1+ne       
        elif arr[i]>0:
            p=1+p
    z=round(z/n,6)
    p=round(p/n,6)
    ne=round(ne/n,6)
    print("{0:.6f}".format(p))
    print("{0:.6f}".format(ne))
    print("{0:.6f}".format(z))
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
