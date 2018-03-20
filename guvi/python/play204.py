n=int(input())
a=[]
ans=0
st=input().strip().split(" ")
for x in range(n):
    a.append(int(st[x]))
for x in a:
    if x<0:
        ans+=x
print(ans)
