import sys
sys.stdin = open("인프런/Chapter[3]/input.txt",'r')

n = int(input())
li = []
Max = 0
#행, 열 받고 행 최댓값  
for i in range(n):
    inputlist=list(map(int,input().split()))
    li.append(inputlist)
    if Max < sum(inputlist):
        Max = sum(inputlist)

#열 최댓값 
오른쪽대각선 = 0 
왼쪽대각선=0
for i in range(n):
    column =0 
    for k in range(n):
        if i == k :
            오른쪽대각선 +=li[i][k]
        if i+k==5:
            왼쪽대각선 +=li[i][k]
        column+=li[k][i]
    Max = max(Max, column, 오른쪽대각선, 왼쪽대각선)
print(Max)
