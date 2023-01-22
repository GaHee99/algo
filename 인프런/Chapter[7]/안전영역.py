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

def BFS(max,Map):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    que=deque()
    count=0
    for i in range(n):
        for k in range(n):
            if Map[i][k]<=max:
                Map[i][k]=0
    for i in range(n):
        for k in range(n):
            if Map[i][k]!=0:
                count+=1
                que.append((i,k))
                Map[i][k]=0
                while(que):
                    x, y = que.popleft()
                    for m in range(4):
                        xx = dx[m]+ x 
                        yy = dy[m]+ y
                        if 0<=xx<n and 0<=yy<n and Map[xx][yy]!=0:
                            Map[xx][yy]=0
                            que.append((xx,yy))
    return count


res= []
for i in S:
    tmp = copy.deepcopy(M)
    res.append(BFS(i,tmp))
res.sort(reverse=True)
print(res[0])

   
