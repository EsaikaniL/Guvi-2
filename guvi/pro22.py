n=int(input("Enter a count value:"))
a=[]
sum1=0
sum2=0
for x in range(n):
	k=int(input())
	a.append(k)
for x in range(0,n,2):
	sum1=sum1+a[x]
for x in range(1,n,2):
	sum2=sum2+a[x]
print(max(sum1,sum2))
