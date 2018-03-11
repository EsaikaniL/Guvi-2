n=input()
st=input().strip()
a=st.split(" ")
b=[]
ans=0
for x in a:
    if x not in b:
        b.append(x)
for x in range(1,len(b)+1):
    ans+=x
print(ans)
