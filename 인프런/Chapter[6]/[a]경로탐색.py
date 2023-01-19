import sys
sys.stdin = open("인프런/Chapter[6]/input.txt",'r')
# 경로탐색...
# 인접해 있을 경우
# 똑같이 DFS로 탐색을 하되, 갈 수 있는 경로는 인접 그래프를 통해서 파악한다..
# DFS는 모든 그래프를 끝까지 탐색 할 수 있다는 것을 기억하자..
# BFS는 최단거리를 기준으로 갈 수 있다! 
def DFS(v):
    global cnt, path
    if v==n:
        cnt+=1
        for x in path:
            print(x, end=' ')
        print()
    else:
        for i in range(1, n+1):
            if g[v][i]==1 and ch[i]==0:
                ch[i]=1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i]=0
           
if __name__=="__main__":
    n, m=map(int, input().split())
    g=[[0]*(n+1) for _ in range(n+1)]
    ch=[0]*(n+1)
    for i in range(m):
        a, b=map(int, input().split())
        g[a][b]=1
    cnt=0
    ch[1]=1
    path=list()
    path.append(1)
    DFS(1)
