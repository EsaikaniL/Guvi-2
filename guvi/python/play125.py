n=int(input())
a=input().strip().split(" ")
for x in range(n):
    f=0
    for y in range(n):
        if int(a[y])%int(a[x])!=0:
            f=1 
            break
    if f==0:
        k=int(a[x])
print(k)
