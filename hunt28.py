str=raw_input('Enter any string:\n')
s=[]
st=list(str)
st.sort()
for x in st:
	if x not in s:
		s.append(x)
for x in s:
	print x,
