import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")
from collections import deque

Matrix = []
for i in range(7):
    Matrix.append(list(map(int,input().split())))
count=0
Matrix[0][0]=1

dx = [0,0,1,-1]
dy =[1,-1,0,0]
def DFS(x,y):
    global count
    if x==6 and y==6:
        count+=1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<=6 and 0<=ny<=6 and Matrix[nx][ny]==0:
                Matrix[nx][ny]=1
                DFS(nx,ny)
                Matrix[nx][ny]=0

            
DFS(0,0)
print(count)