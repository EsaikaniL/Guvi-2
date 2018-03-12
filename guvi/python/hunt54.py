n=int(input())
a=input().strip().split(" ")
ans=""
mi=1000000
for x in a:
    if int(x)<mi:
        mi=int(x)
        ans+=x+" "
    else:
        ans+=str(mi)+" "
print(ans.strip())
