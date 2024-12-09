# Input Format

# The first line contains N and M  separated by a space.
# The next N  lines each contain M elements.
# The last line contains K.

# I/O:
# 5 3
# 10 2 5
# 7 1 0
# 9 9 9
# 1 23 12
# 6 5 9
# 1

# O/P:
# 7 1 0
# 10 2 5
# 6 5 9
# 9 9 9
# 1 23 12

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    #getting the input and removing the white spaces and spliting into list with map fn
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    k = int(input().strip())
    #sorting the list with the 'k' as the key 
    arr.sort(key=lambda x : x[k])
    
    for i in arr:
        for j in i:
            print(j,end =' ')
            #printing in the same line by usin end=''
        print()
        
