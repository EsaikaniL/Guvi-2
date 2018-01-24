n=int(input("Enter Any Number:"))
count=0
for x in range(0,n+1):
	for y in range(0,n+1):
		ans=1*x+2*y
		if ans==n:
			count=count+1
print(count)
