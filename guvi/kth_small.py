n=int(input("How many elements??"))
print("Enter th elements....")
a=[]
for x in range(n):
	k=int(input())
	a.append(k)
a.sort()
print(a)
p=int(input("Enter the k value:"))
print(p,"st smallest number is:",a[p-1])
