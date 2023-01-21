import sys
sys.stdin = open("인프런/실전문제/DFS,BFS/input.txt")
from collections import deque
n,m,k,x = map(int,input().split())

# 그래프의 연결 정보 넣기
graph = [[] for _ in range(n+1)]

# [[], [2, 3], [3, 4], [], []]
for i in range(m):
    start, end = map(int,input().split())
    graph[start].append(end)

# 최소 거리에 대한 리스트 
# 처음 시작점은 x로 초기화 
distance = [-1]*(n+1)
distance[x] = 0

# 맨 처음 시작 점을 넣어서 시작
que = deque([x])
while que:
    now = que.popleft()
    for next_node in graph[now]:
        if distance[next_node]==-1: # 처음 방문한 노드라면!
            distance[next_node] = distance[now]+1
        que.append(next_node)

flag = False
for index, dis in enumerate (distance) :
    if dis == k :
        print(index)
        flag = True

if flag == False :
    print(-1)


