import sys
sys.stdin = open("인프런/Chapter[3]/input.txt",'r')

word = input()
res=0
for i in word:
    if i.isdecimal():
        res=res*10+int(i)
print(res)
count=1
for i in range(2,res+1):
    if res%i==0:
        count+=1
print(count)