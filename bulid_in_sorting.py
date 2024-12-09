# Your task is to sort the string  in the following manner:

# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.
# Input Format

# A single line of input contains the string .

# Sample Input

# Sorting1234

# Sample Output

# ginortS1324

# Enter your code here. Read input from STDIN. Print output to STDOUT
S = input()
upper = []
lower = []
even = []
odd =[]

for i in S:
    if i.isnumeric():
        if ((int(i)%2) == 0):
            even.append(i)
        else:
            odd.append(i)
    else:
        if i.isupper():
            upper.append(i)
        else:
            lower.append(i)

print(''.join(sorted(lower))+''.join(sorted(upper))+''.join(sorted(odd))+''.join(sorted(even)))
