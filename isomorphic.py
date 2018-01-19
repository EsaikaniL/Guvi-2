st1=input("Enter the 1st String: ")
st2=input("Enter the 2nd String: ")
a=list(st1)
b=list(st2)
for x in range(len(a)-1):
	flag=0
	for y in range(x+1,len(a)):
		if (a[x]==a[y]):
			a[y]='*'
			flag=1
	if flag==1:
		a[x]='*'
	elif(flag==0) and a[x]!='*':
		a[x]='#'
for x in range(len(b)-1):
	flag=0
	for y in range(x+1,len(b)):
		if b[x]==b[y]:
			b[y]='*'
			flag=1
	if flag==1:
		b[x]='*'
	elif(flag==0) and b[x]!='*':
		b[x]='#'
if(a[len(a)-1]!='*'):
	a[len(a)-1]='#'
if(b[len(b)-1]!='*'):
	b[len(b)-1]='#'
ans1=''
ans2=''
for x in a:
	ans1=ans1+x
for x in b:
	ans2=ans2+x
if(ans1==ans2):
	print("The strings are isomorphic")
else:
	print("The strings are not isomorphic")
