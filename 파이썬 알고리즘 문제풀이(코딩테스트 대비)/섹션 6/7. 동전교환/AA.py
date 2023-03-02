#거스름돈을 가장 적은 수의 동전으로 교환 해주려면 어떻게 주면 되는가? 
import sys
# sys.stdin = open("인프런/Chapter[6]/input.txt",'r')

n = int(input())
coins = list(map(int,input().split()))
coins.sort(reverse=True)
res = int(input())
Min = 9999999
def DFS(Sum,count):
    global Min
    if count>Min:
        return
    if Sum>res:
        return
    if Sum==res:
        Min = min(Min,count)

    else:
        for i in range(n):
            DFS(Sum+coins[i],count+1)
DFS(0,0)
print(Min)





# coinCount = int(input())
# coins = list(map(int,input().split()))
# change = int(input())
# Min =999999
# def DFS(Sum, count):
#     global Min
#     if count >= Min:
#         return
#     if Sum > change:
#         return
#     if Sum == change:
#         if count < Min :
#             Min = count
#     else:
#         for i in coins:
#             DFS(Sum+i, count+1)
# DFS(0,0)
# print(Min)