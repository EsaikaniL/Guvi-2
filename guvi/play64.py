n=int(input("How many elements??"))
print("Enter  the elements....")
a=[]
for x in range(n):
	k=int(input())
	a.append(k)
p=int(input("Enter the K value:"))
for x in a:
	if x<=p:
		print(x,end=" ")
