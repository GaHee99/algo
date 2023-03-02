import sys
# sys.stdin = open("인프런/Chapter[7]/input.txt")
from collections import deque

# n 이하 모두 잠기기
def rain(n): 
    for i in li:
        for k in range(len(i)):
            if i[k]<=n:
                i[k]=0

dx = [0,0,1,-1]
dy = [1,-1,0,0]


n = int(input())
li = []
Max = 0
Min = 99999
que = deque()
# 리스트 입력 받고, Min, Max 찾기 
for i in range(n):
    l = list(map(int,input().split()))
    Max = max(Max, max(l))
    Min = min(Min, min(l))
    li.append(l)

cnt=0
rain(4)
def BFS():
    global cnt
    for i in range(n):
        for k in range(n):
            if li[i][k]!=0:
                que.append((i,k))
                cnt+=1
                li[i][k]=0
                while que:
                    now = que.popleft()
                    for m in range(4):
                        nx = now[0]+dx[m]
                        ny = now[1]+dy[m]
                        if 0<=nx<n and 0<=ny<n and li[nx][ny]!=0:
                            li[nx][ny]=0
                            que.append((nx,ny))
    return cnt
res = 0
for i in range(Max):
    rain(i)
    res=max(res,BFS())
print(res)    




# n = int(input())
# M = []
# S = set()
# for i in range(n):
#     List = list(map(int,input().split()))
#     M.append(List)
#     for i in List:
#         S.add(i)


# res= []
# que = deque()
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
# for i in S:
#     ch = [[0]*n for _ in range(n)]
#     count=0
#     for k in range(n):
#         for j in range(n):
#             if M[k][j]>i and ch[k][j]==0:
#                 que.append((k,j))
#                 ch[k][j]=1
#                 count+=1
#                 while que:
#                     x, y = que.popleft()
#                     for m in range(4):
#                         xx = dx[m] + x
#                         yy = dy[m] + y
#                         if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and M[xx][yy]>i:
#                             ch[xx][yy]=1
#                             que.append((xx,yy))
#     res.append(count)
# res.sort(reverse=True)
# print(res[0])                  


                

   
