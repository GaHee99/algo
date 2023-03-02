#자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램 작성
import sys
# sys.stdin = open("인프런/Chapter[6]/input.txt",'r')

n = int(input())
res=[]
def DFS(L):
    global res
    if L == n+1 :
        for i in res:
            print(i, end = ' ')
        print()
    else:
        res.append(L)
        DFS(L+1)
        res.pop()
        DFS(L+1)
DFS(1)