import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")

n = int(input())
t = list()
p = list()
t.append(0)
p.append(0)

Max = 0 

for i in range(n):
    time, price = map(int,input().split())
    t.append(time)
    p.append(price)

def DFS(day, price):
    global Max
    if day == n+1 :
        if price>Max :
            Max = price 
    else:
        if day+t[day]<=n+1:
            DFS(day+t[day], price+p[day])
        DFS(day+1, price)
DFS(1,0)
print(Max)