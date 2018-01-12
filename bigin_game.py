loop='Y'
a=[]
while(loop=='Y'):
	nij=input()
	k1=int(nij.split(' ')[0])
	k2=int(nij.split(" ")[1])
	a.append(k2-k1)
	print(k1,k2)
	loop=input("Y or N")
for x in a:
    print(x)
