child=int(input("How many child??"))
rating=[]
points=[1]*child
print("Enter the ratings of Students")
for x in range(child):
	k=int(input())
	rating.append(k)

for x in range(len(rating)):
	if x==0:
		if rating[x]>rating[x+1]:
			points[x]=points[x+1]+1
			print(points)
	elif(x!=0)and(x!=len(rating)-1):
		if rating[x]>rating[x-1]:
			points[x]=points[x-1]+1
		elif rating[x]>rating[x+1]:
			points[x]=points[x+1]+1
	else:
		if rating[x]>rating[x-1]:
			points[x]=points[x-1]+1
ans=0
for x in points:
	ans=ans+x
print(ans)
