import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")
from collections import deque
# 동빈이가 탈출 해야하는 최소한의 개수
# 옆으로 넘어가는거는 1로 동일
# BFS이용 가능 
n, m = map(int,input().split())
Map = []
for i in range(n):
    Map.append(list(map(int,input())))
dx = [0,0,-1,1]
dy = [1,-1,0,0]
que = deque([(0,0)])
Map[0][0] = 0
distance = [[0]* m for _ in range(n)]
distance[0][0]=1
while que:
    x, y = que.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx >=n or ny<0 or ny>=m:
            continue
        if Map[nx][ny] == 1 :
            distance[nx][ny]=distance[x][y]+1
            que.append((nx,ny))
            Map[nx][ny]=0
print(distance[n-1][m-1])