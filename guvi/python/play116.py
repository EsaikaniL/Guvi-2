n=int(input())
a=input().strip().split(" ")
b=[]
ans=""
for x in range(n-1):
    for y in range(x+1,n):
        if a[x]==a[y] and a[x] not in b:
            b.append(a[x])
b.sort()
for x in b[::-1]:
    ans+=str(x)+" "
for x in sorted(a)[::-1]:
    if x not in b:
         ans+=str(x)+" "
print(ans.strip())
