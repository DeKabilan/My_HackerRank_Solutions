#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sums=0
    n=len(arr)
    for i in range(n):
        sums=sums+arr[i]
        cmax=sums-arr[0]
        cmin=sums-arr[0]

    for i in range(1,n):   
        current=sums-arr[i]
        if current<cmin:
            cmin=current
        if current>cmax:
            cmax=current
    print(str(cmin)+" "+str(cmax))
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
