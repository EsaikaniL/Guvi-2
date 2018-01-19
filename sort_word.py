num=int(input("How many elements you will enter??"))
print("Enter the elements:")
a=[]
b=[]
for x in range(num):
	k=input()
	a.append(k)
for x in a:
	t=0
	for y in x:
		t=t+ord(y)
	b.append(t)
for x in range(len(b)-1):
	for y in range(x+1,len(b)):
		if b[x]>b[y]:
			tmp=a[x]
			a[x]=a[y]
			a[y]=tmp
for x in a:
	print(x)
