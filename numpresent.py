n=int(input("Enter N value:"))
l=int(input("Enter L value:"))
r=int(input("Enter R value:"))
flag=0
for x in range(l,r+1):
	if x==n:
		flag=1
if(flag==1):
	print("N is present")
else:
	print("N is not presented")
