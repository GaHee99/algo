import sys
sys.stdin = open("이코테/input.txt")
from collections import deque 
n, m = map(int,input().split())
Mi = []
for i in range(n):
    Mi.append(list(map(int,input())))

que = deque()
que.append((0,0))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

while que:
    x,y = que.popleft()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        elif Mi[nx][ny]==0:
            continue
        elif Mi[nx][ny]==1:
            Mi[nx][ny]=Mi[x][y]+1 
            que.append((nx,ny))
        

print(Mi[n-1][m-1])