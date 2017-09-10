num=int(input("Enter the any number(positive)"))
temp=num
print ("Your number is:",num)
stack=[]
while num!=0:
    a=num%10
    stack.append(a)
    num=num/10
stack.sort();
k=int(input("Enter the no of digit that u want to delete"));
for x in range(k):
    stack.pop()
print("The req least numbers are from the number",temp)   
for Item in stack:
 print(Item)
    
