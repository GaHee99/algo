import sys
sys.stdin = open("인프런/Chapter[6]/input.txt",'r')

n,m = map(int,input().split())

def DFS(L):
    global res
    global cnt
    if L == m:
        for i in res:
            print(i, end = ' ')
        cnt +=1  
        print()
    else:
        for i in range(1,n+1):
            res[L]=i
            DFS(L+1)
res=[0]*m
cnt=0
DFS(0)
print(cnt)






# n,m = map(int,input().split())
# li = [i for i in range(1,n+1)]
# res = [0]*m
# count=0
# def DFS(L):
#     global count
#     if L == m:
#         for i in res:
#             print(i, end= ' ')
#         count+=1
#         print()
#     else:
#         for i in range(1,n+1):
#             res[L]=i
#             DFS(L+1)
# DFS(0)
# print(count)