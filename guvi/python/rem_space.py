st=list(input().strip())
ans=""
for x in range(len(st)-1):
    if st[x]==" " and st[x+1]==" ":
        st[x]=""
for x in st:
    ans+=x
print(ans)
