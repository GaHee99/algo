import sys
# sys.stdin=open("인프런\Chapter[4]\input.txt", "r")

L = int(input())
boxes = list(map(int,input().split()))
M = int(input())
boxes.sort()
while M>0:
    boxes[-1]-=1
    boxes[0]+=1
    boxes.sort()
    M-=1
print(boxes[-1]-boxes[0])