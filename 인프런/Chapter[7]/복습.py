import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")

n = int(input())
T = [0]
P = [0]

for i in range(n):
    time, price = map(int,input().split())
    T.append(time)
    P.append(price)
res = 0
def DFS(day, price):
    global res
    if day == n+1:
        if price>res:
            res = price
    else:
        if day+T[day]<=n+1:
            DFS(day+T[day],price+P[day])
        DFS(day+1, price)
DFS(1,0)
print(res)

