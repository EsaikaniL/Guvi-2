n=int(input())
an=0
while(n>0):
    t=n%10
    an=an+t*t
    n//=10
print(an)
