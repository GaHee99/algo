
import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")

code = list(map(int,input()))
n = len(code) # n이 종착점 
code.insert(n,-1) # 마지막을 알림 , out of index 처리 
res = [0]*(n+3) 
cnt = 0 

def DFS(L, P): 
    global cnt
    if L == n :
        cnt+=1 
        for j in range(P):
            print(chr(res[j]+64),end='')
        print()
    else:
        for i in range(1,27):
            if code[L] == i :
                res[P]=i
                DFS(L+1, P+1)
            elif i >= 10 and code[L]== i//10 and code[L+1] == i%10:
                res[P]=i
                DFS(L+2, P+1) # P는 값을 집어 넣는 index이므로 ,, ,
            

DFS(0,0)
print(cnt)