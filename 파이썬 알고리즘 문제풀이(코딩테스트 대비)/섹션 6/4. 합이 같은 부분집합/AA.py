import sys
# sys.stdin = open("인프런/Chapter[6]/input.txt",'r')

n = int(input())
li = list(map(int,input().split()))
res=[]
flag=False
def DFS(L):
    global res
    if L == n:
        if sum(res)==sum(li)-sum(res):
            print("YES")
            flag=True
            sys.exit(0)
        else:
            flag = False
    else:
        res.append(li[L])
        DFS(L+1)
        res.pop()
        DFS(L+1)

DFS(0)
if flag==False:
    print("NO")





# 이전풀이
# n = int(input())
# numbers = list(map(int,input().split()))
# total = sum(numbers)
# def DFS(L,Sum):
#     if Sum > total - Sum:
#         return
#     if L==n:
#         if Sum == total - Sum:
#             print("YES")
#             sys.exit(0)
#     else:
#         DFS(L+1, Sum+numbers[L])
#         DFS(L+1, Sum)

         
# DFS(0,0)
# print("NO")