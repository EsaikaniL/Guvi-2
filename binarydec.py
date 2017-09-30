num=int(input('Enter the number \n'))
st=[]
s=[]
s2=''
while (num>0):
	t=num%2
	st.append(str(t))
	num=num/2
st.reverse()
print 'Binary equlant is:\n',s2.join(st)
