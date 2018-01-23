n=int(input("Enter the N value:"))
a=[]
b=[]
for x in range(n):
	k=input()
	a.append(k)
for x in a:
	for y in x:
		if y!=' ':
			b.append(y)
print(min(b))
