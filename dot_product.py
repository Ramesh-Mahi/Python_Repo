# You are given two arrays  and . Both have dimensions of X.
# Your task is to compute their matrix product.

# Input Format

# The first line contains the integer .
# The next  lines contains  space separated integers of array .
# The following  lines contains  space separated integers of array .

# Sample Input

# 2
# 1 2
# 3 4
# 1 2
# 3 4

# Sample Output

# [[ 7 10]
#  [15 22]]

import numpy as np

# A = [ 1, 2 ]
# B = [ 3, 4 ]

N = int(input())
A, B = [],[]
for i in range(N):
    A.append(list(map(int,input().split())))
for i in range(N):
    B.append(list(map(int,input().split())))

print(np.dot(A,B))
