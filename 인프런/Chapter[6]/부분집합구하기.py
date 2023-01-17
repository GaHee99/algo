#자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램 작성
import sys
sys.stdin = open("인프런/Chapter[6]/input.txt",'r')

def DFS(v):
    if v == n+1 : 
        for i in range(1,n+1):
            if ch[i] ==1:
                print(i,end=' ')
        print()
    else: 
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)


n = int(input())
ch=[0]*(n+1)
DFS(1)