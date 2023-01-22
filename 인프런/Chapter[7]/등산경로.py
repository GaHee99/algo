import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")

n = int(input())
mountain = []
Max = 0
Min = 9999

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(n):
    li = list(map(int,input().split()))
    Min = min(min(li),Min)
    Max = max(max(li),Max)
    mountain.append(li)

Minx, Miny= 0 ,0
Maxx,Maxy=0,0

for i in range(n):
    for k in range(n):
        if mountain[i][k]==Min:
            Minx ,Miny = i,k
        if mountain[i][k]==Max:
            Maxx,Maxy = i,k
count = 0 
ch = [[0] * n for _ in range(n)]
ch[Minx][Miny] = 1
def DFS(x,y):
    global count
    if x == Maxx and y==Maxy:
        count+=1
    else:
        for i in range(4):
            nx = dx[i]+ x
            ny = dy[i]+ y
            if 0<=nx<n and 0<=ny<n and mountain[nx][ny]>mountain[x][y] and ch[nx][ny]==0:
                ch[nx][ny] = 1
                DFS(nx,ny)
                ch[nx][ny]=0
DFS(Minx, Miny)
print(count)

