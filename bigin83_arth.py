ip=input("Enter your seqence (Mod/Dividee):")
op=['%','/']
for x in ip:
	if x in op:
		if(x=='%'):
			k1=int(ip.split(x)[0])
			k2=int(ip.split(x)[1])
			ans=k1%k2
		elif(x=='/'):
			k1=int(ip.split(x)[0])
			k2=int(ip.split(x)[1])
			ans=k1//k2
print(ans)
