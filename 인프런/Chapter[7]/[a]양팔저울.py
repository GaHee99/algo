import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")

n = int(input())
chu = list(map(int,input().split()))

total = sum(chu)
possible = set()

def DFS(L, Sum) :
    if L == n :
        if Sum > 0:
            possible.add(Sum)
    else:
        DFS(L+1, Sum+chu[L])
        DFS(L+1, Sum)
        DFS(L+1,Sum-chu[L])
DFS(0,0)
print(total-len(possible))