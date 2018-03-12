import itertools as p
ip=input()
n=int(ip)
a=list(ip)
b=p.permutations(a)
a=[]
c=0
mi=10000
for x in b:
   ans=""
   for y in x:
       ans+=y
   a.append(ans)
for x in a:
    if int(x)>n and mi>int(x):
        mi=int(x)
        c=1
if c==0:
    print("impossible")
else:
    print(mi)
