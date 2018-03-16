n=int(input())
a=input().strip().split(" ")
ans=0
for x in a:
    if int(x)<0:
        ans+=int(x)
print(ans)
