r=int(input("Enter the rows:"))
c=int(input("Enter the coulmns:"))
a=[[0 for y in range(c)]for x in range(r)]
print("Enter the values:")
for x in range(r):
	for y in range(c):
		k=int(input())
		a[x][y]=k
for x in range(r):
	for y in range(c-1):
		for z in range(y+1,c):
			if a[x][y]>a[x][z]:
				t=a[x][y]
				a[x][y]=a[x][z]
				a[x][z]=t

for x in range(c):
	for y in range(r-1):
		for z in range(y+1,r):
			if a[y][x]>a[z][x]:
				t=a[y][x]
				a[y][x]=a[z][x]
				a[z][x]=t
for x in range(r):
        for y in range(c):
            print(a[x][y],end=" ")
        print()
