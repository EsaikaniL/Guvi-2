n=int(input("Enter the term"))
n1=0
n2=1
if n==1:
  print n1
else: 
  print n1
  print n2
  for x in range(1,n-1):
      n3=n1+n2
      print n3
      n1=n2
      n2=n3
