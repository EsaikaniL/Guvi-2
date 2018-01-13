n=int(input("Enter N value:"))
k=int(input("Enter K value:"))
print("Enter the Array:")
a=[]
count=0
for x in range(n):
	k1=int(input())
	a.append(k1)
for x in a:
	if x==k:
		count=count+1
print(count)
