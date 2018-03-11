n=int(input())
a=[]
ans=0
for x in range(n):
    a.append(int(input()))
b=[]
for x in a:
    if x not in b:
        b.append(x)
for x in b:
    print(x,end=" ")
