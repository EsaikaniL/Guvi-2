st=input("Enter the line")
a=st.split(" ")
st2=input("Enter the string:")
i=0
for x in a:
	if x==st2:
		i+=1
print(i)
