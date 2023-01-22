import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")
from collections import deque
dx = [0,0,1,-1,1,-1,1,-1]
dy = [1,-1,0,0,-1,1,1,-1]

n = int(input())
M = []
for i in range(n):
    M.append(list(map(int,input().split())))
count=0
que = deque()
for i in range(n):
    for k in range(n):
        if M[i][k]==1:
            que.append((i,k))
            count+=1
            while que:
                x, y = que.popleft()
                for m in range(8):
                    xx = x + dx[m]
                    yy = y + dy[m]
                    if 0<=xx<n and 0<=yy<n and M[xx][yy]==1:
                        M[xx][yy]=0
                        que.append((xx,yy))
print(count)

