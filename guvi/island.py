n=int(input("Enter N value for nXn:"))
count=0
array=[[0 for x in range(0,n)]for y in range(0,n)]
print("Enter your array")
for x in range(0,n):
	for y in range(n):
		array[x][y]=int(input())
for x in range(0,n):
	for y in range(1,n-1):
		if array[x][y]==1:
			if (x==0)and (array[x+1][y]==0 and array[x][y-1]==0 and array[x][y+1]):
				count=count+1
			elif (x==n-1)and (array[x-1][y]==0 and array[x][y-1]==0 and array[x][y+1]):
				count=count+1
			elif x!=0 or x!=n-1 and (array[x+1][y]==0 and array[x][y-1]==0 and array[x][y+1] and array[x-1][y]==0):
				count=count+1
print("Island",count)
