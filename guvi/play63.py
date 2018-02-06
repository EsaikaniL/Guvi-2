n=int(input("How many elements in array1??"))
print("Enter  the elements....")
a=[]
for x in range(n):
	k=int(input())
	a.append(k)
n=int(input("How many elements in array1??"))
print("Enter  the elements....")
b=[]
for x in range(n):
	k=int(input())
	b.append(k)
a.sort()
b.sort()
for x in range(min(len(a),len(b))):
	if a[x]==b[x]:
		print(a[x],end=" ")
