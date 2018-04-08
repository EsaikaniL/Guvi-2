n=int(input())
a=[]
ip=input().strip().split(" ")
for x in ip:
    a.append(int(x))
a.sort()
l=len(a)
bp=l-1
fp=0
ans=''
for x in range(1,l+1):
    if x%2==1:
        ans+=str(a[bp])+" "
        bp-=1
    else:
        ans+=str(a[fp])+" "
        fp+=1
print(ans.strip())
