# Input Format

# The first line of input contains the original string. The next line contains the substring.

# Constraints


# Each character in the string is an ascii character.

# Output Format

# Output the integer number indicating the total number of occurrences of the substring in the original string.

# Sample Input

# ABCDCDC
# CDC
# Sample Output

# 2

def count_substring(string, sub_string):
    #         it will return 1 everytime when the instance occurs and the sum function add everything at the end
    res = sum(1 for i in range(len(string))
                if string.startswith(sub_string,i))
    return res

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
