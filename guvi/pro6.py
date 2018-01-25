n=int(input("How many elemets??"))
a=[]
count=0
for x in range(n):
	k=int(input())
	a.append(k)
for x in range(n):
	for y in range(x,n):
		for z in range(y,n):
			if a[x]+a[y]+a[z]==n:
				count+=1
print(count)
