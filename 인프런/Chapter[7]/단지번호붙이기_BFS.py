import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")
from collections import deque 
n = int(input())
Map = []
for i in range(n):
    Map.append(list(map(int,input())))

que = deque()

dx = [0,0,1,-1]
dy = [1,-1,0,0]
res=[]
for i in range(n):
    for k in range(n):
        if Map[i][k]==1:
            que.append((i,k))
            count=1
            Map[i][k]=0
            while que:
                x,y =que.popleft()
                for m in range(4):
                    xx = dx[m]+ x
                    yy = dy[m]+ y
                    if 0<=xx<n and 0<=yy<n and Map[xx][yy]==1:
                        count+=1
                        Map[xx][yy]=0
                        que.append((xx,yy))
            res.append(count)
print(len(res))
res.sort()
for i in res:
    print(i)
