num=int(input('Enter the number'))
st=[]
while (num>0):
	t=num%2
	st.append(t)
	num=num/2
st.reverse()
print st
