num=int(input("Enter any number"))
f=0
for x in range(1,num+1):
	if(num%x==0):
		f=f+1
if(f>2):
	print("composite")
else:
        print("Not composite")
