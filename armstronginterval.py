num1=int(input("Enter the 1st number"))
num2=int(input("Enter the 2nd number"))
 
for x in range(num1,num2):
   temp=x
   sum = 0
   while temp > 0:
    digit = temp % 10
    sum = sum+digit ** 3
    temp=temp/10
    if x == sum:
     print(x)