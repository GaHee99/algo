import sys
sys.stdin = open("인프런/Chapter[3]/input.txt",'r')

n = int(input())
apples = []
for _ in range(n):
    apples.append(list(map(int,input().split())))
s=e=n//2

res=0
for i in range(n):
    for j in range(s,e+1):
        res+=apples[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)