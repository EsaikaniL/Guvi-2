num1=int(input('Enter your 1st number'))
num2=int(input('Enter your 2nd number'))
print 'Befor swapping: \n',num1,num2
print 'After swapping:\n'
num1=num1^num2
num2=num1^num2
num1=num1^num2
print num1,num2
