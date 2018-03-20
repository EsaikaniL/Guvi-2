n=int(input())
st=input().strip().split(" ")
a=[]
for x in range(n):
    a.append(int(st[x]))
k=(n//2)
for x in range(k):
    for y in range(x+1,k):
        if a[x]>a[y]:
            t=a[x]
            a[x]=a[y]
            a[y]=t
for x in range(k,n):
    for y in range(x+1,n):
        if a[x]<a[y]:
            t=a[x]
            a[x]=a[y]
            a[y]=t
ans=""
for x in a:
    ans+=str(x)+" "
print(ans.strip())
