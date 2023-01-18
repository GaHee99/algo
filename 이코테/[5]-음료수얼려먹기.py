import sys
sys.stdin = open("input.txt",'r')
n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def DFS(x,y):
    if x<=-1 or y<=-1 or x>=n or y>=m:
        return False
    if graph[x][y]==0:
        graph[x][y]=1
        DFS(x-1,y)
        DFS(x+1,y)
        DFS(x,y+1)
        DFS(y,y-1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if DFS(i,j)==True:
            result+=1
print(result)


# 입력 출력 예시

# 4 5
# 00110
# 00011
# 11111
# 00000
# 3


# 15 14 
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111
# 8 