n=int(input("How many elements??"))
a=[]
print("Enter the value of coins:")
for x in range(n):
	k=int(input())
	a.append(k)
s=int(input("Enter the sum value:"))
b=sorted(a,reverse=True)
res=0
print(b)
for x in b:
	while(x<=s):
		res+=1
		s=s-x
print(res)
