import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")
from collections import deque

Matrix = []
for i in range(7):
    Matrix.append(list(map(int,input().split())))
dx = [0,0,1,-1]
dy = [1,-1,0,0]

dis = [[0]*7 for _ in range(7)]
Matrix[0][0]=1

que = deque([0,0])
while que:
    x, y = que.popleft()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx<0 or ny<0 or ny>7 or nx>7 or Matrix[nx][ny]==1:
            continue
        Matrix[nx][ny]=1
        que.append((nx,ny))
        dis[nx][ny]=dis[x][y]+1
if dis[6][6]==0:
    print(-1)
else:
    print()