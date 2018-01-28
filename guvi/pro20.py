n=int(input("How many elements??"))
a=[]
print("Enter the value of coins:")
for x in range(n):
	k=int(input())
	a.append(k)
s=int(input("Enter the sum value:"))
b=sorted(a,reverse=True)
b2=[]
for x in range(len(b)-1):
	for y in range(x+1,len(b)):
		sum=b[x]+b[y]
		b2.append(sum)
res=0
flag=0
for x in b:
	if s in b:
		res+=1
		flag=1
		s=0
		break
	elif s in b2:
		res+=2
		flag=1
		s=0
		break
	else:
		while(x<=s):
			res+=1
			s=s-x
			flag=1
if s==0 and flag==1:
    print(res)
else:
    print("It is impossible")
