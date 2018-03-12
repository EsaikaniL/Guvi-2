n=int(input())
a=input().strip().split(" ")
ans=0
for x in range(5):
    if int(a[x])*x==int(a[x]):
        ans=int(a[x])
print(ans)
