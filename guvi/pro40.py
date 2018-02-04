st=input("Enter the string: ")
temp=ord('d')+ord('h')+ord('o')+ord('n')+ord('i')
ans=0
for x in st:
	ans+=ord(x)
if temp==ans:
	print("Yes")
else:
	print("No")
