import sys
# sys.stdin = open("인프런/Chapter[3]/input.txt",'r')

M = []
for i in range(7):
    M.append(list(map(int,input().split())))

def check(list):
    if list==list[::-1]:
        return True
    return False

count=0
for i in range(7):
    for j in range(3):
        li = M[i][j:j+5]
        if check(li):
            count+=1
        li2=[]
        for k in range(5):
            li2.append(M[j+k][i])
        if check(li2):
            count+=1
print(count)