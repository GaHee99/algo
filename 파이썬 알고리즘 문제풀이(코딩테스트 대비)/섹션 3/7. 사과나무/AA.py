import sys
# sys.stdin = open("인프런/Chapter[3]/input.txt",'r')

n = int(input())
apples= []
for i in range(n):
    apples.append(list(map(int,input().split())))

res=0
for i in range(0,n//2):
    res += sum(apples[i][n//2-i:n//2+i+1])
    # print(apples[i][n//2-i:n//2+i+1])

res+=sum(apples[n//2])
for i in range(n//2-1,-1,-1):
    res += sum(apples[n-1-i][n//2-i:n//2+i+1])
    # print(apples[n-1-i][n//2-i:n//2+i+1])
print(res)