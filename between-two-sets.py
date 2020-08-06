#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    
    ###first generate all numbers between the end of the last list and the first of the next list. Then generate all integers between them and check if 
    the number if all numbes in list a are divisible by it and then also for list b.
    ar = [i for i in range(max(a), min(b)+ 1) if all(i%j==0 for j in a)]

    br = [i for i in ar if all(j%i==0 for j in b)]
    return len(br)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
