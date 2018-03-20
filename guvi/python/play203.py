n=int(input())
a=[]
m=[]
b=['a','e','i','o','u','A','E','I','O','U']
for x in range(n):
    a.append(input())
for x in a:
    c=0
    for y in x:
        if y in b:
            c+=1
    m.append(c)
for x in range(n):
    for y in range(x+1,n):
        if m[x]<m[y]:
            t=m[x]
            m[x]=m[y]
            b[y]=t
            t=a[x]
            a[x]=a[y]
            a[y]=t
for x in a:
    print(x)
