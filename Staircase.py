#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    blank=""
    for i in range(n):
        for j in range((n-i)-1):
            blank=" "+blank
        for k in range((n-i)-1,n):
            blank=blank+"#"
        print(blank)
        blank=""
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
