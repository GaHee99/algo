import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")


code = int(input())
lenth = len(code)
def DFS(L):
    if L == lenth:
        cnt+=1
        for i in 






# code = list(map(int,input()))
# n = len(code)
# code.insert(n,-1)
# res = [0]*(n+3)
# count = 0
# def DFS(L, P):
#     global count
#     if L == n :
#         count+=1
#         for i in range(P):
#             print(chr(res[i]+64),end='')
#         print()
#     else:
#         for i in range(1,27):
#             if code[L]==i:
#                 res[P]=i
#                 DFS(L+1,P+1)
#             elif i >= 10 and code[L] == i //10 and code[L+1] == i%10:
#                 res[P]=i
#                 DFS(L+2,P+1)
        
# DFS(0,0)
# print(count)