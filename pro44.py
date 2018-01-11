n=int(input("Enter N value:"))
p=int(input("Enter P value:"))
q=int(input("Enter Q value:"))
r=int(input("Enter R value:"))
max=0
print("Enter your Array")
a=[]
for x in range(n):
	a.append(int(input()))
for i in range(n):
	for j in range(n):
		for k in range(n):
			ans=(p*a[i])+(q*a[j])+(r*a[k])
			if ans>max:
				max=ans
print(max)
