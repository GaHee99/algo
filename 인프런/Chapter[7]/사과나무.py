import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")
from collections import deque
n = int(input())
Map = []
for i in range(n):
    Map.append(list(map(int,input().split())))

ch = [[0]* n for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
middle = n//2
que = deque([(middle,middle)])
res=Map[middle][middle]
ch[middle][middle]=1
count=0
while que:
    x, y = que.popleft() 
    for i in range(4):
        nx = dx[i]+ x
        ny = dy[i]+ y
        if 0<=nx<n and 0<=ny<n :
            if ch[nx][ny]== 0:
                ch[nx][ny]=1
                res= res+Map[nx][ny]
                que.append((nx,ny))
        else:
            print(res)
            sys.exit(0)
 
            



