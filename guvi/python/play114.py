n=int(input())
ans=0
while(n>0):
    t=n%10
    ans=ans+t*t
    n//=10
print(ans)
