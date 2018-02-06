st=input("Enter the number:")
ans=''
flag=0
for x in st:
	if flag==0 and x=='1':
		ans=ans+x
		i=0
	elif flag==0 and x=='0':
		flag=1
		i=0
	elif flag==1 and x=='0':
		flag=0
		i=0
	elif flag==1 and x=='1':
		i+=1
if flag==0:
	print(ans)
else:
	ans=ans+i*'1'
	print(ans)
