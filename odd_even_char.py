ip=input("Enter any String:")
even=''
odd=''
for x in range(1,len(ip)+1):
	if(x%2==0):
		even=even+ip[x-1]
	else:
		odd=odd+ip[x-1]
print(odd," ",even)
