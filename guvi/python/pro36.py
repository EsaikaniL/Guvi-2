w=int(input("Enter the weakness number:"))
n=int(input("How many man standing there??"))
print("Enter the mans power at in his position")
print("     Rule: a1>a2>a3>...>an    ")
a=[]
c=0
for x in range(n):
    a.append(int(input()))
for x in range(n):
    for y in range(x+1,n):
        for z in range(y+1,n):
            ans=a[x]+a[y]+a[z]
            if ans==w:
                c+=1
print("The roman army weakness is:",c)
