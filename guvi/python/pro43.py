n=int(input("How many elements??"))
a=[]
b=[]
for x in range(n):
    a.append(int(input()))
for x in range(0,n):
    if x+1 not in a:
        b.append(x+1)
for y in b:
    for x in range(0,n):
        if a[x]!=x+1:
            a[x]=y  
            break
print(a)
