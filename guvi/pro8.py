n=int(input("Enter the N value:"))
q=int(input("Enter the Q value:"))
a=[]
b=[]
print("Enter the Elelments:")
for x in range(n):
    p=int(input())
    a.append(p)
for y in range(q):
    l=int(input("L value:"))
    r=int(input("R value:"))
    b=sorted(a)
    for x in b:
             if l%x==0 and r%x==0:
                 ans=x
    print(ans)
