n=int(input("How many elements??"))
a=[]
print("Enter the elements...")
for x in range(n):
    a.append(int(input()))
k=int(input("How many split??"))
if k>n:
    print("It is not possible to split.")
else:
    print("The optimal max is:",max(a))
