r=int(input('How many rows?\n'))
c=int(input('How many clumns?\n'))
s=[[0 for x in range(0,c)]for y in range(0,r)]
print 'Enter the elements\n'
for x in range(0,r):
	for y in range(0,c):
		s[x][y]=int(input())
		print '\n'
for x in range(0,r):
	for y in range(0,c):
		if s[x][0]==s[x][c-1]==0:
			s[x][y]=0
		if s[0][y]==s[r-1][y]==0:
			s[x][y]=0
for x in range(0,r):
	for y in range(0,c):
		print s[x][y],"\t",
	print ""
