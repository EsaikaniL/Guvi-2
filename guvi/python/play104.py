n=int(input())
a=[]
ans=0
for x in range(n):
    a.append(int(input()))
for x in range(n-1):
    ans=ans+a[x]+a[x+1]
print(ans)
