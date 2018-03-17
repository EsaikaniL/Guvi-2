n=int(input().strip())
ans=0
while(n>0):
    t=n%10
    if t%2==1:
        ans+=t
    n//=10
if ans%2==0:
    print("E")
else:
    print("O")
