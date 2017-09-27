k1=raw_input('Enter your name')
print '\n'
k2=raw_input('Enter your partner name:')
s1=k1.lower()
s2=k2.lower()
str1=list(s1)
str2=list(s2)
for x in str1:
	for y in str2:
		if (x==y):
			del str1[str1.index(x)]
			del str2[str2.index(y)]
			break
a=len(str1)+len(str2)
if (a==3) or (a==14) or (a==16) or (a==18):
	print 'Autually you are Friends!!'
if (a==5) or (a==10):
	print 'WOW!! You are Lovers!!'
if (a==8) or (a==12) or (a==13) or (a==17):
	print 'Autually you have a Affection on her!!'
if (a==6) or (a==11) or (a==15):
	print 'You will Marry soon!!'
if (a==2) or (a==4) or (a==7) or (a==9) or (a==20):
	print 'OMG!! You are Enemies!!'
if (a==1) or (a==19):
	print 'Shitt!! She is Your sister!!'
