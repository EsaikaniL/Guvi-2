num=int(input("Enter your number:"))
a=[]
x=2
while(num!=1):
	if num%x==0:
		num=num//x
		a.append(x)
		print(num)
		x=2
	else:
		x=x+1
ans=''
for x in a:
	ans=ans+" "+str(x)
print("The ans is:",ans)
