n=int(input())
a=[int(x) for x in input().split(" ")]
b=[int(x) for x in input().split(" ")]
for x in range(n):
	for y in range(x+1,n):
		if b[x]>b[y]:
			t=b[x]
			b[x]=b[y]
			b[y]=t
			t=a[x]
			a[x]=a[y]
			a[y]=t
for x in a:
	print(x,end=" ")
