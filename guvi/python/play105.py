n=int(input())
a=[]
ans=0
for x in range(n):
    a.append(int(input()))
b=a
for x in sorted(a):
    for y in range(len(a)):
        if x==b[y]:
            print(y+1)
