import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")

def DFS(day, pay):
    global Max
    if day>n:
        return
    else:
        if day == n:
            Max = max(Max, pay)
        else:
            DFS(day+counselor[day][0],pay+counselor[day][1])
            DFS(day+1, pay)


n = int(input())
counselor = [] 
Max = 0
for i in range(n):
    T, P  = map(int,input().split())
    counselor.append((T,P))
DFS(0,0)
print(Max)





# n = int(input())
# payment = []
# for i in range(n):
#     day , money = map(int,input().split())
#     payment.append((day, money))
# res= 0 
# def DFS (L , sum):
#     global res 
#     if L==n+1 :
#         if sum> res:
#             res=sum
#     else:
#         if L+ payment[L][0]<=n+1:
#             DFS(L+payment[L][0], sum+payment[L][1])
#         DFS(L+1, sum) #1씩 증가하다 보면 L+1로 가니까.. 


# DFS(0,0)
# print(res)