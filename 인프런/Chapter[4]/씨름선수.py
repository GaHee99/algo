import sys
sys.stdin=open("인프런\Chapter[4]\input.txt", "r")

n = (int(input()))
people = []
for i in range(n):
    cm, kg = map(int,input().split())
    people.append((cm,kg))

people.sort(reverse= True, key = lambda x : (x[1],x[0]))
cnt = 1
CM = people[0][0]
for i in range(1,len(people)):
    cm , kg = people[i]
    if cm>CM:
        cnt+=1
        CM=cm
print(cnt)
