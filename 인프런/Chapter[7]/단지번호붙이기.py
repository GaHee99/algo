import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")

n = int(input())
Map = []
for i in range(n):
    Map.append(list(map(int,input())))
res = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def DFS(x,y):
    global count
    count+=1
    Map[x][y]=0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n and Map[xx][yy]==1:
            DFS(xx, yy)

count=0
for i in range(n):
    for k in range(n):
        if Map[i][k]==1:
            count=0
            DFS(i,k)
            res.append(count)
print(len(res))
res.sort()
for i in res:
    print(i)
