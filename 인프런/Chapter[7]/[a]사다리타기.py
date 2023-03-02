import sys
from collections import deque
sys.stdin=open("인프런\Chapter[7]\input.txt", "r")


sa = []
dx = [1,0,0]
dy = [0,-1,1]

for i in range(10):
    sa.append(list(map(int,input().split())))
   
# 도착점 확인 
for i in range(10):
    if sa[9][i] == 2:
        resultY = i 

# 도착점  X, Y 
resultX = 9 

print(resultY)

def DFS(x,y):
    if x == 9 and y == resultY:
        return True
    if x== 9 : 
        print(x,y)
        return False
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<=9 and 0<=ny<=9 and sa[nx][ny]==1:
            sa[nx][ny]=0
            DFS(nx,ny)
            sa[nx][ny]=1
            DFS(nx,ny)



for i in range(9):
    if sa[0][i] == 1: 
        print(i)
        DFS(0,i)
