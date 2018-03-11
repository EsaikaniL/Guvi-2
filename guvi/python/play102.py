import itertools as p
n=int(input())
a=[]
m=-1
for x in range(n):
    a.append(int(input()))
for x in p.permutations(a):
    ans=0
    for y in range(len(x)-1):
        ans=ans+max(x[y],x[y+1])
    if m<ans:
        m=ans
print(m)
