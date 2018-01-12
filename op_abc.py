st=input("Enter 3 Numbers for a,b,c:")
ls=st.split(" ")
ans=(int(ls[0])*int(ls[1]))%int(ls[2])
print("(a*b)%c:",ans)
