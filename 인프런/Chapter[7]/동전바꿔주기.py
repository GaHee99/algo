import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")

res = int(input())
coins = int(input())
money = []
count = []
result=0
for i in range(coins):
    m, c = map(int,input().split())
    money.append(m)
    count.append(c)

def DFS(L, total):
    global result
    if total > res:
        return
    if L==coins:
        if total == res:
            result+=1
    else:
        for i in range(0,count[L]+1):
            DFS(L+1, total+money[L]*i)
DFS(0,0)
print(result)

