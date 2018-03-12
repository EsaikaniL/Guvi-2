n=int(input().strip())
ans=0
while(n>0):
    t=n%10
    ans=ans+t
    n//=10
if ans==int(str(ans)[::-1]):
    print("YES")
else:
    print("NO")
