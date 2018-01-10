n1=int(input("How many rows in Graph:"))
print("Enter your nodes from top to bottom")
a=[]
b=[]
for x in range(0,n1):
	t=input()
	a.append(t)
for x in a:
	t=x[::-1]
	b.append(t)
for x in b:
	print(x," ")
