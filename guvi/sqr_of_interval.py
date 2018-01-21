l=int(input("Enter Intial number:"))
r=int(input("Enter final value:"))
for x in range(l+1,r):
	for y in range(1,r):
		temp=y*y
		if temp==x:
			print(x)
