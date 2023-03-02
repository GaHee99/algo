import sys
sys.stdin = open("인프런/Chapter[5]/input.txt",'r')

sik = list(map(str,input()))

stack = []
res=0
for i in sik :
    if  i.isdecimal():
        stack.append(int(i))
    else:
        first = stack.pop()
        second = stack.pop()
        if i == "+" :
            res = first+second
        elif i == "-":
            res = second-first
        elif i == "*":
            res = first*second
        elif i == "/":
            res = second//first
        stack.append(res)
print(res)

