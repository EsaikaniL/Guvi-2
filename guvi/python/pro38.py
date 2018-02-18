n=int(input("How many members??"))
k=int(input("How many times you want to participate?"))
a=[]
c=0
for x in range(n):
    a.append(int(input()))
for x  in a:
    if (x+k)<=5:
        c+=1 
print("The max team is:",c//3)
