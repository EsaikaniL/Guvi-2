n1=int(input("how many elements"))
ele=[]
ans=1
print("Enter the element")
for x in range(0,n1):
    n2=input()
    ele.append(n2)
for x in ele:
    ans=ans*int(x)
print(ans)
