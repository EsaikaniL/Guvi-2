s1=[]
s2=[]
s3=[]
s4=[]
s5=[]
s6=[]
s7=[]
s8=[]
print '1st point'
for x in range(0,2):
	n=int(input())
	s1.append(n)
print '2nd point'
for x in range(0,2):
	n=int(input())
	s2.append(n)
print '3rd point'
for x in range(0,2):
	n=int(input())
	s3.append(n)
print '4th point'
for x in range(0,2):
	n=int(input())
	s4.append(n)
for x in s2:
	for y in s1:
		a=x-y
		s5.append(a)
AB=max(s5)
for x in s4:
	for y in s2:
		a=x-y
		s6.append(a)
BD=max(s6)
for x in s4:
	for y in s3:
		a=x-y
		s7.append(a)
CD=max(s7)
for x in s3:
	for y in s1:
		a=x-y
		s8.append(a)
AC=max(s8)
if(AB==BD==CD==AC):
	print 'True,It is square!!'
 else:
 print 'False,It si not square!!'
