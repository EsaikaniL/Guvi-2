m=int(input("Enter the No of Nodes: "))
n=int(input("Enter the edges: "))
print("Enter the U and V values....")
max=-1
for x in range(n):
	k=input()
	k1=int(k.split(" ")[0].strip())
	k2=int(k.split(" ")[1].strip())
	if max<k1+k2:
		max=k1+k2
print(max)
