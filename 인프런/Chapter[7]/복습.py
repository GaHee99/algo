import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")
from collections import deque

# n : 노드, m: 간선 수, k = 거리, x : 시작 
n,m,k,x = map(int,input().split())

# 연결 돼있는 간선 받기 위한 그래프
graph = [[] for _ in range(n+1)]

# 거리를 위한 그래프 
distance = [0]*(n+1)

for _ in range(m):
    start_node, end_node  = map(int,input().split())
    graph[start_node].append(end_node)

# 처음 시작 노드 넣고 
que = deque([x])
while que:
    current = que.popleft()
    for next_node in graph[current]:
        if distance[next_node]==0:
            distance[next_node] = distance[current]+1
            que.append(next_node)
flg = False
for index, dis in enumerate(distance):
    if dis == k:
        print(index)
        flg = True
if flg==False:
    print(-1)
