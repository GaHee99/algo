import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")
from collections import deque
# 앞 : 1
# 뒤 : -1
# 앞 : 5 
# 최소 몇 번의 점프로 현수가 송아지의 위치까지 갈 수 있는지 
# 현수의 위치 : 5, 송아지의 위치 : 14
h , s = map(int,input().split())
go = [-1,1,5]
que = deque([h])
distance = [-1]*(10000+1)
distance[h]=0
while que:
    now = que.popleft()
    if now==s:
        break
    for next in(now-1,now+1,now+5):
        if distance[next]==-1 and 0<next<=10000:
            distance[next]=distance[now]+1
            que.append(next)

print(distance[s])

