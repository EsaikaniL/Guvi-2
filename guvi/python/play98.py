n=input()
k=int(input())
a=[]
c=0
for x in range(0,k+1):
    a.append(x)
for x in n:
    if int(x) not in a:
        c=1
if c==0:
    print("Yes")
else:
    print("No")
