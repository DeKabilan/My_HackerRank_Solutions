#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    high=0
    low=0
    current=scores[0]
    currentl=scores[0]
    for i in range(len(scores)):
        if scores[i]>current:
            high=high+1
            current=scores[i]
        if scores[i]<currentl:
            low=low+1
            currentl=scores[i]
    return high,low

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
