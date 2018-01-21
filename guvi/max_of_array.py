n=int(input("Enter the N value:"))
k=int(input("Enter the N value:"))
print("Enter your first array:")
a=[]
for x in range(n):
	m=int(input())
	a.append(m)
print("Enter K array:")
for x in range(k):
	m=int(input())
	a.append(m)
	print(max(a))
