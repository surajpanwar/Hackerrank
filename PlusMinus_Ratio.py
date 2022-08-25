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
    # Write your code here

    pos = 0
    neg = 0
    zero = 0
    for i in range(n):
        if arr[i] > 0:
            pos += 1
        if arr[i] < 0:
            neg += 1
        if arr[i] == 0:
            zero += 1
    posratio = (pos / n)

    negratio = abs(neg / n)
    zeroratio = abs(zero / n)
    print(round(posratio, 5))
    print(round(negratio, 5))
    print(round(zeroratio, 5))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
