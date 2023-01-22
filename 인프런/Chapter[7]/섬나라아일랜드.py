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

def DFS(x,y):
    for i in range(8):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n and M[xx][yy]==1:
            M[xx][yy]=0
            DFS(xx,yy)


for i in range(n):
    for k in range(n):
        if M[i][k]==1:
            count+=1
            DFS(i,k)
print(count)

