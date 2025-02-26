# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:44:09 2020

@author: user
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
        numbers = set()
        count = 0
        for n in arr:
            if n + k in numbers:
                count += 1
            if n - k in numbers:
                count += 1
            numbers.add(n)
        return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
