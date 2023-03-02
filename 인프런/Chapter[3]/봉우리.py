import sys
sys.stdin = open("인프런/Chapter[3]/input.txt",'r')

n = int(input())
M = []

for i in range(n):
    M.append(list(map(int,input().split())))
    M[i].insert(0,0)
    M[i].append(0)
M.insert(0,([0]*(n+2)))
M.append([0]*(n+2))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
count=0
# 탐색 
for k in range(1,n+1):
    for j in range(1,n+1):
        point = M[k][j]
        for round in range(4):
            nx = dx[round]+k
            ny = dy[round]+j
            if point<=M[nx][ny]:
                break
        else:
            count+=1


print(count)
