# I/P
# The first line contains an integer .  is the total number of integers in the list.
# The second line contains the space separated list of  integers.

# 5
# 12 9 61 5 14 

# O/P
# True

# Enter your code here. Read input from STDIN. Print output to STDOUT

def palindrome(digits):
    flag = list()
    for i in digits:
        flag.append(any([(i < 9),(i/11 == 0),(str(i)==str(i)[::-1])]))
    return flag
    
def alltrue(digits):
    flag = list()
    for i in digits:
        flag.append(i>0)
    return flag
    
N = int(input())
digits = list(map(int,input().split()))
# flag1, flag2 = list(), list()
# print(all([all([flag1.append(i>0) for i in digits]), 
#         flag2.append(any([(i < 9),(i/11 == 0),(str(i)==str(i)[::-1])]) for j in digits)]))

print(all([all(alltrue(digits)),any(palindrome(digits))]))
