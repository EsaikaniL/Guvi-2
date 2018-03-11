ip=input().strip()
n=int(ip.split(" ")[0])
m=int(ip.split(" ")[1])
st=input()
a=st.split(" ")
ans=""
b=[]
c=[]
d=[]
for x in range(n):
    b.append(a[x])
for x in range(n,n+m):
    c.append(a[x])
for x in b:
    for y in c:
        if x==y:
            if x not in d:
                d.append(x)
for x in d:
    ans+=str(x)+" "
print(ans.strip())
