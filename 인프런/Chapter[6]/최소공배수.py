def gcd(x,y):
	if y==0:
		return x
	else:
		gcd(y,x%y)
print(gcd(24,6))