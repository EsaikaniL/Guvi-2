num=int(input("How many elements?"))
print("Enter the elements:")
a=[]
b=['k','a','b','a','l','i']
for x in range(num):
	k=input()
	a.append(k)
ans=0
for x in a:
	for y in x:
		b.remove(y)
	if len(b)==0:
		ans=ans+1
	b=['k','a','b','a','l','i']
print(ans)
