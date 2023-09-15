N = int(input())
step_list = list(map(str, input().split()))

x, y = 1,1
go = {'R':[1,0], 'L':[-1,0], 'U':[0,-1], 'D':[0,1]}

for i in step_list:
    if i in go:
        nx = x + go.get(i)[0]
        ny = y + go.get(i)[1]
    
    if 1<=nx<=N and 1<=ny<=N:
        x, y = nx, ny

print(y,x)
