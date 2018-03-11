st=input()
a=st.split("/")[0]
b=st.split("/")[1]
c=st.split("/")[2]
if len(a)!=2 or len(b)!=2 or len(c)!=4 or int(a)>31 or int(b)>12:
    print("no")
else:
    print("yes")
