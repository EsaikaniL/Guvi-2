st=input().strip().split(" ")
k=int(st[1])
n=int(st[0])
a=input().strip().split(" ")
ans=""
for x in range(k):
    t=a[0]
    for y in range(n-1):
        a[y]=a[y+1]
    a[n-1]=t
for x in a:
    ans+=x+" "
print(ans.strip())
       
