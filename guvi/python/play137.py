n=int(input())
a=[]
while(n>0):
    t=n%2
    a.append(t)
    n//=2
for x in range(len(a)):
    if a[x]==1:
        break
print(x+1)
