t2=raw_input('Enter the final time:(ex:4:22)\n')
t1=raw_input('Enter the final time:(ex:4:22)\n')
a=t2.split(":")[0]
b=t2.split(":")[1]
c=t1.split(":")[0]
d=t1.split(":")[1]
e=int(a)-int(c)
f=int(b)-int(d)
if(f<0):
	print 'The difference is:',e,":",-f
else:
	print 'The difference is:',e,":",f
