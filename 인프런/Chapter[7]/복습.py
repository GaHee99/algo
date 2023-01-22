import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")
from collections import deque

n = int(input())
apples =[]

for i in range(n):
    apples.append(list(map(int,input().split())))
ch = [[0]*n for _ in range(n)]
middle = n//2
ch[middle][middle]=1
res=apples[middle][middle]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

que = deque([(middle,middle)])
L=0
while True:
    if L == n//2:
        break
    else:
        for _ in range(len(que)):
            x, y = que.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if ch[nx][ny]==0:
                    ch[nx][ny]=1
                    res+=apples[nx][ny]
                    que.append((nx,ny))
        L=L+1
print(res)


