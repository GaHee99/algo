# import sys
# sys.stdin = open("인프런/Chapter[5]/input.txt",'r')

fe = list(map(str,input()))
stack = [] 
last = ""
res=0
for i in fe:
    if i == "(":
        stack.append(i)
        last = "("
    elif i == ")" and last=="(":
        stack.pop()
        res+=len(stack)
        last = ")"
    elif i == ")" and last==")":
        stack.pop()
        res+=1
print(res)