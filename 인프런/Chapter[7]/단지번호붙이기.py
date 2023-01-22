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
    global S
    if x<0 or y < 0 or x>=n or y>=n:
        return 
    else:
        if Map[x][y]==1:
            Map[x][y]=0
            S.add((x,y))
            for i in range(4):
                DFS(dx[i]+x, dy[i]+y)
                


for i in range(n):
    for k in range(n):
        if Map[i][k]==1:
            S = set()
            DFS(i,k)
            S.add((i,k))
            res.append(len(S))
print(len(res))
for i in res:
    print(i)
