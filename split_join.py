def split_and_join(line):
    # write your code here
    line1 = line.split(" ") # converting string to list and spliting with a space
    line2 = "-".join(line1) # converting list to string and join with a "-"
    return line2

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
