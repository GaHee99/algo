import sys
sys.stdin = open("인프런/Chapter[6]/input.txt",'r')

c, n = map(int,input().split())
dogs = []
for i in range(n):
    dogs.append(int(input()))
Max = 0
def DFS (L,Sum,current):
    global Max
    global c
    if sum(dogs)-current+Sum < Max:
        return
    if Sum > c:
        return
    if L==n:
        if Sum>Max:
            Max=Sum
    else:
        DFS(L+1, Sum+dogs[L],Sum+dogs[L])
        DFS(L+1, Sum,Sum+dogs[L])
DFS(0,0,0)
print(Max)