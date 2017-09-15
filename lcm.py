x=int(input("Enter your 1st number"))
y=int(input("Enter ur 2nd number")) 
if x > y:
     greater = x
else:
    greater = y
c=0
while (c==0):
	if (greater%x==0) and (greater%y==0):
		lcm=greater
		break
	greater=greater+1
print "The LCM of",x,"and",y,"is:",lcm
