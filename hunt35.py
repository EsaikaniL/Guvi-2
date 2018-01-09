st1=input("Enter your string")
st2=st1.lower()
length=len(st2)
n=length//2
t=''
for x in range(0,n):
	t=t+st2[x]
t1=t
t=''
for x in range(n,length):
	t=t+st2[x]
t2=t
if t1==t2:
	print("Yes")
else:
	print("No")
