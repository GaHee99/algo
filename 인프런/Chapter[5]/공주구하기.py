import sys
sys.stdin = open("인프런/Chapter[5]/input.txt",'r')
from collections import deque
n , m = map(int,input().split())
li =[i for i in range(1,n+1)]
que = deque(li)

while len(que)>1:
    for i in range(m-1):
        p = que.popleft()
        que.append(p)
    que.popleft()
print(que[0])