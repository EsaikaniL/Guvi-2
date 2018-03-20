n=int(input())
f=0
while(n>=2 and n%2==0):
    n//=2
    if n==2:
        f=1
if f==0:
    print("no")
else:
    print("yes")
