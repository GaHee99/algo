import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")
from collections import deque

# DFS
# 인접 행렬 그래프
node, edge = map(int,input().split())
Matrix = [[0]*(node) for _ in range(node)]

for i in range(edge):
    start, end = map(int,input().split())
    Matrix[start-1][end-1] = 1

count = 0 
ch=[0]*node
ch[0]=1
def DFS(L):
    global count
    if L == node-1:
        count+=1
    else:
        for i in range(0, node):
            if Matrix[L][i]==1 and ch[i]==0:
                ch[i]=1
                DFS(i)
                ch[i]=0
DFS(0)
print(count)

