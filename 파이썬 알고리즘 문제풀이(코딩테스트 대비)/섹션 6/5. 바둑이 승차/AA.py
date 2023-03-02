import sys
# sys.stdin = open("인프런/Chapter[6]/input.txt",'r')

# C킬로그램이 안넘으면서 바둑이들을 가장 무겁게 태우고 
# 철수가 태울 수 있는 가장 무거운 무게 
c, n = map(int,input().split())
dogs=[]
for i in range(n):
    dogs.append(int(input()))

Max= 0 
def DFS(L,Sum,tot):
    global Max
    if Sum>c:
        return
    if sum(dogs)-tot+Sum<Max:
        return
    if L == n :
        if Sum<c:
            Max = max(Max, Sum)
    else:
        DFS(L+1, Sum+dogs[L],tot+dogs[L])
        DFS(L+1, Sum,tot+dogs[L])
DFS(0,0,0)
print(Max)



# c, n = map(int,input().split())
# dogs = []
# for i in range(n):
#     dogs.append(int(input()))
# Max = 0
# def DFS (L,Sum,current):
#     global Max
#     global c
#     if sum(dogs)-current+Sum < Max:
#         return
#     if Sum > c:
#         return
#     if L==n:
#         if Sum>Max:
#             Max=Sum
#     else:
#         DFS(L+1, Sum+dogs[L],Sum+dogs[L])
#         DFS(L+1, Sum,Sum+dogs[L])
# DFS(0,0,0)
# print(Max)