n1=int(input("how many elements \n"))
ele=[]
an=[]
print("Enter the element")
for x in range(0,n1):
    n2=int(input())
    ele.append(n2)
l=len(ele)
for x in range(0,l):
    for y in range(x,l):
        for z in range(y+1,l):
            ans=ele[y]*ele[z]
            an.append(ans)
print("The ans is:",max(an))
