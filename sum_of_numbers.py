n=int(input("Enter N value"))
print("Enter N number")
a=[]
sum=0
for x in range(n):
	k=input()
	a.append(k)
for x in a:
	sum=sum+int(x)
print(sum)
