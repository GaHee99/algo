import sys
sys.stdin = open("input.txt",'r')
n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def DFS(x,y):
    if x<=-1 or y<=-1 or x>=n or y>=m:
        return False
    if graph[x][y]==0:
        graph[x][y]=1
        DFS(x-1,y)
        DFS(x+1,y)
        DFS(x,y+1)
        DFS(y,y-1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if DFS(i,j)==True:
            result+=1
print(result)