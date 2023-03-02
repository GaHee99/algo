import sys
# sys.stdin = open("인프런/Chapter[7]/input.txt")

def DFS(L,time, score):
    global m
    global Max 
    global n
    if time > m:
        return
    if L == n:
        Max = max(score,Max)
    else:
        DFS(L+1, time+problem[L][1],score+problem[L][0])
        DFS(L+1, time,score)


n,m = map(int,input().split())
problem = []
Max = 0 
for i in range(n):
    score, time = map(int,input().split())
    problem.append((score,time))
DFS(0,0,0)
print(Max)


# n, limit = map(int,input().split())
# problems = []
# for i in range(n):
#     score, time = map(int,input().split())
#     problems.append((score,time))
# Max= 0 
# ch=[0]*n
# def DFS (L,score, time):
#     global Max
#     if time>limit:
#         return
#     if L==n:
#         if score>Max:
#             Max = score 
#     else:
#         DFS(L+1, score+problems[L][0], time+problems[L][1])
#         DFS(L+1, score,time)

# DFS(0,0,0)
# print(Max)
