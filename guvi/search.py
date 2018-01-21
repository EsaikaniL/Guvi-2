n=int(input("Enter N value:"))
k=int(input("Enter K value:"))
print("Enter your array:")
a=[]
for x in range(n):
	m=int(input())
	a.append(m)
if k in a:
	print("Yes")
else:
	print("No")
