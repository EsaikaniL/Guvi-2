n=int(input())
a=[]
c=0
for x in range(n*2):
    a.append(int(input()))
for x in range(0,(n*2)-1):
    if (x+1)%2==1:
        if a[x]<a[x+1]:
            c+=1
print(x)
