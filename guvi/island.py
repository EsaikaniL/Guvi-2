n=int(input("Enter N value for nXn:"))
count=0
array=[[0 for x in range(0,n)]for y in range(0,n)]
print("Enter your array")
for x in range(0,n):
	for y in range(n):
		array[x][y]=int(input())
if n==1:
    if array[0][0]==1:
        count+=1
else:
    for x in range(0,n):
        for y in range(0,n):
                if array[x][y]==1:
                    if x==0 and y==0 and array[x+1][y]==0 and array[x][y+1]==0:
                        count+=1
                    elif(x==0 and y==n-1) and array[x+1][y]==0 and array[x][y-1]==0:
                        count+=1
                    elif(x==n-1 and y==0) and array[x-1][y]==0 and array[x][y+1]==0:
                        count+=1
                    elif(x==n-1 and y==n-1) and array[x-1][y]==0 and array[x][y-1]==0:
                        count+=1
                    elif(x==0 and y!=0 and y!=n-1) and array[x+1][y]==0 and array[x][y+1]==0 and array[x][y-1]==0:
                        count+=1
                    elif(x==n-1 and y!=0 and y!=n-1) and array[x-1][y]==0 and array[x][y+1]==0 and array[x][y-1]==0:
                        count+=1
                    elif(y==0 and x!=0 and x!=n-1) and array[x+1][y]==0 and array[x-1][y]==0 and array[x][y+1]==0:
                        count+=1
                    elif(y==n-1 and x!=0 and x!=n-1) and array[x+1][y]==0 and array[x-1][y]==0 and array[x][y-1]==0:
                        count+=1
                    elif y!=n-1 and x!=n-1 and x!=0 and y!=0 and array[x][y-1]==0 and array[x][y+1]==0 and array[x+1][y]==0 and array[x-1][y]==0:
                        count+=1
print("Island",count)   
