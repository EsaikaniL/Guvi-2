n=int(input("Enter The number:"))
for x in range(1,n-1):
    if n%x==0:
       if x%2!=0:
          print(x)
