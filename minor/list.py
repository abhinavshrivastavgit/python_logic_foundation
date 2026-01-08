my_list = []
N = int(input())
for i in range(N):
    line = input().split()
    if line[0]=='append':
        i = int(line[1])
        my_list.append(i)
    elif line[0] == 'insert':
        i = int(line[1])
        e = int(line[2])
        my_list.insert(i,e)
    elif line[0] =='print':
        print(my_list)
    elif line[0] == 'sort':
        my_list.sort()
    elif line[0] == 'pop':
        my_list.pop()
    elif line[0] == 'reverse':
        my_list.reverse()

# print(my_list)
