
def binary_search(key,array):
    first = 0
    last = len(array)-1

    while (first<=last) :
        mid = (last+first)//2
        if array[mid] == key:
            return True
        elif array[mid] > key:
            last = mid-1
        else :
            first = mid+1
    


N = int(input())
my = list(map(int, input().split()))

M = int(input())
customer = list(map(int, input().split()))

my.sort()
for i in customer:
    if(binary_search(i, my)):
        print("yes", end= ' ')
    else:
        print("no", end= ' ')
    
