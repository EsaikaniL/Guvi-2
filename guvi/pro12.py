n=int(input("Enter N value:"))
a=[]
b=[]
print("Enter Elements followed by N\n")
for x in range(n):
	k=int(input())
	a.append(k)
q=int(input("Enter the Q value:"))
print("Enter Q elementsthe U and V value:")
for x in range(q):
	k=input()
	b.append(k)
for x in b:
	k1=x.split(" ")[0].strip()
	k2=x.split(" ")[1].strip()
	ans=0
	for y in range(int(k1),int(k2)+1):
		ans=ans+int(a[y])
	print(ans)
