def DFS(graph, x, y, N, M):
    if 0<=x<=N-1 and 0<=y<=M-1 and graph[x][y] == 0:
        graph[x][y] = 1 
        DFS(graph, x+1, y, N, M)
        DFS(graph, x-1, y, N, M)
        DFS(graph, x, y+1, N, M)
        DFS(graph, x, y-1, N, M)
    else:
        return 

N, M = map(int,input().split())
graph = []
for i in range(N):
    graph.append(list(map(int,input())))
count = 0 
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            count+=1
            DFS(graph, i, j , N,M)
print(count)