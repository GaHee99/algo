
def DFS(x):
    if x>=8:
        return
    else:
        DFS(x*2)
        print(x)
        DFS(x*2+1)
DFS(1)