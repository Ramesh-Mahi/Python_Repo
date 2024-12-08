# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

# INPUT : 

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# O/T:
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

if __name__ == '__main__':
    N = int(input())
    query=list()
    list1=list()
    for _ in range(N):
        query = list(map(str,input().split()))
        #print(query)
        if query[0] == 'insert':
            list1.insert(int(query[1]),int(query[2]))
            continue
        if query[0] == 'print':
            print(list1)
        if query[0] == 'remove':
            try:
                list1.remove(int(query[1]))
            except:
                continue
        if query[0] == 'append':
            list1.append(int(query[1]))
        if query[0] == 'sort':
            list1.sort()
        if query[0] == 'pop':
            list1.pop()
        if query[0] == 'reverse':
            list1.reverse()
        
        
