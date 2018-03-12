n=int(input())
a=input().strip().split(" ")
ans=''
for x in range(len(a)):
    if int(a[x])*x==int(a[x]):
        ans=a[x]
print(ans)
