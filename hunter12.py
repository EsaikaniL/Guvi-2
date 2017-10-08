print 'Enter the 50 students height\n'
a=[]
for x in range(0,50):
	n=int(input())
	a.append(n)
a.sort
print '4th tallest boy of class is',a[3],'\n'
k=int(input('Enter the k value\n'))
print a[k-1]
