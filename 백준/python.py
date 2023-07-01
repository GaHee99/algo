import sys
from collections import deque
sys.stdin = open("input.txt",'r')
N, M, V = map(int,input().split())

def DFS(v):
    global Map
    global N
    global res
    for i in range(N):
        if Map[v-1][i]==1 and ch[i]==0:
            Map[v-1][i]=0
            Map[i][v-1]=0
            ch[i]=1
            res.append(i+1)
            DFS(i+1)
que = deque()
res = []
List = [ [0]*N for _ in range(N)]
Map=[ [0]*N for _ in range(N)]
ch=[0]*N

res.append(V)
ch[V-1]=1
for i in range(M):
    x , y = map(int,input().split())
    List[x-1][y-1]=1
    List[y-1][x-1]=1
    Map[x-1][y-1]=1
    Map[y-1][x-1]=1
DFS(V)

for i in res:
    print(i,end= ' ')
print()


res=[]
res.append(V)
ch=[0]*N
ch[V-1]=1

for i in range(N):
    if List[V-1][i]==1 :
        que.append(i+1)
        List[V-1][i]=0
        List[i][V-1]=0
        ch[i]=1
        res.append(i+1)

while que:
    v = que.popleft()
    for i in range(N):
        if List[v-1][i]==1 and ch[i]==0:
            que.append(i)
            List[v-1][i]=0
            List[i][v-1]=0
            res.append(i+1)
for i in range(len(res)):
    print(res[i],end=' ')


