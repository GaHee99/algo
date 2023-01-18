import itertools as it

a=list((1,2,3,4,5))
for x in it.combinations(a,3):
    print(x)
