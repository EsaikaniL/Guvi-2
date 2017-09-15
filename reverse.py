num=int(input("Enter the number"))
stack=[]
while num>0:
  temp=num%10
  stack.append(temp)
  num=num/10
print stack
