떡의개수, 떡의길이 = map(int, input().split())
dduck = list(map(int,input().split()))


def count(height, dduck):
    result = 0 
    for i in dduck:
        if (i-height) >0 :
            result+=(i-height)
    return result


start = 0
max_height=0
last = max(dduck)
while start<=last:
    mid = (start+last)//2
    tmp = count(mid, dduck)
    if tmp >= 떡의길이:
        max_height = max(mid, max_height)
        start = mid+1
    else:
        last = mid-1
print(max_height)
        
    