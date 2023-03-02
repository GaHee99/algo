import sys
# sys.stdin = open("인프런/Chapter[4]/input.txt",'r')
n, m = map(int,input().split())
li = list(map(int,input().split()))
li.sort()
start = 0 
end = n-1
while True:
    find = (start+end)//2
    if li[find]==m:
        print(find+1)
        break
    else:
        if (li[find]>m):
            end=find-1
        else:
            start=find+1