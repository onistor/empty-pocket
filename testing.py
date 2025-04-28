# N = int(input())
# c=0
# my_list=[]
# while N>c:
#     c=c+1
#     my_list.append(input())
# else:
#     print(my_list)

N = int(input())
c = 2
while c < N:
    if N % c != 0:
        c = c + 1
        continue
    else: print('False')
    break
else:
    print('True')
