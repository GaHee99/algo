
import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")

n = int(input())
money = []
for i in range(n):
    money.append(int(input()))
Max = 0 
Min = 999999
res= 9999
def DFS(L, A, B, C):
    global res 
    if L == n :
        if A == B or  B == C or A==C:
            return 
        Max = max(A,B,C)
        Min = min(A,B,C)
        res = min (res, Max-Min)
    else:
        DFS(L+1, A+money[L], B, C)
        DFS(L+1, A, B+money[L],C)
        DFS(L+1, A, B,C+money[L])
DFS(0,0,0,0)
print(res)
