import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")

n = int(input())
payment = []
for i in range(n):
    day , money = map(int,input().split())
    payment.append((day, money))
res= 0 
def DFS (L , sum):
    global res 
    if L==n+1 :
        if sum> res:
            res=sum
    else:
        if L+ payment[L][0]<=n+1:
            DFS(L+payment[L][0], sum+payment[L][1])
        DFS(L+1, sum) #1씩 증가하다 보면 L+1로 가니까.. 


DFS(0,0)
print(res)