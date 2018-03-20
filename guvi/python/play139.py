n=int(input())
a=[]
c=0
while(n>0):
    t=n%2
    a.append(t)
    n//=2
for x in a:
    if x==1:
        c+=1
print(c)
