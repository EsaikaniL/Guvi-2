def fun(x):
    l=len(x)
    ans=0
    for y in range(len(x)):
        c=0
        l-=1
        ft=1
        for z in range(y+1,len(x)):
            if ord(x[y])>ord(x[z]):
                c+=1
        for f in range(1,l+1):
            ft*=f
        ans+=ft*c
    return ans+1
        
n=int(input())
a=[]
ma=1000000
for x in range(n):
    a.append(input())
for x in a:
    m=fun(x)
    if m<ma:
        ma=m
        k=x
print(k)
