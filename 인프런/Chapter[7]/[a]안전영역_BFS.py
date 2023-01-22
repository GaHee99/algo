import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")
from collections import deque
import copy
n = int(input())
M = []
S = set()
for i in range(n):
    List = list(map(int,input().split()))
    M.append(List)
    for i in List:
        S.add(i)


res= []
que = deque()
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in S:
    ch = [[0]*n for _ in range(n)]
    count=0
    for k in range(n):
        for j in range(n):
            if M[k][j]>i and ch[k][j]==0:
                que.append((k,j))
                ch[k][j]=1
                count+=1
                while que:
                    x, y = que.popleft()
                    for m in range(4):
                        xx = dx[m] + x
                        yy = dy[m] + y
                        if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and M[xx][yy]>i:
                            ch[xx][yy]=1
                            que.append((xx,yy))
    res.append(count)
res.sort(reverse=True)
print(res[0])                  


                

   
