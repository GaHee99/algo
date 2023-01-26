import sys
from collections import deque
sys.stdin=open("인프런\Chapter[7]\input.txt", "r")

sa = []
dx = [0,-1,1]
dy = [1,0,0]
for i in range(10):
    sa.append(list(map(int,input().split())))
   
for k in range(10):
    if sa[9][k]==2:
        resultY = k
resultX = 9
count=0
def DFS(x, y):
    global count
    if y == 9 and sa[x][y]==2:
        return True
    if y == 9 and sa[x][y]==1:
        count+=1
        return False
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<=9 and 0<=ny<=9 and sa[nx][ny]==1:
            sa[nx][ny]=0
            DFS(nx,ny)
            sa[nx][ny]=1

for row in range(10):
    if sa[0][row]==1:
        if (DFS(0,row) == True):
            print(row)
print(count)


