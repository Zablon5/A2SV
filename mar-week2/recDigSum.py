#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
      
        

def superDigit(n, k):
    s=0
    for i in (n):
        s+=int(i)
        
    def rec(x):
        if x<10:
            return x
        else:
            s=0
            while x>0:
                s=s+(x%10)
                x=x//10
            return rec(s)  
    print(rec(k*s))
    return rec((k*s))
    # Write your code here
       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
