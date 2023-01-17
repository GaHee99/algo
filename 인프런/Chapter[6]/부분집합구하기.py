#자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램 작성
import sys
sys.stdin = open("인프런/Chapter[6]/input.txt",'r')
n = int(input())
N = [i for i in range(1, n+1)]

def DFS(L):
    if L > n :
        for k in res:
            print(k, end=' ')
        print()
    else:
        res.append(L)
        DFS(L+1)
        res.pop()
        DFS(L+1)
res=[]
DFS(1)