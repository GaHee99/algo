import sys
# sys.stdin = open("인프런/Chapter[3]/input.txt",'r')
from collections import deque
# m = 곳감 격자 수 
m = int(input())
gam = []
for i in range(m):
    gam.append(deque(list(map(int,input().split()))))

gam =deque(gam)
# r = 회전 
r = int(input())
for k in range(r):
    row, direction, kan = map(int,input().split())
    if direction==0: # 왼쪽
        for _ in range(kan):
            gam[row-1].append(gam[row-1].popleft())
    else:
        for _ in range(kan):
            gam[row-1].insert(0,gam[row-1].pop())


s , e = 0, m
res=0
for i in range(m):
    for j in range(s,e):
        res+=gam[i][j]
    if i<m//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)
    
