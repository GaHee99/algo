import sys
sys.stdin = open("인프런/Chapter[3]/input.txt",'r')

n = int(input())
for i in range(n):
    word = input().upper()
    change = word[::-1].upper()
    if word == change:
        print("#%d YES"%(i+1))
    else:
        print("#%d NO"%(i+1))