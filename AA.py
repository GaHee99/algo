import sys

from collections import deque
m,n = map(int,input().split())
tomatoes = []
for i in range(n):
    tomatoes.append(list(map(int,input().split())))
ripen= deque([])
flag=True
for i in range(n):
    for k in range(m):
        if tomatoes[i][k] == 1:
            ripen.append((i,k))
        if tomatoes[i][k] == -1:
            flag = False
dx = [0,0,1,-1]
dy = [1,-1,0,0]

L=0
if flag == True and len(ripen)==0:
    print(0)
    sys.exit(0)

while ripen:
    l = len(ripen)
    for _ in range(l):
        x, y = ripen.popleft()
        for a in range(4):
            nx = dx[a] + x 
            ny = dy[a] + y
            if 0<=nx<n and 0<=ny<m:
                if tomatoes[nx][ny] == 0:
                    tomatoes[nx][ny]=1
                    ripen.append((nx,ny))
    L=L+1
for b in tomatoes:
    if 0 in b:
        print(-1)
        sys.exit(0)
print(L-1)


