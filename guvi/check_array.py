n=int(input("How many elements??"))
a=[]
for x in range(n):
	k=int(input())
	a.append(k)
b=sorted(a)
if a==b:
	print("Yes")
else:
	print("No")
