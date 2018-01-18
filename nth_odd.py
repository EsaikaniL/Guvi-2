ip=input("Enter your K1 and K2 value in single line with space:")
k1=int(ip.split(" ")[0].strip())
k2=int(ip.split(" ")[1].strip())
print("Enter your array:")
st=[]
b=[]
for x in range(k1):
	a=int(input())
	st.append(a)
for x in st:
	if x%2!=0:
		b.append(x)
print("Ans is:",b[k2-1])
