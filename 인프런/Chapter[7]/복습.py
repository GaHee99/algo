import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")

code = list(map(int,input()))
n = len(code)
res = [0]*(n+3)
code.insert(n,-1)
count=0
def DFS(L, P):
    global count
    if L == n:
        for i in range(P):
            print(chr(res[i]+64),end='')
        print()
        count+=1
     
    else:
        for k in range(1,27):
            if k == code[L]: # 한자리 수 일 경우 
                res[P]=k
                DFS(L+1,P+1)
            elif k//10 == code[L] and k%10 == code[L+1]: # 두자리 수 일 경우
                res[P] = k
                DFS(L+2, P+1)


DFS(0,0)
print(count)

