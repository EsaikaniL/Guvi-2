n=int(input())
a=[]
ans=0
for x in range(0,n):
    a.append(int(input()))
for x in range(0,n-1):
    ans=ans+max(a[x],a[x+1])
print(ans)
