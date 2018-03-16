n=int(input())
a=input().strip().split(" ")
ans=0
ma=""
for x in a:
    if int(x)%2==0:
        ans+=int(x)
        ma+=str(ans)+" "
    else:
        ma+=x+" "
print(ma.strip())
