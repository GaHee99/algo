import sys
# sys.stdin = open("인프런/Chapter[3]/input.txt",'r')
stoq=[]
for i in range(9):
    stoq.append(list(map(int,input().split())))
answer= [ 1,2,3,4,5,6,7,8,9]



for i in range(9):
    list=[]
    list2=[]
    for k in range(9):
        list2.append(stoq[i][k])
        list.append(stoq[k][i])
        list.sort()
        list2.sort()
    if list !=answer or list2!=answer:
        print("NO")
        sys.exit(0)
        

for a in range(0,9,3):
    for b in range(0,9,3):
        list=[]
        for c in range(3):
            for d in range(3):
                list.append(stoq[a+c][b+d])
        list.sort()
        if list == answer:
            continue
        else:
            print("NO")
            sys.exit(0)

else:
    print("YES")